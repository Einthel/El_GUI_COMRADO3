# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Music_widget.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Music_widget(object):
    def setupUi(self, Music_widget):
        if not Music_widget.objectName():
            Music_widget.setObjectName(u"Music_widget")
        Music_widget.setWindowModality(Qt.WindowModality.NonModal)
        Music_widget.resize(270, 80)
        Music_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        Music_widget.setAcceptDrops(True)
        Music_widget.setWindowTitle(u"")
        self.Music_frame = QFrame(Music_widget)
        self.Music_frame.setObjectName(u"Music_frame")
        self.Music_frame.setGeometry(QRect(0, 0, 270, 80))
        self.Music_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Music_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Music_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 7, 5, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.Music_song_Label = QLabel(self.Music_frame)
        self.Music_song_Label.setObjectName(u"Music_song_Label")
        font = QFont()
        font.setPointSize(16)
        self.Music_song_Label.setFont(font)
        self.Music_song_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Music_song_Label)

        self.Music_artist_Label = QLabel(self.Music_frame)
        self.Music_artist_Label.setObjectName(u"Music_artist_Label")
        self.Music_artist_Label.setFont(font)
        self.Music_artist_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Music_artist_Label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.Music_timet_Label = QLabel(self.Music_frame)
        self.Music_timet_Label.setObjectName(u"Music_timet_Label")
        self.Music_timet_Label.setFont(font)
        self.Music_timet_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Music_timet_Label)


        self.retranslateUi(Music_widget)

        QMetaObject.connectSlotsByName(Music_widget)
    # setupUi

    def retranslateUi(self, Music_widget):
        self.Music_song_Label.setText("")
        self.Music_artist_Label.setText("")
        self.Music_timet_Label.setText("")
        pass
    # retranslateUi

