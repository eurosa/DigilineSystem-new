import threading
import time


class MyThread(threading.Thread):
    # overriding constructor
    def __init__(self, ui):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.ui = ui

    # define your own run method
    def run(self):
         pass


