import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QListWidget
from PyQt6.QtCore import QObject

template = """
"""


class Advanced_Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Advanced_Calculator()
    ex.show()
    sys.exit(app.exec())
