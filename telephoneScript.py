import re

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from acora import unicode

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
        self.button11.pressed.connect(self.plusSign)
        self.regexp = re.compile(r'\s\s+')
        self.lcdNumber.textChanged.connect(self.handleTextChanged)
        self.reset()

        # self.show()

    def display(self):
        self.lcdNumber.setText(str(self.stack))

    def reset(self):
        self.state = READY
        self.stack = ''
        self.display()

    def plusSign(self):
        self.stack += str('+')
        self.display()

    def hashSign(self):
        self.stack += str('#')
        self.display()

    def handleTextChanged(self, text):
        if self.regexp.search(text):
            text = unicode(text)
            # do replacements before and after cursor pos
            pos = self.lcdNumber.cursorPosition()
            prefix = self.regexp.sub(' ', text[:pos])
            suffix = self.regexp.sub(' ', text[pos:])
            # cursor might be between spaces
            if prefix.endswith(' ') and suffix.startswith(' '):
                suffix = suffix[1:]
            self.lcdNumber.setText(prefix + suffix)
            self.lcdNumber.setCursorPosition(len(prefix))

    def backspaceClicked(self):
        self.stack = self.lcdNumber.text()[:-1]
        if not self.stack:
            self.stack = ''

        self.lcdNumber.setText(self.stack)

    def input_number(self, v):
            self.stack += str(v)
            self.display()


'''if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    window = TelephoneDialog()
    app.exec_()'''
