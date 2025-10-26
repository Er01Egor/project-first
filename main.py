import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


class Advanced_Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 400, 600)
        self.setWindowTitle('Калькулятор')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Advanced_Calculator()
    calculator.show()
    sys.exit(app.exec())
