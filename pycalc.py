#!/usr/bin/env python3

"""Python desktop calculator"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from functools import partial

__version__ = '0.1'
__author__ = 'Obed Garcia'


class PyCalcUi(QMainWindow):
    """Calculator main view"""
    def __init__(self):
        """View initializer"""
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(235, 235)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """Create display"""
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.generalLayout.addWidget(self.display)

    def _create_buttons(self):
        """Create buttons"""
        self.buttons = {}
        buttons_layout = QGridLayout()

        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                    }

        for text, position in buttons.items():
            self.buttons[text] = QPushButton(text)
            self.buttons[text].setFixedSize(40, 40)
            buttons_layout.addWidget(self.buttons[text], position[0], position[1])

            self.generalLayout.addLayout(buttons_layout)

    def set_display_text(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        """Get display's text."""
        return self.display.text()

    def clear_display(self):
        """Clear the display."""
        self.setDisplayText('')


class PyCalcController:
    """Calculator Contoller"""
    def __init__(self, view):
        """Controller initializer"""
        self._view = view
        self._connect_signals

    def _build_expression(self, sub_exp):
        """Build expression"""
        expression = self._view.display_text() + sub_exp
        self._view.set_display_text(expression)

    def _connect_signals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._build_expression, btnText))

        self._view.buttons['C'].clicked.connect(self._view.clear_isplay)


def main():
    """Main function"""
    calc = QApplication(sys.argv)

    view = PyCalcUi()
    view.show()

    calc(view=view)
    sys.exit(calc.exec_())


if __name__ == '__main__':
    main()
