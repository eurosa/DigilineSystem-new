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


class RTCThread(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(RTCThread, self).__init__()
        self.signal = Signals()
        self.ui = ui
        self.result = ''
        self.time_split = ''
        self.date_time_obj = None
        self.second = ''
        self.date_rtc = ''

    def run(self):
        # time.sleep(5)
        self.result = "Some String"
        while True:
            if self.ui.int_count:
                print("+++++++++++++++Can not access hardware clock for multiple access ++++++++++++++++++++")
            else:
                self.ui.proc = subprocess.getoutput('sudo hwclock -r')

                print("+++++++++++++++Can not access hardware: "+self.ui.proc+": clock for multiple access "
                                                                              "++++++++++++++++++++")

                # subprocess.call(shlex.split("sudo hwclock -r"))
                # list_result = self.insert_dash(proc, 10)
                # list_result = re.split(list_result, )

                try:
                    date_time_str = self.ui.proc
                    # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
                    if date_time_str:
                        self.date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f%z')
                        '''print('Date:', date_time_obj.date())
                    print('Time:', date_time_obj.time())
                    print('Date-time:', date_time_obj)'''
                        self.ui.lastTime = self.date_time_obj.time()
                        self.ui.lastDate = self.date_time_obj.date()
                        '''if self.ui.setTimeSetting.isChecked():
                        self.clock_set_ui.timeEdit.setTime(date_time_obj.time())'''
                        self.time_split = re.split(':', str(self.date_time_obj.time()))
                        self.date_rtc = str(self.date_time_obj.date().strftime('%d/%m/%Y'))
                        self.second = self.time_split[2].split('.', 1)[0]
                        self.ui.lastTimeHwclock = self.time_split[0] + ":" + self.time_split[1] + ":" + self.second
                        '''splitted_string = re.split('\s+', proc)
                    time_split = re.split(':', splitted_string[1])
                    second = time_split[2].split('.', 1)[0]
                    self.ui.day_date_show.setText(splitted_string[0])
                    self.clock_set_ui.timeEdit.setTime(time_split[0] + ":" + time_split[1]+":"+second)
                    self.ui.time_show.setText(
                        time_split[0] + ":" + time_split[1] + "" + "<b><font font size=12pt font weight:40>" +
                        ":" + "</font>" + "<b>< font size=12pt font weight:40>" +
                        second + "</font>")'''
                except IndexError:
                    self.second = 'Please Connect rtc.'
                    print(self.second)
                # self.int_count = False
                # print(proc)
                # time.sleep(1)
                self.signal.return_signal.emit(self.date_rtc)
                time.sleep(1)

    def function_thread(self, signal):
        self.ui.drawRealTimeData()
        print("++++++++++++++++++++++Date++++++++++++++++++++++++++" + self.date_rtc)
        self.ui.ui.day_date_show.setText(self.date_rtc)
        self.ui.ui.time_show.setText(
            self.time_split[0] + ":" + self.time_split[1] + "" + "<b><font font size=12pt font weight:40>" +
            ":" + "</font>" + "<b>< font size=12pt font weight:40>" +
            self.second + "</font>")
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        # self.threadpool.destroyed()

        # ++++++++++++++++++++ Temp , Humidity, Pressure UI update ++++++++++++++++++++++++++
        self.ui.ui.tempShow.setText(str(configVariables.temp_read_value))
        self.ui.ui.humidityShow.setText(str(configVariables.hum_read_value))
        self.ui.ui.differentialPressureShow.setText(str(configVariables.air_pressure_value))
        # ++++++++++++++++++++ Temp , Humidity, Pressure UI update ++++++++++++++++++++++++++

        print(signal)
