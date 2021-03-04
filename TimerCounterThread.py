import datetime
import enum
import modifyGlobalVariables
import configVariables

from PyQt5.QtCore import QThread, QTimer, QEventLoop, QTime, QEvent, QDate, Qt
from PyQt5.QtGui import QImage, QPixmap
import self as self


class TimerStatus(enum.Enum):
    init, counting, paused = 1, 2, 3


class ButtonText:
    start, pause, reset = "Start", "Pause", "Reset"


class TimerCounterThread(QThread):
    # ==================Start Countdown Timer ==============================

    def eventFilter(self, obj, event):
        if obj is self.ui.displayArea.viewport() and event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                self.ui.minutesSpinBox.setFocus()
                self.ui.minutesSpinBox.selectAll()
        # return super(TimerWidget, self).eventFilter(obj, event)

    def _countdown_and_show(self):
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self.showTimerCounter()
        else:
            self.timer_count_down.stop()
            self.showTimerCounter()
            self.ui.startButton.setText(ButtonText.start)
            # icon9 = QtGui.QIcon()
            # icon9.addPixmap(QtGui.QPixmap("icon/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.startButton.setIcon(configVariables.play_changed_image)
            self._status = TimerStatus.init
            self._left_seconds = self.my_timer_seconds
            # self._left_seconds = self.ui.minutesSpinBox.value() * 60

    def _start_event(self):
        if (self._status == TimerStatus.init or self._status == TimerStatus.paused) and self._left_seconds > 0:
            self._left_seconds -= 1
            self._status = TimerStatus.counting
            self.showTimerCounter()
            self.timer_count_down.start(1000)
            self.ui.startButton.setText(ButtonText.pause)
            # icon9 = QtGui.QIcon()
            # icon9.addPixmap(QtGui.QPixmap("icon/pause_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.startButton.setIcon(configVariables.pause_changed_image)
        elif self._status == TimerStatus.counting:
            self.timer_count_down.stop()
            self._status = TimerStatus.paused
            self.ui.startButton.setText(ButtonText.start)
            # icon9 = QtGui.QIcon()
            # icon9.addPixmap(QtGui.QPixmap("icon/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.startButton.setIcon(configVariables.play_changed_image)

    def _reset_event(self):
        self._status = TimerStatus.init
        self._left_seconds = self.my_timer_seconds
        # self._left_seconds = self.ui.minutesSpinBox.value() * 60
        # self.ui.startButton.setText(ButtonText.start)
        # icon9 = QtGui.QIcon()
        # icon9.addPixmap(QtGui.QPixmap("icon/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.startButton.setIcon(configVariables.play_changed_image)
        self.timer_count_down.stop()
        self.showTimerCounter()

    def _edit_event(self):
        if self._status == TimerStatus.init:
            self._left_seconds = self.my_timer_seconds
            # self._left_seconds = self.ui.minutesSpinBox.value() * 60
            self.showTimerCounter()

    def showTimerCounter(self):
        self.total_seconds = min(self._left_seconds, 360060)  # Max time: 99:59:00 #Max time:99:59:59
        self.hours = self.total_seconds // 3600
        self.total_seconds = self.total_seconds - (self.hours * 3600)
        self.minutes = self.total_seconds // 60
        self.seconds = self.total_seconds - (self.minutes * 60)
        # self.ui.displayArea.setStyleSheet("font-weight: bold; color: yellow")
        # "<b><font color='#ffffff' font size=12pt font weight:40>"+ ":"+"</font></b></br>" +
        self.ui.displayArea.setText(
            str("%02d" % self.hours) + ":" + str(
                "%02d" % self.minutes) + "" + "<b><font size=12pt font weight:40>" +
            ":" + "</font></b></br>" + "<b><font size=12pt font weight:40>" + str(
                "%02d" % self.seconds) + "</font></b></br>")
        '''
        self.ui.displayArea.setText(
            str("%02d" % self.hours) + ":" + str(
                "%02d" % self.minutes) + "" + "<b><font color='#FFFF00' font size=12pt font weight:40>" +
            ":" + "</font></b></br>" + "<b><font color='#FFFF00' font size=12pt font weight:40>" + str(
                "%02d" % self.seconds) + "</font></b></br>")
        '''
        # self.ui.displayArea.setText("{:02}:{:02}:{:02}".format(int(self.hours), int(self.minutes), int(self.seconds)))
        self.ui.displayArea.setAlignment(Qt.AlignHCenter)

    def setTimerDialog(self):
        self.setTimerWidget.setStyleSheet(
            "color:" + self.dataModel.get_text_col() + ";background-color:" + self.dataModel.get_theme_color() + ";")
        self.ok_hours = self.timer_set_ui.spinHourBox.value()
        self.ok_minutes = self.timer_set_ui.spinMinuteBox.value()
        self.ok_seconds = self.timer_set_ui.spinSecondBox.value()
        print(str(self.ok_hours))
        if self.ui.timerSet.isChecked():
            self.setTimerWidget.show()
        else:
            self.setTimerWidget.hide()
        self.timer_set_ui.hourSlider.valueChanged.connect(self.sliderValueChange)
        self.timer_set_ui.minuteSlider.valueChanged.connect(self.sliderValueChange)
        self.timer_set_ui.secondSlider.valueChanged.connect(self.sliderValueChange)

        self.timer_set_ui.spinHourBox.valueChanged.connect(self.spinValueChange)
        self.timer_set_ui.spinMinuteBox.valueChanged.connect(self.spinValueChange)
        self.timer_set_ui.spinSecondBox.valueChanged.connect(self.spinValueChange)
        # self._left_seconds = self.my_timer_seconds

        self.setTimerWidget.exec_()

        '''
        self.my_timer_seconds   
        d = QDialog()
        b1 = QPushButton("ok", d)
        b1.move(50, 50)
        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        self.timer_set_ui.exec_()'''

    def toggle_timerSet(self, state):
        if state:
            self.setTimerWidget.show()
        else:
            self.setTimerWidget.hide()

    def spinValueChange(self):
        if self.timer_set_ui.spinHourBox.value() >= 0:
            self.timer_set_ui.hourSlider.setValue(self.timer_set_ui.spinHourBox.value())
        if self.timer_set_ui.spinMinuteBox.value() >= 0:
            self.timer_set_ui.minuteSlider.setValue(self.timer_set_ui.spinMinuteBox.value())
        if self.timer_set_ui.spinSecondBox.value() >= 0:
            self.timer_set_ui.secondSlider.setValue(self.timer_set_ui.spinSecondBox.value())
    # +++++++++++++++++ I have added this 20/02/2021++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.ok_hours = self.timer_set_ui.spinHourBox.value()
        self.ok_minutes = self.timer_set_ui.spinMinuteBox.value()
        self.ok_seconds = self.timer_set_ui.spinSecondBox.value()
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.my_timer_seconds = (
                self.timer_set_ui.spinHourBox.value() * 3600 + self.timer_set_ui.spinMinuteBox.value() * 60
                + self.timer_set_ui.spinSecondBox.value())

    def sliderValueChange(self):
        if self.timer_set_ui.hourSlider.value() >= 0:
            self.timer_set_ui.spinHourBox.setValue(self.timer_set_ui.hourSlider.value())
        if self.timer_set_ui.minuteSlider.value() >= 0:
            self.timer_set_ui.spinMinuteBox.setValue(self.timer_set_ui.minuteSlider.value())
        if self.timer_set_ui.secondSlider.value() >= 0:
            self.timer_set_ui.spinSecondBox.setValue(self.timer_set_ui.secondSlider.value())

        # +++++++++++++++++ I have added this 20/02/2021++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.ok_hours = self.timer_set_ui.spinHourBox.value()
        self.ok_minutes = self.timer_set_ui.spinMinuteBox.value()
        self.ok_seconds = self.timer_set_ui.spinSecondBox.value()
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        self.my_timer_seconds = (
                self.timer_set_ui.spinHourBox.value() * 3600 + self.timer_set_ui.spinMinuteBox.value() * 60
                + self.timer_set_ui.spinSecondBox.value())

    def acceptOk(self):
        self._reset_event()
        self.int_count = True
        print("Hours:"+str(self.ok_hours))
        print("Minutes:" + str(self.ok_minutes))
        print("Seconds:" + str(self.ok_seconds))
        # ++++++++++++++++++++++++ Update Counter Value in Database ++++++++++++++
        self.dataModel.set_hours_cnt(self.ok_hours)
        self.dataModel.set_minutes_cnt(self.ok_minutes)
        self.dataModel.set_seconds_cnt(self.ok_seconds)
        configVariables.light_database.updateCntDwnTimer(self.dataModel)
        self.setTimerWidget.close()

    def rejectCancel(self):
        self.timer_set_ui.spinHourBox.setValue(self.ok_hours)
        self.timer_set_ui.spinMinuteBox.setValue(self.ok_minutes)
        self.timer_set_ui.spinSecondBox.setValue(self.ok_seconds)
        # ++++++++++++++++++++++++++ Update Counter Value in Database ++++++++++++
        self.dataModel.set_hours_cnt(self.ok_hours)
        self.dataModel.set_minutes_cnt(self.ok_minutes)
        self.dataModel.set_seconds_cnt(self.ok_seconds)
        configVariables.light_database.updateCntDwnTimer(self.dataModel)
        self.setTimerWidget.close()

    def initCounterValue(self):
        configVariables.light_database.queryCountDownTimerData(self.dataModel)
        self.ok_hours = self.dataModel.get_hours_cnt()
        self.ok_minutes = self.dataModel.get_minutes_cnt()
        self.ok_seconds = self.dataModel.get_seconds_cnt()

        print("Hours: "+str(self.ok_hours)+" Minutes: "+str(self.ok_minutes)+" Seconds: "+str(self.ok_seconds))
        print("Hours: " + str(self.ok_hours) + " Minutes: " + str(self.ok_minutes) + " Seconds: " + str(self.ok_seconds))

    # ==================End Countdown Timer ===============================

    def __init__(self, ui, timer_set_ui, alldisplayobj, datamodel, setTimerWidget,  *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        self.ui = ui
        self.timer_set_ui = timer_set_ui
        self.dataModel = datamodel
        self.setTimerWidget = setTimerWidget

        # ================Start Count Down Timer Layout =========================================
        self.ui.startButton.clicked.connect(self._start_event)
        self.ui.resetButton.clicked.connect(self._reset_event)
        self.ui.timerSet.clicked.connect(self.setTimerDialog)

        self.total_seconds = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.ok_hours = 0
        self.ok_minutes = 0
        self.ok_seconds = 0
        self.initCounterValue()
        self.int_count = True
        self._status = TimerStatus.init
        self.appearance_color_name = str()

        self.label_time = 0
        self.tickPart = 0
        self.current_time = 0
        self.timer_set_ui.spinHourBox.setValue(self.ok_hours)
        self.timer_set_ui.spinMinuteBox.setValue(self.ok_minutes)
        self.timer_set_ui.spinSecondBox.setValue(self.ok_seconds)

        self.timer_set_ui.hourSlider.setValue(self.ok_hours)
        self.timer_set_ui.minuteSlider.setValue(self.ok_minutes)
        self.timer_set_ui.secondSlider.setValue(self.ok_seconds)
        # ++++++++++Initialize time of countdown timer using QSpinBox initial
        # values++++++++++++++++++_left_seconds+++++++360060+++++++++++++++++++++++++++++++++++++++++++++++
        self._left_seconds = (
                self.timer_set_ui.spinHourBox.value() * 3600 + self.timer_set_ui.spinMinuteBox.value() * 60
                + self.timer_set_ui.spinSecondBox.value())
        self.my_timer_seconds = self._left_seconds

        self.timer_count_down = QTimer()
        self.timer_count_down.timeout.connect(self._countdown_and_show)
        self.showTimerCounter()
        self.timer_set_ui.buttonOk.clicked.connect(self.acceptOk)
        self.timer_set_ui.buttonCancel.clicked.connect(self.rejectCancel)

        # self.widget = TimerWidget(self)
        # self.setCentralWidget(self.widget)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.resize(150, 90)
        # self.move(10, 10)
        # ================End Count Down Timer Layout===========================================
        # ------------------------------Data Capture Thread ------------------------------------

    def run(self):
        # self.dataCollectionTimer.start(1000)
        loop = QEventLoop()
        loop.exec_()

