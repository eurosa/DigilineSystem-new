# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import *

# This is our window from QtCreator
import mainwindow_auto


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    # method called by timer
    def showTime(self):
        # getting current time

        current_time = QTime.currentTime()

        # converting QTime object to string 
        label_time = current_time.toString('hh:mm:ss')
        #tickPart = current_time.toString('ss').lower()


        # showing it to the label 
        self.time_show.setText(label_time)

    def pressedOnButton(self):
        print("Pressed On!")

    def pressedOffButton(self):
        print("Pressed Off!")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file

        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        timer.start(1000)  # update every second

        self.showTime()
        ### Hooks to for buttons
        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())


# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.showFullScreen()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
