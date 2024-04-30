from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# CONSTANTES
XPOS = 200
YPOS = 200
WIDTH = 642
HEIGHT = 368

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)
        self.setWindowTitle("Pelicam GUI")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(260, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Pelicam")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(300, 40, 21, 321))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(10, 150, 69, 22))
        self.comboBox.setObjectName("comboBox")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText(" choix de l\'ip a attack")

        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(20, 90, 51, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setText("ONVIF")

        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 90, 51, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setText("RTSP")

        self.radioButton_3 = QtWidgets.QRadioButton(self)
        self.radioButton_3.setGeometry(QtCore.QRect(90, 90, 91, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setText("Scan network")

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(0, 40, WIDTH, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(80, 60, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Choisissez l\'option")

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(QtCore.QRect(10, 250, 100, 30))
        self.b1.setObjectName("b1")
        self.b1.setText("button")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("button pressed")
        self.uptade()

    def uptade(self):
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
