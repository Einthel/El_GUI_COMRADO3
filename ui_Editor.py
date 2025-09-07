# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Editor.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFontComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_Editor_Window(object):
    def setupUi(self, Editor_Window):
        if not Editor_Window.objectName():
            Editor_Window.setObjectName(u"Editor_Window")
        Editor_Window.resize(820, 710)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Editor_Window.sizePolicy().hasHeightForWidth())
        Editor_Window.setSizePolicy(sizePolicy)
        Editor_Window.setMinimumSize(QSize(820, 710))
        Editor_Window.setMaximumSize(QSize(820, 710))
        self.centralwidget = QWidget(Editor_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(516, 10, 294, 352))
        self.Widget_list_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.Widget_list_layout.setObjectName(u"Widget_list_layout")
        self.Widget_list_layout.setContentsMargins(0, 0, 0, 0)
        self.Ready_Button_listWidget = QListWidget(self.verticalLayoutWidget)
        self.Ready_Button_listWidget.setObjectName(u"Ready_Button_listWidget")
        self.Ready_Button_listWidget.setMinimumSize(QSize(280, 360))
        self.Ready_Button_listWidget.setMaximumSize(QSize(280, 360))
        self.Ready_Button_listWidget.setTabletTracking(True)
        self.Ready_Button_listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Ready_Button_listWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.Ready_Button_listWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.Widget_list_layout.addWidget(self.Ready_Button_listWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 369, 788, 332))
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Edit_Button_groupBox = QGroupBox(self.widget)
        self.Edit_Button_groupBox.setObjectName(u"Edit_Button_groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Edit_Button_groupBox.sizePolicy().hasHeightForWidth())
        self.Edit_Button_groupBox.setSizePolicy(sizePolicy1)
        self.Edit_Button_groupBox.setMinimumSize(QSize(500, 330))
        self.Edit_Button_groupBox.setMaximumSize(QSize(500, 330))
        self.Edit_Button_groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Edit_Button_groupBox.setCheckable(False)
        self.Edit_Button_groupBox.setChecked(False)
        self.verticalLayout_4 = QVBoxLayout(self.Edit_Button_groupBox)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 5, 5, 5)
        self.Edit_ico_groupBox = QGroupBox(self.Edit_Button_groupBox)
        self.Edit_ico_groupBox.setObjectName(u"Edit_ico_groupBox")
        self.Edit_ico_groupBox.setMinimumSize(QSize(480, 150))
        self.Edit_ico_groupBox.setMaximumSize(QSize(480, 16777215))
        self.Edit_ico_groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Edit_ico_groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.Edit_ico_groupBox)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.Icon_layout = QVBoxLayout()
        self.Icon_layout.setSpacing(5)
        self.Icon_layout.setObjectName(u"Icon_layout")
        self.Icon_layout.setContentsMargins(5, 5, 5, 5)
        self.Choose_lib_icon_label = QLabel(self.Edit_ico_groupBox)
        self.Choose_lib_icon_label.setObjectName(u"Choose_lib_icon_label")
        self.Choose_lib_icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Icon_layout.addWidget(self.Choose_lib_icon_label)

        self.Browse_custom_pushButton = QPushButton(self.Edit_ico_groupBox)
        self.Browse_custom_pushButton.setObjectName(u"Browse_custom_pushButton")
        sizePolicy.setHeightForWidth(self.Browse_custom_pushButton.sizePolicy().hasHeightForWidth())
        self.Browse_custom_pushButton.setSizePolicy(sizePolicy)
        self.Browse_custom_pushButton.setMinimumSize(QSize(130, 30))
        self.Browse_custom_pushButton.setMaximumSize(QSize(130, 30))

        self.Icon_layout.addWidget(self.Browse_custom_pushButton)

        self.Choose_custom_icon_label = QLabel(self.Edit_ico_groupBox)
        self.Choose_custom_icon_label.setObjectName(u"Choose_custom_icon_label")
        self.Choose_custom_icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Icon_layout.addWidget(self.Choose_custom_icon_label)

        self.Browse_lib_pushButton = QPushButton(self.Edit_ico_groupBox)
        self.Browse_lib_pushButton.setObjectName(u"Browse_lib_pushButton")
        self.Browse_lib_pushButton.setMinimumSize(QSize(130, 30))
        self.Browse_lib_pushButton.setMaximumSize(QSize(130, 30))

        self.Icon_layout.addWidget(self.Browse_lib_pushButton)


        self.horizontalLayout_5.addLayout(self.Icon_layout)

        self.line_spacer_left = QFrame(self.Edit_ico_groupBox)
        self.line_spacer_left.setObjectName(u"line_spacer_left")
        self.line_spacer_left.setFrameShape(QFrame.Shape.VLine)
        self.line_spacer_left.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_spacer_left)

        self.Sign_layout = QVBoxLayout()
        self.Sign_layout.setSpacing(5)
        self.Sign_layout.setObjectName(u"Sign_layout")
        self.Sign_layout.setContentsMargins(5, 5, 5, 5)
        self.Add_sign_label = QLabel(self.Edit_ico_groupBox)
        self.Add_sign_label.setObjectName(u"Add_sign_label")
        self.Add_sign_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Sign_layout.addWidget(self.Add_sign_label)

        self.Sign_button_lineEdit = QLineEdit(self.Edit_ico_groupBox)
        self.Sign_button_lineEdit.setObjectName(u"Sign_button_lineEdit")
        sizePolicy.setHeightForWidth(self.Sign_button_lineEdit.sizePolicy().hasHeightForWidth())
        self.Sign_button_lineEdit.setSizePolicy(sizePolicy)
        self.Sign_button_lineEdit.setMinimumSize(QSize(130, 30))
        self.Sign_button_lineEdit.setMaximumSize(QSize(130, 30))

        self.Sign_layout.addWidget(self.Sign_button_lineEdit)

        self.Change_font = QLabel(self.Edit_ico_groupBox)
        self.Change_font.setObjectName(u"Change_font")
        self.Change_font.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Sign_layout.addWidget(self.Change_font)

        self.fontComboBox = QFontComboBox(self.Edit_ico_groupBox)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setMinimumSize(QSize(130, 30))
        self.fontComboBox.setMaximumSize(QSize(130, 30))

        self.Sign_layout.addWidget(self.fontComboBox)


        self.horizontalLayout_5.addLayout(self.Sign_layout)

        self.line_spacer_right = QFrame(self.Edit_ico_groupBox)
        self.line_spacer_right.setObjectName(u"line_spacer_right")
        self.line_spacer_right.setFrameShape(QFrame.Shape.VLine)
        self.line_spacer_right.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_spacer_right)

        self.Align_size_layout = QVBoxLayout()
        self.Align_size_layout.setSpacing(5)
        self.Align_size_layout.setObjectName(u"Align_size_layout")
        self.Align_size_layout.setContentsMargins(5, 5, 5, 5)
        self.Size_sign_label = QLabel(self.Edit_ico_groupBox)
        self.Size_sign_label.setObjectName(u"Size_sign_label")
        self.Size_sign_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Align_size_layout.addWidget(self.Size_sign_label)

        self.Size_font_comboBox = QComboBox(self.Edit_ico_groupBox)
        self.Size_font_comboBox.setObjectName(u"Size_font_comboBox")
        sizePolicy.setHeightForWidth(self.Size_font_comboBox.sizePolicy().hasHeightForWidth())
        self.Size_font_comboBox.setSizePolicy(sizePolicy)
        self.Size_font_comboBox.setMinimumSize(QSize(130, 30))
        self.Size_font_comboBox.setMaximumSize(QSize(130, 30))

        self.Align_size_layout.addWidget(self.Size_font_comboBox)

        self.Align_sign_label = QLabel(self.Edit_ico_groupBox)
        self.Align_sign_label.setObjectName(u"Align_sign_label")
        self.Align_sign_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Align_size_layout.addWidget(self.Align_sign_label)

        self.Align_combobox = QComboBox(self.Edit_ico_groupBox)
        self.Align_combobox.setObjectName(u"Align_combobox")
        self.Align_combobox.setMinimumSize(QSize(130, 30))
        self.Align_combobox.setMaximumSize(QSize(130, 30))

        self.Align_size_layout.addWidget(self.Align_combobox)


        self.horizontalLayout_5.addLayout(self.Align_size_layout)


        self.verticalLayout_4.addWidget(self.Edit_ico_groupBox)

        self.Action_Sav_layout = QHBoxLayout()
        self.Action_Sav_layout.setSpacing(5)
        self.Action_Sav_layout.setObjectName(u"Action_Sav_layout")
        self.Action_Sav_layout.setContentsMargins(0, -1, 0, -1)
        self.Action_groupbox = QGroupBox(self.Edit_Button_groupBox)
        self.Action_groupbox.setObjectName(u"Action_groupbox")
        self.Action_groupbox.setMinimumSize(QSize(345, 150))
        self.Action_groupbox.setMaximumSize(QSize(345, 150))
        self.Action_groupbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Action_groupbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_6 = QHBoxLayout(self.Action_groupbox)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.Edit_action_tabWidget = QTabWidget(self.Action_groupbox)
        self.Edit_action_tabWidget.setObjectName(u"Edit_action_tabWidget")
        sizePolicy.setHeightForWidth(self.Edit_action_tabWidget.sizePolicy().hasHeightForWidth())
        self.Edit_action_tabWidget.setSizePolicy(sizePolicy)
        self.Edit_action_tabWidget.setMinimumSize(QSize(310, 120))
        self.Edit_action_tabWidget.setMaximumSize(QSize(310, 120))
        self.Edit_action_tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Edit_action_tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.Edit_action_tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.Edit_action_tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.shortcut_tab = QWidget()
        self.shortcut_tab.setObjectName(u"shortcut_tab")
        self.verticalLayout_3 = QVBoxLayout(self.shortcut_tab)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.Add_shortcut_label = QLabel(self.shortcut_tab)
        self.Add_shortcut_label.setObjectName(u"Add_shortcut_label")

        self.verticalLayout_3.addWidget(self.Add_shortcut_label)

        self.Edit_action_tabWidget.addTab(self.shortcut_tab, "")
        self.soft_tab = QWidget()
        self.soft_tab.setObjectName(u"soft_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.soft_tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Soft_layout = QVBoxLayout()
        self.Soft_layout.setSpacing(5)
        self.Soft_layout.setObjectName(u"Soft_layout")
        self.Soft_layout.setContentsMargins(5, 5, 5, 5)
        self.Soft_Layout_but = QHBoxLayout()
        self.Soft_Layout_but.setSpacing(5)
        self.Soft_Layout_but.setObjectName(u"Soft_Layout_but")
        self.Soft_Layout_but.setContentsMargins(5, 5, 5, 5)
        self.Choose_soft_label = QLabel(self.soft_tab)
        self.Choose_soft_label.setObjectName(u"Choose_soft_label")

        self.Soft_Layout_but.addWidget(self.Choose_soft_label)

        self.Browse_pushButton = QPushButton(self.soft_tab)
        self.Browse_pushButton.setObjectName(u"Browse_pushButton")
        sizePolicy.setHeightForWidth(self.Browse_pushButton.sizePolicy().hasHeightForWidth())
        self.Browse_pushButton.setSizePolicy(sizePolicy)
        self.Browse_pushButton.setMaximumSize(QSize(150, 16777215))

        self.Soft_Layout_but.addWidget(self.Browse_pushButton)


        self.Soft_layout.addLayout(self.Soft_Layout_but)

        self.Soft_lineEdit = QLineEdit(self.soft_tab)
        self.Soft_lineEdit.setObjectName(u"Soft_lineEdit")
        sizePolicy.setHeightForWidth(self.Soft_lineEdit.sizePolicy().hasHeightForWidth())
        self.Soft_lineEdit.setSizePolicy(sizePolicy)
        self.Soft_lineEdit.setMinimumSize(QSize(0, 30))
        self.Soft_lineEdit.setMaximumSize(QSize(16777215, 30))

        self.Soft_layout.addWidget(self.Soft_lineEdit)


        self.horizontalLayout_3.addLayout(self.Soft_layout)

        self.Edit_action_tabWidget.addTab(self.soft_tab, "")
        self.Action_tab = QWidget()
        self.Action_tab.setObjectName(u"Action_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.Action_tab)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, -1, 5)
        self.Choose_action_label = QLabel(self.Action_tab)
        self.Choose_action_label.setObjectName(u"Choose_action_label")

        self.horizontalLayout_4.addWidget(self.Choose_action_label)

        self.Action_comboBox = QComboBox(self.Action_tab)
        self.Action_comboBox.setObjectName(u"Action_comboBox")

        self.horizontalLayout_4.addWidget(self.Action_comboBox)

        self.Edit_action_tabWidget.addTab(self.Action_tab, "")

        self.horizontalLayout_6.addWidget(self.Edit_action_tabWidget)


        self.Action_Sav_layout.addWidget(self.Action_groupbox)

        self.Save_but_GB = QGroupBox(self.Edit_Button_groupBox)
        self.Save_but_GB.setObjectName(u"Save_but_GB")
        self.Save_but_GB.setMinimumSize(QSize(125, 150))
        self.Save_but_GB.setMaximumSize(QSize(125, 150))
        self.Save_but_GB.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Save_but_GB.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.Save_but_GB)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.Save_Button_pushButton = QPushButton(self.Save_but_GB)
        self.Save_Button_pushButton.setObjectName(u"Save_Button_pushButton")
        sizePolicy.setHeightForWidth(self.Save_Button_pushButton.sizePolicy().hasHeightForWidth())
        self.Save_Button_pushButton.setSizePolicy(sizePolicy)
        self.Save_Button_pushButton.setMinimumSize(QSize(115, 50))
        self.Save_Button_pushButton.setMaximumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.Save_Button_pushButton)

        self.line = QFrame(self.Save_but_GB)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.Save_new_pushButton = QPushButton(self.Save_but_GB)
        self.Save_new_pushButton.setObjectName(u"Save_new_pushButton")
        sizePolicy.setHeightForWidth(self.Save_new_pushButton.sizePolicy().hasHeightForWidth())
        self.Save_new_pushButton.setSizePolicy(sizePolicy)
        self.Save_new_pushButton.setMinimumSize(QSize(115, 50))
        self.Save_new_pushButton.setMaximumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.Save_new_pushButton)


        self.Action_Sav_layout.addWidget(self.Save_but_GB)


        self.verticalLayout_4.addLayout(self.Action_Sav_layout)


        self.horizontalLayout_8.addWidget(self.Edit_Button_groupBox)

        self.Button_example_layout = QFrame(self.widget)
        self.Button_example_layout.setObjectName(u"Button_example_layout")
        sizePolicy1.setHeightForWidth(self.Button_example_layout.sizePolicy().hasHeightForWidth())
        self.Button_example_layout.setSizePolicy(sizePolicy1)
        self.Button_example_layout.setMinimumSize(QSize(280, 330))
        self.Button_example_layout.setMaximumSize(QSize(280, 330))
        self.Button_example_layout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Button_example_layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.Button_example_layout.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Button_example_layout)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.Page_control_frame_editor = QFrame(self.Button_example_layout)
        self.Page_control_frame_editor.setObjectName(u"Page_control_frame_editor")
        sizePolicy1.setHeightForWidth(self.Page_control_frame_editor.sizePolicy().hasHeightForWidth())
        self.Page_control_frame_editor.setSizePolicy(sizePolicy1)
        self.Page_control_frame_editor.setMinimumSize(QSize(270, 45))
        self.Page_control_frame_editor.setMaximumSize(QSize(270, 45))
        self.Page_control_frame_editor.setFrameShape(QFrame.Shape.StyledPanel)
        self.Page_control_frame_editor.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Page_control_frame_editor)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.BackButton_editor = QPushButton(self.Page_control_frame_editor)
        self.BackButton_editor.setObjectName(u"BackButton_editor")
        sizePolicy.setHeightForWidth(self.BackButton_editor.sizePolicy().hasHeightForWidth())
        self.BackButton_editor.setSizePolicy(sizePolicy)
        self.BackButton_editor.setMinimumSize(QSize(50, 30))
        self.BackButton_editor.setMaximumSize(QSize(50, 30))

        self.horizontalLayout.addWidget(self.BackButton_editor)

        self.Remove_page_button_editor = QPushButton(self.Page_control_frame_editor)
        self.Remove_page_button_editor.setObjectName(u"Remove_page_button_editor")
        sizePolicy.setHeightForWidth(self.Remove_page_button_editor.sizePolicy().hasHeightForWidth())
        self.Remove_page_button_editor.setSizePolicy(sizePolicy)
        self.Remove_page_button_editor.setMinimumSize(QSize(30, 30))
        self.Remove_page_button_editor.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Remove_page_button_editor)

        self.Current_page_label_editor = QLabel(self.Page_control_frame_editor)
        self.Current_page_label_editor.setObjectName(u"Current_page_label_editor")
        self.Current_page_label_editor.setMinimumSize(QSize(50, 30))
        self.Current_page_label_editor.setMaximumSize(QSize(50, 30))
        self.Current_page_label_editor.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Current_page_label_editor.setFrameShape(QFrame.Shape.StyledPanel)
        self.Current_page_label_editor.setFrameShadow(QFrame.Shadow.Plain)
        self.Current_page_label_editor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Current_page_label_editor)

        self.Add_page_button_editor = QPushButton(self.Page_control_frame_editor)
        self.Add_page_button_editor.setObjectName(u"Add_page_button_editor")
        sizePolicy.setHeightForWidth(self.Add_page_button_editor.sizePolicy().hasHeightForWidth())
        self.Add_page_button_editor.setSizePolicy(sizePolicy)
        self.Add_page_button_editor.setMinimumSize(QSize(30, 30))
        self.Add_page_button_editor.setMaximumSize(QSize(30, 30))
        self.Add_page_button_editor.setBaseSize(QSize(25, 25))
        self.Add_page_button_editor.setMouseTracking(False)
        self.Add_page_button_editor.setTabletTracking(False)
        self.Add_page_button_editor.setFlat(False)

        self.horizontalLayout.addWidget(self.Add_page_button_editor)

        self.NextButton_editor = QPushButton(self.Page_control_frame_editor)
        self.NextButton_editor.setObjectName(u"NextButton_editor")
        sizePolicy.setHeightForWidth(self.NextButton_editor.sizePolicy().hasHeightForWidth())
        self.NextButton_editor.setSizePolicy(sizePolicy)
        self.NextButton_editor.setMinimumSize(QSize(50, 30))
        self.NextButton_editor.setMaximumSize(QSize(50, 30))

        self.horizontalLayout.addWidget(self.NextButton_editor)


        self.verticalLayout.addWidget(self.Page_control_frame_editor)

        self.Example_groupBox = QGroupBox(self.Button_example_layout)
        self.Example_groupBox.setObjectName(u"Example_groupBox")
        sizePolicy1.setHeightForWidth(self.Example_groupBox.sizePolicy().hasHeightForWidth())
        self.Example_groupBox.setSizePolicy(sizePolicy1)
        self.Example_groupBox.setMinimumSize(QSize(270, 250))
        self.Example_groupBox.setMaximumSize(QSize(270, 250))
        self.Example_groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.Example_groupBox)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.Example_toolButton = QToolButton(self.Example_groupBox)
        self.Example_toolButton.setObjectName(u"Example_toolButton")
        sizePolicy.setHeightForWidth(self.Example_toolButton.sizePolicy().hasHeightForWidth())
        self.Example_toolButton.setSizePolicy(sizePolicy)
        self.Example_toolButton.setMinimumSize(QSize(150, 150))
        self.Example_toolButton.setMaximumSize(QSize(150, 150))
        self.Example_toolButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Example_toolButton.setIconSize(QSize(128, 128))
        self.Example_toolButton.setCheckable(False)
        self.Example_toolButton.setChecked(False)
        self.Example_toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.Example_toolButton)


        self.verticalLayout.addWidget(self.Example_groupBox)


        self.horizontalLayout_8.addWidget(self.Button_example_layout)

        self.Button_editor_stackedWidget = QStackedWidget(self.centralwidget)
        self.Button_editor_stackedWidget.setObjectName(u"Button_editor_stackedWidget")
        self.Button_editor_stackedWidget.setGeometry(QRect(10, 10, 500, 360))
        self.Button_editor_stackedWidget.setMinimumSize(QSize(500, 360))
        self.Button_editor_stackedWidget.setMaximumSize(QSize(500, 360))
        self.Button_editor_stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMinimumSize(QSize(500, 360))
        self.page_1.setMaximumSize(QSize(500, 360))
        self.Button_frame = QFrame(self.page_1)
        self.Button_frame.setObjectName(u"Button_frame")
        self.Button_frame.setGeometry(QRect(0, 0, 500, 360))
        self.Button_frame.setMinimumSize(QSize(500, 360))
        self.Button_frame.setMaximumSize(QSize(500, 360))
        self.Button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.Button_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Edit_toolButton_01 = QToolButton(self.Button_frame)
        self.Edit_toolButton_01.setObjectName(u"Edit_toolButton_01")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_01.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_01.setSizePolicy(sizePolicy)
        self.Edit_toolButton_01.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_01.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_01.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_01.setIconSize(QSize(96, 96))
        self.Edit_toolButton_01.setCheckable(True)
        self.Edit_toolButton_01.setChecked(False)
        self.Edit_toolButton_01.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_01, 0, 0, 1, 1)

        self.Edit_toolButton_02 = QToolButton(self.Button_frame)
        self.Edit_toolButton_02.setObjectName(u"Edit_toolButton_02")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_02.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_02.setSizePolicy(sizePolicy)
        self.Edit_toolButton_02.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_02.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_02.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_02.setIconSize(QSize(96, 96))
        self.Edit_toolButton_02.setCheckable(True)
        self.Edit_toolButton_02.setChecked(False)
        self.Edit_toolButton_02.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_02, 0, 1, 1, 1)

        self.Edit_toolButton_03 = QToolButton(self.Button_frame)
        self.Edit_toolButton_03.setObjectName(u"Edit_toolButton_03")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_03.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_03.setSizePolicy(sizePolicy)
        self.Edit_toolButton_03.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_03.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_03.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_03.setIconSize(QSize(96, 96))
        self.Edit_toolButton_03.setCheckable(True)
        self.Edit_toolButton_03.setChecked(False)
        self.Edit_toolButton_03.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_03, 0, 2, 1, 1)

        self.Edit_toolButton_04 = QToolButton(self.Button_frame)
        self.Edit_toolButton_04.setObjectName(u"Edit_toolButton_04")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_04.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_04.setSizePolicy(sizePolicy)
        self.Edit_toolButton_04.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_04.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_04.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_04.setIconSize(QSize(96, 96))
        self.Edit_toolButton_04.setCheckable(True)
        self.Edit_toolButton_04.setChecked(False)
        self.Edit_toolButton_04.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_04, 0, 3, 1, 1)

        self.Edit_toolButton_05 = QToolButton(self.Button_frame)
        self.Edit_toolButton_05.setObjectName(u"Edit_toolButton_05")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_05.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_05.setSizePolicy(sizePolicy)
        self.Edit_toolButton_05.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_05.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_05.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_05.setIconSize(QSize(96, 96))
        self.Edit_toolButton_05.setCheckable(True)
        self.Edit_toolButton_05.setChecked(False)
        self.Edit_toolButton_05.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_05, 1, 0, 1, 1)

        self.Edit_toolButton_06 = QToolButton(self.Button_frame)
        self.Edit_toolButton_06.setObjectName(u"Edit_toolButton_06")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_06.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_06.setSizePolicy(sizePolicy)
        self.Edit_toolButton_06.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_06.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_06.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_06.setIconSize(QSize(96, 96))
        self.Edit_toolButton_06.setCheckable(True)
        self.Edit_toolButton_06.setChecked(False)
        self.Edit_toolButton_06.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_06, 1, 1, 1, 1)

        self.Edit_toolButton_07 = QToolButton(self.Button_frame)
        self.Edit_toolButton_07.setObjectName(u"Edit_toolButton_07")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_07.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_07.setSizePolicy(sizePolicy)
        self.Edit_toolButton_07.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_07.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_07.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_07.setIconSize(QSize(96, 96))
        self.Edit_toolButton_07.setCheckable(True)
        self.Edit_toolButton_07.setChecked(False)
        self.Edit_toolButton_07.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_07, 1, 2, 1, 1)

        self.Edit_toolButton_08 = QToolButton(self.Button_frame)
        self.Edit_toolButton_08.setObjectName(u"Edit_toolButton_08")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_08.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_08.setSizePolicy(sizePolicy)
        self.Edit_toolButton_08.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_08.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_08.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_08.setIconSize(QSize(96, 96))
        self.Edit_toolButton_08.setCheckable(True)
        self.Edit_toolButton_08.setChecked(False)
        self.Edit_toolButton_08.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_08, 1, 3, 1, 1)

        self.Edit_toolButton_09 = QToolButton(self.Button_frame)
        self.Edit_toolButton_09.setObjectName(u"Edit_toolButton_09")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_09.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_09.setSizePolicy(sizePolicy)
        self.Edit_toolButton_09.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_09.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_09.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_09.setIconSize(QSize(96, 96))
        self.Edit_toolButton_09.setCheckable(True)
        self.Edit_toolButton_09.setChecked(False)
        self.Edit_toolButton_09.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_09, 2, 0, 1, 1)

        self.Edit_toolButton_10 = QToolButton(self.Button_frame)
        self.Edit_toolButton_10.setObjectName(u"Edit_toolButton_10")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_10.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_10.setSizePolicy(sizePolicy)
        self.Edit_toolButton_10.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_10.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_10.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_10.setIconSize(QSize(96, 96))
        self.Edit_toolButton_10.setCheckable(True)
        self.Edit_toolButton_10.setChecked(False)
        self.Edit_toolButton_10.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_10, 2, 1, 1, 1)

        self.Edit_toolButton_11 = QToolButton(self.Button_frame)
        self.Edit_toolButton_11.setObjectName(u"Edit_toolButton_11")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_11.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_11.setSizePolicy(sizePolicy)
        self.Edit_toolButton_11.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_11.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_11.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_11.setIconSize(QSize(96, 96))
        self.Edit_toolButton_11.setCheckable(True)
        self.Edit_toolButton_11.setChecked(False)
        self.Edit_toolButton_11.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_11, 2, 2, 1, 1)

        self.Edit_toolButton_12 = QToolButton(self.Button_frame)
        self.Edit_toolButton_12.setObjectName(u"Edit_toolButton_12")
        sizePolicy.setHeightForWidth(self.Edit_toolButton_12.sizePolicy().hasHeightForWidth())
        self.Edit_toolButton_12.setSizePolicy(sizePolicy)
        self.Edit_toolButton_12.setMinimumSize(QSize(100, 100))
        self.Edit_toolButton_12.setMaximumSize(QSize(100, 100))
        self.Edit_toolButton_12.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Edit_toolButton_12.setIconSize(QSize(96, 96))
        self.Edit_toolButton_12.setCheckable(True)
        self.Edit_toolButton_12.setChecked(False)
        self.Edit_toolButton_12.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.Edit_toolButton_12, 2, 3, 1, 1)

        self.Button_editor_stackedWidget.addWidget(self.page_1)
        Editor_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Editor_Window)

        self.Edit_action_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Editor_Window)
    # setupUi

    def retranslateUi(self, Editor_Window):
        Editor_Window.setWindowTitle(QCoreApplication.translate("Editor_Window", u"Editor Window", None))
        self.Edit_Button_groupBox.setTitle("")
        self.Edit_ico_groupBox.setTitle(QCoreApplication.translate("Editor_Window", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043a\u043e\u043d\u043a\u0443", None))
        self.Choose_lib_icon_label.setText(QCoreApplication.translate("Editor_Window", u"\u0421\u0432\u043e\u044f \u0438\u043a\u043e\u043d\u043a\u0430:", None))
        self.Browse_custom_pushButton.setText(QCoreApplication.translate("Editor_Window", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.Choose_custom_icon_label.setText(QCoreApplication.translate("Editor_Window", u"\u0418\u0437 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438:", None))
        self.Browse_lib_pushButton.setText(QCoreApplication.translate("Editor_Window", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.Add_sign_label.setText(QCoreApplication.translate("Editor_Window", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u044c:", None))
        self.Change_font.setText(QCoreApplication.translate("Editor_Window", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0448\u0440\u0438\u0444\u0442:", None))
        self.Size_sign_label.setText(QCoreApplication.translate("Editor_Window", u"\u0420\u0430\u0437\u043c\u0435\u0440:", None))
        self.Align_sign_label.setText(QCoreApplication.translate("Editor_Window", u"\u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435:", None))
        self.Action_groupbox.setTitle(QCoreApplication.translate("Editor_Window", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.Add_shortcut_label.setText(QCoreApplication.translate("Editor_Window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e \u043a\u043b\u0430\u0432\u0438\u0448:", None))
        self.Edit_action_tabWidget.setTabText(self.Edit_action_tabWidget.indexOf(self.shortcut_tab), QCoreApplication.translate("Editor_Window", u"\u0421\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448", None))
        self.Choose_soft_label.setText(QCoreApplication.translate("Editor_Window", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443:", None))
        self.Browse_pushButton.setText(QCoreApplication.translate("Editor_Window", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.Edit_action_tabWidget.setTabText(self.Edit_action_tabWidget.indexOf(self.soft_tab), QCoreApplication.translate("Editor_Window", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.Choose_action_label.setText(QCoreApplication.translate("Editor_Window", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435:", None))
        self.Edit_action_tabWidget.setTabText(self.Edit_action_tabWidget.indexOf(self.Action_tab), QCoreApplication.translate("Editor_Window", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.Save_but_GB.setTitle(QCoreApplication.translate("Editor_Window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435", None))
        self.Save_Button_pushButton.setText(QCoreApplication.translate("Editor_Window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.Save_new_pushButton.setText(QCoreApplication.translate("Editor_Window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u043a\u043d\u043e\u043f\u043a\u0443", None))
        self.BackButton_editor.setText(QCoreApplication.translate("Editor_Window", u"Back", None))
        self.Remove_page_button_editor.setText(QCoreApplication.translate("Editor_Window", u"-", None))
        self.Current_page_label_editor.setText("")
        self.Add_page_button_editor.setText(QCoreApplication.translate("Editor_Window", u"+", None))
        self.NextButton_editor.setText(QCoreApplication.translate("Editor_Window", u"Next", None))
        self.Example_groupBox.setTitle(QCoreApplication.translate("Editor_Window", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430", None))
        self.Example_toolButton.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_01.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_02.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_03.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_04.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_05.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_06.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_07.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_08.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_09.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_10.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_11.setText(QCoreApplication.translate("Editor_Window", u"...", None))
        self.Edit_toolButton_12.setText(QCoreApplication.translate("Editor_Window", u"...", None))
    # retranslateUi

