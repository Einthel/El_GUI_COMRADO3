# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ok_cancle_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QToolButton, QWidget)

class Ui_YesNo_widget(object):
    def setupUi(self, YesNo_widget):
        if not YesNo_widget.objectName():
            YesNo_widget.setObjectName(u"YesNo_widget")
        YesNo_widget.setWindowModality(Qt.WindowModality.NonModal)
        YesNo_widget.resize(270, 80)
        YesNo_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        YesNo_widget.setAcceptDrops(True)
        YesNo_widget.setWindowTitle(u"")
        self.YesNo_frame = QFrame(YesNo_widget)
        self.YesNo_frame.setObjectName(u"YesNo_frame")
        self.YesNo_frame.setGeometry(QRect(0, 0, 270, 80))
        self.YesNo_frame.setMinimumSize(QSize(270, 80))
        self.YesNo_frame.setMaximumSize(QSize(270, 80))
        font = QFont()
        font.setPointSize(12)
        self.YesNo_frame.setFont(font)
        self.YesNo_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.YesNo_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.YesNo_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.yes_button = QToolButton(self.YesNo_frame)
        self.yes_button.setObjectName(u"yes_button")
        self.yes_button.setMinimumSize(QSize(70, 70))
        self.yes_button.setMaximumSize(QSize(70, 70))
        self.yes_button.setBaseSize(QSize(70, 70))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.yes_button.setFont(font1)
        self.yes_button.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.yes_button.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.yes_button.setIconSize(QSize(96, 96))
        self.yes_button.setCheckable(False)
        self.yes_button.setChecked(False)
        self.yes_button.setAutoRepeatDelay(600)
        self.yes_button.setAutoRepeatInterval(300)
        self.yes_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.yes_button.setAutoRaise(False)
        self.yes_button.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout.addWidget(self.yes_button)

        self.no_button = QToolButton(self.YesNo_frame)
        self.no_button.setObjectName(u"no_button")
        self.no_button.setMinimumSize(QSize(70, 70))
        self.no_button.setMaximumSize(QSize(70, 70))
        self.no_button.setBaseSize(QSize(70, 70))
        self.no_button.setFont(font1)
        self.no_button.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.no_button.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.no_button.setIconSize(QSize(96, 96))
        self.no_button.setCheckable(False)
        self.no_button.setChecked(False)
        self.no_button.setAutoRepeatDelay(600)
        self.no_button.setAutoRepeatInterval(300)
        self.no_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.no_button.setAutoRaise(False)
        self.no_button.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout.addWidget(self.no_button)


        self.retranslateUi(YesNo_widget)

        QMetaObject.connectSlotsByName(YesNo_widget)
    # setupUi

    def retranslateUi(self, YesNo_widget):
        self.yes_button.setText(QCoreApplication.translate("YesNo_widget", u"Yes", None))
        self.no_button.setText(QCoreApplication.translate("YesNo_widget", u"No", None))
        pass
    # retranslateUi

