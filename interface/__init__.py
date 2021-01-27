from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

class DCCUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ics_selector = QPushButton('Select ICS file')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.ics_selector)
        self.setWindowTitle('DCC by Gideon Tong')
        self.icon = QIcon('icons/icon.png')
        self.setWindowIcon(self.icon)
        self.setLayout(self.layout)

def generate_app() -> tuple:
    return QApplication([])