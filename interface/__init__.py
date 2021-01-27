from PySide6.QtWidgets import (QApplication,
                               QLabel,
                               QPushButton,
                               QVBoxLayout,
                               QFileDialog,
                               QMessageBox,
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
        self.show_main()

    def show_main(self):
        layout = QVBoxLayout()
        image_map = QPixmap('icons/cat.jpg')
        image_label = QLabel(self)
        image_label.setPixmap(image_map)
        ics_selector = QPushButton(
            'Select iCalendar (Google Calendar, Apple Calendar)')
        ics_selector.clicked.connect(self.select_file)
        layout.addWidget(image_label)
        layout.addWidget(ics_selector)
        self.setLayout(layout)

    def show_success(self):
        box = QMessageBox()
        box.setWindowTitle('Export Complete')
        box.setWindowIcon(self.icon)
        box.setText(
            'Success. The file has been exported and should show up in the same folder as this program.\n\nDCC by Gideon Tong v1.0')
        box.exec_()

    def select_file(self):
        filename = QFileDialog.getOpenFileName(self,
                                               "Open Calendar File",
                                               "",
                                               "iCalendar (*.ics)")
        if filename and filename[0]:
            process(filename[0], show_success)


def generate_app() -> tuple:
    return QApplication([])
