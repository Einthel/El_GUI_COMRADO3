# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QWidget)

class Ui_test_widget(object):
    def setupUi(self, test_widget):
        if not test_widget.objectName():
            test_widget.setObjectName(u"test_widget")
        test_widget.setWindowModality(Qt.WindowModality.NonModal)
        test_widget.resize(270, 160)
        test_widget.setMinimumSize(QSize(270, 160))
        test_widget.setMaximumSize(QSize(270, 160))
        test_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        test_widget.setAcceptDrops(True)
        test_widget.setWindowTitle(u"")
        self.frame = QFrame(test_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 270, 160))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.retranslateUi(test_widget)

        QMetaObject.connectSlotsByName(test_widget)
    # setupUi

    def retranslateUi(self, test_widget):
        pass
    # retranslateUi

