import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


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

        # --------------- ПЕРВАЯ СТРОКА ЧИСЕЛ И ЗНАКОВ -----------

        self.sqrt = QPushButton(self)
        self.sqrt.move(0, 150)
        self.sqrt.resize(100, 100)
        self.sqrt.setText('√x')
        # self.sqrt.clicked.connect()

        self.num_7 = QPushButton(self)
        self.num_7.move(100, 150)
        self.num_7.resize(100, 100)
        self.num_7.setText('7')
        # self.num_7.clicked.connect()

        self.num_8 = QPushButton(self)
        self.num_8.move(200, 150)
        self.num_8.resize(100, 100)
        self.num_8.setText('8')
        # self.num_8.clicked.connect()

        self.num_9 = QPushButton(self)
        self.num_9.move(300, 150)
        self.num_9.resize(100, 100)
        self.num_9.setText('9')
        # self.num_9.clicked.connect()

        self.divide_button = QPushButton(self)
        self.divide_button.move(400, 150)
        self.divide_button.resize(100, 100)
        self.divide_button.setText('/')
        # self.divide_button.clicked.connect()

        # --------------- ВТОРАЯ СТРОКА ЧИСЕЛ И ЗНАКОВ -----------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Advanced_Calculator()
    calculator.show()
    sys.exit(app.exec())
