# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MusicPlayer.ui'
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
    QLayout, QListWidget, QListWidgetItem, QProgressBar,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Music_player(object):
    def setupUi(self, Music_player):
        if not Music_player.objectName():
            Music_player.setObjectName(u"Music_player")
        Music_player.resize(720, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Music_player.sizePolicy().hasHeightForWidth())
        Music_player.setSizePolicy(sizePolicy)
        Music_player.setMinimumSize(QSize(710, 570))
        Music_player.setMaximumSize(QSize(720, 570))
        self.horizontalLayout_2 = QHBoxLayout(Music_player)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.central_container = QWidget(Music_player)
        self.central_container.setObjectName(u"central_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.central_container.sizePolicy().hasHeightForWidth())
        self.central_container.setSizePolicy(sizePolicy1)
        self.central_container.setMinimumSize(QSize(710, 560))
        self.central_container.setMaximumSize(QSize(710, 560))
        self.PlayList_frame = QFrame(self.central_container)
        self.PlayList_frame.setObjectName(u"PlayList_frame")
        self.PlayList_frame.setGeometry(QRect(357, 0, 345, 550))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PlayList_frame.sizePolicy().hasHeightForWidth())
        self.PlayList_frame.setSizePolicy(sizePolicy2)
        self.PlayList_frame.setMinimumSize(QSize(345, 550))
        self.PlayList_frame.setMaximumSize(QSize(345, 550))
        self.PlayList_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_3 = QVBoxLayout(self.PlayList_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.play_stack = QStackedWidget(self.PlayList_frame)
        self.play_stack.setObjectName(u"play_stack")
        self.play_stack.setFrameShape(QFrame.Shape.StyledPanel)
        self.play_stack.setFrameShadow(QFrame.Shadow.Raised)
        self.playList_page = QWidget()
        self.playList_page.setObjectName(u"playList_page")
        self.playList_listW = QListWidget(self.playList_page)
        self.playList_listW.setObjectName(u"playList_listW")
        self.playList_listW.setGeometry(QRect(30, 20, 260, 380))
        self.play_stack.addWidget(self.playList_page)
        self.songList_page = QWidget()
        self.songList_page.setObjectName(u"songList_page")
        self.songList_listW = QListWidget(self.songList_page)
        self.songList_listW.setObjectName(u"songList_listW")
        self.songList_listW.setGeometry(QRect(30, 20, 260, 380))
        self.play_stack.addWidget(self.songList_page)

        self.verticalLayout_3.addWidget(self.play_stack)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.toolButton = QToolButton(self.PlayList_frame)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy2.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.PlayList_frame)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy2.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.PlayList_frame)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy2.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.toolButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.Music_frame = QFrame(self.central_container)
        self.Music_frame.setObjectName(u"Music_frame")
        self.Music_frame.setGeometry(QRect(6, 0, 345, 550))
        sizePolicy2.setHeightForWidth(self.Music_frame.sizePolicy().hasHeightForWidth())
        self.Music_frame.setSizePolicy(sizePolicy2)
        self.Music_frame.setMinimumSize(QSize(345, 550))
        self.Music_frame.setMaximumSize(QSize(345, 550))
        self.Music_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.Music_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Cover_layout = QVBoxLayout()
        self.Cover_layout.setSpacing(5)
        self.Cover_layout.setObjectName(u"Cover_layout")
        self.Cover_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.Cover_layout.setContentsMargins(5, 5, 5, 5)
        self.Cover_Frame = QFrame(self.Music_frame)
        self.Cover_Frame.setObjectName(u"Cover_Frame")
        self.Cover_Frame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Cover_Frame.sizePolicy().hasHeightForWidth())
        self.Cover_Frame.setSizePolicy(sizePolicy)
        self.Cover_Frame.setMinimumSize(QSize(256, 256))
        self.Cover_Frame.setMaximumSize(QSize(256, 256))
        self.Cover_Frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Cover_Frame.setAutoFillBackground(True)
        self.Cover_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cover_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Cover_Frame.setLineWidth(1)
        self.Cover_Frame.setMidLineWidth(1)

        self.Cover_layout.addWidget(self.Cover_Frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.Playlist_ToolB = QToolButton(self.Music_frame)
        self.Playlist_ToolB.setObjectName(u"Playlist_ToolB")
        self.Playlist_ToolB.setMinimumSize(QSize(40, 40))
        self.Playlist_ToolB.setMaximumSize(QSize(40, 40))
        self.Playlist_ToolB.setIconSize(QSize(40, 40))

        self.Cover_layout.addWidget(self.Playlist_ToolB)


        self.verticalLayout.addLayout(self.Cover_layout)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.Track_Layout = QHBoxLayout()
        self.Track_Layout.setSpacing(5)
        self.Track_Layout.setObjectName(u"Track_Layout")
        self.Track_Layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.Track_Layout.setContentsMargins(5, 5, 5, 5)
        self.Left_Time_label = QLabel(self.Music_frame)
        self.Left_Time_label.setObjectName(u"Left_Time_label")
        sizePolicy.setHeightForWidth(self.Left_Time_label.sizePolicy().hasHeightForWidth())
        self.Left_Time_label.setSizePolicy(sizePolicy)
        self.Left_Time_label.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setPointSize(7)
        self.Left_Time_label.setFont(font)
        self.Left_Time_label.setTextFormat(Qt.TextFormat.RichText)
        self.Left_Time_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.Track_Layout.addWidget(self.Left_Time_label)

        self.Length_track_bar = QProgressBar(self.Music_frame)
        self.Length_track_bar.setObjectName(u"Length_track_bar")
        sizePolicy.setHeightForWidth(self.Length_track_bar.sizePolicy().hasHeightForWidth())
        self.Length_track_bar.setSizePolicy(sizePolicy)
        self.Length_track_bar.setMinimumSize(QSize(240, 30))
        self.Length_track_bar.setMaximumSize(QSize(240, 30))
        self.Length_track_bar.setValue(0)
        self.Length_track_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Length_track_bar.setTextVisible(False)
        self.Length_track_bar.setInvertedAppearance(False)

        self.Track_Layout.addWidget(self.Length_track_bar)

        self.Right_Time_label = QLabel(self.Music_frame)
        self.Right_Time_label.setObjectName(u"Right_Time_label")
        self.Right_Time_label.setMaximumSize(QSize(20, 20))
        self.Right_Time_label.setFont(font)
        self.Right_Time_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.Track_Layout.addWidget(self.Right_Time_label)


        self.verticalLayout.addLayout(self.Track_Layout)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.TrackArtist_layout = QHBoxLayout()
        self.TrackArtist_layout.setSpacing(5)
        self.TrackArtist_layout.setObjectName(u"TrackArtist_layout")
        self.TrackArtist_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.TrackArtist_layout.setContentsMargins(5, 5, 5, 5)
        self.Dis_ToolB = QToolButton(self.Music_frame)
        self.Dis_ToolB.setObjectName(u"Dis_ToolB")
        sizePolicy.setHeightForWidth(self.Dis_ToolB.sizePolicy().hasHeightForWidth())
        self.Dis_ToolB.setSizePolicy(sizePolicy)
        self.Dis_ToolB.setMinimumSize(QSize(40, 40))
        self.Dis_ToolB.setMaximumSize(QSize(40, 40))
        self.Dis_ToolB.setIconSize(QSize(40, 40))
        self.Dis_ToolB.setCheckable(False)

        self.TrackArtist_layout.addWidget(self.Dis_ToolB, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TrackArtist_layout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Artist_label = QLabel(self.Music_frame)
        self.Artist_label.setObjectName(u"Artist_label")
        sizePolicy.setHeightForWidth(self.Artist_label.sizePolicy().hasHeightForWidth())
        self.Artist_label.setSizePolicy(sizePolicy)
        self.Artist_label.setMinimumSize(QSize(200, 25))
        self.Artist_label.setMaximumSize(QSize(200, 25))
        self.Artist_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Artist_label.setFrameShape(QFrame.Shape.NoFrame)
        self.Artist_label.setTextFormat(Qt.TextFormat.RichText)
        self.Artist_label.setScaledContents(False)
        self.Artist_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Artist_label.setMargin(5)

        self.verticalLayout_2.addWidget(self.Artist_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Track_label = QLabel(self.Music_frame)
        self.Track_label.setObjectName(u"Track_label")
        sizePolicy.setHeightForWidth(self.Track_label.sizePolicy().hasHeightForWidth())
        self.Track_label.setSizePolicy(sizePolicy)
        self.Track_label.setMinimumSize(QSize(200, 25))
        self.Track_label.setMaximumSize(QSize(200, 25))
        self.Track_label.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Track_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Track_label.setFrameShape(QFrame.Shape.NoFrame)
        self.Track_label.setLineWidth(1)
        self.Track_label.setTextFormat(Qt.TextFormat.PlainText)
        self.Track_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Track_label.setWordWrap(False)
        self.Track_label.setMargin(5)

        self.verticalLayout_2.addWidget(self.Track_label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.TrackArtist_layout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TrackArtist_layout.addItem(self.horizontalSpacer)

        self.Like_ToolB = QToolButton(self.Music_frame)
        self.Like_ToolB.setObjectName(u"Like_ToolB")
        sizePolicy.setHeightForWidth(self.Like_ToolB.sizePolicy().hasHeightForWidth())
        self.Like_ToolB.setSizePolicy(sizePolicy)
        self.Like_ToolB.setMinimumSize(QSize(40, 40))
        self.Like_ToolB.setMaximumSize(QSize(40, 40))
        self.Like_ToolB.setIconSize(QSize(40, 40))
        self.Like_ToolB.setCheckable(True)

        self.TrackArtist_layout.addWidget(self.Like_ToolB, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addLayout(self.TrackArtist_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.Control_Layout = QHBoxLayout()
        self.Control_Layout.setSpacing(5)
        self.Control_Layout.setObjectName(u"Control_Layout")
        self.Control_Layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.Control_Layout.setContentsMargins(5, 5, 5, 5)
        self.Repeat_ToolB = QToolButton(self.Music_frame)
        self.Repeat_ToolB.setObjectName(u"Repeat_ToolB")
        sizePolicy.setHeightForWidth(self.Repeat_ToolB.sizePolicy().hasHeightForWidth())
        self.Repeat_ToolB.setSizePolicy(sizePolicy)
        self.Repeat_ToolB.setMinimumSize(QSize(40, 40))
        self.Repeat_ToolB.setMaximumSize(QSize(40, 40))
        self.Repeat_ToolB.setIconSize(QSize(40, 40))
        self.Repeat_ToolB.setCheckable(True)

        self.Control_Layout.addWidget(self.Repeat_ToolB)

        self.Previous_ToolB = QToolButton(self.Music_frame)
        self.Previous_ToolB.setObjectName(u"Previous_ToolB")
        sizePolicy.setHeightForWidth(self.Previous_ToolB.sizePolicy().hasHeightForWidth())
        self.Previous_ToolB.setSizePolicy(sizePolicy)
        self.Previous_ToolB.setMinimumSize(QSize(60, 60))
        self.Previous_ToolB.setMaximumSize(QSize(60, 60))
        self.Previous_ToolB.setAutoFillBackground(False)
        self.Previous_ToolB.setIconSize(QSize(65, 65))
        self.Previous_ToolB.setArrowType(Qt.ArrowType.NoArrow)

        self.Control_Layout.addWidget(self.Previous_ToolB)

        self.PlayPause_ToolB = QToolButton(self.Music_frame)
        self.PlayPause_ToolB.setObjectName(u"PlayPause_ToolB")
        sizePolicy.setHeightForWidth(self.PlayPause_ToolB.sizePolicy().hasHeightForWidth())
        self.PlayPause_ToolB.setSizePolicy(sizePolicy)
        self.PlayPause_ToolB.setMinimumSize(QSize(80, 80))
        self.PlayPause_ToolB.setMaximumSize(QSize(80, 80))
        self.PlayPause_ToolB.setAutoFillBackground(False)
        self.PlayPause_ToolB.setIconSize(QSize(80, 80))
        self.PlayPause_ToolB.setCheckable(True)
        self.PlayPause_ToolB.setArrowType(Qt.ArrowType.NoArrow)

        self.Control_Layout.addWidget(self.PlayPause_ToolB)

        self.Next_ToolB = QToolButton(self.Music_frame)
        self.Next_ToolB.setObjectName(u"Next_ToolB")
        sizePolicy.setHeightForWidth(self.Next_ToolB.sizePolicy().hasHeightForWidth())
        self.Next_ToolB.setSizePolicy(sizePolicy)
        self.Next_ToolB.setMinimumSize(QSize(60, 60))
        self.Next_ToolB.setMaximumSize(QSize(60, 60))
        self.Next_ToolB.setAutoFillBackground(False)
        self.Next_ToolB.setIconSize(QSize(65, 65))
        self.Next_ToolB.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.Next_ToolB.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.Next_ToolB.setAutoRaise(False)
        self.Next_ToolB.setArrowType(Qt.ArrowType.NoArrow)

        self.Control_Layout.addWidget(self.Next_ToolB)

        self.Random_ToolB = QToolButton(self.Music_frame)
        self.Random_ToolB.setObjectName(u"Random_ToolB")
        sizePolicy.setHeightForWidth(self.Random_ToolB.sizePolicy().hasHeightForWidth())
        self.Random_ToolB.setSizePolicy(sizePolicy)
        self.Random_ToolB.setMinimumSize(QSize(40, 40))
        self.Random_ToolB.setMaximumSize(QSize(40, 40))
        self.Random_ToolB.setIconSize(QSize(40, 40))
        self.Random_ToolB.setCheckable(True)

        self.Control_Layout.addWidget(self.Random_ToolB)


        self.verticalLayout.addLayout(self.Control_Layout)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.central_container)


        self.retranslateUi(Music_player)

        QMetaObject.connectSlotsByName(Music_player)
    # setupUi

    def retranslateUi(self, Music_player):
        Music_player.setWindowTitle("")
        self.toolButton.setText(QCoreApplication.translate("Music_player", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("Music_player", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("Music_player", u"...", None))
        self.Playlist_ToolB.setText("")
        self.Left_Time_label.setText(QCoreApplication.translate("Music_player", u"0:00", None))
        self.Right_Time_label.setText(QCoreApplication.translate("Music_player", u"0:00", None))
        self.Dis_ToolB.setText("")
        self.Artist_label.setText(QCoreApplication.translate("Music_player", u"TextLabel", None))
        self.Track_label.setText(QCoreApplication.translate("Music_player", u"Track", None))
        self.Like_ToolB.setText("")
        self.Repeat_ToolB.setText("")
        self.Previous_ToolB.setText("")
        self.PlayPause_ToolB.setText("")
        self.Next_ToolB.setText("")
        self.Random_ToolB.setText("")
    # retranslateUi

