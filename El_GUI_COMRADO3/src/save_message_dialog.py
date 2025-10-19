from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

from ui_save_message_dialog import Ui_save_message_dialog
import constants

class SaveMessageDialog(QDialog):
    """
    Кастомное диалоговое окно для подтверждения сохранения изменений.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_save_message_dialog()
        self.ui.setupUi(self)

        # Убираем стандартную рамку окна
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Устанавливаем тексты из констант
        self.ui.questions_lable.setText(constants.QUESTION_SAVE_CHANGES)
        self.ui.save_toolB.setText(constants.ANSWER_SAVE_CHANGES_YES)
        self.ui.cancle_toolB.setText(constants.ANSWER_SAVE_CHANGES_NO)
        self.setWindowTitle(constants.windows_title_save_changes)

        # Подключаем кнопки к стандартным слотам accept/reject
        self.ui.save_toolB.clicked.connect(self.accept)
        self.ui.cancle_toolB.clicked.connect(self.reject)
