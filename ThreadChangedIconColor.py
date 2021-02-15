from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, QTimer


class Signals(QObject):
    return_signal = pyqtSignal(str)


class ThreadChangedIcon(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(ThreadChangedIcon, self).__init__()
        self.signal = Signals()
        self.ui = ui

    def run(self):
        # time.sleep(5)
        result = "Some String"
        # self.ui.modifyGlobalVariablesObj.setChangedImage()
        self.ui.modifyGlobalVariablesObj.setChangedLightColor()
        # ======================= Login UI ==========================================================================

        self.signal.return_signal.emit(result)

    def function_thread(self, signal):
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        # self.threadpool.destroyed()
        print("My Goodness")
        print(signal)
