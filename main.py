import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit


class Advanced_Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(450, 150, 500, 650)
        self.setWindowTitle('Калькулятор')

        # ------------------ основное поле ввода (нижнее) -----------------
        self.main_label = QLineEdit(self)
        self.main_label.setText('0')
        self.main_label.setReadOnly(True)
        self.main_label.move(0, 50)
        self.main_label.resize(500, 100)
        font = QFont("Arial", 30)
        self.main_label.setFont(font)
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # -----------------дополнительное поле (верхнее)---------------------

        self.secondary_label = QLineEdit(self)
        self.secondary_label.setReadOnly(True)
        self.secondary_label.move(0, 50)
        self.secondary_label.resize(500, 20)
        self.secondary_label.setAlignment(Qt.AlignmentFlag.AlignRight)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Advanced_Calculator()
    calculator.show()
    sys.exit(app.exec())
