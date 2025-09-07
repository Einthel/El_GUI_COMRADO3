# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Volume_widget.ui'
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

class Ui_Volume_widget(object):
    def setupUi(self, Volume_widget):
        if not Volume_widget.objectName():
            Volume_widget.setObjectName(u"Volume_widget")
        Volume_widget.setWindowModality(Qt.WindowModality.NonModal)
        Volume_widget.resize(270, 80)
        Volume_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        Volume_widget.setAcceptDrops(True)
        Volume_widget.setWindowTitle(u"")
        self.Volume_frame = QFrame(Volume_widget)
        self.Volume_frame.setObjectName(u"Volume_frame")
        self.Volume_frame.setGeometry(QRect(0, 0, 270, 80))
        self.Volume_frame.setMinimumSize(QSize(270, 80))
        self.Volume_frame.setMaximumSize(QSize(270, 80))
        self.Volume_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Volume_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Volume_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.Volume_iconLabel = QLabel(self.Volume_frame)
        self.Volume_iconLabel.setObjectName(u"Volume_iconLabel")
        self.Volume_iconLabel.setMinimumSize(QSize(125, 65))
        self.Volume_iconLabel.setMaximumSize(QSize(125, 65))
        font = QFont()
        font.setPointSize(12)
        self.Volume_iconLabel.setFont(font)
        self.Volume_iconLabel.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Volume_iconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Volume_iconLabel.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.Volume_iconLabel)

        self.Volume_LevelLabel = QLabel(self.Volume_frame)
        self.Volume_LevelLabel.setObjectName(u"Volume_LevelLabel")
        self.Volume_LevelLabel.setEnabled(True)
        self.Volume_LevelLabel.setMinimumSize(QSize(125, 65))
        self.Volume_LevelLabel.setMaximumSize(QSize(125, 65))
        font1 = QFont()
        font1.setPointSize(16)
        self.Volume_LevelLabel.setFont(font1)
        self.Volume_LevelLabel.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Volume_LevelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Volume_LevelLabel.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.Volume_LevelLabel)


        self.retranslateUi(Volume_widget)

        QMetaObject.connectSlotsByName(Volume_widget)
    # setupUi

    def retranslateUi(self, Volume_widget):
        self.Volume_iconLabel.setText(QCoreApplication.translate("Volume_widget", u"Volume", None))
        self.Volume_LevelLabel.setText("")
        pass
    # retranslateUi

