from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time
import traceback, sys

from Database import database
from Database.dataModel import DataModel


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:
    https://www.learnpyqt.com/tutorials/multithreading-pyqt-applications-qthreadpool/#the-complete-code
    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress


    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)'''

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
    openDataBase = pyqtSignal()


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn,ui, alldisp , *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.ui = ui
        self.alldisplayColorChangeObj = alldisp
        self.kwargs = kwargs
        self.dataModel = kwargs
        self.signals = WorkerSignals()
        self.database_manage = database.DataBaseManagement()
        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.

        self.database_manage.db = None
        self.database_manage.init('datafile', 'QSQLITE')
        # self.database_manage.updateIconColorSettings(self.dataModel)
        # Retrieve args/kwargs here; and fire processing using them'''
        try:
            #result = self.fn(*self.args, **self.kwargs)
            result = self.ui.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
