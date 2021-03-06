#!/usr/bin/env python

import sys

from PyQt5 import Qt
from PyQt5.uic import loadUi

# [ms]
TICK_TIME = 2**6

class StopWatch(Qt.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loadUi("stopWatch.ui", self)
        self.reset.clicked.connect(self.do_reset)
        self.start.clicked.connect(self.do_start)

        self.timer = Qt.QTimer()
        self.timer.setInterval(TICK_TIME)
        self.timer.timeout.connect(self.tick)

        self.do_reset()

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

    def display(self):
        self.lcd.display("%d:%05.2f" % (self.time // 60, self.time % 60))

    @Qt.pyqtSlot()
    def tick(self):
        self.time += TICK_TIME/1000
        self.display()

    @Qt.pyqtSlot()
    def do_start(self):
        self.timer.start()
        self.start.setText("Pause")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_pause)

    @Qt.pyqtSlot()
    def do_pause(self):
        self.timer.stop()
        self.start.setText("Start")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_start)

    @Qt.pyqtSlot()
    def do_reset(self):
        self.time = 0
        self.display()

app = Qt.QApplication(sys.argv)

watch = StopWatch()
watch.show()

app.exec_()
