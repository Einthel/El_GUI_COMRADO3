# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Music_playlist_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Playlist_qw(object):
    def setupUi(self, Playlist_qw):
        if not Playlist_qw.objectName():
            Playlist_qw.setObjectName(u"Playlist_qw")
        Playlist_qw.setWindowModality(Qt.WindowModality.NonModal)
        Playlist_qw.resize(300, 560)
        self.horizontalLayout = QHBoxLayout(Playlist_qw)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.PL_list_Frame = QFrame(Playlist_qw)
        self.PL_list_Frame.setObjectName(u"PL_list_Frame")
        self.PL_list_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PL_list_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.PL_list_Frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.PL_name_lable = QLabel(self.PL_list_Frame)
        self.PL_name_lable.setObjectName(u"PL_name_lable")

        self.verticalLayout.addWidget(self.PL_name_lable, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.PL_listW = QListWidget(self.PL_list_Frame)
        self.PL_listW.setObjectName(u"PL_listW")

        self.verticalLayout.addWidget(self.PL_listW)

        self.Butt_layout = QHBoxLayout()
        self.Butt_layout.setSpacing(5)
        self.Butt_layout.setObjectName(u"Butt_layout")
        self.back_PL_qBt = QToolButton(self.PL_list_Frame)
        self.back_PL_qBt.setObjectName(u"back_PL_qBt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_PL_qBt.sizePolicy().hasHeightForWidth())
        self.back_PL_qBt.setSizePolicy(sizePolicy)
        self.back_PL_qBt.setMinimumSize(QSize(0, 40))

        self.Butt_layout.addWidget(self.back_PL_qBt)

        self.select_PL_qBt = QToolButton(self.PL_list_Frame)
        self.select_PL_qBt.setObjectName(u"select_PL_qBt")
        sizePolicy.setHeightForWidth(self.select_PL_qBt.sizePolicy().hasHeightForWidth())
        self.select_PL_qBt.setSizePolicy(sizePolicy)
        self.select_PL_qBt.setMinimumSize(QSize(0, 40))

        self.Butt_layout.addWidget(self.select_PL_qBt)


        self.verticalLayout.addLayout(self.Butt_layout)


        self.horizontalLayout.addWidget(self.PL_list_Frame)


        self.retranslateUi(Playlist_qw)

        QMetaObject.connectSlotsByName(Playlist_qw)
    # setupUi

    def retranslateUi(self, Playlist_qw):
        Playlist_qw.setWindowTitle(QCoreApplication.translate("Playlist_qw", u"Playlist's", None))
        self.PL_name_lable.setText(QCoreApplication.translate("Playlist_qw", u"Playlist's", None))
        self.back_PL_qBt.setText(QCoreApplication.translate("Playlist_qw", u"...", None))
        self.select_PL_qBt.setText(QCoreApplication.translate("Playlist_qw", u"...", None))
    # retranslateUi

