from PySide6.QtWidgets import (QApplication,
                               QLabel,
                               QPushButton,
                               QVBoxLayout,
                               QFileDialog,
                               QWidget)
from PySide6.QtGui import (QIcon,
                           QPixmap)
from interface.process import process_ics

class DCCUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DCC by Gideon Tong')
        self.icon = QIcon('icons/icon.png')
        self.setWindowIcon(self.icon)
        self.setMainWindow()

    def setMainWindow(self):
        layout = QVBoxLayout()
        image_map = QPixmap('icons/cat.jpg')
        image_label = QLabel(self)
        image_label.setPixmap(image_map)
        ics_selector = QPushButton('Select iCalendar (Google Calendar, Apple Calendar)')
        ics_selector.clicked.connect(self.selectFile)
        layout.addWidget(image_label)
        layout.addWidget(ics_selector)
        self.setLayout(layout)

    def selectFile(self):
        filename = QFileDialog.getOpenFileName(self,
                                               "Open Calendar File",
                                               "",
                                               "iCalendar (*.ics)")
        if filename and filename[0]:
            process_ics(filename[0])


def generate_app() -> tuple:
    return QApplication([])
