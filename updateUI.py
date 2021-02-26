import datetime
import os
import re
import subprocess
from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, QTimer
import time

import configVariables
from main import Thread


class Signals(QObject):
    return_signal = pyqtSignal(str)


class updateUi(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(updateUi, self).__init__()
        self.signal = Signals()
        self.ui = ui
        self.result = ''

    def run(self):
        # time.sleep(5)
        self.result = "Some String"
        while True:
                self.signal.return_signal.emit(self.result)
                time.sleep(1)

    def function_thread(self, signal):

        # ++++++++++++++++++++ Temp , Humidity, Pressure UI update ++++++++++++++++++++++++++
        self.ui.ui.tempShow.setText(str(configVariables.temp_read_value))
        self.ui.ui.humidityShow.setText(str(configVariables.hum_read_value))
        self.ui.ui.differentialPressureShow.setText(str(configVariables.air_pressure_value))
        # ++++++++++++++++++++ Temp , Humidity, Pressure UI update ++++++++++++++++++++++++++

        print(signal)
