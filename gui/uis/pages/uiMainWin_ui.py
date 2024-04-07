# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiMainWin.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QFormLayout, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 890)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionload = QAction(MainWindow)
        self.actionload.setObjectName(u"actionload")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actiondad = QAction(MainWindow)
        self.actiondad.setObjectName(u"actiondad")
        self.actiongg = QAction(MainWindow)
        self.actiongg.setObjectName(u"actiongg")
        self.actiongraph_2 = QAction(MainWindow)
        self.actiongraph_2.setObjectName(u"actiongraph_2")
        self.actiongraph_2.setCheckable(True)
        self.actiongraph_2.setChecked(True)
        self.actiongraph_2.setEnabled(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(191, 300))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.formLayoutWidget_2 = QWidget(self.widget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 10, 161, 141))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(7)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox = QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBox_2 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_2)

        self.label_3 = QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.comboBox_3 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBox_3)

        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.comboBox_4 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBox_4)

        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.comboBox_5 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBox_5)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(45, 160, 133, 22))
        self.labelStatus = QLabel(self.widget)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setGeometry(QRect(20, 160, 16, 21))
        self.labelStatus.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus.setTextFormat(Qt.AutoText)
        self.pushButton_scan = QPushButton(self.widget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setGeometry(QRect(20, 190, 151, 24))
        self.pushButton_scan_classic = QPushButton(self.widget)
        self.pushButton_scan_classic.setObjectName(u"pushButton_scan_classic")
        self.pushButton_scan_classic.setGeometry(QRect(20, 220, 151, 24))
        self.labelStatus_2 = QLabel(self.widget)
        self.labelStatus_2.setObjectName(u"labelStatus_2")
        self.labelStatus_2.setGeometry(QRect(20, 260, 31, 21))
        self.labelStatus_2.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_2.setTextFormat(Qt.AutoText)
        self.labelStatus_3 = QLabel(self.widget)
        self.labelStatus_3.setObjectName(u"labelStatus_3")
        self.labelStatus_3.setGeometry(QRect(80, 260, 31, 21))
        self.labelStatus_3.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_3.setTextFormat(Qt.AutoText)
        self.labelStatus_4 = QLabel(self.widget)
        self.labelStatus_4.setObjectName(u"labelStatus_4")
        self.labelStatus_4.setGeometry(QRect(140, 260, 31, 21))
        self.labelStatus_4.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_4.setFrameShadow(QFrame.Plain)
        self.labelStatus_4.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menudata = QMenu(self.menubar)
        self.menudata.setObjectName(u"menudata")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.verticalLayout.addLayout(self.gridLayout_5)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget)
        self.dockWidget_12 = QDockWidget(MainWindow)
        self.dockWidget_12.setObjectName(u"dockWidget_12")
        self.dockWidget_12.setMinimumSize(QSize(865, 123))
        self.dockWidget_12.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents_12 = QWidget()
        self.dockWidgetContents_12.setObjectName(u"dockWidgetContents_12")
        self.gridLayout_9 = QGridLayout(self.dockWidgetContents_12)
        self.gridLayout_9.setSpacing(1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(1, 1, 1, 1)
        self.widget_3 = QWidget(self.dockWidgetContents_12)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.widget_3)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(6)
        self.checkBox_2 = QCheckBox(self.widget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 6, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(20, 0))

        self.gridLayout_2.addWidget(self.label_6, 0, 7, 1, 1)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 4, 1, 1)

        self.checkBox_4 = QCheckBox(self.widget_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_4, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.widget_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 5, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_3, 0, 0, 1, 1)

        self.dockWidget_12.setWidget(self.dockWidgetContents_12)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_12)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menudata.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menudata.addAction(self.actionload)
        self.menuView.addAction(self.actiongraph_2)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.textBrowser.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VO", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionload.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actiondad.setText(QCoreApplication.translate("MainWindow", u"dad", None))
        self.actiongg.setText(QCoreApplication.translate("MainWindow", u"gg", None))
        self.actiongraph_2.setText(QCoreApplication.translate("MainWindow", u"graph", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\uff1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"25600", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"4800", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"2400", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d\uff1a", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Even", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Space", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Mark", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.labelStatus.setText("")
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22BLE\u84dd\u7259", None))
        self.pushButton_scan_classic.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ecf\u5178\u84dd\u7259", None))
        self.labelStatus_2.setText("")
        self.labelStatus_3.setText("")
        self.labelStatus_4.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menudata.setTitle(QCoreApplication.translate("MainWindow", u"data", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u5230\u6587\u4ef6", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"ff aa 03 08 00 ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Hex", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u63a5\u6536\u533a", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u53d1\u9001", None))
    # retranslateUi

