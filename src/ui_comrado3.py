# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comrado3.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QListView, QMainWindow,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1024, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1024, 600))
        MainWindow.setMaximumSize(QSize(1024, 1800))
        MainWindow.setTabletTracking(True)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        MainWindow.setWindowTitle(u"EL GUI COMRADO v 0.6.2")
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.Main_Frame = QFrame(self.centralwidget)
        self.Main_Frame.setObjectName(u"Main_Frame")
        self.Main_Frame.setGeometry(QRect(0, 0, 1000, 600))
        self.Main_Frame.setMinimumSize(QSize(1000, 600))
        self.Main_Frame.setMaximumSize(QSize(1000, 600))
        self.Main_Frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Main_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Main_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Main_Frame.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.Main_Frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.Widget_bar_frame = QFrame(self.Main_Frame)
        self.Widget_bar_frame.setObjectName(u"Widget_bar_frame")
        self.Widget_bar_frame.setMinimumSize(QSize(280, 570))
        self.Widget_bar_frame.setMaximumSize(QSize(280, 570))
        self.Widget_bar_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.Widget_bar_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.Widget_bar_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.Widget_bar_frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 0, 0, 0)
        self._1Main_tab = QWidget(self.Widget_bar_frame)
        self._1Main_tab.setObjectName(u"_1Main_tab")
        self._1Main_tab.setEnabled(True)
        sizePolicy.setHeightForWidth(self._1Main_tab.sizePolicy().hasHeightForWidth())
        self._1Main_tab.setSizePolicy(sizePolicy)
        self._1Main_tab.setMinimumSize(QSize(270, 136))
        self._1Main_tab.setMaximumSize(QSize(270, 136))
        self._1Main_tab.setStyleSheet(u"background-color: rgb(170, 22, 22);")
        self.verticalLayout_6 = QVBoxLayout(self._1Main_tab)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 15, 10)
        self.Time_GB = QGroupBox(self._1Main_tab)
        self.Time_GB.setObjectName(u"Time_GB")
        self.Time_GB.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_10 = QHBoxLayout(self.Time_GB)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.HH = QHBoxLayout()
        self.HH.setObjectName(u"HH")
        self.HH_lcdN = QLCDNumber(self.Time_GB)
        self.HH_lcdN.setObjectName(u"HH_lcdN")
        self.HH_lcdN.setFrameShape(QFrame.Shape.Panel)
        self.HH_lcdN.setFrameShadow(QFrame.Shadow.Raised)
        self.HH_lcdN.setSmallDecimalPoint(False)
        self.HH_lcdN.setDigitCount(2)
        self.HH_lcdN.setMode(QLCDNumber.Mode.Dec)
        self.HH_lcdN.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)

        self.HH.addWidget(self.HH_lcdN)


        self.horizontalLayout_10.addLayout(self.HH)

        self.MM = QHBoxLayout()
        self.MM.setObjectName(u"MM")
        self.MM_lcdN = QLCDNumber(self.Time_GB)
        self.MM_lcdN.setObjectName(u"MM_lcdN")
        self.MM_lcdN.setFrameShape(QFrame.Shape.Panel)
        self.MM_lcdN.setFrameShadow(QFrame.Shadow.Raised)
        self.MM_lcdN.setSmallDecimalPoint(False)
        self.MM_lcdN.setDigitCount(2)
        self.MM_lcdN.setMode(QLCDNumber.Mode.Dec)
        self.MM_lcdN.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)

        self.MM.addWidget(self.MM_lcdN)


        self.horizontalLayout_10.addLayout(self.MM)


        self.verticalLayout_6.addWidget(self.Time_GB)


        self.verticalLayout.addWidget(self._1Main_tab)

        self._2Button_tab = QWidget(self.Widget_bar_frame)
        self._2Button_tab.setObjectName(u"_2Button_tab")
        sizePolicy.setHeightForWidth(self._2Button_tab.sizePolicy().hasHeightForWidth())
        self._2Button_tab.setSizePolicy(sizePolicy)
        self._2Button_tab.setMinimumSize(QSize(270, 136))
        self._2Button_tab.setMaximumSize(QSize(270, 136))

        self.verticalLayout.addWidget(self._2Button_tab, 0, Qt.AlignmentFlag.AlignHCenter)

        self._3Settings_tab = QWidget(self.Widget_bar_frame)
        self._3Settings_tab.setObjectName(u"_3Settings_tab")
        sizePolicy.setHeightForWidth(self._3Settings_tab.sizePolicy().hasHeightForWidth())
        self._3Settings_tab.setSizePolicy(sizePolicy)
        self._3Settings_tab.setMinimumSize(QSize(270, 136))
        self._3Settings_tab.setMaximumSize(QSize(270, 136))

        self.verticalLayout.addWidget(self._3Settings_tab, 0, Qt.AlignmentFlag.AlignHCenter)

        self._4Music_tab = QWidget(self.Widget_bar_frame)
        self._4Music_tab.setObjectName(u"_4Music_tab")
        sizePolicy.setHeightForWidth(self._4Music_tab.sizePolicy().hasHeightForWidth())
        self._4Music_tab.setSizePolicy(sizePolicy)
        self._4Music_tab.setMinimumSize(QSize(270, 136))
        self._4Music_tab.setMaximumSize(QSize(270, 136))
        self._4Music_tab.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self._4Music_tab)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 10, 5, 10)
        self.frame = QFrame(self._4Music_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.Sound_ToolB = QToolButton(self.frame)
        self.Sound_ToolB.setObjectName(u"Sound_ToolB")
        sizePolicy.setHeightForWidth(self.Sound_ToolB.sizePolicy().hasHeightForWidth())
        self.Sound_ToolB.setSizePolicy(sizePolicy)
        self.Sound_ToolB.setMaximumSize(QSize(40, 40))
        self.Sound_ToolB.setIconSize(QSize(40, 40))
        self.Sound_ToolB.setCheckable(False)

        self.horizontalLayout_9.addWidget(self.Sound_ToolB)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self._4Music_tab, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.Widget_bar_frame, 0, Qt.AlignmentFlag.AlignRight)

        self.Main_stackW = QStackedWidget(self.Main_Frame)
        self.Main_stackW.setObjectName(u"Main_stackW")
        self.Main_stackW.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Main_stackW.sizePolicy().hasHeightForWidth())
        self.Main_stackW.setSizePolicy(sizePolicy)
        self.Main_stackW.setMinimumSize(QSize(700, 570))
        self.Main_stackW.setMaximumSize(QSize(700, 570))
        self.Main_stackW.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Main_stackW.setStyleSheet(u"")
        self.Main_stackW.setFrameShape(QFrame.Shape.NoFrame)
        self.Main_stackW.setFrameShadow(QFrame.Shadow.Plain)
        self.Main_stackW.setLineWidth(1)
        self.Main_page = QWidget()
        self.Main_page.setObjectName(u"Main_page")
        self.Main_page.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Main_page.sizePolicy().hasHeightForWidth())
        self.Main_page.setSizePolicy(sizePolicy)
        self.Main_page.setMinimumSize(QSize(700, 570))
        self.Main_page.setMaximumSize(QSize(16777215, 570))
        self.Title_main_W = QWidget(self.Main_page)
        self.Title_main_W.setObjectName(u"Title_main_W")
        self.Title_main_W.setGeometry(QRect(0, 0, 700, 570))
        self.Title_main_W.setMinimumSize(QSize(700, 570))
        self.Title_main_W.setMaximumSize(QSize(700, 560))
        self.horizontalLayout_5 = QHBoxLayout(self.Title_main_W)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Left_layout = QVBoxLayout()
        self.Left_layout.setSpacing(5)
        self.Left_layout.setObjectName(u"Left_layout")
        self.Left_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.GPU_frame = QFrame(self.Title_main_W)
        self.GPU_frame.setObjectName(u"GPU_frame")
        self.GPU_frame.setMinimumSize(QSize(250, 250))
        self.GPU_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.GPU_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.GPU_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.name_gpu_layout = QHBoxLayout()
        self.name_gpu_layout.setSpacing(5)
        self.name_gpu_layout.setObjectName(u"name_gpu_layout")
        self.name_gpu = QLabel(self.GPU_frame)
        self.name_gpu.setObjectName(u"name_gpu")
        font = QFont()
        font.setPointSize(12)
        self.name_gpu.setFont(font)
        self.name_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.name_gpu_layout.addWidget(self.name_gpu)

        self.value_name_gpu = QLabel(self.GPU_frame)
        self.value_name_gpu.setObjectName(u"value_name_gpu")
        self.value_name_gpu.setFont(font)
        self.value_name_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.name_gpu_layout.addWidget(self.value_name_gpu)


        self.verticalLayout_12.addLayout(self.name_gpu_layout)

        self.load_gpu_layout = QHBoxLayout()
        self.load_gpu_layout.setObjectName(u"load_gpu_layout")
        self.load_gpu = QLabel(self.GPU_frame)
        self.load_gpu.setObjectName(u"load_gpu")
        self.load_gpu.setFont(font)
        self.load_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.load_gpu_layout.addWidget(self.load_gpu)

        self.value_load_gpu = QLabel(self.GPU_frame)
        self.value_load_gpu.setObjectName(u"value_load_gpu")
        self.value_load_gpu.setFont(font)
        self.value_load_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.load_gpu_layout.addWidget(self.value_load_gpu)


        self.verticalLayout_12.addLayout(self.load_gpu_layout)

        self.temp_gpu_layout = QHBoxLayout()
        self.temp_gpu_layout.setObjectName(u"temp_gpu_layout")
        self.temp_gpu = QLabel(self.GPU_frame)
        self.temp_gpu.setObjectName(u"temp_gpu")
        self.temp_gpu.setFont(font)
        self.temp_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.temp_gpu_layout.addWidget(self.temp_gpu)

        self.value_temp_gpu = QLabel(self.GPU_frame)
        self.value_temp_gpu.setObjectName(u"value_temp_gpu")
        self.value_temp_gpu.setFont(font)
        self.value_temp_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.temp_gpu_layout.addWidget(self.value_temp_gpu)


        self.verticalLayout_12.addLayout(self.temp_gpu_layout)

        self.tempHot_gpu_layout = QHBoxLayout()
        self.tempHot_gpu_layout.setObjectName(u"tempHot_gpu_layout")
        self.tempHot_gpu = QLabel(self.GPU_frame)
        self.tempHot_gpu.setObjectName(u"tempHot_gpu")
        self.tempHot_gpu.setFont(font)
        self.tempHot_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.tempHot_gpu_layout.addWidget(self.tempHot_gpu)

        self.value_temHot_gpu = QLabel(self.GPU_frame)
        self.value_temHot_gpu.setObjectName(u"value_temHot_gpu")
        self.value_temHot_gpu.setFont(font)
        self.value_temHot_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.tempHot_gpu_layout.addWidget(self.value_temHot_gpu)


        self.verticalLayout_12.addLayout(self.tempHot_gpu_layout)

        self.power_gpu_layout = QHBoxLayout()
        self.power_gpu_layout.setObjectName(u"power_gpu_layout")
        self.power_gpu = QLabel(self.GPU_frame)
        self.power_gpu.setObjectName(u"power_gpu")
        self.power_gpu.setFont(font)
        self.power_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.power_gpu_layout.addWidget(self.power_gpu)

        self.value_power_gpu = QLabel(self.GPU_frame)
        self.value_power_gpu.setObjectName(u"value_power_gpu")
        self.value_power_gpu.setFont(font)
        self.value_power_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.power_gpu_layout.addWidget(self.value_power_gpu)


        self.verticalLayout_12.addLayout(self.power_gpu_layout)

        self.clocks_gpu_layout = QHBoxLayout()
        self.clocks_gpu_layout.setObjectName(u"clocks_gpu_layout")
        self.clocks_gpu = QLabel(self.GPU_frame)
        self.clocks_gpu.setObjectName(u"clocks_gpu")
        self.clocks_gpu.setFont(font)
        self.clocks_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.clocks_gpu_layout.addWidget(self.clocks_gpu)

        self.value_clocks_gpu = QLabel(self.GPU_frame)
        self.value_clocks_gpu.setObjectName(u"value_clocks_gpu")
        self.value_clocks_gpu.setFont(font)
        self.value_clocks_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.clocks_gpu_layout.addWidget(self.value_clocks_gpu)


        self.verticalLayout_12.addLayout(self.clocks_gpu_layout)

        self.fanPer_gpu_layout = QHBoxLayout()
        self.fanPer_gpu_layout.setObjectName(u"fanPer_gpu_layout")
        self.fanPer_gpu = QLabel(self.GPU_frame)
        self.fanPer_gpu.setObjectName(u"fanPer_gpu")
        self.fanPer_gpu.setFont(font)
        self.fanPer_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.fanPer_gpu_layout.addWidget(self.fanPer_gpu)

        self.value_fanPer_gpu = QLabel(self.GPU_frame)
        self.value_fanPer_gpu.setObjectName(u"value_fanPer_gpu")
        self.value_fanPer_gpu.setFont(font)
        self.value_fanPer_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.fanPer_gpu_layout.addWidget(self.value_fanPer_gpu)


        self.verticalLayout_12.addLayout(self.fanPer_gpu_layout)

        self.fanRPM_gpu_layout = QHBoxLayout()
        self.fanRPM_gpu_layout.setObjectName(u"fanRPM_gpu_layout")
        self.fanRPM_gpu = QLabel(self.GPU_frame)
        self.fanRPM_gpu.setObjectName(u"fanRPM_gpu")
        self.fanRPM_gpu.setFont(font)
        self.fanRPM_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.fanRPM_gpu_layout.addWidget(self.fanRPM_gpu)

        self.value_fanRPM_gpu = QLabel(self.GPU_frame)
        self.value_fanRPM_gpu.setObjectName(u"value_fanRPM_gpu")
        self.value_fanRPM_gpu.setFont(font)
        self.value_fanRPM_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.fanRPM_gpu_layout.addWidget(self.value_fanRPM_gpu)


        self.verticalLayout_12.addLayout(self.fanRPM_gpu_layout)

        self.vramUMb_gpu_layout = QHBoxLayout()
        self.vramUMb_gpu_layout.setObjectName(u"vramUMb_gpu_layout")
        self.vramUMb_gpu = QLabel(self.GPU_frame)
        self.vramUMb_gpu.setObjectName(u"vramUMb_gpu")
        self.vramUMb_gpu.setFont(font)
        self.vramUMb_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.vramUMb_gpu_layout.addWidget(self.vramUMb_gpu)

        self.value_vramUMb_gpu = QLabel(self.GPU_frame)
        self.value_vramUMb_gpu.setObjectName(u"value_vramUMb_gpu")
        self.value_vramUMb_gpu.setFont(font)
        self.value_vramUMb_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.vramUMb_gpu_layout.addWidget(self.value_vramUMb_gpu)


        self.verticalLayout_12.addLayout(self.vramUMb_gpu_layout)

        self.vramUPer_gpu_layout = QHBoxLayout()
        self.vramUPer_gpu_layout.setObjectName(u"vramUPer_gpu_layout")
        self.vramUPer_gpu = QLabel(self.GPU_frame)
        self.vramUPer_gpu.setObjectName(u"vramUPer_gpu")
        self.vramUPer_gpu.setFont(font)
        self.vramUPer_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.vramUPer_gpu_layout.addWidget(self.vramUPer_gpu)

        self.value_vramUPer_gpu = QLabel(self.GPU_frame)
        self.value_vramUPer_gpu.setObjectName(u"value_vramUPer_gpu")
        self.value_vramUPer_gpu.setFont(font)
        self.value_vramUPer_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.vramUPer_gpu_layout.addWidget(self.value_vramUPer_gpu)


        self.verticalLayout_12.addLayout(self.vramUPer_gpu_layout)

        self.vram_total_gpu_layout = QHBoxLayout()
        self.vram_total_gpu_layout.setObjectName(u"vram_total_gpu_layout")
        self.vram_total_gpu = QLabel(self.GPU_frame)
        self.vram_total_gpu.setObjectName(u"vram_total_gpu")
        self.vram_total_gpu.setFont(font)
        self.vram_total_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.vram_total_gpu_layout.addWidget(self.vram_total_gpu)

        self.value_vram_total_gpu = QLabel(self.GPU_frame)
        self.value_vram_total_gpu.setObjectName(u"value_vram_total_gpu")
        self.value_vram_total_gpu.setFont(font)
        self.value_vram_total_gpu.setFrameShape(QFrame.Shape.NoFrame)

        self.vram_total_gpu_layout.addWidget(self.value_vram_total_gpu)


        self.verticalLayout_12.addLayout(self.vram_total_gpu_layout)


        self.Left_layout.addWidget(self.GPU_frame)

        self.CPU_Frame = QFrame(self.Title_main_W)
        self.CPU_Frame.setObjectName(u"CPU_Frame")
        self.CPU_Frame.setMinimumSize(QSize(400, 120))
        self.CPU_Frame.setMaximumSize(QSize(400, 240))
        self.CPU_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.CPU_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.CPU_Frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.name_cpu_layout = QHBoxLayout()
        self.name_cpu_layout.setSpacing(5)
        self.name_cpu_layout.setObjectName(u"name_cpu_layout")
        self.name_cpu = QLabel(self.CPU_Frame)
        self.name_cpu.setObjectName(u"name_cpu")
        self.name_cpu.setFont(font)
        self.name_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.name_cpu_layout.addWidget(self.name_cpu)

        self.value_name_cpu = QLabel(self.CPU_Frame)
        self.value_name_cpu.setObjectName(u"value_name_cpu")
        self.value_name_cpu.setFont(font)
        self.value_name_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.name_cpu_layout.addWidget(self.value_name_cpu)


        self.verticalLayout_13.addLayout(self.name_cpu_layout)

        self.load_cpu_layout = QHBoxLayout()
        self.load_cpu_layout.setObjectName(u"load_cpu_layout")
        self.load_cpu = QLabel(self.CPU_Frame)
        self.load_cpu.setObjectName(u"load_cpu")
        self.load_cpu.setFont(font)
        self.load_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.load_cpu_layout.addWidget(self.load_cpu)

        self.value_load_cpu = QLabel(self.CPU_Frame)
        self.value_load_cpu.setObjectName(u"value_load_cpu")
        self.value_load_cpu.setFont(font)
        self.value_load_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.load_cpu_layout.addWidget(self.value_load_cpu)


        self.verticalLayout_13.addLayout(self.load_cpu_layout)

        self.clocks_cpu_layout = QHBoxLayout()
        self.clocks_cpu_layout.setObjectName(u"clocks_cpu_layout")
        self.clocks_cpu = QLabel(self.CPU_Frame)
        self.clocks_cpu.setObjectName(u"clocks_cpu")
        self.clocks_cpu.setFont(font)
        self.clocks_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.clocks_cpu_layout.addWidget(self.clocks_cpu)

        self.value_clocks_cpu = QLabel(self.CPU_Frame)
        self.value_clocks_cpu.setObjectName(u"value_clocks_cpu")
        self.value_clocks_cpu.setFont(font)
        self.value_clocks_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.clocks_cpu_layout.addWidget(self.value_clocks_cpu)


        self.verticalLayout_13.addLayout(self.clocks_cpu_layout)

        self.temp_cpu_layout = QHBoxLayout()
        self.temp_cpu_layout.setObjectName(u"temp_cpu_layout")
        self.temp_cpu = QLabel(self.CPU_Frame)
        self.temp_cpu.setObjectName(u"temp_cpu")
        self.temp_cpu.setFont(font)
        self.temp_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.temp_cpu_layout.addWidget(self.temp_cpu)

        self.value_temp_cpu = QLabel(self.CPU_Frame)
        self.value_temp_cpu.setObjectName(u"value_temp_cpu")
        self.value_temp_cpu.setFont(font)
        self.value_temp_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.temp_cpu_layout.addWidget(self.value_temp_cpu)


        self.verticalLayout_13.addLayout(self.temp_cpu_layout)

        self.power_cpu_layout = QHBoxLayout()
        self.power_cpu_layout.setObjectName(u"power_cpu_layout")
        self.power_cpu = QLabel(self.CPU_Frame)
        self.power_cpu.setObjectName(u"power_cpu")
        self.power_cpu.setFont(font)
        self.power_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.power_cpu_layout.addWidget(self.power_cpu)

        self.value_power_cpu = QLabel(self.CPU_Frame)
        self.value_power_cpu.setObjectName(u"value_power_cpu")
        self.value_power_cpu.setFont(font)
        self.value_power_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.power_cpu_layout.addWidget(self.value_power_cpu)


        self.verticalLayout_13.addLayout(self.power_cpu_layout)

        self.fan_cpu_layout = QHBoxLayout()
        self.fan_cpu_layout.setObjectName(u"fan_cpu_layout")
        self.fan_speed_cpu = QLabel(self.CPU_Frame)
        self.fan_speed_cpu.setObjectName(u"fan_speed_cpu")
        self.fan_speed_cpu.setFont(font)
        self.fan_speed_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.fan_cpu_layout.addWidget(self.fan_speed_cpu)

        self.value_fan_speed_cpu = QLabel(self.CPU_Frame)
        self.value_fan_speed_cpu.setObjectName(u"value_fan_speed_cpu")
        self.value_fan_speed_cpu.setFont(font)
        self.value_fan_speed_cpu.setFrameShape(QFrame.Shape.NoFrame)

        self.fan_cpu_layout.addWidget(self.value_fan_speed_cpu)


        self.verticalLayout_13.addLayout(self.fan_cpu_layout)


        self.Left_layout.addWidget(self.CPU_Frame)


        self.horizontalLayout_5.addLayout(self.Left_layout)

        self.Right_layout = QVBoxLayout()
        self.Right_layout.setSpacing(5)
        self.Right_layout.setObjectName(u"Right_layout")
        self.Ram_frame = QFrame(self.Title_main_W)
        self.Ram_frame.setObjectName(u"Ram_frame")
        self.Ram_frame.setMinimumSize(QSize(270, 0))
        self.Ram_frame.setMaximumSize(QSize(270, 16777215))
        self.Ram_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Ram_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Ram_frame_layout = QVBoxLayout(self.Ram_frame)
        self.Ram_frame_layout.setSpacing(5)
        self.Ram_frame_layout.setObjectName(u"Ram_frame_layout")
        self.Ram_frame_layout.setContentsMargins(5, 5, 5, 5)
        self.ram_layout = QVBoxLayout()
        self.ram_layout.setSpacing(5)
        self.ram_layout.setObjectName(u"ram_layout")
        self.ram_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ram_layout.setContentsMargins(5, 0, 5, 0)
        self.name_ram = QLabel(self.Ram_frame)
        self.name_ram.setObjectName(u"name_ram")
        self.name_ram.setMinimumSize(QSize(0, 20))
        self.name_ram.setMaximumSize(QSize(16777215, 20))

        self.ram_layout.addWidget(self.name_ram)

        self.progressBar_ram = QProgressBar(self.Ram_frame)
        self.progressBar_ram.setObjectName(u"progressBar_ram")
        sizePolicy.setHeightForWidth(self.progressBar_ram.sizePolicy().hasHeightForWidth())
        self.progressBar_ram.setSizePolicy(sizePolicy)
        self.progressBar_ram.setMinimumSize(QSize(240, 30))
        self.progressBar_ram.setMaximumSize(QSize(240, 30))
        self.progressBar_ram.setValue(0)
        self.progressBar_ram.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_ram.setTextVisible(True)
        self.progressBar_ram.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar_ram.setInvertedAppearance(False)
        self.progressBar_ram.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.ram_layout.addWidget(self.progressBar_ram, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.lable_GB_ram = QHBoxLayout()
        self.lable_GB_ram.setSpacing(0)
        self.lable_GB_ram.setObjectName(u"lable_GB_ram")
        self.lable_GB_ram.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.value_freeGB_ram_label = QLabel(self.Ram_frame)
        self.value_freeGB_ram_label.setObjectName(u"value_freeGB_ram_label")
        self.value_freeGB_ram_label.setMinimumSize(QSize(0, 20))
        self.value_freeGB_ram_label.setMaximumSize(QSize(16777215, 20))

        self.lable_GB_ram.addWidget(self.value_freeGB_ram_label)

        self.value_totalGB_ram_lable = QLabel(self.Ram_frame)
        self.value_totalGB_ram_lable.setObjectName(u"value_totalGB_ram_lable")
        self.value_totalGB_ram_lable.setMinimumSize(QSize(0, 20))
        self.value_totalGB_ram_lable.setMaximumSize(QSize(16777215, 20))
        self.value_totalGB_ram_lable.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.lable_GB_ram.addWidget(self.value_totalGB_ram_lable)


        self.ram_layout.addLayout(self.lable_GB_ram)

        self.ram_layout.setStretch(1, 2)
        self.ram_layout.setStretch(2, 1)

        self.Ram_frame_layout.addLayout(self.ram_layout)


        self.Right_layout.addWidget(self.Ram_frame)

        self.Network_frame = QFrame(self.Title_main_W)
        self.Network_frame.setObjectName(u"Network_frame")
        self.Network_frame.setMinimumSize(QSize(270, 0))
        self.Network_frame.setMaximumSize(QSize(270, 16777215))
        self.Network_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Network_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Network_frame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.upload_layout = QHBoxLayout()
        self.upload_layout.setSpacing(5)
        self.upload_layout.setObjectName(u"upload_layout")
        self.upload_lable = QLabel(self.Network_frame)
        self.upload_lable.setObjectName(u"upload_lable")
        font1 = QFont()
        font1.setPointSize(10)
        self.upload_lable.setFont(font1)

        self.upload_layout.addWidget(self.upload_lable)

        self.value_upload__net = QLabel(self.Network_frame)
        self.value_upload__net.setObjectName(u"value_upload__net")
        self.value_upload__net.setFont(font)
        self.value_upload__net.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.value_upload__net.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.upload_layout.addWidget(self.value_upload__net)


        self.verticalLayout_4.addLayout(self.upload_layout)

        self.download_layout = QHBoxLayout()
        self.download_layout.setSpacing(5)
        self.download_layout.setObjectName(u"download_layout")
        self.download_lable = QLabel(self.Network_frame)
        self.download_lable.setObjectName(u"download_lable")
        self.download_lable.setFont(font1)

        self.download_layout.addWidget(self.download_lable)

        self.value_download_net = QLabel(self.Network_frame)
        self.value_download_net.setObjectName(u"value_download_net")
        self.value_download_net.setFont(font)
        self.value_download_net.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.value_download_net.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.download_layout.addWidget(self.value_download_net)


        self.verticalLayout_4.addLayout(self.download_layout)


        self.Right_layout.addWidget(self.Network_frame)

        self.Storage_scrollArea = QScrollArea(self.Title_main_W)
        self.Storage_scrollArea.setObjectName(u"Storage_scrollArea")
        sizePolicy.setHeightForWidth(self.Storage_scrollArea.sizePolicy().hasHeightForWidth())
        self.Storage_scrollArea.setSizePolicy(sizePolicy)
        self.Storage_scrollArea.setMinimumSize(QSize(270, 0))
        self.Storage_scrollArea.setMaximumSize(QSize(270, 350))
        self.Storage_scrollArea.setLineWidth(1)
        self.Storage_scrollArea.setMidLineWidth(1)
        self.Storage_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Storage_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Storage_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.Storage_scrollArea.setWidgetResizable(True)
        self.Storage_scrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.storage_scrollAW = QWidget()
        self.storage_scrollAW.setObjectName(u"storage_scrollAW")
        self.storage_scrollAW.setGeometry(QRect(0, 0, 256, 348))
        self.storage_container_layout = QVBoxLayout(self.storage_scrollAW)
        self.storage_container_layout.setSpacing(5)
        self.storage_container_layout.setObjectName(u"storage_container_layout")
        self.storage_container_layout.setContentsMargins(5, 5, 5, 5)
        self.Storage_scrollArea.setWidget(self.storage_scrollAW)

        self.Right_layout.addWidget(self.Storage_scrollArea)

        self.Right_layout.setStretch(0, 2)
        self.Right_layout.setStretch(1, 2)
        self.Right_layout.setStretch(2, 8)

        self.horizontalLayout_5.addLayout(self.Right_layout)

        self.Main_stackW.addWidget(self.Main_page)
        self.Button_page = QWidget()
        self.Button_page.setObjectName(u"Button_page")
        self.Button_page.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Button_page.sizePolicy().hasHeightForWidth())
        self.Button_page.setSizePolicy(sizePolicy)
        self.Button_page.setMinimumSize(QSize(700, 570))
        self.Button_page.setMaximumSize(QSize(16777215, 570))
        self.horizontalLayout_4 = QHBoxLayout(self.Button_page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.Button_stackedWidget = QStackedWidget(self.Button_page)
        self.Button_stackedWidget.setObjectName(u"Button_stackedWidget")
        self.Button_stackedWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Button_stackedWidget.sizePolicy().hasHeightForWidth())
        self.Button_stackedWidget.setSizePolicy(sizePolicy)
        self.Button_stackedWidget.setMinimumSize(QSize(690, 560))
        self.Button_stackedWidget.setMaximumSize(QSize(690, 560))
        self.Button_stackedWidget.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(5)
        self.Button_stackedWidget.setFont(font2)
        self.Button_stackedWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Button_stackedWidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.Button_stackedWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.Button_stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Button_stackedWidget.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.Button_stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.Button_stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.Button_stackedWidget.setLineWidth(0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy)
        self.page_1.setMaximumSize(QSize(680, 560))
        self.page_1.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.page_1.setToolTipDuration(-1)
        self.page_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_1.setAutoFillBackground(False)
        self.gridLayout_6 = QGridLayout(self.page_1)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.Button_frame_01 = QFrame(self.page_1)
        self.Button_frame_01.setObjectName(u"Button_frame_01")
        self.Button_frame_01.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.Button_frame_01.sizePolicy().hasHeightForWidth())
        self.Button_frame_01.setSizePolicy(sizePolicy1)
        self.Button_frame_01.setMaximumSize(QSize(680, 560))
        self.Button_frame_01.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.Button_frame_01.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Button_frame_01.setStyleSheet(u"")
        self.Button_frame_01.setFrameShadow(QFrame.Shadow.Plain)
        self.Button_frame_01.setLineWidth(3)
        self.Button_frame_01.setMidLineWidth(0)
        self.gridLayout = QGridLayout(self.Button_frame_01)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.ToolButton_09 = QToolButton(self.Button_frame_01)
        self.ToolButton_09.setObjectName(u"ToolButton_09")
        self.ToolButton_09.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_09.sizePolicy().hasHeightForWidth())
        self.ToolButton_09.setSizePolicy(sizePolicy)
        self.ToolButton_09.setMinimumSize(QSize(150, 150))
        self.ToolButton_09.setMaximumSize(QSize(150, 150))
        self.ToolButton_09.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_09.setIconSize(QSize(96, 96))
        self.ToolButton_09.setCheckable(False)
        self.ToolButton_09.setChecked(False)
        self.ToolButton_09.setAutoRepeatDelay(600)
        self.ToolButton_09.setAutoRepeatInterval(300)
        self.ToolButton_09.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_09.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_09, 2, 0, 1, 1)

        self.ToolButton_02 = QToolButton(self.Button_frame_01)
        self.ToolButton_02.setObjectName(u"ToolButton_02")
        self.ToolButton_02.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_02.sizePolicy().hasHeightForWidth())
        self.ToolButton_02.setSizePolicy(sizePolicy)
        self.ToolButton_02.setMinimumSize(QSize(150, 150))
        self.ToolButton_02.setMaximumSize(QSize(150, 150))
        self.ToolButton_02.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_02.setIconSize(QSize(96, 96))
        self.ToolButton_02.setCheckable(False)
        self.ToolButton_02.setChecked(False)
        self.ToolButton_02.setAutoRepeatDelay(600)
        self.ToolButton_02.setAutoRepeatInterval(300)
        self.ToolButton_02.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_02.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_02, 0, 1, 1, 1)

        self.ToolButton_01 = QToolButton(self.Button_frame_01)
        self.ToolButton_01.setObjectName(u"ToolButton_01")
        self.ToolButton_01.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_01.sizePolicy().hasHeightForWidth())
        self.ToolButton_01.setSizePolicy(sizePolicy)
        self.ToolButton_01.setMinimumSize(QSize(150, 150))
        self.ToolButton_01.setMaximumSize(QSize(150, 150))
        self.ToolButton_01.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_01.setIconSize(QSize(96, 96))
        self.ToolButton_01.setCheckable(False)
        self.ToolButton_01.setChecked(False)
        self.ToolButton_01.setAutoRepeatDelay(600)
        self.ToolButton_01.setAutoRepeatInterval(300)
        self.ToolButton_01.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_01.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_01, 0, 0, 1, 1)

        self.ToolButton_12 = QToolButton(self.Button_frame_01)
        self.ToolButton_12.setObjectName(u"ToolButton_12")
        self.ToolButton_12.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_12.sizePolicy().hasHeightForWidth())
        self.ToolButton_12.setSizePolicy(sizePolicy)
        self.ToolButton_12.setMinimumSize(QSize(150, 150))
        self.ToolButton_12.setMaximumSize(QSize(150, 150))
        self.ToolButton_12.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_12.setIconSize(QSize(96, 96))
        self.ToolButton_12.setCheckable(False)
        self.ToolButton_12.setChecked(False)
        self.ToolButton_12.setAutoRepeatDelay(600)
        self.ToolButton_12.setAutoRepeatInterval(300)
        self.ToolButton_12.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_12.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_12, 2, 3, 1, 1)

        self.ToolButton_04 = QToolButton(self.Button_frame_01)
        self.ToolButton_04.setObjectName(u"ToolButton_04")
        self.ToolButton_04.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_04.sizePolicy().hasHeightForWidth())
        self.ToolButton_04.setSizePolicy(sizePolicy)
        self.ToolButton_04.setMinimumSize(QSize(150, 150))
        self.ToolButton_04.setMaximumSize(QSize(150, 150))
        self.ToolButton_04.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_04.setIconSize(QSize(96, 96))
        self.ToolButton_04.setCheckable(False)
        self.ToolButton_04.setChecked(False)
        self.ToolButton_04.setAutoRepeatDelay(600)
        self.ToolButton_04.setAutoRepeatInterval(300)
        self.ToolButton_04.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_04.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_04, 0, 3, 1, 1)

        self.ToolButton_03 = QToolButton(self.Button_frame_01)
        self.ToolButton_03.setObjectName(u"ToolButton_03")
        self.ToolButton_03.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_03.sizePolicy().hasHeightForWidth())
        self.ToolButton_03.setSizePolicy(sizePolicy)
        self.ToolButton_03.setMinimumSize(QSize(150, 150))
        self.ToolButton_03.setMaximumSize(QSize(150, 150))
        self.ToolButton_03.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_03.setIconSize(QSize(96, 96))
        self.ToolButton_03.setCheckable(False)
        self.ToolButton_03.setChecked(False)
        self.ToolButton_03.setAutoRepeatDelay(600)
        self.ToolButton_03.setAutoRepeatInterval(300)
        self.ToolButton_03.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_03.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_03, 0, 2, 1, 1)

        self.ToolButton_07 = QToolButton(self.Button_frame_01)
        self.ToolButton_07.setObjectName(u"ToolButton_07")
        self.ToolButton_07.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_07.sizePolicy().hasHeightForWidth())
        self.ToolButton_07.setSizePolicy(sizePolicy)
        self.ToolButton_07.setMinimumSize(QSize(150, 150))
        self.ToolButton_07.setMaximumSize(QSize(150, 150))
        self.ToolButton_07.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_07.setIconSize(QSize(96, 96))
        self.ToolButton_07.setCheckable(False)
        self.ToolButton_07.setChecked(False)
        self.ToolButton_07.setAutoRepeatDelay(600)
        self.ToolButton_07.setAutoRepeatInterval(300)
        self.ToolButton_07.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_07.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_07, 1, 2, 1, 1)

        self.ToolButton_06 = QToolButton(self.Button_frame_01)
        self.ToolButton_06.setObjectName(u"ToolButton_06")
        self.ToolButton_06.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_06.sizePolicy().hasHeightForWidth())
        self.ToolButton_06.setSizePolicy(sizePolicy)
        self.ToolButton_06.setMinimumSize(QSize(150, 150))
        self.ToolButton_06.setMaximumSize(QSize(150, 150))
        self.ToolButton_06.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_06.setIconSize(QSize(96, 96))
        self.ToolButton_06.setCheckable(False)
        self.ToolButton_06.setChecked(False)
        self.ToolButton_06.setAutoRepeatDelay(600)
        self.ToolButton_06.setAutoRepeatInterval(300)
        self.ToolButton_06.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_06.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_06, 1, 1, 1, 1)

        self.ToolButton_05 = QToolButton(self.Button_frame_01)
        self.ToolButton_05.setObjectName(u"ToolButton_05")
        self.ToolButton_05.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_05.sizePolicy().hasHeightForWidth())
        self.ToolButton_05.setSizePolicy(sizePolicy)
        self.ToolButton_05.setMinimumSize(QSize(150, 150))
        self.ToolButton_05.setMaximumSize(QSize(150, 150))
        self.ToolButton_05.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_05.setIconSize(QSize(96, 96))
        self.ToolButton_05.setCheckable(False)
        self.ToolButton_05.setChecked(False)
        self.ToolButton_05.setAutoRepeatDelay(600)
        self.ToolButton_05.setAutoRepeatInterval(300)
        self.ToolButton_05.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_05.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_05, 1, 0, 1, 1)

        self.ToolButton_11 = QToolButton(self.Button_frame_01)
        self.ToolButton_11.setObjectName(u"ToolButton_11")
        self.ToolButton_11.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_11.sizePolicy().hasHeightForWidth())
        self.ToolButton_11.setSizePolicy(sizePolicy)
        self.ToolButton_11.setMinimumSize(QSize(150, 150))
        self.ToolButton_11.setMaximumSize(QSize(150, 150))
        self.ToolButton_11.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_11.setIconSize(QSize(96, 96))
        self.ToolButton_11.setCheckable(False)
        self.ToolButton_11.setChecked(False)
        self.ToolButton_11.setAutoRepeatDelay(600)
        self.ToolButton_11.setAutoRepeatInterval(300)
        self.ToolButton_11.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_11.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_11, 2, 2, 1, 1)

        self.ToolButton_08 = QToolButton(self.Button_frame_01)
        self.ToolButton_08.setObjectName(u"ToolButton_08")
        self.ToolButton_08.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_08.sizePolicy().hasHeightForWidth())
        self.ToolButton_08.setSizePolicy(sizePolicy)
        self.ToolButton_08.setMinimumSize(QSize(150, 150))
        self.ToolButton_08.setMaximumSize(QSize(150, 150))
        self.ToolButton_08.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_08.setIconSize(QSize(96, 96))
        self.ToolButton_08.setCheckable(False)
        self.ToolButton_08.setChecked(False)
        self.ToolButton_08.setAutoRepeatDelay(600)
        self.ToolButton_08.setAutoRepeatInterval(300)
        self.ToolButton_08.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_08.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_08, 1, 3, 1, 1)

        self.ToolButton_10 = QToolButton(self.Button_frame_01)
        self.ToolButton_10.setObjectName(u"ToolButton_10")
        self.ToolButton_10.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ToolButton_10.sizePolicy().hasHeightForWidth())
        self.ToolButton_10.setSizePolicy(sizePolicy)
        self.ToolButton_10.setMinimumSize(QSize(150, 150))
        self.ToolButton_10.setMaximumSize(QSize(150, 150))
        self.ToolButton_10.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToolButton_10.setIconSize(QSize(96, 96))
        self.ToolButton_10.setCheckable(False)
        self.ToolButton_10.setChecked(False)
        self.ToolButton_10.setAutoRepeatDelay(600)
        self.ToolButton_10.setAutoRepeatInterval(300)
        self.ToolButton_10.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.ToolButton_10.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.ToolButton_10, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.Button_frame_01, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.Button_stackedWidget.addWidget(self.page_1)

        self.horizontalLayout_4.addWidget(self.Button_stackedWidget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.Main_stackW.addWidget(self.Button_page)
        self.Settings_page = QWidget()
        self.Settings_page.setObjectName(u"Settings_page")
        self.Settings_page.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Settings_page.sizePolicy().hasHeightForWidth())
        self.Settings_page.setSizePolicy(sizePolicy)
        self.Settings_page.setMinimumSize(QSize(700, 570))
        self.Settings_page.setMaximumSize(QSize(16777215, 570))
        self.Settings_page.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.widget = QWidget(self.Settings_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 653, 439))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Header_Button = QHBoxLayout()
        self.Header_Button.setObjectName(u"Header_Button")
        self.Editor_frame = QFrame(self.widget)
        self.Editor_frame.setObjectName(u"Editor_frame")
        self.Editor_frame.setMinimumSize(QSize(250, 46))
        self.Editor_frame.setMaximumSize(QSize(250, 46))
        self.Editor_frame.setStyleSheet(u"background-color: rgb(34, 3, 3);")
        self.Editor_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Editor_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Editor_frame)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 5, 6, 5)
        self.Change_Button = QPushButton(self.Editor_frame)
        self.Change_Button.setObjectName(u"Change_Button")
        sizePolicy.setHeightForWidth(self.Change_Button.sizePolicy().hasHeightForWidth())
        self.Change_Button.setSizePolicy(sizePolicy)
        self.Change_Button.setMinimumSize(QSize(0, 30))
        self.Change_Button.setCheckable(True)
        self.Change_Button.setChecked(False)
        self.Change_Button.setFlat(False)

        self.horizontalLayout.addWidget(self.Change_Button)

        self.Editor_button = QPushButton(self.Editor_frame)
        self.Editor_button.setObjectName(u"Editor_button")
        sizePolicy.setHeightForWidth(self.Editor_button.sizePolicy().hasHeightForWidth())
        self.Editor_button.setSizePolicy(sizePolicy)
        self.Editor_button.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.Editor_button)


        self.Header_Button.addWidget(self.Editor_frame)

        self.Page_control_frame = QFrame(self.widget)
        self.Page_control_frame.setObjectName(u"Page_control_frame")
        sizePolicy.setHeightForWidth(self.Page_control_frame.sizePolicy().hasHeightForWidth())
        self.Page_control_frame.setSizePolicy(sizePolicy)
        self.Page_control_frame.setMinimumSize(QSize(250, 46))
        self.Page_control_frame.setMaximumSize(QSize(250, 46))
        self.Page_control_frame.setStyleSheet(u"background-color: rgb(0, 37, 111);")
        self.Page_control_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Page_control_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Page_control_frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.BackButton_main = QPushButton(self.Page_control_frame)
        self.BackButton_main.setObjectName(u"BackButton_main")
        sizePolicy.setHeightForWidth(self.BackButton_main.sizePolicy().hasHeightForWidth())
        self.BackButton_main.setSizePolicy(sizePolicy)
        self.BackButton_main.setMinimumSize(QSize(0, 30))
        self.BackButton_main.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.BackButton_main)

        self.Current_page_label = QLabel(self.Page_control_frame)
        self.Current_page_label.setObjectName(u"Current_page_label")
        self.Current_page_label.setMinimumSize(QSize(0, 30))
        self.Current_page_label.setMaximumSize(QSize(16777215, 40))
        self.Current_page_label.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Current_page_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Current_page_label.setFrameShadow(QFrame.Shadow.Plain)
        self.Current_page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Current_page_label)

        self.Music_bttn = QPushButton(self.Page_control_frame)
        self.Music_bttn.setObjectName(u"Music_bttn")
        sizePolicy.setHeightForWidth(self.Music_bttn.sizePolicy().hasHeightForWidth())
        self.Music_bttn.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.Music_bttn)

        self.NextButton_main = QPushButton(self.Page_control_frame)
        self.NextButton_main.setObjectName(u"NextButton_main")
        sizePolicy.setHeightForWidth(self.NextButton_main.sizePolicy().hasHeightForWidth())
        self.NextButton_main.setSizePolicy(sizePolicy)
        self.NextButton_main.setMinimumSize(QSize(0, 30))
        self.NextButton_main.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.NextButton_main)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)

        self.Header_Button.addWidget(self.Page_control_frame)

        self.Settings_tB = QToolButton(self.widget)
        self.Settings_tB.setObjectName(u"Settings_tB")

        self.Header_Button.addWidget(self.Settings_tB)

        self.switch_audio_butt = QPushButton(self.widget)
        self.switch_audio_butt.setObjectName(u"switch_audio_butt")
        self.switch_audio_butt.setStyleSheet(u"background-color: rgb(255, 0, 4);\n"
"border-color: rgb(0, 34, 255);")

        self.Header_Button.addWidget(self.switch_audio_butt)


        self.verticalLayout_3.addLayout(self.Header_Button)

        self.Settings_scrollArea = QScrollArea(self.widget)
        self.Settings_scrollArea.setObjectName(u"Settings_scrollArea")
        self.Settings_scrollArea.setFrameShape(QFrame.Shape.Box)
        self.Settings_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Settings_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Settings_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.Settings_scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -168, 650, 600))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget1 = QWidget(self.scrollAreaWidgetContents)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 641, 241))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.Settings_HWINFO = QGroupBox(self.widget1)
        self.Settings_HWINFO.setObjectName(u"Settings_HWINFO")
        self.Settings_HWINFO.setMinimumSize(QSize(260, 0))
        self.Settings_HWINFO.setMaximumSize(QSize(290, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.Settings_HWINFO)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fan_cpu_sensor_layout = QHBoxLayout()
        self.fan_cpu_sensor_layout.setObjectName(u"fan_cpu_sensor_layout")
        self.fan_cpu_sensor_lable = QLabel(self.Settings_HWINFO)
        self.fan_cpu_sensor_lable.setObjectName(u"fan_cpu_sensor_lable")

        self.fan_cpu_sensor_layout.addWidget(self.fan_cpu_sensor_lable)

        self.fan_cpu_sensor_CB = QComboBox(self.Settings_HWINFO)
        self.fan_cpu_sensor_CB.setObjectName(u"fan_cpu_sensor_CB")

        self.fan_cpu_sensor_layout.addWidget(self.fan_cpu_sensor_CB)

        self.fan_cpu_sensor_layout.setStretch(0, 2)
        self.fan_cpu_sensor_layout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.fan_cpu_sensor_layout)

        self.pump_cpu_sensor_layout = QHBoxLayout()
        self.pump_cpu_sensor_layout.setObjectName(u"pump_cpu_sensor_layout")
        self.pump_cpu_sensor_label = QLabel(self.Settings_HWINFO)
        self.pump_cpu_sensor_label.setObjectName(u"pump_cpu_sensor_label")

        self.pump_cpu_sensor_layout.addWidget(self.pump_cpu_sensor_label)

        self.pump_cpu_sensor_CB = QComboBox(self.Settings_HWINFO)
        self.pump_cpu_sensor_CB.setObjectName(u"pump_cpu_sensor_CB")

        self.pump_cpu_sensor_layout.addWidget(self.pump_cpu_sensor_CB)

        self.pump_cpu_sensor_layout.setStretch(0, 2)
        self.pump_cpu_sensor_layout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.pump_cpu_sensor_layout)

        self.system_drive_letter_layout = QHBoxLayout()
        self.system_drive_letter_layout.setObjectName(u"system_drive_letter_layout")
        self.system_drive_letter_label = QLabel(self.Settings_HWINFO)
        self.system_drive_letter_label.setObjectName(u"system_drive_letter_label")

        self.system_drive_letter_layout.addWidget(self.system_drive_letter_label)

        self.system_drive_letter_CB = QComboBox(self.Settings_HWINFO)
        self.system_drive_letter_CB.setObjectName(u"system_drive_letter_CB")

        self.system_drive_letter_layout.addWidget(self.system_drive_letter_CB)

        self.system_drive_letter_layout.setStretch(0, 2)
        self.system_drive_letter_layout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.system_drive_letter_layout)

        self.storage_sensor_layout = QHBoxLayout()
        self.storage_sensor_layout.setObjectName(u"storage_sensor_layout")
        self.storage_sensor_label = QLabel(self.Settings_HWINFO)
        self.storage_sensor_label.setObjectName(u"storage_sensor_label")

        self.storage_sensor_layout.addWidget(self.storage_sensor_label)

        self.storage_sensor_CB = QComboBox(self.Settings_HWINFO)
        self.storage_sensor_CB.setObjectName(u"storage_sensor_CB")

        self.storage_sensor_layout.addWidget(self.storage_sensor_CB)

        self.storage_sensor_layout.setStretch(0, 2)
        self.storage_sensor_layout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.storage_sensor_layout)

        self.gpu_name_layout = QHBoxLayout()
        self.gpu_name_layout.setObjectName(u"gpu_name_layout")
        self.gpu_name_lable = QLabel(self.Settings_HWINFO)
        self.gpu_name_lable.setObjectName(u"gpu_name_lable")

        self.gpu_name_layout.addWidget(self.gpu_name_lable)

        self.gpu_name_CB = QComboBox(self.Settings_HWINFO)
        self.gpu_name_CB.setObjectName(u"gpu_name_CB")

        self.gpu_name_layout.addWidget(self.gpu_name_CB)

        self.gpu_name_layout.setStretch(0, 2)
        self.gpu_name_layout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.gpu_name_layout)

        self.Save_sett_HWINFO_tB = QToolButton(self.Settings_HWINFO)
        self.Save_sett_HWINFO_tB.setObjectName(u"Save_sett_HWINFO_tB")
        sizePolicy.setHeightForWidth(self.Save_sett_HWINFO_tB.sizePolicy().hasHeightForWidth())
        self.Save_sett_HWINFO_tB.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.Save_sett_HWINFO_tB)


        self.horizontalLayout_6.addWidget(self.Settings_HWINFO)

        self.Audio_Sett_GB = QGroupBox(self.widget1)
        self.Audio_Sett_GB.setObjectName(u"Audio_Sett_GB")
        self.Audio_Sett_GB.setMinimumSize(QSize(260, 0))
        self.Audio_Sett_GB.setMaximumSize(QSize(290, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.Audio_Sett_GB)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Audio_change_layout = QHBoxLayout()
        self.Audio_change_layout.setSpacing(5)
        self.Audio_change_layout.setObjectName(u"Audio_change_layout")
        self.lable_layout = QVBoxLayout()
        self.lable_layout.setSpacing(5)
        self.lable_layout.setObjectName(u"lable_layout")
        self.Main_AD_lable = QLabel(self.Audio_Sett_GB)
        self.Main_AD_lable.setObjectName(u"Main_AD_lable")

        self.lable_layout.addWidget(self.Main_AD_lable)

        self.Second_AD_lable = QLabel(self.Audio_Sett_GB)
        self.Second_AD_lable.setObjectName(u"Second_AD_lable")

        self.lable_layout.addWidget(self.Second_AD_lable)

        self.Third_AD_lable = QLabel(self.Audio_Sett_GB)
        self.Third_AD_lable.setObjectName(u"Third_AD_lable")

        self.lable_layout.addWidget(self.Third_AD_lable)

        self.Fourth_AD_lable = QLabel(self.Audio_Sett_GB)
        self.Fourth_AD_lable.setObjectName(u"Fourth_AD_lable")

        self.lable_layout.addWidget(self.Fourth_AD_lable)


        self.Audio_change_layout.addLayout(self.lable_layout)

        self.CB_layout = QVBoxLayout()
        self.CB_layout.setSpacing(5)
        self.CB_layout.setObjectName(u"CB_layout")
        self.Main_AD_CB = QComboBox(self.Audio_Sett_GB)
        self.Main_AD_CB.setObjectName(u"Main_AD_CB")
        self.Main_AD_CB.setMinimumSize(QSize(0, 30))

        self.CB_layout.addWidget(self.Main_AD_CB)

        self.Second_AD_CB = QComboBox(self.Audio_Sett_GB)
        self.Second_AD_CB.setObjectName(u"Second_AD_CB")
        self.Second_AD_CB.setMinimumSize(QSize(0, 30))

        self.CB_layout.addWidget(self.Second_AD_CB)

        self.Third_AD_CB = QComboBox(self.Audio_Sett_GB)
        self.Third_AD_CB.setObjectName(u"Third_AD_CB")
        self.Third_AD_CB.setMinimumSize(QSize(0, 30))

        self.CB_layout.addWidget(self.Third_AD_CB)

        self.Fourth_AD_CB = QComboBox(self.Audio_Sett_GB)
        self.Fourth_AD_CB.setObjectName(u"Fourth_AD_CB")
        self.Fourth_AD_CB.setMinimumSize(QSize(0, 30))

        self.CB_layout.addWidget(self.Fourth_AD_CB)


        self.Audio_change_layout.addLayout(self.CB_layout)

        self.Audio_change_layout.setStretch(0, 2)
        self.Audio_change_layout.setStretch(1, 5)

        self.verticalLayout_10.addLayout(self.Audio_change_layout)

        self.Accept_AD_tB = QToolButton(self.Audio_Sett_GB)
        self.Accept_AD_tB.setObjectName(u"Accept_AD_tB")
        self.Accept_AD_tB.setMinimumSize(QSize(100, 35))

        self.verticalLayout_10.addWidget(self.Accept_AD_tB, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.Audio_Sett_GB)

        self.Settings_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.Settings_scrollArea)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 8)
        self.Main_stackW.addWidget(self.Settings_page)
        self.Music_page = QWidget()
        self.Music_page.setObjectName(u"Music_page")
        sizePolicy.setHeightForWidth(self.Music_page.sizePolicy().hasHeightForWidth())
        self.Music_page.setSizePolicy(sizePolicy)
        self.Music_page.setMinimumSize(QSize(700, 570))
        self.Music_page.setMaximumSize(QSize(16777215, 570))
        self.Music_main = QFrame(self.Music_page)
        self.Music_main.setObjectName(u"Music_main")
        self.Music_main.setGeometry(QRect(5, 5, 690, 560))
        self.Music_main.setMinimumSize(QSize(690, 560))
        self.Music_main.setMaximumSize(QSize(690, 560))
        self.Music_main.setFrameShape(QFrame.Shape.NoFrame)
        self.Music_main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Music_main)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self._1Left_side_F = QFrame(self.Music_main)
        self._1Left_side_F.setObjectName(u"_1Left_side_F")
        self._1Left_side_F.setStyleSheet(u"")
        self._1Left_side_F.setFrameShape(QFrame.Shape.NoFrame)
        self._1Left_side_F.setFrameShadow(QFrame.Shadow.Plain)
        self._1Left_side_F.setLineWidth(0)
        self.horizontalLayout_11 = QHBoxLayout(self._1Left_side_F)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.Player_F = QFrame(self._1Left_side_F)
        self.Player_F.setObjectName(u"Player_F")
        self.Player_F.setFrameShape(QFrame.Shape.StyledPanel)
        self.Player_F.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Player_F)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Track_label = QLabel(self.Player_F)
        self.Track_label.setObjectName(u"Track_label")
        sizePolicy.setHeightForWidth(self.Track_label.sizePolicy().hasHeightForWidth())
        self.Track_label.setSizePolicy(sizePolicy)
        self.Track_label.setMinimumSize(QSize(300, 30))
        self.Track_label.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(16)
        self.Track_label.setFont(font3)
        self.Track_label.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Track_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Track_label.setFrameShape(QFrame.Shape.NoFrame)
        self.Track_label.setLineWidth(1)
        self.Track_label.setTextFormat(Qt.TextFormat.PlainText)
        self.Track_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Track_label.setWordWrap(False)
        self.Track_label.setMargin(5)

        self.verticalLayout_7.addWidget(self.Track_label)

        self.Artist_label = QLabel(self.Player_F)
        self.Artist_label.setObjectName(u"Artist_label")
        sizePolicy.setHeightForWidth(self.Artist_label.sizePolicy().hasHeightForWidth())
        self.Artist_label.setSizePolicy(sizePolicy)
        self.Artist_label.setMinimumSize(QSize(200, 40))
        self.Artist_label.setMaximumSize(QSize(16777215, 70))
        font4 = QFont()
        font4.setPointSize(14)
        self.Artist_label.setFont(font4)
        self.Artist_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Artist_label.setFrameShape(QFrame.Shape.NoFrame)
        self.Artist_label.setTextFormat(Qt.TextFormat.RichText)
        self.Artist_label.setScaledContents(False)
        self.Artist_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Artist_label.setMargin(5)

        self.verticalLayout_7.addWidget(self.Artist_label)

        self.Album_label = QLabel(self.Player_F)
        self.Album_label.setObjectName(u"Album_label")
        sizePolicy.setHeightForWidth(self.Album_label.sizePolicy().hasHeightForWidth())
        self.Album_label.setSizePolicy(sizePolicy)
        self.Album_label.setMinimumSize(QSize(200, 30))
        self.Album_label.setMaximumSize(QSize(16777215, 70))
        self.Album_label.setFont(font)
        self.Album_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Album_label.setFrameShape(QFrame.Shape.NoFrame)
        self.Album_label.setTextFormat(Qt.TextFormat.RichText)
        self.Album_label.setScaledContents(False)
        self.Album_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Album_label.setMargin(5)

        self.verticalLayout_7.addWidget(self.Album_label)

        self.Playlist_label = QLabel(self.Player_F)
        self.Playlist_label.setObjectName(u"Playlist_label")
        sizePolicy.setHeightForWidth(self.Playlist_label.sizePolicy().hasHeightForWidth())
        self.Playlist_label.setSizePolicy(sizePolicy)
        self.Playlist_label.setMinimumSize(QSize(200, 20))
        self.Playlist_label.setFont(font1)
        self.Playlist_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Playlist_label.setFrameShape(QFrame.Shape.NoFrame)
        self.Playlist_label.setTextFormat(Qt.TextFormat.RichText)
        self.Playlist_label.setScaledContents(False)
        self.Playlist_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Playlist_label.setMargin(5)

        self.verticalLayout_7.addWidget(self.Playlist_label)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Previous_ToolB = QToolButton(self.Player_F)
        self.Previous_ToolB.setObjectName(u"Previous_ToolB")
        sizePolicy.setHeightForWidth(self.Previous_ToolB.sizePolicy().hasHeightForWidth())
        self.Previous_ToolB.setSizePolicy(sizePolicy)
        self.Previous_ToolB.setMinimumSize(QSize(80, 0))
        self.Previous_ToolB.setMaximumSize(QSize(160, 70))
        self.Previous_ToolB.setAutoFillBackground(False)
        self.Previous_ToolB.setIconSize(QSize(60, 60))
        self.Previous_ToolB.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_14.addWidget(self.Previous_ToolB)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.PlayPause_ToolB = QToolButton(self.Player_F)
        self.PlayPause_ToolB.setObjectName(u"PlayPause_ToolB")
        sizePolicy.setHeightForWidth(self.PlayPause_ToolB.sizePolicy().hasHeightForWidth())
        self.PlayPause_ToolB.setSizePolicy(sizePolicy)
        self.PlayPause_ToolB.setMinimumSize(QSize(100, 100))
        self.PlayPause_ToolB.setMaximumSize(QSize(256, 256))
        self.PlayPause_ToolB.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.PlayPause_ToolB.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.PlayPause_ToolB.setAutoFillBackground(False)
        self.PlayPause_ToolB.setIconSize(QSize(60, 60))
        self.PlayPause_ToolB.setCheckable(True)
        self.PlayPause_ToolB.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.PlayPause_ToolB.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_14.addWidget(self.PlayPause_ToolB)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.Next_ToolB = QToolButton(self.Player_F)
        self.Next_ToolB.setObjectName(u"Next_ToolB")
        sizePolicy.setHeightForWidth(self.Next_ToolB.sizePolicy().hasHeightForWidth())
        self.Next_ToolB.setSizePolicy(sizePolicy)
        self.Next_ToolB.setMinimumSize(QSize(80, 0))
        self.Next_ToolB.setMaximumSize(QSize(16777215, 70))
        self.Next_ToolB.setAutoFillBackground(False)
        self.Next_ToolB.setIconSize(QSize(60, 60))
        self.Next_ToolB.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.Next_ToolB.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.Next_ToolB.setAutoRaise(False)
        self.Next_ToolB.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_14.addWidget(self.Next_ToolB)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.Time_F = QFrame(self.Player_F)
        self.Time_F.setObjectName(u"Time_F")
        self.Time_F.setFrameShape(QFrame.Shape.StyledPanel)
        self.Time_F.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.Time_F)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Left_Time_label = QLabel(self.Time_F)
        self.Left_Time_label.setObjectName(u"Left_Time_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Left_Time_label.sizePolicy().hasHeightForWidth())
        self.Left_Time_label.setSizePolicy(sizePolicy2)
        self.Left_Time_label.setMaximumSize(QSize(20, 20))
        font5 = QFont()
        font5.setPointSize(8)
        self.Left_Time_label.setFont(font5)
        self.Left_Time_label.setTextFormat(Qt.TextFormat.RichText)
        self.Left_Time_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_8.addWidget(self.Left_Time_label)

        self.Length_track_bar = QProgressBar(self.Time_F)
        self.Length_track_bar.setObjectName(u"Length_track_bar")
        sizePolicy.setHeightForWidth(self.Length_track_bar.sizePolicy().hasHeightForWidth())
        self.Length_track_bar.setSizePolicy(sizePolicy)
        self.Length_track_bar.setMinimumSize(QSize(50, 20))
        self.Length_track_bar.setValue(0)
        self.Length_track_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Length_track_bar.setTextVisible(False)
        self.Length_track_bar.setInvertedAppearance(False)

        self.horizontalLayout_8.addWidget(self.Length_track_bar)

        self.Right_Time_label = QLabel(self.Time_F)
        self.Right_Time_label.setObjectName(u"Right_Time_label")
        self.Right_Time_label.setMaximumSize(QSize(20, 20))
        self.Right_Time_label.setFont(font5)
        self.Right_Time_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_8.addWidget(self.Right_Time_label)


        self.verticalLayout_8.addWidget(self.Time_F)

        self.verticalLayout_8.setStretch(0, 10)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 2)

        self.verticalLayout_5.addWidget(self.Player_F)

        self.Button_F = QFrame(self._1Left_side_F)
        self.Button_F.setObjectName(u"Button_F")
        self.Button_F.setFrameShape(QFrame.Shape.StyledPanel)
        self.Button_F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Button_F)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.Random_ToolB = QToolButton(self.Button_F)
        self.Random_ToolB.setObjectName(u"Random_ToolB")
        sizePolicy.setHeightForWidth(self.Random_ToolB.sizePolicy().hasHeightForWidth())
        self.Random_ToolB.setSizePolicy(sizePolicy)
        self.Random_ToolB.setMaximumSize(QSize(80, 80))
        self.Random_ToolB.setIconSize(QSize(40, 40))
        self.Random_ToolB.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.Random_ToolB)

        self.Like_ToolB = QToolButton(self.Button_F)
        self.Like_ToolB.setObjectName(u"Like_ToolB")
        sizePolicy.setHeightForWidth(self.Like_ToolB.sizePolicy().hasHeightForWidth())
        self.Like_ToolB.setSizePolicy(sizePolicy)
        self.Like_ToolB.setMaximumSize(QSize(80, 80))
        self.Like_ToolB.setIconSize(QSize(40, 40))
        self.Like_ToolB.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.Like_ToolB)

        self.Repeat_ToolB = QToolButton(self.Button_F)
        self.Repeat_ToolB.setObjectName(u"Repeat_ToolB")
        sizePolicy.setHeightForWidth(self.Repeat_ToolB.sizePolicy().hasHeightForWidth())
        self.Repeat_ToolB.setSizePolicy(sizePolicy)
        self.Repeat_ToolB.setMaximumSize(QSize(80, 80))
        self.Repeat_ToolB.setIconSize(QSize(40, 40))
        self.Repeat_ToolB.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.Repeat_ToolB)

        self.Dis_ToolB = QToolButton(self.Button_F)
        self.Dis_ToolB.setObjectName(u"Dis_ToolB")
        sizePolicy.setHeightForWidth(self.Dis_ToolB.sizePolicy().hasHeightForWidth())
        self.Dis_ToolB.setSizePolicy(sizePolicy)
        self.Dis_ToolB.setMaximumSize(QSize(80, 80))
        self.Dis_ToolB.setIconSize(QSize(40, 40))
        self.Dis_ToolB.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.Dis_ToolB)


        self.verticalLayout_5.addWidget(self.Button_F)

        self.verticalLayout_5.setStretch(0, 12)
        self.verticalLayout_5.setStretch(1, 3)

        self.horizontalLayout_11.addLayout(self.verticalLayout_5)


        self.horizontalLayout_7.addWidget(self._1Left_side_F)

        self._2Right_side_F = QFrame(self.Music_main)
        self._2Right_side_F.setObjectName(u"_2Right_side_F")
        self._2Right_side_F.setMinimumSize(QSize(270, 0))
        self._2Right_side_F.setStyleSheet(u"")
        self._2Right_side_F.setFrameShape(QFrame.Shape.NoFrame)
        self._2Right_side_F.setFrameShadow(QFrame.Shadow.Plain)
        self._2Right_side_F.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self._2Right_side_F)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Cover_Frame = QFrame(self._2Right_side_F)
        self.Cover_Frame.setObjectName(u"Cover_Frame")
        sizePolicy.setHeightForWidth(self.Cover_Frame.sizePolicy().hasHeightForWidth())
        self.Cover_Frame.setSizePolicy(sizePolicy)
        self.Cover_Frame.setMinimumSize(QSize(250, 250))
        self.Cover_Frame.setMaximumSize(QSize(200, 200))
        self.Cover_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cover_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_3 = QGridLayout(self.Cover_Frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.Cover_Frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.PL_stWidget = QStackedWidget(self._2Right_side_F)
        self.PL_stWidget.setObjectName(u"PL_stWidget")
        self.PL_stWidget.setMaximumSize(QSize(260, 16777215))
        self.PL_stWidget.setStyleSheet(u"")
        self.PL_stWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.PL_list_page = QWidget()
        self.PL_list_page.setObjectName(u"PL_list_page")
        self.PL_list_layout = QVBoxLayout(self.PL_list_page)
        self.PL_list_layout.setSpacing(5)
        self.PL_list_layout.setObjectName(u"PL_list_layout")
        self.PL_list_layout.setContentsMargins(5, 5, 5, 5)
        self.Back_ToolB = QToolButton(self.PL_list_page)
        self.Back_ToolB.setObjectName(u"Back_ToolB")
        sizePolicy.setHeightForWidth(self.Back_ToolB.sizePolicy().hasHeightForWidth())
        self.Back_ToolB.setSizePolicy(sizePolicy)
        self.Back_ToolB.setIconSize(QSize(40, 40))
        self.Back_ToolB.setCheckable(True)

        self.PL_list_layout.addWidget(self.Back_ToolB)

        self.PL_list_qList = QListView(self.PL_list_page)
        self.PL_list_qList.setObjectName(u"PL_list_qList")
        self.PL_list_qList.setMinimumSize(QSize(250, 220))
        self.PL_list_qList.setMaximumSize(QSize(250, 220))
        self.PL_list_qList.setStyleSheet(u"")
        self.PL_list_qList.setFrameShape(QFrame.Shape.StyledPanel)

        self.PL_list_layout.addWidget(self.PL_list_qList, 0, Qt.AlignmentFlag.AlignHCenter)

        self.PL_list_layout.setStretch(0, 1)
        self.PL_list_layout.setStretch(1, 5)
        self.PL_stWidget.addWidget(self.PL_list_page)
        self.PL_Fav_page = QWidget()
        self.PL_Fav_page.setObjectName(u"PL_Fav_page")
        self.PL_fav_layout = QVBoxLayout(self.PL_Fav_page)
        self.PL_fav_layout.setSpacing(5)
        self.PL_fav_layout.setObjectName(u"PL_fav_layout")
        self.PL_fav_layout.setContentsMargins(5, 5, 5, 5)
        self.Back_f_ToolB = QToolButton(self.PL_Fav_page)
        self.Back_f_ToolB.setObjectName(u"Back_f_ToolB")
        sizePolicy.setHeightForWidth(self.Back_f_ToolB.sizePolicy().hasHeightForWidth())
        self.Back_f_ToolB.setSizePolicy(sizePolicy)
        self.Back_f_ToolB.setMinimumSize(QSize(250, 0))
        self.Back_f_ToolB.setMaximumSize(QSize(250, 40))
        self.Back_f_ToolB.setIconSize(QSize(40, 40))
        self.Back_f_ToolB.setCheckable(True)

        self.PL_fav_layout.addWidget(self.Back_f_ToolB)

        self.PL_Fav_tracks_qList = QListView(self.PL_Fav_page)
        self.PL_Fav_tracks_qList.setObjectName(u"PL_Fav_tracks_qList")
        self.PL_Fav_tracks_qList.setMinimumSize(QSize(250, 220))
        self.PL_Fav_tracks_qList.setMaximumSize(QSize(250, 220))
        self.PL_Fav_tracks_qList.setStyleSheet(u"")
        self.PL_Fav_tracks_qList.setFrameShape(QFrame.Shape.StyledPanel)

        self.PL_fav_layout.addWidget(self.PL_Fav_tracks_qList, 0, Qt.AlignmentFlag.AlignHCenter)

        self.PL_fav_layout.setStretch(0, 1)
        self.PL_fav_layout.setStretch(1, 5)
        self.PL_stWidget.addWidget(self.PL_Fav_page)
        self.PL_Day_page = QWidget()
        self.PL_Day_page.setObjectName(u"PL_Day_page")
        self.PL_day_layout = QVBoxLayout(self.PL_Day_page)
        self.PL_day_layout.setSpacing(5)
        self.PL_day_layout.setObjectName(u"PL_day_layout")
        self.PL_day_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Back_D_ToolB = QToolButton(self.PL_Day_page)
        self.Back_D_ToolB.setObjectName(u"Back_D_ToolB")
        sizePolicy.setHeightForWidth(self.Back_D_ToolB.sizePolicy().hasHeightForWidth())
        self.Back_D_ToolB.setSizePolicy(sizePolicy)
        self.Back_D_ToolB.setIconSize(QSize(40, 40))
        self.Back_D_ToolB.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.Back_D_ToolB)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)

        self.PL_day_layout.addLayout(self.horizontalLayout_12)

        self.PL_Day_tracks_qList = QListView(self.PL_Day_page)
        self.PL_Day_tracks_qList.setObjectName(u"PL_Day_tracks_qList")
        self.PL_Day_tracks_qList.setMinimumSize(QSize(250, 220))
        self.PL_Day_tracks_qList.setMaximumSize(QSize(250, 220))
        self.PL_Day_tracks_qList.setStyleSheet(u"")
        self.PL_Day_tracks_qList.setFrameShape(QFrame.Shape.StyledPanel)

        self.PL_day_layout.addWidget(self.PL_Day_tracks_qList, 0, Qt.AlignmentFlag.AlignHCenter)

        self.PL_day_layout.setStretch(0, 1)
        self.PL_day_layout.setStretch(1, 5)
        self.PL_stWidget.addWidget(self.PL_Day_page)
        self.PL_mistery_page = QWidget()
        self.PL_mistery_page.setObjectName(u"PL_mistery_page")
        self.PL_mistery_layout = QVBoxLayout(self.PL_mistery_page)
        self.PL_mistery_layout.setSpacing(5)
        self.PL_mistery_layout.setObjectName(u"PL_mistery_layout")
        self.PL_mistery_layout.setContentsMargins(5, 5, 5, 5)
        self.Back_m_ToolB = QToolButton(self.PL_mistery_page)
        self.Back_m_ToolB.setObjectName(u"Back_m_ToolB")
        sizePolicy.setHeightForWidth(self.Back_m_ToolB.sizePolicy().hasHeightForWidth())
        self.Back_m_ToolB.setSizePolicy(sizePolicy)
        self.Back_m_ToolB.setIconSize(QSize(40, 40))

        self.PL_mistery_layout.addWidget(self.Back_m_ToolB)

        self.PL_mistery_tracks_qList = QListView(self.PL_mistery_page)
        self.PL_mistery_tracks_qList.setObjectName(u"PL_mistery_tracks_qList")
        self.PL_mistery_tracks_qList.setMinimumSize(QSize(250, 220))
        self.PL_mistery_tracks_qList.setMaximumSize(QSize(250, 220))
        self.PL_mistery_tracks_qList.setStyleSheet(u"")
        self.PL_mistery_tracks_qList.setFrameShape(QFrame.Shape.StyledPanel)

        self.PL_mistery_layout.addWidget(self.PL_mistery_tracks_qList, 0, Qt.AlignmentFlag.AlignHCenter)

        self.PL_mistery_layout.setStretch(0, 1)
        self.PL_mistery_layout.setStretch(1, 5)
        self.PL_stWidget.addWidget(self.PL_mistery_page)

        self.verticalLayout_9.addWidget(self.PL_stWidget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)

        self.horizontalLayout_7.addWidget(self._2Right_side_F)

        self.horizontalLayout_7.setStretch(0, 8)
        self.horizontalLayout_7.setStretch(1, 5)
        self.Main_stackW.addWidget(self.Music_page)

        self.horizontalLayout_3.addWidget(self.Main_stackW)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1090, 140, 75, 24))
        self.pushButton.setMaximumSize(QSize(250, 80))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1090, 180, 75, 24))
        self.pushButton_2.setMaximumSize(QSize(250, 80))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Main_stackW.setCurrentIndex(0)
        self.Button_stackedWidget.setCurrentIndex(0)
        self.PL_stWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        MainWindow.setStyleSheet("")
        self.action.setIconText("")
        self.Time_GB.setTitle("")
        self.Sound_ToolB.setText(QCoreApplication.translate("MainWindow", u"sound", None))
        self.name_gpu.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.value_name_gpu.setText("")
        self.load_gpu.setText(QCoreApplication.translate("MainWindow", u"Load:", None))
        self.value_load_gpu.setText(QCoreApplication.translate("MainWindow", u"Load GPU", None))
        self.temp_gpu.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.value_temp_gpu.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.tempHot_gpu.setText(QCoreApplication.translate("MainWindow", u"Temp Hot", None))
        self.value_temHot_gpu.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.power_gpu.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.value_power_gpu.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.clocks_gpu.setText(QCoreApplication.translate("MainWindow", u"Clocks GPU", None))
        self.value_clocks_gpu.setText(QCoreApplication.translate("MainWindow", u"Clocks", None))
        self.fanPer_gpu.setText(QCoreApplication.translate("MainWindow", u"Fan Speed%", None))
        self.value_fanPer_gpu.setText(QCoreApplication.translate("MainWindow", u"Fan Speed", None))
        self.fanRPM_gpu.setText(QCoreApplication.translate("MainWindow", u"Fan SpeedRPM", None))
        self.value_fanRPM_gpu.setText(QCoreApplication.translate("MainWindow", u"Fan Speed", None))
        self.vramUMb_gpu.setText(QCoreApplication.translate("MainWindow", u"VRAM MB", None))
        self.value_vramUMb_gpu.setText(QCoreApplication.translate("MainWindow", u"Vram", None))
        self.vramUPer_gpu.setText(QCoreApplication.translate("MainWindow", u"VRAM %", None))
        self.value_vramUPer_gpu.setText(QCoreApplication.translate("MainWindow", u"Vram", None))
        self.vram_total_gpu.setText(QCoreApplication.translate("MainWindow", u"VRAM TOTAL", None))
        self.value_vram_total_gpu.setText(QCoreApplication.translate("MainWindow", u"Vram", None))
        self.name_cpu.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.value_name_cpu.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.load_cpu.setText(QCoreApplication.translate("MainWindow", u"Load Pers", None))
        self.value_load_cpu.setText(QCoreApplication.translate("MainWindow", u"Load CPU", None))
        self.clocks_cpu.setText(QCoreApplication.translate("MainWindow", u"Clocks", None))
        self.value_clocks_cpu.setText(QCoreApplication.translate("MainWindow", u"Clocks", None))
        self.temp_cpu.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.value_temp_cpu.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.power_cpu.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.value_power_cpu.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.fan_speed_cpu.setText(QCoreApplication.translate("MainWindow", u"Fan Speed", None))
        self.value_fan_speed_cpu.setText(QCoreApplication.translate("MainWindow", u"Fan Speed", None))
        self.name_ram.setText(QCoreApplication.translate("MainWindow", u"ramSpec", None))
        self.progressBar_ram.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.value_freeGB_ram_label.setText(QCoreApplication.translate("MainWindow", u"freeGB", None))
        self.value_totalGB_ram_lable.setText(QCoreApplication.translate("MainWindow", u"totalGB", None))
        self.upload_lable.setText(QCoreApplication.translate("MainWindow", u"Upload:", None))
        self.value_upload__net.setText(QCoreApplication.translate("MainWindow", u"speedU", None))
        self.download_lable.setText(QCoreApplication.translate("MainWindow", u"Download:", None))
        self.value_download_net.setText(QCoreApplication.translate("MainWindow", u"speedD", None))
        self.ToolButton_09.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_02.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_01.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_12.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_04.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_03.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_07.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_06.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_05.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_11.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_08.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ToolButton_10.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Change_Button.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.Editor_button.setText(QCoreApplication.translate("MainWindow", u"Editor", None))
        self.BackButton_main.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Current_page_label.setText("")
        self.Music_bttn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.NextButton_main.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.Settings_tB.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.switch_audio_butt.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Settings_HWINFO.setTitle(QCoreApplication.translate("MainWindow", u"Settings HWINFO", None))
        self.fan_cpu_sensor_lable.setText(QCoreApplication.translate("MainWindow", u"Fan CPU", None))
        self.pump_cpu_sensor_label.setText(QCoreApplication.translate("MainWindow", u"Pump CPU", None))
        self.system_drive_letter_label.setText(QCoreApplication.translate("MainWindow", u"System Letter", None))
        self.storage_sensor_label.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.gpu_name_lable.setText(QCoreApplication.translate("MainWindow", u"GPU name", None))
        self.Save_sett_HWINFO_tB.setText(QCoreApplication.translate("MainWindow", u"Save HWINFO", None))
        self.Audio_Sett_GB.setTitle(QCoreApplication.translate("MainWindow", u"Settings Device", None))
        self.Main_AD_lable.setText(QCoreApplication.translate("MainWindow", u"Main Audio Device", None))
        self.Second_AD_lable.setText(QCoreApplication.translate("MainWindow", u"Second Audio Device", None))
        self.Third_AD_lable.setText(QCoreApplication.translate("MainWindow", u"Third Audio Device", None))
        self.Fourth_AD_lable.setText(QCoreApplication.translate("MainWindow", u"Fourth Audio Device", None))
        self.Accept_AD_tB.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.Track_label.setText(QCoreApplication.translate("MainWindow", u"Track", None))
        self.Artist_label.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.Album_label.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.Playlist_label.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.Previous_ToolB.setText(QCoreApplication.translate("MainWindow", u"prev_track", None))
        self.PlayPause_ToolB.setText(QCoreApplication.translate("MainWindow", u"play", None))
        self.Next_ToolB.setText(QCoreApplication.translate("MainWindow", u"next_track", None))
        self.Left_Time_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.Right_Time_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.Random_ToolB.setText(QCoreApplication.translate("MainWindow", u"random", None))
        self.Like_ToolB.setText(QCoreApplication.translate("MainWindow", u"like", None))
        self.Repeat_ToolB.setText(QCoreApplication.translate("MainWindow", u"repeat", None))
        self.Dis_ToolB.setText(QCoreApplication.translate("MainWindow", u"dislike", None))
        self.Back_ToolB.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Back_f_ToolB.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Back_D_ToolB.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Back_m_ToolB.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

