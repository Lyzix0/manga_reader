# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 665)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(180, 130, 611, 471))
        self.gridFrame.setStyleSheet(" border: 2px solid #555;")
        self.gridFrame.setObjectName("gridFrame")
        self.mangamenu = QtWidgets.QGridLayout(self.gridFrame)
        self.mangamenu.setObjectName("mangamenu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.gridFrame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setStyleSheet(" border: 1px solid #555;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.mangamenu.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.gridFrame)
        self.pushButton_4.setMinimumSize(QtCore.QSize(10, 30))
        self.pushButton_4.setStyleSheet(" border: 1px solid #555;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.mangamenu.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Devanagari Cn XBd")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(" border: 1px solid #555;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.mangamenu.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridFrame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Devanagari Cn XBd")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(" border: 1px solid #555;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.mangamenu.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridFrame)
        self.label_5.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Devanagari Cn XBd")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(" border: 1px solid #555;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.mangamenu.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Devanagari Cn XBd")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(" border: 1px solid #555;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.mangamenu.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Devanagari Cn XBd")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(" border: 1px solid #555;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.mangamenu.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.gridFrame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 200))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_5.setObjectName("pushButton_5")
        self.mangamenu.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.verticalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 130, 161, 471))
        self.verticalWidget.setStyleSheet("QWidget{\n"
"    color: rgb(0, 0, 0);\n"
"     border: 1px solid;\n"
"}")
        self.verticalWidget.setObjectName("verticalWidget")
        self.all_buttons = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.all_buttons.setContentsMargins(0, 0, 0, 0)
        self.all_buttons.setObjectName("all_buttons")
        self.genresBox = QtWidgets.QComboBox(parent=self.verticalWidget)
        self.genresBox.setMinimumSize(QtCore.QSize(0, 0))
        self.genresBox.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.genresBox.setFont(font)
        self.genresBox.setStyleSheet(" border: 0px solid #555;")
        self.genresBox.setEditable(True)
        self.genresBox.setCurrentText("Жанры")
        self.genresBox.setObjectName("genresBox")
        self.all_buttons.addWidget(self.genresBox)
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.verticalWidget)
        self.comboBox_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox_3.setStyleSheet(" border: 0px solid #555;")
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setCurrentText("Год выпуска")
        self.comboBox_3.setObjectName("comboBox_3")
        self.all_buttons.addWidget(self.comboBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.verticalWidget)
        self.comboBox_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_2.setStyleSheet(" border: 0px solid #555;")
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setCurrentText("Количество страниц")
        self.comboBox_2.setObjectName("comboBox_2")
        self.all_buttons.addWidget(self.comboBox_2)
        self.horizontalFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(10, 20, 781, 102))
        self.horizontalFrame.setStyleSheet(" border: 2px solid #555;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalFrame)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 70))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalFrame)
        self.lineEdit.setMaximumSize(QtCore.QSize(360, 25))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.lineEdit.setStyleSheet(" border: 2px solid rgb(56, 46, 46);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalFrame)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setStyleSheet(" border: 2px solid rgb(100, 100, 100);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Следующая страница"))
        self.pushButton_4.setText(_translate("MainWindow", "Предыдущая страница"))
        self.label_6.setText(_translate("MainWindow", "тут что-то"))
        self.label_3.setText(_translate("MainWindow", "тут что-то"))
        self.label_5.setText(_translate("MainWindow", "тут что-то"))
        self.label_4.setText(_translate("MainWindow", "тут что-то"))
        self.label_2.setText(_translate("MainWindow", "тут что-то"))
        self.pushButton_5.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Профиль"))
        self.lineEdit.setText(_translate("MainWindow", "Поиск по названию"))
        self.pushButton_3.setText(_translate("MainWindow", "Найти"))
