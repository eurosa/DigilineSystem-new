from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from telephonepad import Ui_telephonePad

# Calculator state.
READY = 0
INPUT = 1


class TelephoneDialog(QDialog, Ui_telephonePad):
    def __init__(self, *args, **kwargs):
        super(TelephoneDialog, self).__init__(*args, **kwargs)

        # self.lcdNumber.setAlignment(Qt.AlignRight)
        # self.lcdNumber.setLayoutDirection(Qt.AnchorRight)
        self.setupUi(self)
        self.waitingForOperand = True
        # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'button%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        self.lcdNumber.setAlignment(Qt.AlignRight)
        self.buttonClear.pressed.connect(self.backspaceClicked)
        self.button10.pressed.connect(self.hashSign)

        self.reset()

        self.show()

    def display(self):
        self.lcdNumber.setText(str(self.stack[-1]))

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()

    def plusSign(self):
        pass

    def hashSign(self):
        pass

    def backspaceClicked(self):
        text = self.lcdNumber.text()[:-1]
        if not text:
            text = '0'
            self.stack = [0]
            self.waitingForOperand = True

        self.lcdNumber.setText(text)
        self.stack[-1] = int(text)

    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    window = TelephoneDialog()
    app.exec_()
