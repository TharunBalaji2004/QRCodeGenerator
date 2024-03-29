from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(520, 350, 171, 51))
        self.Button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button1.setObjectName("Button1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(130, 30, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(260, 90, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(172, 470, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(100, 150, 300, 300))
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.menuFile.addAction(self.actionNew_Window)
        self.menubar.addAction(self.menuFile.menuAction())
        self.TextBox1 = QtWidgets.QPlainTextEdit(MainWindow)
        self.TextBox1.setGeometry(QtCore.QRect(450, 250, 321, 31))
        self.TextBox1.setPlainText("")
        self.TextBox1.setObjectName("TextBox1")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Button1.clicked.connect(self.show_QR)
        self.Button1.clicked.connect(self.show_DownloadButton)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application MainWindow"))
        MainWindow.setWindowIcon(QtGui.QIcon("E:\Coding Files\Tharun Projects\QRCodeGeneratorLogo.png"))
        self.Button1.setText(_translate("MainWindow", "Generate QR Code"))
        self.label1.setText(_translate("MainWindow", "QR CODE GENERATOR"))
        self.label2.setText(_translate("MainWindow", "Developed and Designed by: R.THARUN BALAJI"))
        self.Image.setText(_translate("MainWindow", ""))
        self.menuFile.setTitle(_translate("MainWindow", "Options"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionNew_Window.setStatusTip(_translate("MainWindow", "Select to open a New Window"))
    
    def show_QR(self):
        self.Image.setPixmap(QtGui.QPixmap("E:\Coding Files\Tharun Projects\QRCodeGeneratorLogo.png"))
        self.label3.setText('QR Code generated')
        self.label3.adjustSize()

    def show_DownloadButton(self):
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(520, 420, 171, 51))
        self.Button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button2.setObjectName("Button2")
        self.Button2.setText('Download QR Code\n(as PNG)')
        self.Button2.show()
        self.Button2.clicked.connect(self.show_popup)
        
    def show_popup(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("ERROR")
        msgbox.setWindowIcon(QtGui.QIcon("E:\Coding Files\Tharun Projects\QRCodeGeneratorLogo.png"))
        msgbox.setText("Invalid QR Code")
        msgbox.setIcon(QMessageBox.Question)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setInformativeText("Re enter the Text or URL") 
        msgbox.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())