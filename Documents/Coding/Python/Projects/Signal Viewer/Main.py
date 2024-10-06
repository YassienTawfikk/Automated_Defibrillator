from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget {\n"
                                    "    background-color: black;\n"
                                    "}\n"
                                    "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 70, 1300, 2))
        self.line.setStyleSheet("background-color:white;\n"
                                "")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Define buttons
        self.pushButton = self.create_button(self.centralwidget, "Home", 790, 18, "rgb(252, 108, 248)")
        self.pushButton_2 = self.create_button(self.centralwidget, "Signals", 950, 18, "rgb(147, 247, 167)")
        self.pushButton_3 = self.create_button(self.centralwidget, "Quit Application", 1120, 18, "rgb(179, 15, 66)")
        self.pushButton_3.clicked.connect(QtWidgets.QApplication.quit)

        # Logo image (left)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 5, 60, 60))
        self.label.setMaximumSize(QtCore.QSize(16777210, 16777215))
        self.label.setStyleSheet("color: white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("src/radio-waves.png"))
        self.label.setObjectName("label")

        # Title text next to logo
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 18, 161, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777210, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # Background image
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 790, 630))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("src/Graph.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        # Title "Hello from the Signal Innovators"
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 260, 305, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(35)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        # Subtitle with line breaks
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(830, 350, 390, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setText(
            "Empowering data, one signal at a time.<br>As a team of passionate problem-solvers, we transform complex signals into meaningful insights,<br>helping you visualize and understand the world of medical data with precision and innovation.<br>Let’s shape the future of signal analysis together, one breakthrough at a time.")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        # Proceed button
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(830, 570, 390, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(252, 108, 248);\n"
                                        "    padding: 10px;\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border-color:rgb(147, 247, 167);\n"
                                        "    background-color: rgb(30,30,30);\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "Signals"))
        self.pushButton_3.setText(_translate("MainWindow", "Quit Application"))
        self.label_2.setText(_translate("MainWindow", "Multi-Port Signal Viewer"))
        self.label_4.setText(_translate("MainWindow", "Hello from the Signal Innovators"))
        self.pushButton_4.setText(_translate("MainWindow", "Proceed to Signal"))
    # Helper function to create buttons
    def create_button(self, parent, text, x, y, hover_color):
        button = QtWidgets.QPushButton(parent)
        button.setGeometry(QtCore.QRect(x, y, 115, 40))
        button.setMaximumSize(QtCore.QSize(16777210, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        button.setFont(font)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(f"""
            QPushButton {{
                border: none;
                padding: 10px;
                color: white;
                border-bottom: 2px solid transparent;
            }}

            QPushButton:hover {{
                border-bottom-color: {hover_color};
                color: {hover_color};
            }}
        """)
        button.setText(text)
        return button


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
