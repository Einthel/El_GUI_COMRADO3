# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clock_widget.ui'
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
    QSizePolicy, QWidget)

class Ui_Clock_widget(object):
    def setupUi(self, Clock_widget):
        if not Clock_widget.objectName():
            Clock_widget.setObjectName(u"Clock_widget")
        Clock_widget.setWindowModality(Qt.WindowModality.NonModal)
        Clock_widget.resize(270, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Clock_widget.sizePolicy().hasHeightForWidth())
        Clock_widget.setSizePolicy(sizePolicy)
        Clock_widget.setMinimumSize(QSize(270, 80))
        Clock_widget.setMaximumSize(QSize(270, 80))
        Clock_widget.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(15)
        Clock_widget.setFont(font)
        Clock_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        Clock_widget.setAcceptDrops(True)
        Clock_widget.setWindowTitle(u"")
        Clock_widget.setWindowOpacity(1.000000000000000)
        Clock_widget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.Clock_frame = QFrame(Clock_widget)
        self.Clock_frame.setObjectName(u"Clock_frame")
        self.Clock_frame.setGeometry(QRect(0, 0, 270, 80))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Clock_frame.sizePolicy().hasHeightForWidth())
        self.Clock_frame.setSizePolicy(sizePolicy1)
        self.Clock_frame.setMinimumSize(QSize(270, 80))
        self.Clock_frame.setMaximumSize(QSize(270, 80))
        self.Clock_frame.setFont(font)
        self.Clock_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Clock_frame.setInputMethodHints(Qt.InputMethodHint.ImhTime)
        self.Clock_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Clock_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.Clock_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.Clock_iconLabel = QLabel(self.Clock_frame)
        self.Clock_iconLabel.setObjectName(u"Clock_iconLabel")
        self.Clock_iconLabel.setEnabled(True)
        self.Clock_iconLabel.setMinimumSize(QSize(125, 65))
        self.Clock_iconLabel.setMaximumSize(QSize(125, 65))
        font1 = QFont()
        font1.setPointSize(20)
        self.Clock_iconLabel.setFont(font1)
        self.Clock_iconLabel.setScaledContents(True)
        self.Clock_iconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Clock_iconLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.Clock_iconLabel)

        self.Clock_timeLabel = QLabel(self.Clock_frame)
        self.Clock_timeLabel.setObjectName(u"Clock_timeLabel")
        self.Clock_timeLabel.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Clock_timeLabel.sizePolicy().hasHeightForWidth())
        self.Clock_timeLabel.setSizePolicy(sizePolicy1)
        self.Clock_timeLabel.setMinimumSize(QSize(125, 65))
        self.Clock_timeLabel.setMaximumSize(QSize(125, 65))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.Clock_timeLabel.setFont(font2)
        self.Clock_timeLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Clock_timeLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.Clock_timeLabel.setLineWidth(1)
        self.Clock_timeLabel.setMidLineWidth(0)
        self.Clock_timeLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.Clock_timeLabel.setScaledContents(True)
        self.Clock_timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Clock_timeLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.Clock_timeLabel)


        self.retranslateUi(Clock_widget)

        QMetaObject.connectSlotsByName(Clock_widget)
    # setupUi

    def retranslateUi(self, Clock_widget):
        self.Clock_iconLabel.setText(QCoreApplication.translate("Clock_widget", u"Time:", None))
        self.Clock_timeLabel.setText(QCoreApplication.translate("Clock_widget", u"111", None))
        pass
    # retranslateUi

