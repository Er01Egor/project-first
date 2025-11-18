import sys
from PyQt6.QtWidgets import QApplication

from calculator_window import Advanced_Calculator

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Advanced_Calculator()
    calculator.show()
    sys.exit(app.exec())
