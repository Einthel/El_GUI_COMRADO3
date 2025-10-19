from PySide6.QtWidgets import QWidget
from ui_storage_GB import Ui_storage_GB

class StorageWidget(QWidget):
    """
    Виджет для отображения информации об одном дисковом накопителе.
    Этот класс является оберткой над UI, сгенерированным из 'storage_GB.ui'.
    """
    def __init__(self, parent: QWidget = None):
        """
        Инициализатор виджета.
        """
        super().__init__(parent)
        self.ui = Ui_storage_GB()
        self.ui.setupUi(self)

    def setData(self, drive_data: dict):
        """
        Заполняет виджет данными о диске.

        :param drive_data: Словарь с данными одного диска,
                           полученный от HwInfoReader.
        """
        # Название диска. Приоритет - имя модели, если нет - точка монтирования.
        name = drive_data.get('name') or drive_data.get('mountpoint', 'N/A')
        self.ui.name_storage_1.setText(str(name))

        # Температура. Скрываем метку, если данных нет.
        temperature = drive_data.get('temperature')
        if temperature is not None:
            self.ui.temp_storage_lable_1.setText(f"{temperature:.0f}°C")
            self.ui.temp_storage_lable_1.show()
        else:
            self.ui.temp_storage_lable_1.hide()

        # Прогресс-бар использования.
        percent_used = drive_data.get('percent', 0)
        self.ui.progressBar_storage_1.setValue(int(percent_used))
        self.ui.progressBar_storage_1.setTextVisible(True)
        self.ui.progressBar_storage_1.setFormat(f"{percent_used:.1f}%")

        # Метки с информацией об объеме ("XX.X ГБ занято из YY.Y ГБ").
        used_gb = drive_data.get('used', 0)
        total_gb = drive_data.get('total', 0)
        
        self.ui.freeGB_storage_label_1.setText(f"{used_gb:.1f} ГБ")
        self.ui.totalGB_storage_lable_1.setText(f"{total_gb:.1f} ГБ")
