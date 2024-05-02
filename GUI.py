from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QComboBox, QRadioButton, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

class Window(QMainWindow):
    # Signaux
    rtsp_selected = pyqtSignal()
    onvif_selected = pyqtSignal()
    scan_selected = pyqtSignal()

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200, 200, 642, 368)
        self.setWindowTitle("Pelicam GUI")
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setGeometry(260, 10, 111, 31)
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setText("Pelicam")

        self.line = QFrame(self)
        self.line.setGeometry(300, 40, 21, 320)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(10, 150, 69, 22)

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(80, 150, 111, 16)
        self.label_2.setText("Choix de l'IP à attaquer")

        self.radioButton = QRadioButton(self)
        self.radioButton.setGeometry(20, 90, 51, 17)
        self.radioButton.setText("ONVIF")

        self.radioButton_2 = QRadioButton(self)
        self.radioButton_2.setGeometry(200, 90, 51, 17)
        self.radioButton_2.setText("RTSP")

        self.radioButton_3 = QRadioButton(self)
        self.radioButton_3.setGeometry(90, 90, 91, 17)
        self.radioButton_3.setText("Scan réseau")

        self.line_2 = QFrame(self)
        self.line_2.setGeometry(0, 40, 642, 20)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(80, 60, 131, 21)
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("Choisissez l'option")

        self.b1 = QPushButton(self)
        self.b1.setGeometry(10, 250, 100, 30)
        self.b1.setText("Bouton")
        self.b1.clicked.connect(self.clicked_button)

    def clicked_button(self):
        if self.radioButton.isChecked():
            self.onvif_selected.emit()
        elif self.radioButton_2.isChecked():
            self.rtsp_selected.emit()
        elif self.radioButton_3.isChecked():
            self.scan_selected.emit()
