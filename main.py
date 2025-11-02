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
        font = QFont('Arial', 30)
        self.main_label.setFont(font)
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # -----------------дополнительное поле ввода (верхнее)---------------------

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
        font = QFont('Arial', 20)
        self.sqrt.setFont(font)

        self.num_7 = QPushButton(self)
        self.num_7.move(100, 150)
        self.num_7.resize(100, 100)
        self.num_7.setText('7')
        font = QFont('Arial', 20)
        self.num_7.setFont(font)
        self.num_7.clicked.connect(lambda: self.append_to_string('7'))

        self.num_8 = QPushButton(self)
        self.num_8.move(200, 150)
        self.num_8.resize(100, 100)
        self.num_8.setText('8')
        font = QFont('Arial', 20)
        self.num_8.setFont(font)
        self.num_8.clicked.connect(lambda: self.append_to_string('8'))

        self.num_9 = QPushButton(self)
        self.num_9.move(300, 150)
        self.num_9.resize(100, 100)
        self.num_9.setText('9')
        font = QFont('Arial', 20)
        self.num_9.setFont(font)
        self.num_9.clicked.connect(lambda: self.append_to_string('9'))

        self.divide_button = QPushButton(self)
        self.divide_button.move(400, 150)
        self.divide_button.resize(100, 100)
        self.divide_button.setText('÷')
        font = QFont('Arial', 20)
        self.divide_button.setFont(font)
        self.divide_button.clicked.connect(lambda: self.append_to_string('÷'))

        # --------------- ВТОРАЯ СТРОКА ЧИСЕЛ И ЗНАКОВ -----------
        self.quadrad = QPushButton(self)
        self.quadrad.move(0, 250)
        self.quadrad.resize(100, 100)
        self.quadrad.setText('x²')
        font = QFont('Arial', 20)
        self.quadrad.setFont(font)

        self.num_4 = QPushButton(self)
        self.num_4.move(100, 250)
        self.num_4.resize(100, 100)
        self.num_4.setText('4')
        font = QFont('Arial', 20)
        self.num_4.setFont(font)
        self.num_4.clicked.connect(lambda: self.append_to_string('4'))

        self.num_5 = QPushButton(self)
        self.num_5.move(200, 250)
        self.num_5.resize(100, 100)
        self.num_5.setText('5')
        font = QFont('Arial', 20)
        self.num_5.setFont(font)
        self.num_5.clicked.connect(lambda: self.append_to_string('5'))

        self.num_6 = QPushButton(self)
        self.num_6.move(300, 250)
        self.num_6.resize(100, 100)
        self.num_6.setText('6')
        font = QFont('Arial', 20)
        self.num_6.setFont(font)
        self.num_6.clicked.connect(lambda: self.append_to_string('6'))

        self.multiply_button = QPushButton(self)
        self.multiply_button.move(400, 250)
        self.multiply_button.resize(100, 100)
        self.multiply_button.setText('*')
        font = QFont('Arial', 20)
        self.multiply_button.setFont(font)
        self.multiply_button.clicked.connect(lambda: self.append_to_string('*'))

        # --------------- ТРЕТЬЯ СТРОКА ЧИСЕЛ И ЗНАКОВ -----------

        self.degree = QPushButton(self)
        self.degree.move(0, 350)
        self.degree.resize(100, 100)
        self.degree.setText('xⁿ')
        font = QFont('Arial', 20)
        self.degree.setFont(font)
        self.degree.clicked.connect(lambda: self.append_to_string('^'))

        self.num_1 = QPushButton(self)
        self.num_1.move(100, 350)
        self.num_1.resize(100, 100)
        self.num_1.setText('1')
        font = QFont('Arial', 20)
        self.num_1.setFont(font)
        self.num_1.clicked.connect(lambda: self.append_to_string('1'))

        self.num_2 = QPushButton(self)
        self.num_2.move(200, 350)
        self.num_2.resize(100, 100)
        self.num_2.setText('2')
        font = QFont('Arial', 20)
        self.num_2.setFont(font)
        self.num_2.clicked.connect(lambda: self.append_to_string('2'))

        self.num_3 = QPushButton(self)
        self.num_3.move(300, 350)
        self.num_3.resize(100, 100)
        self.num_3.setText('3')
        font = QFont('Arial', 20)
        self.num_3.setFont(font)
        self.num_3.clicked.connect(lambda: self.append_to_string('3'))

        self.substract_button = QPushButton(self)
        self.substract_button.move(400, 350)
        self.substract_button.resize(100, 100)
        self.substract_button.setText('-')
        font = QFont('Arial', 20)
        self.substract_button.setFont(font)
        self.substract_button.clicked.connect(lambda: self.append_to_string('-'))

        # --------------- ЧЕТВЕРТАЯ СТРОКА ЧИСЕЛ И ЗНАКОВ -----------

        self.proc = QPushButton(self)
        self.proc.move(0, 450)
        self.proc.resize(100, 100)
        self.proc.setText('%')
        font = QFont('Arial', 20)
        self.proc.setFont(font)

        self.clear_button = QPushButton(self)
        self.clear_button.move(100, 450)
        self.clear_button.resize(100, 100)
        self.clear_button.setText('C')
        font = QFont('Arial', 20)
        self.clear_button.setFont(font)
        self.clear_button.clicked.connect(self.clear_all)

        self.num_0 = QPushButton(self)
        self.num_0.move(200, 450)
        self.num_0.resize(100, 100)
        self.num_0.setText('0')
        font = QFont('Arial', 20)
        self.num_0.setFont(font)
        self.num_0.clicked.connect(lambda: self.append_to_string('0'))

        self.clear_entry_button = QPushButton(self)
        self.clear_entry_button.move(300, 450)
        self.clear_entry_button.resize(100, 100)
        self.clear_entry_button.setText('CE')
        font = QFont('Arial', 20)
        self.clear_entry_button.setFont(font)
        self.clear_entry_button.clicked.connect(self.clear_entry)

        self.add_button = QPushButton(self)
        self.add_button.move(400, 450)
        self.add_button.resize(100, 100)
        self.add_button.setText('+')
        font = QFont('Arial', 20)
        self.add_button.setFont(font)
        self.add_button.clicked.connect(lambda: self.append_to_string('+'))

        # --------------- ПЯТАЯ СТРОКА ЗНАКОВ -----------

        self.plus_minus_button = QPushButton(self)
        self.plus_minus_button.move(0, 550)
        self.plus_minus_button.resize(100, 100)
        self.plus_minus_button.setText('±')
        font = QFont('Arial', 20)
        self.plus_minus_button.setFont(font)

        self.float_point_button = QPushButton(self)
        self.float_point_button.move(100, 550)
        self.float_point_button.resize(100, 100)
        self.float_point_button.setText('.')
        font = QFont('Arial', 20)
        self.float_point_button.setFont(font)
        self.float_point_button.clicked.connect(lambda: self.append_to_string('.'))

        self.backspace_button = QPushButton(self)
        self.backspace_button.move(200, 550)
        self.backspace_button.resize(100, 100)
        self.backspace_button.setText('\u232b')  # изпользован unicode
        font = QFont('Arial', 20)
        self.backspace_button.setFont(font)

        self.equals_button = QPushButton(self)
        self.equals_button.move(300, 550)
        self.equals_button.resize(200, 100)
        self.equals_button.setText('=')
        font = QFont('Arial', 20)
        self.equals_button.setFont(font)
        self.equals_button.clicked.connect(self.calculate_result)

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

            # если есть какая нибудь ошибка то вычисления не продолжаются
            if self.main_label.text() in ('Деление на ноль!', 'Ошибка', 'Отрицательное число'):
                self.clear_all()
                return

            if self.second_operand is not None:
                self.calculate_intermediate_result()

            self.operator = value
            display_text = str(self.first_operand) if self.first_operand is not None else '0'
            self.secondary_label.setText(display_text + ' ' + str(self.operator))

    # Функция для работы с результатом
    def calculate_result(self):
        try:
            # если есть какая нибудь ошибка то вычисления не продолжаются
            if self.main_label.text() in ('Деление на ноль!', 'Ошибка', 'Отрицательное число'):
                return

            if self.first_operand is None or self.operator is None or self.second_operand is None:
                return

            num1 = float(self.first_operand)
            num2 = float(self.second_operand)

            if self.operator == '+':
                result = num1 + num2
            elif self.operator == '-':
                result = num1 - num2
            elif self.operator == '*':
                result = num1 * num2
            elif self.operator == '÷':
                if num2 == 0:
                    self.main_label.setText('Ошибка')
                    self.secondary_label.setText('Деление на ноль!')
                    return
                result = num1 / num2
            elif self.operator == '^':
                result = num1 ** num2
            else:
                return  # если нет такого оператора

            if result == int(result):
                result = int(result)

            self.main_label.setText(str(result))
            self.secondary_label.setText(str(num1) + ' ' + self.operator + ' ' + str(num2) + ' = ' + str(result))

            # ждать другие вычисления
            self.first_operand = str(result)
            self.operator = None
            self.second_operand = None
        except Exception as e:
            self.main_label.setText('Ошибка')
            self.secondary_label.setText(f'Ошибка: {e}')

    # Функция для удаления всех действий
    def clear_all(self):
        self.first_operand = None
        self.operator = None
        self.second_operand = None
        self.main_label.setText('0')
        self.secondary_label.clear()

    # Функция для удаления посдеднего действия
    def clear_entry(self):
        # если есть какая нибудь ошибка то вычисления не продолжаются и все очистить
        if self.main_label.text() in ('Деление на ноль!', 'Ошибка', 'Отрицательное число'):
            self.clear_all()
            return

        if self.second_operand is not None:
            self.second_operand = None
            self.main_label.setText('0')
        elif self.operator is not None:
            self.operator = None
            self.main_label.setText(str(self.first_operand) if self.first_operand is not None else '0')
            self.secondary_label.clear()
        elif self.first_operand is not None:
            self.first_operand = None
            self.main_label.setText('0')
            self.secondary_label.clear()
        else:
            self.main_label.setText('0')
            self.secondary_label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Advanced_Calculator()
    calculator.show()
    sys.exit(app.exec())
