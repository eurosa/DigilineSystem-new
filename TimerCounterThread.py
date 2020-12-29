import datetime
import enum


from PyQt5.QtCore import QThread, QTimer, QEventLoop, QTime, QEvent, QDate, Qt
from PyQt5.QtGui import QImage, QPixmap
import self as self


class TimerStatus(enum.Enum):
    init, counting, paused = 1, 2, 3


class ButtonText:
    start, pause, reset = "Start", "Pause", "Reset"


class TimerCounterThread(QThread):
    # ==================Start Countdown Timer ==============================
    def setClockDialog(self):
        self.setClockWidget.setStyleSheet(
            "color:" + self.dataModel.get_text_col() + ";background-color:" + self.dataModel.get_theme_color() + ";")
        current_time = QTime.currentTime()
        self.clock_set_ui.timeEdit.setTime(current_time)
        self.clock_set_ui.timeEdit.setDisplayFormat("H:mm:ss")
        # self.clock_set_ui.dateEdit.setDate(current_time)
        date = QDate.currentDate()
        # now = datetime.datetime.now()
        # today = datetime.datetime.today().strftime('%d/%m/%Y')
        # setting only date
        self.clock_set_ui.dateEdit.setDate(date)
        self.setClockWidget.show()
        self.setClockWidget.exec_()

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
            self.ui.startButton.setIcon(self.changed_play_image)
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
            self.ui.startButton.setIcon(self.changed_pause_image)
        elif self._status == TimerStatus.counting:
            self.timer_count_down.stop()
            self._status = TimerStatus.paused
            self.ui.startButton.setText(ButtonText.start)
            # icon9 = QtGui.QIcon()
            # icon9.addPixmap(QtGui.QPixmap("icon/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.ui.startButton.setIcon(self.changed_play_image)

    def _reset_event(self):
        self._status = TimerStatus.init
        self._left_seconds = self.my_timer_seconds
        # self._left_seconds = self.ui.minutesSpinBox.value() * 60
        # self.ui.startButton.setText(ButtonText.start)
        # icon9 = QtGui.QIcon()
        # icon9.addPixmap(QtGui.QPixmap("icon/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.startButton.setIcon(self.changed_play_image)
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

        self.my_timer_seconds = (
                self.timer_set_ui.spinHourBox.value() * 3600 + self.timer_set_ui.spinMinuteBox.value() * 60
                + self.timer_set_ui.spinSecondBox.value())

    def acceptOk(self):
        self._reset_event()
        self.int_count = True

    def rejectCancel(self):
        self.timer_set_ui.spinHourBox.setValue(self.ok_hours)
        self.timer_set_ui.spinMinuteBox.setValue(self.ok_minutes)
        self.timer_set_ui.spinSecondBox.setValue(self.ok_seconds)

    def setClockOk(self):
        self.int_count = True

    def rejectClock(self):
        self.int_count = True

    def timeChange(self):
        self.current_time = self.clock_set_ui.timeEdit.time()
        # os.system('sudo date -u --set="%s"' % self.current_time.toString('hh:mm'))
        print(str(self.clock_set_ui.timeEdit.time()))
        # converting QTime object to string
        self.label_time = self.current_time.toString('hh:mm')
        self.tickPart = self.current_time.toString('ss')

        # showing it to the label
        # self.ui.time_show.setText(self.label_time)
        self.ui.time_show.setText(
            self.label_time + ":" + self.tickPart)
        '''
        self.ui.time_show.setText(
            self.label_time + "" + "<b><font color='#FFFF00' font size=12pt font weight:40>" +
            ":" + "</font></b></br>" + "<b><font color='#FFFF00' font size=12pt font weight:40>" +
            self.tickPart + "</font></b></br>")
        '''
        # self.ui.tick_show.setText(self.tickPart)
        # self.clock_set_ui.timeEdit.setTime(self.clock_set_ui.timeEdit.time())

    def dateChange(self):
        self.int_count = True

    # ==================End Countdown Timer ===============================

    def __init__(self, ui, timer_set_ui, alldisplayobj, clock_set_ui, datamodel, setTimerWidget, setClockWidget,  *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        self.ui = ui
        self.timer_set_ui = timer_set_ui
        self.clock_set_ui = clock_set_ui
        self.dataModel = datamodel
        self.setTimerWidget = setTimerWidget
        self.setClockWidget = setClockWidget
        # ================Start Count Down Timer Layout =========================================
        self.play_wh = QImage(QPixmap("icon/play_white.png"))
        self.pause_wh = QImage(QPixmap("icon/pause_white.png"))
        self.changed_play_image = alldisplayobj.changedIconColorImage(self.play_wh)
        self.changed_pause_image = alldisplayobj.changedIconColorImage(self.pause_wh)

        self.ui.startButton.clicked.connect(self._start_event)
        self.ui.resetButton.clicked.connect(self._reset_event)
        self.ui.timerSet.clicked.connect(self.setTimerDialog)
        self.ui.setTimeSetting.clicked.connect(self.setClockDialog)
        self.clock_set_ui.buttonClockBox.accepted.connect(self.setClockOk)
        self.clock_set_ui.buttonClockBox.rejected.connect(self.rejectClock)
        self.clock_set_ui.timeEdit.timeChanged.connect(self.timeChange)
        self.clock_set_ui.dateEdit.dateChanged.connect(self.dateChange)
        self.total_seconds = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.ok_hours = 0
        self.ok_minutes = 0
        self.ok_seconds = 0
        self.int_count = True
        self._status = TimerStatus.init
        self.appearance_color_name = str()

        self.label_time = 0
        self.tickPart = 0
        self.current_time = 0

        # ++++++++++Initialize time of countdown timer using QSpinBox initial
        # values++++++++++++++++++_left_seconds+++++++360060+++++++++++++++++++++++++++++++++++++++++++++++
        self._left_seconds = (
                self.timer_set_ui.spinHourBox.value() * 3600 + self.timer_set_ui.spinMinuteBox.value() * 60
                + self.timer_set_ui.spinSecondBox.value())
        self.my_timer_seconds = self._left_seconds

        self.timer_count_down = QTimer()
        self.timer_count_down.timeout.connect(self._countdown_and_show)
        self.showTimerCounter()
        self.timer_set_ui.buttonBox.accepted.connect(self.acceptOk)
        self.timer_set_ui.buttonBox.rejected.connect(self.rejectCancel)
        # self.widget = TimerWidget(self)
        # self.setCentralWidget(self.widget)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.resize(150, 90)
        # self.move(10, 10)
        # ================End Count Down Timer Layout======================
        # ------------------------------Data Capture Thread ------------------------------------

    def run(self):
        # self.dataCollectionTimer.start(1000)
        loop = QEventLoop()
        loop.exec_()