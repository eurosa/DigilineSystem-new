import datetime

from PyQt5.QtCore import QThread, QTimer, QEventLoop, QTime, QDate
from PyQt5.QtGui import QImage, QPixmap


class ShowTimeDateThread(QThread):
    def setClockDialog(self):
        self.setClockWidget.setStyleSheet(
            "color:" + self.dataModel.get_text_col() + ";background-color:" + self.dataModel.get_theme_color() + ";")
        # current_time = QTime.currentTime()
        # self.clock_set_ui.timeEdit.setTime(current_time)
        self.clock_set_ui.timeEdit.setDisplayFormat("H:mm:ss")
        # self.clock_set_ui.dateEdit.setDate(current_time)
        date = QDate.currentDate()
        # now = datetime.datetime.now()
        # today = datetime.datetime.today().strftime('%d/%m/%Y')
        # setting only date
        self.clock_set_ui.dateEdit.setDate(date)
        if self.ui.setTimeSetting.isChecked():
            self.setClockWidget.show()
        else:
            self.setClockWidget.hide()
        self.setClockWidget.exec_()

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

    def collectProcessData(self):
        print("Collecting Process Data")
        self.ui.lcd1.setText("Collecting Process Data")

    def showTime(self):
        # getting current time
        # self.fontColorChangesName()
        QTime.currentTime().start()
        self.current_time = QTime.currentTime()
        # converting QTime object to string
        self.label_time = self.current_time.toString('hh:mm')
        self.tickPart = self.current_time.toString('ss')

        # showing it to the label
        # self.ui.time_show.setText(self.label_time)
        # self.ui.tick_show.setText(self.tickPart)
        # if self.appearance_color_name == 'Dark':
        # self.ui.time_show.setStyleSheet("color:#FFFFFF")
        self.ui.time_show.setText(
            self.label_time + "" + "<b><font font size=12pt font weight:40>" +
            ":" + "</font></b></br>" + "<b>< font size=12pt font weight:40>" +
            self.tickPart + "</font></b></br>")
        '''elif self.appearance_color_name == 'White':
            self.ui.time_show.setStyleSheet("color:#000000")
            self.ui.time_show.setText(
                self.label_time + "" + "<b><font color='#000000' font size=12pt font weight:40>" +
                ":" + "</font></b></br>" + "<b><font color='#000000' font size=12pt font weight:40>" +
                self.tickPart + "</font></b></br>")'''

    def showDate(self):
        now = datetime.datetime.now()
        today = datetime.datetime.today().strftime('%d/%m/%Y')
        # self.ui.day_date_show.setText(now.strftime("%A") + "  " + today)

    def RunTimer(self):
        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        timer.start(1000)  # update every second

    def __init__(self, ui, setClockWidget, datamodel, clock_set_ui, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        # self.dataCollectionTimer = QTimer()
        # self.dataCollectionTimer.moveToThread(self)
        # self.dataCollectionTimer.timeout.connect(self.collectProcessData)
        self.dataModel = datamodel
        self.ui = ui
        self.setClockWidget = setClockWidget
        self.clock_set_ui = clock_set_ui
        self.label_time = 0
        self.tickPart = 0
        self.current_time = 0
        self.showDate()
        self.clock_set_ui.buttonClockBox.accepted.connect(self.setClockOk)
        self.clock_set_ui.buttonClockBox.rejected.connect(self.rejectClock)
        self.clock_set_ui.timeEdit.timeChanged.connect(self.timeChange)
        self.clock_set_ui.dateEdit.dateChanged.connect(self.dateChange)
        self.ui.setTimeSetting.clicked.connect(self.setClockDialog)
        # ==================Stop Watch =====================================
        self.RunTimer()

        # ------------------------------Data Capture Thread ------------------------------------

    def run(self):
        # self.dataCollectionTimer.start(1000)
        loop = QEventLoop()
        loop.exec_()
