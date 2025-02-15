from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)

        # Set main window font and style
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: black; color: white;")

        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Horizontal layout for buttons
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(790, 10, 481, 51))
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Upload Signal button
        self.upload_signal = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.upload_signal.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.upload_signal.setMaximumSize(QtCore.QSize(140, 40))
        self.upload_signal.setFont(font)
        self.upload_signal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_signal.setStyleSheet("""
            QPushButton {
                border: none;
                padding: 10px;
                color: white;
                background-color: rgb(24, 24, 24);
                border-bottom: 2px solid transparent;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgb(65, 65, 65);
            }
        """)
        self.upload_signal.setObjectName("upload_signal")
        self.horizontalLayout.addWidget(self.upload_signal)

        # Quit Application button
        self.quit_app = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.quit_app.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.quit_app.setMaximumSize(QtCore.QSize(140, 40))
        self.quit_app.setFont(font)
        self.quit_app.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit_app.setStyleSheet("""
            QPushButton {
                border: none;
                padding: 10px;
                color: white;
                background-color: rgb(24, 24, 24);
                border-bottom: 2px solid transparent;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgb(65, 65, 65);
            }
        """)
        self.quit_app.setObjectName("quit_app")
        self.horizontalLayout.addWidget(self.quit_app)

        # Line separator
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 670, 1240, 1))
        self.line.setStyleSheet("background-color: white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Status Group Box
        self.status_group = QtWidgets.QGroupBox(self.centralwidget)
        self.status_group.setGeometry(QtCore.QRect(20, 680, 1240, 91))
        self.status_group.setStyleSheet("background-color: rgb(32, 32, 32); color: white;")
        self.status_group.setObjectName("status_group")

        # Title layout with icon and name
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 291, 52))
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.title_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setObjectName("title_layout")

        # Title Icon
        self.title_icon = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.title_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.title_icon.setFont(font)
        self.title_icon.setText("")
        self.title_icon.setPixmap(QtGui.QPixmap("../src/heart.png"))
        self.title_icon.setScaledContents(True)
        self.title_icon.setObjectName("title_icon")
        self.title_layout.addWidget(self.title_icon)

        # Title Name
        self.title_name = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.title_name.setMaximumSize(QtCore.QSize(220, 40))
        font.setPointSize(22)
        self.title_name.setFont(font)
        self.title_name.setAlignment(QtCore.Qt.AlignCenter)
        self.title_name.setObjectName("title_name")
        self.title_layout.addWidget(self.title_name)

        # ECG Group Box for Graph
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 1251, 591))
        self.groupBox.setObjectName("groupBox")

        # Placeholder widget for ECG Plot
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 30, 1250, 561))
        self.widget.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.widget.setObjectName("widget")

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Inside the setupUi function, add this line after defining self.status_group
        self.status_label = QtWidgets.QLabel(self.status_group)
        self.status_label.setGeometry(QtCore.QRect(10, 30, 1220, 40))  # Adjust size and position as needed
        self.status_label.setStyleSheet("color: white;")  # Set text color to white
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Defibrillator ECG Analyzer"))
        self.upload_signal.setText(_translate("MainWindow", "Upadte Patient Signal"))
        self.quit_app.setText(_translate("MainWindow", "Quit Application"))
        self.status_group.setTitle(_translate("MainWindow", "Status Bar"))
        self.title_name.setText(_translate("MainWindow", "Automated Defibrillator"))
        self.groupBox.setTitle(_translate("MainWindow", "ECG"))
