# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ABCD.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 492)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image_Frame = QtWidgets.QLabel(self.centralwidget)
        self.Image_Frame.setGeometry(QtCore.QRect(480, 20, 300, 300))
        self.Image_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image_Frame.setLineWidth(5)
        self.Image_Frame.setText("")
        self.Image_Frame.setPixmap(QtGui.QPixmap("../_image/background1.png"))
        self.Image_Frame.setScaledContents(True)
        self.Image_Frame.setObjectName("Image_Frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 330, 91, 42))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.JPG = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.JPG.setChecked(True)
        self.JPG.setObjectName("JPG")
        self.verticalLayout_4.addWidget(self.JPG)
        self.PNG = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.PNG.setObjectName("PNG")
        self.verticalLayout_4.addWidget(self.PNG)
        self.Control_Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Control_Tab.setGeometry(QtCore.QRect(30, 20, 441, 431))
        self.Control_Tab.setObjectName("Control_Tab")
        self.Imaging = QtWidgets.QWidget()
        self.Imaging.setObjectName("Imaging")
        self.layoutWidget = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_Title = QtWidgets.QLabel(self.layoutWidget)
        self.Image_Title.setObjectName("Image_Title")
        self.verticalLayout.addWidget(self.Image_Title)
        self.IST_Editor = QtWidgets.QLineEdit(self.layoutWidget)
        self.IST_Editor.setEnabled(True)
        self.IST_Editor.setObjectName("IST_Editor")
        self.verticalLayout.addWidget(self.IST_Editor)
        self.Image_Interval = QtWidgets.QLabel(self.layoutWidget)
        self.Image_Interval.setObjectName("Image_Interval")
        self.verticalLayout.addWidget(self.Image_Interval)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.ICI_spinBox.setEnabled(False)
        self.ICI_spinBox.setMaximum(9999999)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout.addWidget(self.ICI_spinBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_Duration = QtWidgets.QLabel(self.layoutWidget)
        self.Image_Duration.setObjectName("Image_Duration")
        self.verticalLayout_2.addWidget(self.Image_Duration)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.ISD_spinBox.setEnabled(False)
        self.ISD_spinBox.setMaximum(9999999)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.Live_Feed = QtWidgets.QPushButton(self.layoutWidget)
        self.Live_Feed.setObjectName("Live_Feed")
        self.verticalLayout_3.addWidget(self.Live_Feed)
        self.layoutWidget1 = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget1.setGeometry(QtCore.QRect(14, 330, 381, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Progress_Label = QtWidgets.QLabel(self.layoutWidget1)
        self.Progress_Label.setObjectName("Progress_Label")
        self.verticalLayout_6.addWidget(self.Progress_Label)
        self.Progress_Bar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.Progress_Bar.setEnabled(False)
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setObjectName("Progress_Bar")
        self.verticalLayout_6.addWidget(self.Progress_Bar)
        self.Control_Tab.addTab(self.Imaging, "")
        self.Cloud = QtWidgets.QWidget()
        self.Cloud.setObjectName("Cloud")
        self.Service_Select = QtWidgets.QTabWidget(self.Cloud)
        self.Service_Select.setEnabled(True)
        self.Service_Select.setGeometry(QtCore.QRect(10, 10, 401, 271))
        self.Service_Select.setObjectName("Service_Select")
        self.Dropbox = QtWidgets.QWidget()
        self.Dropbox.setObjectName("Dropbox")
        self.label = QtWidgets.QLabel(self.Dropbox)
        self.label.setGeometry(QtCore.QRect(60, 10, 271, 140))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../_image/dropbox_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Dropbox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 130, 291, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.Dropbox_Email_Prompt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Dropbox_Email_Prompt.setObjectName("Dropbox_Email_Prompt")
        self.verticalLayout_9.addWidget(self.Dropbox_Email_Prompt)
        self.Dropbox_Email = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Dropbox_Email.setObjectName("Dropbox_Email")
        self.verticalLayout_9.addWidget(self.Dropbox_Email)
        self.Dropbox_Confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Dropbox_Confirm.setEnabled(False)
        self.Dropbox_Confirm.setObjectName("Dropbox_Confirm")
        self.verticalLayout_9.addWidget(self.Dropbox_Confirm)
        self.Service_Select.addTab(self.Dropbox, "")
        self.CyVerse = QtWidgets.QWidget()
        self.CyVerse.setObjectName("CyVerse")
        self.label_2 = QtWidgets.QLabel(self.CyVerse)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 281, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../_image/cyverse_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.CyVerse)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(50, 130, 291, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.CyVerse_Email_Prompt = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.CyVerse_Email_Prompt.setObjectName("CyVerse_Email_Prompt")
        self.verticalLayout_10.addWidget(self.CyVerse_Email_Prompt)
        self.CyVerse_Email = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.CyVerse_Email.setEnabled(False)
        self.CyVerse_Email.setObjectName("CyVerse_Email")
        self.verticalLayout_10.addWidget(self.CyVerse_Email)
        self.CyVerse_Confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.CyVerse_Confirm.setEnabled(False)
        self.CyVerse_Confirm.setObjectName("CyVerse_Confirm")
        self.verticalLayout_10.addWidget(self.CyVerse_Confirm)
        self.Service_Select.addTab(self.CyVerse, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Cloud)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 330, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Frequency_Off = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Off.setEnabled(False)
        self.Frequency_Off.setCheckable(True)
        self.Frequency_Off.setChecked(False)
        self.Frequency_Off.setObjectName("Frequency_Off")
        self.horizontalLayout_6.addWidget(self.Frequency_Off)
        self.Frequency_Low = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Low.setEnabled(False)
        self.Frequency_Low.setObjectName("Frequency_Low")
        self.horizontalLayout_6.addWidget(self.Frequency_Low)
        self.Frequency_Average = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Average.setEnabled(False)
        self.Frequency_Average.setCheckable(True)
        self.Frequency_Average.setChecked(True)
        self.Frequency_Average.setObjectName("Frequency_Average")
        self.horizontalLayout_6.addWidget(self.Frequency_Average)
        self.Frequency_High = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_High.setEnabled(False)
        self.Frequency_High.setObjectName("Frequency_High")
        self.horizontalLayout_6.addWidget(self.Frequency_High)
        self.Email_Update_Prompt = QtWidgets.QLabel(self.Cloud)
        self.Email_Update_Prompt.setGeometry(QtCore.QRect(40, 310, 311, 20))
        self.Email_Update_Prompt.setObjectName("Email_Update_Prompt")
        self.Control_Tab.addTab(self.Cloud, "")
        self.Start_Imaging = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Start_Imaging.setEnabled(False)
        self.Start_Imaging.setGeometry(QtCore.QRect(480, 380, 291, 51))
        self.Start_Imaging.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon1)
        self.Start_Imaging.setIconSize(QtCore.QSize(35, 35))
        self.Start_Imaging.setObjectName("Start_Imaging")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(680, 320, 101, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Snapshot = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Snapshot.setEnabled(True)
        self.Snapshot.setObjectName("Snapshot")
        self.verticalLayout_13.addWidget(self.Snapshot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setEnabled(False)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate_Timelapse = QtWidgets.QAction(MainWindow)
        self.actionCreate_Timelapse.setObjectName("actionCreate_Timelapse")

        self.retranslateUi(MainWindow)
        self.Control_Tab.setCurrentIndex(0)
        self.Service_Select.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.JPG.setText(_translate("MainWindow", "JPG"))
        self.PNG.setText(_translate("MainWindow", "PNG"))
        self.Image_Title.setText(_translate("MainWindow", "Image Sequence Title"))
        self.Image_Interval.setText(_translate("MainWindow", "Image Capture Interval"))
        self.ICI_spinBox.setSuffix(_translate("MainWindow", " s"))
        self.Image_Duration.setText(_translate("MainWindow", "Image Sequence Duration"))
        self.ISD_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.Live_Feed.setText(_translate("MainWindow", "Start Live Feed (30s)"))
        self.Progress_Label.setText(_translate("MainWindow", "Progress:"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Imaging), _translate("MainWindow", "Imaging"))
        self.Dropbox_Email_Prompt.setText(_translate("MainWindow", "Please Enter Your Email Adress: "))
        self.Dropbox_Confirm.setText(_translate("MainWindow", "Confirm Email"))
        self.Service_Select.setTabText(self.Service_Select.indexOf(self.Dropbox), _translate("MainWindow", "Dropbox"))
        self.CyVerse_Email_Prompt.setText(_translate("MainWindow", "Please Enter Your Email Adress:"))
        self.CyVerse_Confirm.setText(_translate("MainWindow", "Confirm Email"))
        self.Service_Select.setTabText(self.Service_Select.indexOf(self.CyVerse), _translate("MainWindow", "CyVerse "))
        self.Frequency_Off.setText(_translate("MainWindow", "OFF"))
        self.Frequency_Low.setText(_translate("MainWindow", "LOW"))
        self.Frequency_Average.setText(_translate("MainWindow", "AVERAGE"))
        self.Frequency_High.setText(_translate("MainWindow", "HIGH"))
        self.Email_Update_Prompt.setText(_translate("MainWindow", "Email Status Update Frequency:"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Cloud), _translate("MainWindow", "Cloud"))
        self.Start_Imaging.setText(_translate("MainWindow", "Start Image Sequence"))
        self.Snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))

