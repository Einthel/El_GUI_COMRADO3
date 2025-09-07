# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Timer_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Timer_widget(object):
    def setupUi(self, Timer_widget):
        if not Timer_widget.objectName():
            Timer_widget.setObjectName(u"Timer_widget")
        Timer_widget.setWindowModality(Qt.WindowModality.NonModal)
        Timer_widget.resize(270, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Timer_widget.sizePolicy().hasHeightForWidth())
        Timer_widget.setSizePolicy(sizePolicy)
        Timer_widget.setMinimumSize(QSize(270, 80))
        Timer_widget.setMaximumSize(QSize(270, 80))
        Timer_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        Timer_widget.setAcceptDrops(True)
        Timer_widget.setWindowTitle(u"")
        self.Timer_frame = QFrame(Timer_widget)
        self.Timer_frame.setObjectName(u"Timer_frame")
        self.Timer_frame.setGeometry(QRect(0, 0, 270, 80))
        self.Timer_frame.setMinimumSize(QSize(270, 80))
        self.Timer_frame.setMaximumSize(QSize(270, 80))
        self.Timer_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.Timer_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.Timer_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.Timer_label = QLabel(self.Timer_frame)
        self.Timer_label.setObjectName(u"Timer_label")
        self.Timer_label.setMinimumSize(QSize(125, 65))
        self.Timer_label.setMaximumSize(QSize(125, 65))
        font = QFont()
        font.setPointSize(15)
        self.Timer_label.setFont(font)
        self.Timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Timer_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.Timer_button = QPushButton(self.Timer_frame)
        self.Timer_button.setObjectName(u"Timer_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Timer_button.sizePolicy().hasHeightForWidth())
        self.Timer_button.setSizePolicy(sizePolicy1)
        self.Timer_button.setMinimumSize(QSize(125, 60))
        self.Timer_button.setMaximumSize(QSize(125, 65))
        self.Timer_button.setFont(font)

        self.verticalLayout.addWidget(self.Timer_button)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Timer_widget)

        QMetaObject.connectSlotsByName(Timer_widget)
    # setupUi

    def retranslateUi(self, Timer_widget):
        self.Timer_label.setText("")
        self.Timer_button.setText(QCoreApplication.translate("Timer_widget", u"Timer", None))
        pass
    # retranslateUi

