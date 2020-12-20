import datetime

from PyQt5.QtCore import QThread, QTimer, QEventLoop, QTime
from PyQt5.QtGui import QImage, QPixmap


class ShowTimeDateThread(QThread):
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
        self.ui.day_date_show.setText(now.strftime("%A") + "  " + today)

    def RunTimer(self):
        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        timer.start(1000)  # update every second

    def __init__(self, ui, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        # self.dataCollectionTimer = QTimer()
        # self.dataCollectionTimer.moveToThread(self)
        # self.dataCollectionTimer.timeout.connect(self.collectProcessData)

        self.ui = ui
        self.label_time = 0
        self.tickPart = 0
        self.current_time = 0
        self.showDate()
        # ==================Stop Watch =====================================
        self.RunTimer()

        # ------------------------------Data Capture Thread ------------------------------------

    def run(self):
        # self.dataCollectionTimer.start(1000)
        loop = QEventLoop()
        loop.exec_()
