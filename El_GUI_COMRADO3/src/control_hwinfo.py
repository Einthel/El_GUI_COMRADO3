import time
from PySide6.QtCore import QObject, Signal
import psutil
import wmi
import os
import sys
import clr # Для загрузки .NET сборок

# --- Явная загрузка .NET библиотек ---
# 1. Определяем путь к папке с библиотеками
# (поднимаемся на 2 уровня от control_hwinfo.py до корня проекта, затем идем в libs/library/HWMonitor)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
hw_monitor_lib_path = os.path.join(project_root, 'libs', 'library', 'HWMonitor')

# 2. Добавляем этот путь в sys.path, чтобы Python мог найти зависимости
sys.path.append(hw_monitor_lib_path)

# 3. Удаляем блок clr.AddReference, так как он вызывает конфликты.
#    Загрузка будет неявной, через sys.path и последующий import.
# ------------------------------------

try:
    from HardwareMonitor.Hardware import Computer, IVisitor, IComputer, IHardware, ISensor, IParameter, HardwareType, SensorType
except ImportError:
    # Этот блок нужен, чтобы приложение не падало, если библиотека не установлена.
    # Мы можем обработать это в основном коде и вывести пользователю сообщение.
    print("Ошибка: Библиотека PyHardwareMonitor не найдена. Установите ее командой: pip install HardwareMonitor")
    # Создаем классы-пустышки, чтобы остальной код не вызывал ошибок импорта
    class QObject: pass
    class Signal: 
        def emit(self, *args, **kwargs): pass
    class Computer: pass
    class IVisitor: pass
    HardwareType = SensorType = None


class UpdateVisitor(IVisitor):
    """
    Класс-посетитель для обновления данных об оборудовании.
    Это обязательная часть для работы с LibreHardwareMonitor.
    """
    __namespace__ = "HwInfoUpdateVisitor"

    def VisitComputer(self, computer: IComputer):
        computer.Traverse(self)

    def VisitHardware(self, hardware: IHardware):
        hardware.Update()
        for subHardware in hardware.SubHardware:
            subHardware.Update()

    def VisitSensor(self, sensor: ISensor):
        pass

    def VisitParameter(self, parameter: IParameter):
        pass


class HwInfoReader(QObject):
    """
    Класс, выполняющий в отдельном потоке чтение данных с датчиков ПК.
    """
    # Сигнал, передающий словарь с данными о процессоре
    cpu_data_updated = Signal(dict)
    gpu_data_updated = Signal(dict)
    memory_data_updated = Signal(dict)
    storage_data_updated = Signal(list)
    available_gpus_found = Signal(list)

    def __init__(self):
        super().__init__()
        self._is_running = True
        self.target_gpu_name = None # Имя GPU, которое нужно отслеживать
        self._gpus_found_and_emitted = False # Флаг для однократного поиска и отправки списка GPU
        self._cpu_sensors_logged = True # Флаг для однократного логирования датчиков CPU
        
        if HardwareType is None: # Проверка, что библиотека не загрузилась
            self.computer = None
            return

        self.computer = Computer()
        self.computer.IsCpuEnabled = True
        self.computer.IsGpuEnabled = True
        # self.computer.IsMemoryEnabled = True # Больше не используется для RAM
        self.computer.IsStorageEnabled = True

    def run_monitoring(self):
        """
        Основной цикл мониторинга. Запускается в отдельном потоке.
        """
        if not self.computer:
            print("HwInfoReader: Компьютер не инициализирован, мониторинг невозможен.")
            return
            
        print("HwInfoReader: Запуск потока мониторинга...")
        self.computer.Open()
        
        # Создаем экземпляр визитора один раз
        update_visitor = UpdateVisitor()

        while self._is_running:
            try:
                # Обновляем все датчики
                self.computer.Accept(update_visitor)
                # Ищем и отправляем данные
                self._find_and_parse_cpu_data()
                self._find_and_parse_gpu_data()
                self._find_and_parse_memory_data()
                self._find_and_parse_storage_data()
                # Пауза между опросами
                time.sleep(2)
            except Exception as e:
                print(f"HwInfoReader: Ошибка в цикле мониторинга: {e}")
                time.sleep(5) # В случае ошибки делаем паузу подольше

        self.computer.Close()
        print("HwInfoReader: Поток мониторинга остановлен.")

    def _find_and_parse_cpu_data(self):
        """
        Находит оборудование CPU, парсит его датчики и отправляет сигнал.
        """
        for hardware in self.computer.Hardware:
            if hardware.HardwareType == HardwareType.Cpu:
                # --- ОДНОКРАТНОЕ ЛОГИРОВАНИЕ ВСЕХ ДАТЧИКОВ CPU ---
                if not self._cpu_sensors_logged:
                    print("\n" + "="*20 + " Все датчики CPU " + "="*20)
                    for sensor in hardware.Sensors:
                        print(f"  - Имя: {sensor.Name}, Тип: {sensor.SensorType}, Значение: {sensor.Value}")
                    print("="*57 + "\n")
                    self._cpu_sensors_logged = True
                # ----------------------------------------------------

                # Инициализируем словарь с None, чтобы гарантировать наличие всех ключей
                cpu_data = {
                    'name': hardware.Name,
                    'temp': None,
                    'load': None,
                    'power': None,
                    'clocks': None
                }
                
                # Временные переменные для выбора лучшего датчика частоты
                fallback_clock_value = None
                preferred_clock_value = None

                for sensor in hardware.Sensors:
                    sensor_name_lower = sensor.Name.lower()
                    # Ищем нужные датчики по типу и имени
                    if sensor.SensorType == SensorType.Temperature and ("package" in sensor_name_lower or "tctl" in sensor_name_lower):
                        cpu_data['temp'] = sensor.Value
                    elif sensor.SensorType == SensorType.Load and "total" in sensor_name_lower:
                        cpu_data['load'] = sensor.Value
                    elif sensor.SensorType == SensorType.Power and "package" in sensor_name_lower:
                        cpu_data['power'] = sensor.Value
                    elif sensor.SensorType == SensorType.Clock:
                        # Логика приоритетного выбора датчика частоты
                        if "core clocks" in sensor_name_lower:
                            # Это идеальный вариант - агрегированное значение
                            preferred_clock_value = sensor.Value
                        elif "core" in sensor_name_lower and fallback_clock_value is None:
                            # Это запасной вариант - частота первого попавшегося ядра
                            fallback_clock_value = sensor.Value
                
                # Приоритет отдается 'preferred', если он найден, иначе используется 'fallback'
                if preferred_clock_value is not None:
                    cpu_data['clocks'] = preferred_clock_value
                else:
                    cpu_data['clocks'] = fallback_clock_value
                
                # Отправляем собранные данные, только если они есть
                self.cpu_data_updated.emit(cpu_data)
                
                # Так как CPU у нас один, выходим из цикла после его обработки
                return

    def _find_and_parse_memory_data(self):
        """
        Собирает данные об оперативной памяти с помощью psutil и отправляет сигнал.
        Также выводит в консоль все найденные метрики для отладки.
        """
        try:
            mem_info = psutil.virtual_memory()


            # --- Подготовка данных для интерфейса ---
            memory_data = {
                'load': mem_info.percent,
                'used': mem_info.used / (1024**3),    # Конвертация из байт в ГБ
                'total': mem_info.total / (1024**3),   # Конвертация из байт в ГБ
                'available': mem_info.available / (1024**3) # Добавляем доступную память
            }
            
            self.memory_data_updated.emit(memory_data)

        except Exception as e:
            print(f"HwInfoReader: Ошибка при получении данных RAM от psutil: {e}")

    def _find_and_parse_storage_data(self):
        """
        Собирает и объединяет данные о накопителях из LHM (температура) и psutil (объемы).
        """
        try:
            # --- Шаг 1: Получаем температуры от LHM ---
            lhm_temperatures = {}
            for hardware in self.computer.Hardware:
                if hardware.HardwareType == HardwareType.Storage:
                    drive_name = hardware.Name
                    for sensor in hardware.Sensors:
                        if sensor.SensorType == SensorType.Temperature:
                            lhm_temperatures[drive_name] = sensor.Value
                            break 

            # --- Шаг 2: Получаем логические разделы от psutil и готовим WMI ---
            partitions = psutil.disk_partitions(all=False)
            c = wmi.WMI()
            all_drives_data = []

            # --- Шаг 3: Объединяем данные для каждого раздела ---
            for p in partitions:
                if 'fixed' not in p.opts.lower():
                    continue

                usage = psutil.disk_usage(p.mountpoint)
                
                # --- Сопоставление раздела (C:) с физическим диском ---
                physical_disk_name = None # Сбрасываем имя перед попыткой
                try:
                    #print(f"--- WMI для {p.mountpoint} ---")
                    # Очищаем имя диска от слэшей (psutil -> 'C:\\', WMI -> 'C:')
                    device_id = p.device.strip('\\')
                    logical_disk_query = c.Win32_LogicalDisk(DeviceID=device_id)
                    if logical_disk_query:
                        #print(f"  [1] Логический диск найден: {logical_disk_query[0].Name}")
                        partition_query = logical_disk_query[0].associators("Win32_LogicalDiskToPartition")
                        if partition_query:
                            #print(f"  [2] Связанный раздел найден: {partition_query[0].DeviceID}")
                            physical_disk_query = partition_query[0].associators("Win32_DiskDriveToDiskPartition")
                            if physical_disk_query:
                                physical_disk_name = physical_disk_query[0].Model
                                #print(f"  [3] Физический диск найден. Модель: {physical_disk_name}")
                            else:
                                print("  [3] Физический диск НЕ найден.")
                        else:
                            print("  [2] Связанный раздел НЕ найден.")
                    else:
                        print("  [1] Логический диск НЕ найден.")
                    #print("--------------------")

                except Exception as wmi_error:
                    # Если сопоставление не удалось, логируем ошибку, но не прерываем работу
                    print(f"HwInfoReader: КРИТИЧЕСКАЯ ОШИБКА при сопоставлении диска {p.mountpoint} через WMI: {wmi_error}")
                
                temperature = lhm_temperatures.get(physical_disk_name) if physical_disk_name else None

                drive_data = {
                    'mountpoint': p.mountpoint,
                    'total': usage.total / (1024**3),
                    'used': usage.used / (1024**3),
                    'free': usage.free / (1024**3),
                    'percent': usage.percent,
                    'temperature': temperature,
                    'name': physical_disk_name or p.mountpoint # Имя диска, или буква если имя не найдено
                }
                all_drives_data.append(drive_data)

            # --- Шаг 4: Отправляем собранные данные ---
            if all_drives_data:
                self.storage_data_updated.emit(all_drives_data)

        except Exception as e:
            print(f"HwInfoReader: Ошибка при получении данных о накопителях: {e}")

    def _find_and_parse_gpu_data(self):
        """
        На первом запуске находит все доступные GPU и отправляет их список.
        На последующих запусках парсит датчики только для целевого GPU.
        """
        # --- Фаза 1: Поиск и отправка списка всех GPU (выполняется один раз) ---
        if not self._gpus_found_and_emitted:
            found_gpus = []
            for hardware in self.computer.Hardware:
                if hardware.HardwareType == HardwareType.GpuNvidia or hardware.HardwareType == HardwareType.GpuAmd or hardware.HardwareType.GpuIntel:
                    found_gpus.append(hardware.Name)
            
            if found_gpus:
                self.available_gpus_found.emit(found_gpus)
            
            self._gpus_found_and_emitted = True

        # --- Фаза 2: Парсинг датчиков для выбранного GPU ---
        if not self.target_gpu_name:
            # Если целевой GPU еще не задан из главного потока, ничего не делаем
            return

        for hardware in self.computer.Hardware:
            # Ищем конкретно тот GPU, который был выбран
            if hardware.Name == self.target_gpu_name:
                gpu_data = {'name': hardware.Name}
                
                for sensor in hardware.Sensors:
                    name_lower = sensor.Name.lower()
                    sensor_type = sensor.SensorType
                    
                    # Температура
                    if sensor_type == SensorType.Temperature:
                        if name_lower == 'gpu core':
                            gpu_data['temp'] = sensor.Value
                        elif name_lower == 'gpu hot spot':
                            gpu_data['temp_hotspot'] = sensor.Value
                    
                    # Загрузка
                    elif sensor_type == SensorType.Load:
                        if name_lower == 'gpu core':
                            gpu_data['load'] = sensor.Value
                        elif name_lower == 'gpu memory':
                            gpu_data['vram_percent'] = sensor.Value
                    
                    # Частота
                    elif sensor_type == SensorType.Clock and name_lower == 'gpu core':
                        gpu_data['clocks'] = sensor.Value
                        
                    # Мощность
                    elif sensor_type == SensorType.Power and name_lower == 'gpu package':
                        gpu_data['power'] = sensor.Value
                        
                    # Вентиляторы
                    elif sensor_type == SensorType.Fan and 'gpu fan' in name_lower:
                        if 'fan_rpm' not in gpu_data: # Берем первый попавшийся
                             gpu_data['fan_rpm'] = sensor.Value
                    elif sensor_type == SensorType.Control and 'gpu fan' in name_lower:
                        if 'fan_percent' not in gpu_data: # Берем первый попавшийся
                            gpu_data['fan_percent'] = sensor.Value

                    # Видеопамять
                    elif sensor_type == SensorType.SmallData:
                        if name_lower == 'gpu memory total':
                            gpu_data['vram_total'] = sensor.Value
                        elif name_lower == 'gpu memory used':
                            gpu_data['vram_used'] = sensor.Value

                self.gpu_data_updated.emit(gpu_data)
                
                # Нашли и обработали нужный GPU, выходим
                return

    def stop(self):
        """
        Останавливает цикл мониторинга.
        """
        self._is_running = False
