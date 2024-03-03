import psutil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 371)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set transparent background

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 500, 351))
        self.frame.setStyleSheet("background-color:#191a1c;  border-radius:20px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(44)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{ background-color: #333738; color: #f15800; border-radius:60px; border:4px solid #f15800;} QPushButton:hover{background-color: transparent; font:61px; border:2px solid #f15800;} QPushButton:pressed{background-color: black; font:56px; border:3px solid #f15800; }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.set_all_processes_low_priority)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 110, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(44)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{background-color: #333738; color: #29ebeb; border-radius:60px; border:4px solid #29ebeb;} QPushButton:hover{background-color: transparent; font:61px; border:2px solid #29ebeb;} QPushButton:pressed{background-color: black; font:56px; border:3px solid #29ebeb;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.set_all_processes_normal_priority)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 50, 131, 51))
        self.label.setStyleSheet("background-color:transparent; color:#f15800; font: 16px; font-weight: bold")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(310, 50, 131, 51))
        self.label_2.setStyleSheet("background-color:transparent; color:#29ebeb; font: 16px; font-weight: bold")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(420, 310, 61, 16))
        self.label_3.setStyleSheet("color:grey")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 291, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:none; font:20px; font-weight:bold; color:grey")
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(210, 260, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(163, 255, 70, 30))
        self.label_5.setStyleSheet("background-color:none; font:20px; font-weight:bold; color:grey")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(210, 310, 101, 31))
        self.closeButton.setStyleSheet("QPushButton{background-color: #333738; color: white; border-radius: 5px;} QPushButton:hover{background-color:transparent;color:red; font:12px; font-weight: bold; border: 1px solid red;}")
        self.closeButton.setText("Close")
        self.closeButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()  # Create a QTimer
        self.timer.timeout.connect(self.update_cpu_usage)  # Connect the timer to the update_cpu_usage method
        self.timer.start(1000)  # Start the timer with a 1-second interval (1000 milliseconds)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "L"))
        self.pushButton_2.setText(_translate("MainWindow", "N"))
        self.label.setText(_translate("MainWindow", "BELOW NORMAL"))
        self.label_2.setText(_translate("MainWindow", "NORMAL"))
        self.label_3.setText(_translate("MainWindow", "MADE BY RX"))
        self.label_4.setText(_translate("MainWindow", "PRIORITY CHANGER"))
        self.label_5.setText(_translate("MainWindow", "CPU"))

  #function
    def set_all_processes_low_priority(self):
        for proc in psutil.process_iter(['pid']):
            try:
                p = psutil.Process(proc.info['pid'])
                p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
            except Exception as e:
                print(f"Failed to set priority for process {proc.info['pid']}: {e}")

    def set_all_processes_normal_priority(self):
        for proc in psutil.process_iter(['pid']):
            try:
                p = psutil.Process(proc.info['pid'])
                p.nice(psutil.NORMAL_PRIORITY_CLASS)
            except Exception as e:
                print(f"Failed to set priority for process {proc.info['pid']}: {e}")

    def update_cpu_usage(self):
        cpu_percent = psutil.cpu_percent(interval=None)
        self.lcdNumber.display(cpu_percent)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
