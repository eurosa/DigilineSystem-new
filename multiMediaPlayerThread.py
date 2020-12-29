from PyQt5.QtCore import pyqtSlot, QRunnable, QObject, pyqtSignal


class Signals(QObject):
    return_signal = pyqtSignal(str)


class MultiMediaThread(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, player):
        super(MultiMediaThread, self).__init__()
        self.signal = Signals()
        # self.layout = layout
        self.player = player


    @pyqtSlot()
    def run(self):
        # time.sleep(5)
        self.player.show()
        #  self.signal.return_signal.emit()