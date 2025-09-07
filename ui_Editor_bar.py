# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Editor_bar.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_Editor_bar_Window(object):
    def setupUi(self, Editor_bar_Window):
        if not Editor_bar_Window.objectName():
            Editor_bar_Window.setObjectName(u"Editor_bar_Window")
        Editor_bar_Window.resize(554, 518)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Editor_bar_Window.sizePolicy().hasHeightForWidth())
        Editor_bar_Window.setSizePolicy(sizePolicy)
        Editor_bar_Window.setMinimumSize(QSize(0, 0))
        Editor_bar_Window.setMaximumSize(QSize(1024, 800))
        self.centralwidget = QWidget(Editor_bar_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Page_control_frame_editor = QFrame(self.centralwidget)
        self.Page_control_frame_editor.setObjectName(u"Page_control_frame_editor")
        self.Page_control_frame_editor.setGeometry(QRect(0, 470, 551, 44))
        self.Page_control_frame_editor.setFrameShape(QFrame.Shape.StyledPanel)
        self.Page_control_frame_editor.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Page_control_frame_editor)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 2, 5, 2)
        self.BackButton_editor = QPushButton(self.Page_control_frame_editor)
        self.BackButton_editor.setObjectName(u"BackButton_editor")

        self.horizontalLayout.addWidget(self.BackButton_editor)

        self.Current_page_label_editor = QLabel(self.Page_control_frame_editor)
        self.Current_page_label_editor.setObjectName(u"Current_page_label_editor")
        self.Current_page_label_editor.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Current_page_label_editor.setFrameShape(QFrame.Shape.StyledPanel)
        self.Current_page_label_editor.setFrameShadow(QFrame.Shadow.Plain)
        self.Current_page_label_editor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Current_page_label_editor)

        self.NextButton_editor = QPushButton(self.Page_control_frame_editor)
        self.NextButton_editor.setObjectName(u"NextButton_editor")

        self.horizontalLayout.addWidget(self.NextButton_editor)

        self.Add_page_button_editor = QPushButton(self.Page_control_frame_editor)
        self.Add_page_button_editor.setObjectName(u"Add_page_button_editor")
        self.Add_page_button_editor.setBaseSize(QSize(25, 25))
        self.Add_page_button_editor.setMouseTracking(False)
        self.Add_page_button_editor.setTabletTracking(False)
        self.Add_page_button_editor.setFlat(False)

        self.horizontalLayout.addWidget(self.Add_page_button_editor)

        self.Remove_page_button_editor = QPushButton(self.Page_control_frame_editor)
        self.Remove_page_button_editor.setObjectName(u"Remove_page_button_editor")

        self.horizontalLayout.addWidget(self.Remove_page_button_editor)

        self.save_bar_button = QPushButton(self.Page_control_frame_editor)
        self.save_bar_button.setObjectName(u"save_bar_button")

        self.horizontalLayout.addWidget(self.save_bar_button)

        self.load_bar_button = QPushButton(self.Page_control_frame_editor)
        self.load_bar_button.setObjectName(u"load_bar_button")

        self.horizontalLayout.addWidget(self.load_bar_button)

        self.Ready_Widget_list = QListWidget(self.centralwidget)
        self.Ready_Widget_list.setObjectName(u"Ready_Widget_list")
        self.Ready_Widget_list.setGeometry(QRect(290, 10, 261, 451))
        self.Bar_editor_QFrame = QFrame(self.centralwidget)
        self.Bar_editor_QFrame.setObjectName(u"Bar_editor_QFrame")
        self.Bar_editor_QFrame.setGeometry(QRect(0, 10, 281, 451))
        self.Bar_editor_QFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Bar_editor_QFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.Bar_editor_QFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.Bar_editor_target_1 = QFrame(self.Bar_editor_QFrame)
        self.Bar_editor_target_1.setObjectName(u"Bar_editor_target_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Bar_editor_target_1.sizePolicy().hasHeightForWidth())
        self.Bar_editor_target_1.setSizePolicy(sizePolicy1)
        self.Bar_editor_target_1.setMinimumSize(QSize(260, 80))
        self.Bar_editor_target_1.setMaximumSize(QSize(260, 80))
        self.Bar_editor_target_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Bar_editor_target_1.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Bar_editor_target_1, 0, 0, 1, 1)

        self.Bar_editor_target_2 = QFrame(self.Bar_editor_QFrame)
        self.Bar_editor_target_2.setObjectName(u"Bar_editor_target_2")
        self.Bar_editor_target_2.setMinimumSize(QSize(260, 80))
        self.Bar_editor_target_2.setMaximumSize(QSize(260, 80))
        self.Bar_editor_target_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Bar_editor_target_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Bar_editor_target_2, 1, 0, 1, 1)

        self.Bar_editor_target_3 = QFrame(self.Bar_editor_QFrame)
        self.Bar_editor_target_3.setObjectName(u"Bar_editor_target_3")
        self.Bar_editor_target_3.setMinimumSize(QSize(260, 80))
        self.Bar_editor_target_3.setMaximumSize(QSize(260, 80))
        self.Bar_editor_target_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Bar_editor_target_3.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Bar_editor_target_3, 2, 0, 1, 1)

        self.Bar_editor_target_4 = QFrame(self.Bar_editor_QFrame)
        self.Bar_editor_target_4.setObjectName(u"Bar_editor_target_4")
        self.Bar_editor_target_4.setMinimumSize(QSize(260, 80))
        self.Bar_editor_target_4.setMaximumSize(QSize(260, 80))
        self.Bar_editor_target_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Bar_editor_target_4.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Bar_editor_target_4, 3, 0, 1, 1)

        self.Bar_editor_target_5 = QFrame(self.Bar_editor_QFrame)
        self.Bar_editor_target_5.setObjectName(u"Bar_editor_target_5")
        self.Bar_editor_target_5.setMinimumSize(QSize(260, 80))
        self.Bar_editor_target_5.setMaximumSize(QSize(260, 80))
        self.Bar_editor_target_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Bar_editor_target_5.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Bar_editor_target_5, 4, 0, 1, 1)

        Editor_bar_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Editor_bar_Window)

        QMetaObject.connectSlotsByName(Editor_bar_Window)
    # setupUi

    def retranslateUi(self, Editor_bar_Window):
        Editor_bar_Window.setWindowTitle(QCoreApplication.translate("Editor_bar_Window", u"Editor Window", None))
        self.BackButton_editor.setText(QCoreApplication.translate("Editor_bar_Window", u"TempBack", None))
        self.Current_page_label_editor.setText("")
        self.NextButton_editor.setText(QCoreApplication.translate("Editor_bar_Window", u"TempNext", None))
        self.Add_page_button_editor.setText(QCoreApplication.translate("Editor_bar_Window", u"+", None))
        self.Remove_page_button_editor.setText(QCoreApplication.translate("Editor_bar_Window", u"-", None))
        self.save_bar_button.setText(QCoreApplication.translate("Editor_bar_Window", u"Save", None))
        self.load_bar_button.setText(QCoreApplication.translate("Editor_bar_Window", u"Load", None))
    # retranslateUi

