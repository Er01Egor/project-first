import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class Advanced_Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.first_operand = None
        self.operator = None
        self.second_operand = None

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

        self.quadrad = QPushButton(self)
        self.quadrad.move(0, 250)
        self.quadrad.resize(100, 100)
        self.quadrad.setText('x²')
        # self.quadrad.clicked.connect()

        self.num_4 = QPushButton(self)
        self.num_4.move(100, 250)
        self.num_4.resize(100, 100)
        self.num_4.setText('4')
        # self.num_4.clicked.connect()

        self.num_5 = QPushButton(self)
        self.num_5.move(200, 250)
        self.num_5.resize(100, 100)
        self.num_5.setText('5')
        # self.num_5.clicked.connect()

        self.num_6 = QPushButton(self)
        self.num_6.move(300, 250)
        self.num_6.resize(100, 100)
        self.num_6.setText('6')
        # self.num_6.clicked.connect()

        self.multiply_button = QPushButton(self)
        self.multiply_button.move(400, 250)
        self.multiply_button.resize(100, 100)
        self.multiply_button.setText('*')
        # self.multiply_button.clicked.connect()

        # --------------- ТРЕТЬЯ СТРОКА ЧИСЕЛ И ЗНАКОВ -----------

        self.proc = QPushButton(self)
        self.proc.move(0, 350)
        self.proc.resize(100, 100)
        self.proc.setText('%')
        # self.proc.clicked.connect()

        self.num_1 = QPushButton(self)
        self.num_1.move(100, 350)
        self.num_1.resize(100, 100)
        self.num_1.setText('1')
        # self.num_1.clicked.connect()

        self.num_2 = QPushButton(self)
        self.num_2.move(200, 350)
        self.num_2.resize(100, 100)
        self.num_2.setText('2')
        # self.num_2.clicked.connect()

        self.num_3 = QPushButton(self)
        self.num_3.move(300, 350)
        self.num_3.resize(100, 100)
        self.num_3.setText('3')
        # self.num_3.clicked.connect()

        self.substract_button = QPushButton(self)
        self.substract_button.move(400, 350)
        self.substract_button.resize(100, 100)
        self.substract_button.setText('-')
        # self.substract_button.clicked.connect()

        # --------------- ЧЕТВЕРТАЯ СТРОКА ЧИСЕЛ И ЗНАКОВ -----------
        self.clear_button = QPushButton(self)
        self.clear_button.move(100, 450)
        self.clear_button.resize(100, 100)
        self.clear_button.setText('C')
        # self.clear_button.clicked.connect()

        self.num_0 = QPushButton(self)
        self.num_0.move(200, 450)
        self.num_0.resize(100, 100)
        self.num_0.setText('0')
        # self.num_0.clicked.connect()

        self.clear_entry_button = QPushButton(self)
        self.clear_entry_button.move(300, 450)
        self.clear_entry_button.resize(100, 100)
        self.clear_entry_button.setText('CE')
        # self.clear_entry_button.clicked.connect()

        self.add_button = QPushButton(self)
        self.add_button.move(400, 450)
        self.add_button.resize(100, 100)
        self.add_button.setText('+')
        # self.add_button.clicked.connect()

        # --------------- ПЯТАЯ СТРОКА ЗНАКОВ -----------
        self.float_point_button = QPushButton(self)
        self.float_point_button.move(100, 550)
        self.float_point_button.resize(100, 100)
        self.float_point_button.setText('.')
        # self.float_point_button.clicked.connect()

        self.plus_minus_button = QPushButton(self)
        self.plus_minus_button.move(200, 550)
        self.plus_minus_button.resize(100, 100)
        self.plus_minus_button.setText('±')
        # self.plus_minus_button.clicked.connect()

        self.equals_button = QPushButton(self)
        self.equals_button.move(300, 550)
        self.equals_button.resize(200, 100)
        self.equals_button.setText('=')
        # self.equals_button.clicked.connect()

    # Функция отвечает за добавление цифр к данному числу или за выбор операции

    def append_to_string(self, value):
        if value.isdigit() or value == '.':  # если цифра или точка
            if self.operator is None:
                if self.first_operand is None or self.first_operand == '0':
                    self.first_operand = value if value != '.' else '0.'
                else:
                    if value == '.' and '.' in self.first_operand:
                        return
                    self.first_operand += value
                self.main_label.setText(self.first_operand)
            else:
                if self.second_operand is None or self.second_operand == '0':
                    self.second_operand = value if value != '.' else '0.'
                else:
                    if value == '.' and '.' in self.second_operand:
                        return
                    self.second_operand += value
                self.main_label.setText(self.second_operand)
        else:  # если оператор
            if self.first_operand is None:
                # если сначала ввели оператор
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Advanced_Calculator()
    calculator.show()
    sys.exit(app.exec())
