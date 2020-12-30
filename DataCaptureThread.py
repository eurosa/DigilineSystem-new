from PyQt5.QtCore import QThread, QTimer, QEventLoop
from PyQt5.QtGui import QImage, QPixmap
import modifyGlobalVariables
import configVariables

TICK_TIME = 2 ** 6


class CounterThread(QThread):
    def collectProcessData(self):
        print("Collecting Process Data")
        self.ui.lcd1.setText("Collecting Process Data")

    def tick(self):
        self.time += TICK_TIME / 1000
        self.display()

    def do_reset(self):
        self.time = 0
        self.display()

    def display(self):
        # self.ui.lcd.display("%d:%05.2f" % (self.time // 60, self.time % 60))
        hour = "%0d:" % (self.time // 60)
        minSecond = "%05.2f" % (self.time % 60)
        self.convert(self.time)
        listMinSec = minSecond.split(".")
        # self.ui.lcd1.setFont(QFont('Times', 72))
        # self.ui.lcd2.setFont(QFont('Times', 20))
        '''self.ui.lcd1.setText(hour + "" + listMinSec[
            0] + "" + "<b><font color='#ffffff' font size=12pt font weight:40>" + ":" + "</font></b></br>" + "<b><i><font color='#ff0000' font size=12pt font weight:40>" +
                             listMinSec[1] + "</font></i></b></br>")'''
        # self.ui.lcd1.setText(hour + "" + listMinSec[0] + "" + "<b><font color='#ffffff' font size=12pt font
        # weight:40>" + ":" + "</font></b></br>" + "<b><font color='#ff0000' font size=12pt font weight:40>" +
        # listMinSec[1] + "</font></b></br>") self.ui.lcd1.setText('My normal text, font = 10pt') self.ui.lcd2.hide()
        # self.ui.lcd2.setText(":" + listMinSec[1])

    def convert(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        self.ui.lcd1.setText(str("%02d:" % hour) + "" + str(
            "%02d" % minutes) + "" + "<b>< font size=12pt font weight:40>" + ":" + "</font></b></br>" + "<b>< font size=12pt font weight:40>" +
                             str("%02d" % seconds) + "</font></b></br>")
        '''
                if self.fontColorChangesName() == 'Dark':
            self.ui.lcd1.setStyleSheet("color:#FFFFFF")
            self.ui.lcd1.setText(str("%02d:" % hour) + "" + str(
                "%02d" % minutes) + "" + "<b><font color='#ffffff' font size=12pt font weight:40>" + ":" + "</font></b></br>" + "<b><font color='#ffffff' font size=12pt font weight:40>" +
                             str("%02d" % seconds) + "</font></b></br>")
        elif self.fontColorChangesName() == 'White':
            self.ui.lcd1.setStyleSheet("color:#000000")
            self.ui.lcd1.setText(str("%02d:" % hour) + "" + str(
                "%02d" % minutes) + "" + "<b><font color='#000000' font size=12pt font weight:40>" + ":" + "</font></b></br>" + "<b><font color='#000000' font size=12pt font weight:40>" +
                             str("%02d" % seconds) + "</font></b></br>")
        '''

    def do_start(self):
        self.timer.start()
        self.ui.start.setText("Pause")
        # icon9 = QtGui.QIcon()
        # icon9.addPixmap(QtGui.QPixmap("icon/pause_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # path_image = os.path.join(dir_path, "icon/pause_white.png").replace("\\", "/")
        # self.image_pause = QtGui.QImage(QPixmap("icon/pause_white.png"))
        # self.alldisplayColorChangeObj.changeIconColorOfTimer(self.ui.start, self.image_pause)
        self.ui.start.setIcon(configVariables.pause_changed_image)
        self.ui.start.clicked.disconnect()
        self.ui.start.clicked.connect(self.do_pause)

    def do_pause(self):
        self.timer.stop()
        self.ui.start.setText("Start")
        # icon9 = QtGui.QIcon()
        # icon9.addPixmap(QtGui.QPixmap("icon/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.start.setIcon(configVariables.play_changed_image)
        # self.image_play = QtGui.QImage(QPixmap("icon/play_white.png"))
        # self.alldisplayColorChangeObj.changeIconColorOfTimer(self.ui.start, self.image_play)
        self.ui.start.clicked.disconnect()
        self.ui.start.clicked.connect(self.do_start)

    def __init__(self, ui, allDisplay, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        # self.dataCollectionTimer = QTimer()
        # self.dataCollectionTimer.moveToThread(self)
        # self.dataCollectionTimer.timeout.connect(self.collectProcessData)

        self.ui = ui
        # ==================Stop Watch =====================================
        self.ui.reset.clicked.connect(self.do_reset)
        self.ui.start.clicked.connect(self.do_start)

        self.timer = QTimer()
        self.timer.setInterval(TICK_TIME)
        self.timer.timeout.connect(self.tick)
        self.do_reset()
        # ------------------------------Data Capture Thread ------------------------------------

    def run(self):
        # self.dataCollectionTimer.start(1000)
        loop = QEventLoop()
        loop.exec_()
