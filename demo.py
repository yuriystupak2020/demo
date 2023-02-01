import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('alton drone')
        self.setWindowIcon(QIcon('ukr_flag.ico'))
        self.resize(500, 500)

#app = QApplication([])
app = QApplication(sys.argv)

window = MyApp()
window.show()


sys.exit(app.exec())