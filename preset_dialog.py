# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox, QLabel

class PresetNameDialog(QDialog):
    """
    Диалоговое окно для ввода имени нового пресета.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Сохранить пресет")

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Введите уникальное имя для нового пресета:")
        self.layout.addWidget(self.label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Например, 'Открыть Photoshop'")
        self.layout.addWidget(self.name_input)

        # Добавляем кнопки "ОК" и "Отмена"
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def get_preset_name(self):
        """
        Возвращает введенное пользователем имя пресета.
        """
        return self.name_input.text().strip() 