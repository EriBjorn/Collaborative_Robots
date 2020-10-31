# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colab_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1394, 861)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.WidgetMenu = QtWidgets.QWidget(self.centralwidget)
        self.WidgetMenu.setMaximumSize(QtCore.QSize(500, 16777215))
        self.WidgetMenu.setStyleSheet("background-color:rgb(127, 127, 127)")
        self.WidgetMenu.setObjectName("WidgetMenu")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.WidgetMenu)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.WidgetJustifier = QtWidgets.QWidget(self.WidgetMenu)
        self.WidgetJustifier.setObjectName("WidgetJustifier")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.WidgetJustifier)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.modbusConnectBtn = QtWidgets.QPushButton(self.WidgetJustifier)
        self.modbusConnectBtn.setStyleSheet("background-color: rgb(0, 226, 0)")
        self.modbusConnectBtn.setObjectName("modbusConnectBtn")
        self.gridLayout_3.addWidget(self.modbusConnectBtn, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.WidgetJustifier)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 6, 0, 1, 1)
        self.modbusDisconnectBtn = QtWidgets.QPushButton(self.WidgetJustifier)
        self.modbusDisconnectBtn.setStyleSheet("background-color: rgb(255, 83, 108)")
        self.modbusDisconnectBtn.setObjectName("modbusDisconnectBtn")
        self.gridLayout_3.addWidget(self.modbusDisconnectBtn, 4, 0, 1, 1)
        self.PageSelectors = QtWidgets.QFrame(self.WidgetJustifier)
        self.PageSelectors.setStyleSheet("background-color:rgb(153, 153, 153);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.PageSelectors.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.PageSelectors.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PageSelectors.setLineWidth(1)
        self.PageSelectors.setMidLineWidth(0)
        self.PageSelectors.setObjectName("PageSelectors")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PageSelectors)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Demo1PageBtn = QtWidgets.QPushButton(self.PageSelectors)
        self.Demo1PageBtn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Demo1PageBtn.setFont(font)
        self.Demo1PageBtn.setStyleSheet("background-color: lightgrey;\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"padding: 4px;\n"
"\n"
"QPushbutton::pressed\n"
"{\n"
"background-color: grey;\n"
"border-style: inset;\n"
"border-color: grey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"padding: 4px;\n"
"}")
        self.Demo1PageBtn.setFlat(False)
        self.Demo1PageBtn.setObjectName("Demo1PageBtn")
        self.verticalLayout.addWidget(self.Demo1PageBtn)
        self.Demo2PageBtn = QtWidgets.QPushButton(self.PageSelectors)
        self.Demo2PageBtn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Demo2PageBtn.setFont(font)
        self.Demo2PageBtn.setStyleSheet("background-color: lightgrey;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.Demo2PageBtn.setObjectName("Demo2PageBtn")
        self.verticalLayout.addWidget(self.Demo2PageBtn)
        self.Demo3PageBtn = QtWidgets.QPushButton(self.PageSelectors)
        self.Demo3PageBtn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Demo3PageBtn.setFont(font)
        self.Demo3PageBtn.setStyleSheet("background-color: lightgrey;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.Demo3PageBtn.setObjectName("Demo3PageBtn")
        self.verticalLayout.addWidget(self.Demo3PageBtn)
        self.AboutPageBtn = QtWidgets.QPushButton(self.PageSelectors)
        self.AboutPageBtn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.AboutPageBtn.setFont(font)
        self.AboutPageBtn.setMouseTracking(False)
        self.AboutPageBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AboutPageBtn.setAutoFillBackground(False)
        self.AboutPageBtn.setStyleSheet("background-color: lightgrey;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: grey;\n"
"padding: 4px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/LogoPrefix/about-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutPageBtn.setIcon(icon)
        self.AboutPageBtn.setIconSize(QtCore.QSize(40, 40))
        self.AboutPageBtn.setObjectName("AboutPageBtn")
        self.verticalLayout.addWidget(self.AboutPageBtn)
        self.gridLayout_3.addWidget(self.PageSelectors, 2, 0, 1, 1)
        self.LogoJustifier = QtWidgets.QWidget(self.WidgetJustifier)
        self.LogoJustifier.setObjectName("LogoJustifier")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.LogoJustifier)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.LogoJustifier)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.logo = QtWidgets.QLabel(self.LogoJustifier)
        self.logo.setObjectName("logo")
        self.gridLayout_4.addWidget(self.logo, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.LogoJustifier, 0, 0, 1, 1)
        self.whichDemoIsRunLabel = QtWidgets.QLabel(self.WidgetJustifier)
        self.whichDemoIsRunLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setPointSize(16)
        font.setItalic(False)
        self.whichDemoIsRunLabel.setFont(font)
        self.whichDemoIsRunLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.whichDemoIsRunLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.whichDemoIsRunLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.whichDemoIsRunLabel.setObjectName("whichDemoIsRunLabel")
        self.gridLayout_3.addWidget(self.whichDemoIsRunLabel, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.WidgetJustifier, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.WidgetMenu, 0, 0, 1, 1)
        self.Widget_Contents = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Widget_Contents.sizePolicy().hasHeightForWidth())
        self.Widget_Contents.setSizePolicy(sizePolicy)
        self.Widget_Contents.setStyleSheet("background-color:rgb(153, 153, 153)")
        self.Widget_Contents.setObjectName("Widget_Contents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Widget_Contents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.WidgetPages = QtWidgets.QStackedWidget(self.Widget_Contents)
        self.WidgetPages.setObjectName("WidgetPages")
        self.Demo1Page = QtWidgets.QWidget()
        self.Demo1Page.setObjectName("Demo1Page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Demo1Page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Demo1Label = QtWidgets.QLabel(self.Demo1Page)
        self.Demo1Label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Demo1Label.setFont(font)
        self.Demo1Label.setTextFormat(QtCore.Qt.PlainText)
        self.Demo1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Demo1Label.setObjectName("Demo1Label")
        self.verticalLayout_2.addWidget(self.Demo1Label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalFrame_2 = QtWidgets.QFrame(self.Demo1Page)
        self.verticalFrame_2.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.verticalFrame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.verticalFrame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.verticalFrame_2)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.ModbusInputDemo1Rob1 = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ModbusInputDemo1Rob1.setFont(font)
        self.ModbusInputDemo1Rob1.setStyleSheet("")
        self.ModbusInputDemo1Rob1.setText("")
        self.ModbusInputDemo1Rob1.setAlignment(QtCore.Qt.AlignCenter)
        self.ModbusInputDemo1Rob1.setObjectName("ModbusInputDemo1Rob1")
        self.verticalLayout_8.addWidget(self.ModbusInputDemo1Rob1)
        self.horizontalLayout_3.addWidget(self.verticalFrame_2)
        self.verticalFrame = QtWidgets.QFrame(self.Demo1Page)
        self.verticalFrame.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame.setLineWidth(1)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.verticalFrame)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.ModbusInputDemo1Rob2 = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ModbusInputDemo1Rob2.setFont(font)
        self.ModbusInputDemo1Rob2.setText("")
        self.ModbusInputDemo1Rob2.setObjectName("ModbusInputDemo1Rob2")
        self.verticalLayout_7.addWidget(self.ModbusInputDemo1Rob2)
        self.horizontalLayout_3.addWidget(self.verticalFrame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.StartDemo1Btn = QtWidgets.QPushButton(self.Demo1Page)
        self.StartDemo1Btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StartDemo1Btn.setFont(font)
        self.StartDemo1Btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/LogoPrefix/start_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartDemo1Btn.setIcon(icon1)
        self.StartDemo1Btn.setIconSize(QtCore.QSize(100, 100))
        self.StartDemo1Btn.setCheckable(False)
        self.StartDemo1Btn.setObjectName("StartDemo1Btn")
        self.verticalLayout_2.addWidget(self.StartDemo1Btn)
        self.StopDemo1Btn = QtWidgets.QPushButton(self.Demo1Page)
        self.StopDemo1Btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StopDemo1Btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/LogoPrefix/stop_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopDemo1Btn.setIcon(icon2)
        self.StopDemo1Btn.setIconSize(QtCore.QSize(70, 70))
        self.StopDemo1Btn.setObjectName("StopDemo1Btn")
        self.verticalLayout_2.addWidget(self.StopDemo1Btn)
        self.WidgetPages.addWidget(self.Demo1Page)
        self.Demo2Page = QtWidgets.QWidget()
        self.Demo2Page.setObjectName("Demo2Page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Demo2Page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Demo2Label = QtWidgets.QLabel(self.Demo2Page)
        self.Demo2Label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Demo2Label.setFont(font)
        self.Demo2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Demo2Label.setObjectName("Demo2Label")
        self.verticalLayout_3.addWidget(self.Demo2Label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalFrame_21 = QtWidgets.QFrame(self.Demo2Page)
        self.verticalFrame_21.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.verticalFrame_21.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.verticalFrame_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame_21.setObjectName("verticalFrame_21")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalFrame_21)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.verticalFrame_21)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.ModbusInputDemo2Rob1 = QtWidgets.QLabel(self.verticalFrame_21)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ModbusInputDemo2Rob1.setFont(font)
        self.ModbusInputDemo2Rob1.setText("")
        self.ModbusInputDemo2Rob1.setAlignment(QtCore.Qt.AlignCenter)
        self.ModbusInputDemo2Rob1.setObjectName("ModbusInputDemo2Rob1")
        self.verticalLayout_10.addWidget(self.ModbusInputDemo2Rob1)
        self.horizontalLayout_4.addWidget(self.verticalFrame_21)
        self.verticalFrame1 = QtWidgets.QFrame(self.Demo2Page)
        self.verticalFrame1.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.verticalFrame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.verticalFrame1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.verticalFrame1)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.ModbusInputDemo2Rob2 = QtWidgets.QLabel(self.verticalFrame1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ModbusInputDemo2Rob2.setFont(font)
        self.ModbusInputDemo2Rob2.setText("")
        self.ModbusInputDemo2Rob2.setAlignment(QtCore.Qt.AlignCenter)
        self.ModbusInputDemo2Rob2.setObjectName("ModbusInputDemo2Rob2")
        self.verticalLayout_9.addWidget(self.ModbusInputDemo2Rob2)
        self.horizontalLayout_4.addWidget(self.verticalFrame1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.StartDemo2Btn = QtWidgets.QPushButton(self.Demo2Page)
        self.StartDemo2Btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StartDemo2Btn.setFont(font)
        self.StartDemo2Btn.setIcon(icon1)
        self.StartDemo2Btn.setIconSize(QtCore.QSize(100, 100))
        self.StartDemo2Btn.setObjectName("StartDemo2Btn")
        self.verticalLayout_3.addWidget(self.StartDemo2Btn)
        self.StopDemo2Btn = QtWidgets.QPushButton(self.Demo2Page)
        self.StopDemo2Btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StopDemo2Btn.setFont(font)
        self.StopDemo2Btn.setIcon(icon2)
        self.StopDemo2Btn.setIconSize(QtCore.QSize(70, 70))
        self.StopDemo2Btn.setObjectName("StopDemo2Btn")
        self.verticalLayout_3.addWidget(self.StopDemo2Btn)
        self.WidgetPages.addWidget(self.Demo2Page)
        self.Demo3Page = QtWidgets.QWidget()
        self.Demo3Page.setObjectName("Demo3Page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Demo3Page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Demo3Label = QtWidgets.QLabel(self.Demo3Page)
        self.Demo3Label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Demo3Label.setFont(font)
        self.Demo3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Demo3Label.setObjectName("Demo3Label")
        self.verticalLayout_4.addWidget(self.Demo3Label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalFrame2 = QtWidgets.QFrame(self.Demo3Page)
        self.verticalFrame2.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.verticalFrame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.verticalFrame2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame2.setObjectName("verticalFrame2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalFrame2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.verticalFrame2)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.ModbusInputDemo3Rob1 = QtWidgets.QLabel(self.verticalFrame2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ModbusInputDemo3Rob1.setFont(font)
        self.ModbusInputDemo3Rob1.setText("")
        self.ModbusInputDemo3Rob1.setAlignment(QtCore.Qt.AlignCenter)
        self.ModbusInputDemo3Rob1.setObjectName("ModbusInputDemo3Rob1")
        self.verticalLayout_11.addWidget(self.ModbusInputDemo3Rob1)
        self.horizontalLayout_5.addWidget(self.verticalFrame2)
        self.verticalFrame_22 = QtWidgets.QFrame(self.Demo3Page)
        self.verticalFrame_22.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: grey;\n"
"padding: 4px;")
        self.verticalFrame_22.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.verticalFrame_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame_22.setObjectName("verticalFrame_22")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalFrame_22)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.verticalFrame_22)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_12.addWidget(self.label_13)
        self.ModbusInputDemo3Rob2 = QtWidgets.QLabel(self.verticalFrame_22)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ModbusInputDemo3Rob2.setFont(font)
        self.ModbusInputDemo3Rob2.setText("")
        self.ModbusInputDemo3Rob2.setAlignment(QtCore.Qt.AlignCenter)
        self.ModbusInputDemo3Rob2.setObjectName("ModbusInputDemo3Rob2")
        self.verticalLayout_12.addWidget(self.ModbusInputDemo3Rob2)
        self.horizontalLayout_5.addWidget(self.verticalFrame_22)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.StartDemo3Btn = QtWidgets.QPushButton(self.Demo3Page)
        self.StartDemo3Btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StartDemo3Btn.setFont(font)
        self.StartDemo3Btn.setIcon(icon1)
        self.StartDemo3Btn.setIconSize(QtCore.QSize(100, 100))
        self.StartDemo3Btn.setObjectName("StartDemo3Btn")
        self.verticalLayout_4.addWidget(self.StartDemo3Btn)
        self.StopDemo3Btn = QtWidgets.QPushButton(self.Demo3Page)
        self.StopDemo3Btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StopDemo3Btn.setFont(font)
        self.StopDemo3Btn.setIcon(icon2)
        self.StopDemo3Btn.setIconSize(QtCore.QSize(70, 70))
        self.StopDemo3Btn.setObjectName("StopDemo3Btn")
        self.verticalLayout_4.addWidget(self.StopDemo3Btn)
        self.WidgetPages.addWidget(self.Demo3Page)
        self.AboutPage = QtWidgets.QWidget()
        self.AboutPage.setObjectName("AboutPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.AboutPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.AboutLabel = QtWidgets.QLabel(self.AboutPage)
        self.AboutLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.AboutLabel.setFont(font)
        self.AboutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutLabel.setObjectName("AboutLabel")
        self.verticalLayout_5.addWidget(self.AboutLabel)
        self.AboutTxt = QtWidgets.QLabel(self.AboutPage)
        self.AboutTxt.setObjectName("AboutTxt")
        self.verticalLayout_5.addWidget(self.AboutTxt)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.AboutPage)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.AboutPage)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.AboutPage)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_14 = QtWidgets.QLabel(self.AboutPage)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.label_4 = QtWidgets.QLabel(self.AboutPage)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.AboutPage)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.WidgetPages.addWidget(self.AboutPage)
        self.horizontalLayout.addWidget(self.WidgetPages)
        self.gridLayout.addWidget(self.Widget_Contents, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.WidgetPages.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.modbusConnectBtn.setText(_translate("MainWindow", "Connect Modbus Server"))
        self.label_12.setText(_translate("MainWindow", "Modbus is not connected"))
        self.modbusDisconnectBtn.setText(_translate("MainWindow", "Disconnect Modbus Server"))
        self.Demo1PageBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Demo1PageBtn.setText(_translate("MainWindow", "Demo 1: Easy Collaborative Task"))
        self.Demo2PageBtn.setText(_translate("MainWindow", "Demo 2: Simple Gear Assembly"))
        self.Demo3PageBtn.setText(_translate("MainWindow", "Demo 3: Advanced Gear Assembly"))
        self.AboutPageBtn.setText(_translate("MainWindow", "About this project"))
        self.label.setText(_translate("MainWindow", "Collaborative Robots in Manulab"))
        self.logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/LogoPrefix/Intro-Pic-Cobot-Page-1.png\"/></p></body></html>"))
        self.whichDemoIsRunLabel.setText(_translate("MainWindow", "No demo is currently running"))
        self.Demo1Label.setText(_translate("MainWindow", "Demo 1: Easy Collaborative Task"))
        self.label_7.setText(_translate("MainWindow", "Current task of Robot 1"))
        self.label_8.setText(_translate("MainWindow", "Current task of Robot 2"))
        self.StartDemo1Btn.setText(_translate("MainWindow", "Start Demo 1"))
        self.StopDemo1Btn.setText(_translate("MainWindow", "Stop Demo 1"))
        self.Demo2Label.setText(_translate("MainWindow", "Demo 2: Simple Gear Assembly"))
        self.label_9.setText(_translate("MainWindow", "Current task of Robot 1"))
        self.label_11.setText(_translate("MainWindow", "Current task of Robot 2"))
        self.StartDemo2Btn.setText(_translate("MainWindow", "Start Demo 2"))
        self.StopDemo2Btn.setText(_translate("MainWindow", "Stop Demo 2"))
        self.Demo3Label.setText(_translate("MainWindow", "Demo 3: Advanced Gear Assembly"))
        self.label_10.setText(_translate("MainWindow", "Current task of Robot 1"))
        self.label_13.setText(_translate("MainWindow", "Current task of Robot 2"))
        self.StartDemo3Btn.setText(_translate("MainWindow", "Start Demo 3"))
        self.StopDemo3Btn.setText(_translate("MainWindow", "Stop Demo 3"))
        self.AboutLabel.setText(_translate("MainWindow", "About this project"))
        self.AboutTxt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">This system was created by a group of automation engineering students at NTNU in Aalesund.<br/>The system was created as part of a project in the Mechatronics subject.<br/>The purpose of the project was to make the robots collaborate on a complex task, using vision and a force sensor.</span></p><p><span style=\" font-size:18pt;\">The group consisted of the following students:<br/>Isak Gamnes Sneltvedt<br/>Erik Bjørnøy<br/>Erlend Holseker<br/>Arvin Khodabandeh</span></p><p><span style=\" font-size:18pt;\">The collaborative robots in the Manulab are delivered by Omron.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/LogoPrefix/robothandinhand.png\"/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/LogoPrefix/standard_logo_ntnu_u-slagord.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/LogoPrefix/OMRON_Logo.svg.png\"/></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/LogoPrefix/amatec.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/LogoPrefix/Python_logo_and_wordmark.svg.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "This HMI is powered by Python."))
import Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
