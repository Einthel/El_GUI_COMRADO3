# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'storage_GB.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_storage_GB(object):
    def setupUi(self, storage_GB):
        if not storage_GB.objectName():
            storage_GB.setObjectName(u"storage_GB")
        storage_GB.resize(250, 80)
        storage_GB.setMinimumSize(QSize(250, 80))
        storage_GB.setMaximumSize(QSize(250, 80))
        self.verticalLayout = QVBoxLayout(storage_GB)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.storage_groupB_1 = QGroupBox(storage_GB)
        self.storage_groupB_1.setObjectName(u"storage_groupB_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storage_groupB_1.sizePolicy().hasHeightForWidth())
        self.storage_groupB_1.setSizePolicy(sizePolicy)
        self.storage_groupB_1.setMinimumSize(QSize(250, 80))
        self.storage_groupB_1.setMaximumSize(QSize(250, 80))
        self.storage_groupB_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.storage_groupB_1.setFlat(False)
        self.storage_groupB_1.setCheckable(False)
        self.verticalLayout_11 = QVBoxLayout(self.storage_groupB_1)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.name_temp_layout = QHBoxLayout()
        self.name_temp_layout.setSpacing(5)
        self.name_temp_layout.setObjectName(u"name_temp_layout")
        self.name_storage_1 = QLabel(self.storage_groupB_1)
        self.name_storage_1.setObjectName(u"name_storage_1")
        self.name_storage_1.setMinimumSize(QSize(0, 20))
        self.name_storage_1.setMaximumSize(QSize(16777215, 20))

        self.name_temp_layout.addWidget(self.name_storage_1)

        self.temp_storage_lable_1 = QLabel(self.storage_groupB_1)
        self.temp_storage_lable_1.setObjectName(u"temp_storage_lable_1")
        self.temp_storage_lable_1.setMinimumSize(QSize(0, 20))
        self.temp_storage_lable_1.setMaximumSize(QSize(16777215, 20))
        self.temp_storage_lable_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.name_temp_layout.addWidget(self.temp_storage_lable_1)


        self.verticalLayout_11.addLayout(self.name_temp_layout)

        self.progressBar_storage_1 = QProgressBar(self.storage_groupB_1)
        self.progressBar_storage_1.setObjectName(u"progressBar_storage_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar_storage_1.sizePolicy().hasHeightForWidth())
        self.progressBar_storage_1.setSizePolicy(sizePolicy1)
        self.progressBar_storage_1.setMinimumSize(QSize(230, 30))
        self.progressBar_storage_1.setMaximumSize(QSize(230, 30))
        self.progressBar_storage_1.setValue(0)
        self.progressBar_storage_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_storage_1.setTextVisible(True)
        self.progressBar_storage_1.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar_storage_1.setInvertedAppearance(False)
        self.progressBar_storage_1.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_11.addWidget(self.progressBar_storage_1)

        self.lable_GB_storage_1 = QHBoxLayout()
        self.lable_GB_storage_1.setSpacing(0)
        self.lable_GB_storage_1.setObjectName(u"lable_GB_storage_1")
        self.lable_GB_storage_1.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.freeGB_storage_label_1 = QLabel(self.storage_groupB_1)
        self.freeGB_storage_label_1.setObjectName(u"freeGB_storage_label_1")
        self.freeGB_storage_label_1.setMinimumSize(QSize(0, 20))
        self.freeGB_storage_label_1.setMaximumSize(QSize(16777215, 20))

        self.lable_GB_storage_1.addWidget(self.freeGB_storage_label_1)

        self.totalGB_storage_lable_1 = QLabel(self.storage_groupB_1)
        self.totalGB_storage_lable_1.setObjectName(u"totalGB_storage_lable_1")
        self.totalGB_storage_lable_1.setMinimumSize(QSize(0, 20))
        self.totalGB_storage_lable_1.setMaximumSize(QSize(16777215, 20))
        self.totalGB_storage_lable_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.lable_GB_storage_1.addWidget(self.totalGB_storage_lable_1)


        self.verticalLayout_11.addLayout(self.lable_GB_storage_1)


        self.verticalLayout.addWidget(self.storage_groupB_1)


        self.retranslateUi(storage_GB)

        QMetaObject.connectSlotsByName(storage_GB)
    # setupUi

    def retranslateUi(self, storage_GB):
        self.storage_groupB_1.setTitle("")
        self.name_storage_1.setText(QCoreApplication.translate("storage_GB", u"storageName", None))
        self.temp_storage_lable_1.setText(QCoreApplication.translate("storage_GB", u"temp", None))
        self.progressBar_storage_1.setFormat(QCoreApplication.translate("storage_GB", u"%p%", None))
        self.freeGB_storage_label_1.setText(QCoreApplication.translate("storage_GB", u"freeGB", None))
        self.totalGB_storage_lable_1.setText(QCoreApplication.translate("storage_GB", u"totalGB", None))
        pass
    # retranslateUi

