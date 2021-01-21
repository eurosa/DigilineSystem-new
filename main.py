# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import enum
import os
import shlex
import signal
import subprocess
import threading
import time
from functools import partial
from multiprocessing import Pool, cpu_count
import sys

import dateutil
import pytz

import multithreading as mt
from PyQt5.QtSql import QSqlQueryModel

from DataCaptureThread import CounterThread
from MovieSplashScreen import MovieSplashScreen
from RTCmodule import *
from ShowTimeDateThread import ShowTimeDateThread
from ThreadClass import ThreadParallel
from TimerCounterThread import TimerCounterThread
from allDisplayAttributeColor import *
from gasColorAlterRXTX import ThreadGasColorRXTX
from multiMediaPlayerThread import MultiMediaThread
from player import Player
from pushButtonColorControl import PushButtonColorControl
from repeatedTimer import RepeatedTimer
from serialDataTXRX import SerialWrapper
from switchDataSendThread import ThreadDataSwitchData
from telephoneScript import TelephoneDialog
from toolButtonColorControl import ToolButtonColorControl
from ventilationDetails import Ui_ventilationDetails
from virtual_keyboard import *
import login_virtual_keyboard
from iconColorControl import *
# This gets the Qt stuff
import PyQt5

import self as self
from PyQt5.QtCore import QTime, QTimer, Qt, QPoint, QAbstractListModel, pyqtSignal, QSize, QUrl, pyqtSlot, QEvent, QDate
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
# This is our window from QtCreator
# from PyQt5.uic.properties import QtWidgets
import pyqtgraph as pg

import mainwindow_auto
from pyqtgraph import PlotWidget, plot
# create class for our Raspberry Pi GUI
from Database import database
from Database.dataModel import DataModel
from secondForm import Ui_Form
from otLightening import Ui_Form as Ot_Ui
from multiMedia import Ui_Form as MultiMedia_Ui
from history import Ui_MainWindow as History_Ui
from Gas import Ui_Form as Gas_Ui
from tempGraph import Ui_Form as Temp_Ui
from humidityGraph import Ui_Form as Hum_Ui
from multiMediaForm import Ui_MainWindow as Multi_Ui_Media
# from timer import TimerStatus, ButtonText, TimerWidget
from setTimerDialog import Ui_setTimer
from setClockDialog import Ui_setClockTime
from settingsDialog import Ui_SettingsQDialog
from changeLabelName import Ui_changeLabelName
from shutDownDialog import Ui_shutDownDialog
from loginDialog import Ui_loginDialog
from telephonepad import Ui_telephonePad
from additionalChronos import Ui_additionalChronos as AdditionalChronos_Ui
from historyDetailsOfData import Ui_historydetailsofdata as historydetailsofdata_ui

import toggleButton
import lightBrightness
import chronos3, chronos2
from MessageBox import AutoCloseMessageBox
import modifyGlobalVariables
import configVariables
import Database.database

dir_path = os.path.dirname(os.path.realpath(__file__))
TICK_TIME = 2 ** 6


def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    h, r = divmod(ms, 36000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


class Signals(QObject):
    return_signal = pyqtSignal(str)


class Thread(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(Thread, self).__init__()
        self.signal = Signals()
        self.ui = ui

    @pyqtSlot()
    def run(self):
        # time.sleep(5)
        result = "Some String"
        # ------------------------------------------------------
        # self.ui.settings_dialog_set_ui.labelDisplayTheme.setPixmap(QtGui.QPixmap(self.ui.dataModel.get_theme_color_preview()))
        # self.ui.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.ui.SettingsQDialog)
        self.ui.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.ui.shutDialog)
        self.ui.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.ui.loginDialogQtWidget)
        self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.setTimerWidget)
        # ++++++++++++++++++++++++++++++ Settings Dialog UI Color Changes ++++++++++++++++++++++++++++++++++
        # self.ui.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.ui.settings_dialog_set_ui.tabWidget)
        # -------------------------------------------------------------------------------------
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.oxygen, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.ips, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.vacuum, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.cabonDiOxide, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.air7, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.air, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.nitrousOxide, "QToolButton")  # 00-

        # -----------------------Menu Tool Button ----------------------------------------------
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.otLighteningDetails, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.ventiLationDetails, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.gasIndicator, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.historyDetails, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.multiMediaDetails, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.ui.menuTitleName, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelBackgroundColor(self.ui.ui.leftMenuTitleLine, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelBackgroundColor(self.ui.ui.rightMenuTitleLine, "QLabel")
        # --------------------------------Timer Control Color-------------------------------------------
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.start, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.reset, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.addAdditonalChronosButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.timerSet, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.startButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.resetButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.setTimeSetting, "QToolButton")
        # -------------------------------Miscellaneous---------------------------------------------------
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.powerButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.settingsButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.homeButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.phoneCallingButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.toolButton_9, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.upHumidityButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.downHumidityButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.upTemperatureButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.downTemperatureButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.temeratureGraph, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ui.humidityGraph, "QToolButton")
        # ------------------------------- Gas Label Color Changes ----------------------------------------
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.gas_ui.gasLabel_1, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.gas_ui.gasLabel_2, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.gas_ui.gasLabel_3, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.gas_ui.gasLabel_4, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.gas_ui.gasLabel_5, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.gas_ui.gasLabel_6, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_1_high, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_1_normal, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_1_low, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_2_high, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_2_normal, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_2_low, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_3_high, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_3_normal, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_3_low, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_4_high, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_4_normal, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_4_low, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_5_high, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_5_normal, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_5_low, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_6_normal, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.gas_ui.gasLabel_6_low, "QLabel")
        # ------------------------------- Label Color Changes --------------------------------------------
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.differentialLabel, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.hepaLabel, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.differentialPressureShow, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.hepaFilterStatus, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.tempLabelName, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.humidityLabelName, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.tempSetLabel, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.humiditySetLabel, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.tempSetShow, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.humiditySetShow, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.tempShow, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.humidityShow, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.anaesthesiaTimeLabel, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.elapsedTimeLabel, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.time_label, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ui.medicalGasLabelTitle, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDateTimeAttributeColor(self.ui.ui.day_date_show, "QLabel")
        self.ui.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.ui.displayArea, "QLabel")
        self.ui.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.ui.lcd1, "QLabel")
        self.ui.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.ui.time_show, "QLabel")
        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ui.tempIcon)
        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ui.humidityIcon)
        # -------------------------------Icon color changes ----------------------------------------------
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.humidityGraph)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.powerButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.settingsButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.homeButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.phoneCallingButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.toolButton_9)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.upHumidityButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.downHumidityButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.upTemperatureButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.downTemperatureButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.temeratureGraph)

        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.start)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.reset)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.addAdditonalChronosButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.timerSet)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.startButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.resetButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.setTimeSetting)

        # -----------------------Menu Tool Icon color changes----------------------------------------------
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.otLighteningDetails)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.ventiLationDetails)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.gasIndicator)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.historyDetails)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ui.multiMediaDetails)
        # ---------------------- Additional Chronos Label and Tool Button --------------------------------------------------
        self.ui.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.additionChronos_ui.chronos2, "QLabel")
        self.ui.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.additionChronos_ui.chronos3, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.additionChronos_ui.chronosLabel2, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.additionChronos_ui.chronosLabel3, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.additionChronos_ui.startChrono2, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.additionChronos_ui.resetChrono2, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.additionChronos_ui.startChrono3, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.additionChronos_ui.resetChrono3, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.additionChronos_ui.startChrono2)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.additionChronos_ui.resetChrono2)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.additionChronos_ui.startChrono3)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.additionChronos_ui.resetChrono3)
        # -------------------------------------- OT Lightening -----------------------------------------------------------
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ot_ui.lightLabel1, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ot_ui.lightLabel2, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ot_ui.lightLabel3, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ot_ui.lightLabel4, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ot_ui.lightLabel5, "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.ot_ui.lightLabel6, "QLabel")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light1Decrement, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light1Increment, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light2Decrement, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light2Increment, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light3Decrement, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light3Increment, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light4Decrement, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.ot_ui.light4Increment, "QToolButton")

        '''
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light1Decrement)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light1Increment)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light2Decrement)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light2Increment)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light3Decrement)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light3Increment)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light4Decrement)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.ot_ui.light4Increment)

        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ot_ui.lightBulb1)
        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ot_ui.lightBulb2)
        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ot_ui.otLightBulb1)
        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ot_ui.lightBulb3)
        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ot_ui.lightBulb4)
        self.ui.alldisplayColorChangeObj.changePixmapColor(self.ui.ot_ui.otLightBulb2)'''
        # -------------------------- history menu data text color change ---------------------------

        self.ui.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.ui.shutDialog)
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.shutDownButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.rebootButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.cancelShutButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.logoutButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.login_ui.loginButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.ui.loginDialogQtWidget)
        self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.setTimerWidget)
        #  self.shutDialog.setStyleSheet("background-color: " + self.dataModel.get_theme_color() + ";")

        # self.ui.allChangeToolButtonAttributeColor(self.ui.alldisplayColorChangeObj)

        # -------------------------- Multimedia Menu Color & Font Settings -------------------------
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.fullScreenButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.colorButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.openButton, "QPushButton")

        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.stopButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.playButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.stopButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.nextButton, "QToolButton")

        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.player.controls.stopButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.player.controls.playButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.player.controls.nextButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.player.controls.previousButton)
        self.ui.alldisplayColorChangeObj.changeIconColor(self.ui.player.controls.muteButton)
        '''# ----------------culprit below------------------------------------------------------------------------
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.previousButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.muteButton, "QToolButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.rateBox, "QComboBox")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.player.controls.volumeSlider, "QSlider")
        # self.alldisplayColorChangeObj.changePlayerAttributeColor(AutoCloseMessageBox())
        # self.ui.alldisplayColorChangeObj.changePlayerAttributeColor(self.ui.player) # 8 timer

        self.ui.alldisplayColorChangeObj.changeTableViewAttributeColor(self.ui.tableWidget, "QTableView")  # 1 timer
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.iconColor,
                                                          "QPushButton") # 2 timer
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.comboBoxTheme,
                                                          "QComboBox") # 2 timer

        self.ui.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.ui.SettingsQDialog)# 8 timer problem
        # ----------------culprit Up------------------------------------------------------------------------'''

        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.buttonApplyGeneral,
                                                              "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.applyColor,
                                                              "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.buttonApplyBackGroundImage,
                                                              "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.buttonApplyLogo,
                                                              "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.buttonPowerOnScreenImage,
                                                              "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.buttonApplyTheme,
                                                              "QPushButton")

        # ---------------------------------------------------------
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.chooseLogo,
                                                              "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.choosePowerOnScreenImage,
                                                              "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.chooseBackGroundImage,
                                                              "QPushButton")

        # =============================== Settings Dialog ==================================================
        '''self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.light1,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.light2,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.light3,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.light4,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.light5,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.light6,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.gasNameEdit1,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.gasNameEdit2,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.gasNameEdit3,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.gasNameEdit4,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.gasNameEdit5,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.gasNameEdit6,
                                                                      "QTextEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.gasNameEdit7,
                                                                      "QTextEdit")'''

        # ====================== Login UI ==========================================================================
        '''self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.login_ui.user_name,
                                                                      "QLineEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.login_ui.user_pass,
                                                                      "QLineEdit")'''
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLight1,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLight2,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLight3,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLight4,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLight5,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLight6,
                                                                     "QLabel")

        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxLight1,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxLight2,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxLight3,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxLight4,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxLight5,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxLight6,
                                                                     "QCheckBox")

        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxDim1,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxDim2,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxDim3,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxDim4,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxGas1,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxGas2,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxGas3,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxGas4,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxGas5,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxGas6,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.checkBoxGas7,
                                                                     "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(
            self.ui.settings_dialog_set_ui.checkBoxDifferentialPressure,
            "QCheckBox")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelBorderColor,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(
            self.ui.settings_dialog_set_ui.labelBackGroundColor,
            "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelTextColor,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelIconColor,
                                                                     "QLabel")

        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelTheme,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(
            self.ui.settings_dialog_set_ui.labelBackGroundImage,
            "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLogo,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelPowerOnImage,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLightTitle,
                                                                     "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelGasAlarmTitle,
                                                                     "QLabel")

        # ======================= Login UI ==========================================================================
        self.ui.modifyGlobalVariablesObj.setChangedImage()
        self.ui.modifyGlobalVariablesObj.setChangedLightColor()
        # self.ui.lightBrightnessObject.allLightBarInitialSetup(self.ui.ot_ui)
        '''self.ui.lightBrightnessObject.otLightBrightIncrementControl()
        self.ui.lightBrightnessObject.otLightBrightDecrementControl()
        self.ui.lightBrightnessObject.otLightBrightIncrementControl2()
        self.ui.lightBrightnessObject.otLightBrightDecrementControl2()
        self.ui.lightBrightnessObject.otLightBrightIncrementControl3()
        self.ui.lightBrightnessObject.otLightBrightDecrementControl3()
        self.ui.lightBrightnessObject.otLightBrightIncrementControl4()
        self.ui.lightBrightnessObject.otLightBrightDecrementControl4()'''

        self.signal.return_signal.emit(result)


class CloneThread(QThread):
    signal = pyqtSignal()

    # signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.git_url = ""
        self.ui = None
        self.database = None
        self.datamodel = None
        self.allObj = None

    # run method gets called when we start the thread
    def run(self):
        # self.database_manage = database.DataBaseManagement()
        # self.database_manage.init('datafile', 'QSQLITE')
        # self.database_manage.updateIconColorSettings(self.datamodel)
        # self.ui.queryIconColorSettingsMain(self.datamodel, self.database_manage)
        # self.finished()
        self.ui.allChangeToolButtonAttributeColor(self.allObj)
        # while 1:
        # time.sleep(2)
        # self.exit(1)

        self.signal.emit()
        # return self


class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    def ventilationOpen(self):
        self.clear()
        self.ui.menuTitleName.setText("Ventilation")
        self.layout.addWidget(self.ventilationWidget)
        self.hisForm.hide()
        self.ventilationWidget.show()
        self.otForm.hide()
        self.mulFormWindo.hide()
        # self.mulForm.hide()
        self.gasForm.hide()

    def AddOtLighteningWidget(self):
        self.clear()
        self.ui.menuTitleName.setText("Lightening")
        self.layout.addWidget(self.otForm)
        self.hisForm.hide()
        self.otForm.show()
        self.mulFormWindo.hide()
        self.ventilationWidget.hide()
        # self.mulForm.hide()
        self.gasForm.hide()

    def additionalChronosWidget(self):
        self.clear()
        self.ui.menuTitleName.setText("Chronos")
        self.layout.addWidget(self.additionChronos)
        self.additionChronos.show()
        self.hisForm.hide()
        self.otForm.hide()
        self.mulFormWindo.hide()
        self.ventilationWidget.hide()
        # self.mulForm.hide()
        self.gasForm.hide()
        self.player.hide()

    def multimediaPlayer(self):
        self.clear()
        self.ui.menuTitleName.setText("Multimedia")
        self.layout.addWidget(self.player)
        '''
        self.multiMedia_ui.setupUi(self.mulForm)
        self.layout.addWidget(self.mulForm)'''
        '''
        self.multiMediaThread = MultiMediaThread(self.player)

        self.threadpool.start(self.multiMediaThread)'''

        self.player.show()
        self.hisForm.hide()
        self.otForm.hide()
        self.mulFormWindo.hide()
        self.ventilationWidget.hide()
        # self.mulForm.hide()
        self.gasForm.hide()

    def AddHistoryWidget(self):
        self.clear()
        self.ui.menuTitleName.setText("Alarm History")
        self.createTable()
        # self.layout = QVBoxLayout()

        # self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.hisForm)
        self.hisForm.show()
        self.otForm.hide()
        self.ventilationWidget.hide()
        self.mulFormWindo.hide()
        # self.mulForm.hide()
        self.gasForm.hide()

        # Create table

    def createTable(self):
        # self.tableWidget = QTableWidget()
        # Row count
        # self.tableWidget.setRowCount(4)
        # Column count
        # self.tableWidget.setColumnCount(2)

        '''self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("City"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Aloysius"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Indore"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Alan"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Bhopal"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Arnavi"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Mandsaur"))'''
        self.projectModel = QSqlQueryModel()
        self.projectModel.setQuery(self.database_manage.queryofhistorydata())
        # projectView = QTableView()
        self.projectModel.setHeaderData(1, Qt.Horizontal, 'Date')
        self.projectModel.setHeaderData(2, Qt.Horizontal, 'Alarm')
        # self.tableWidget.setStyleSheet("color:red")
        self.tableWidget.setModel(self.projectModel)
        self.tableWidget.setColumnHidden(0, True)

        # projectView.show()

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    def AddGasWidget(self):
        self.clear()
        self.ui.menuTitleName.setText("Gas Alarm")
        # self.gas_ui.setupUi(self.gasForm)
        self.layout.addWidget(self.gasForm)
        self.gasForm.show()
        self.otForm.hide()
        self.mulFormWindo.hide()
        # self.mulForm.hide()
        self.hisForm.hide()

    def showTemperatureGraph(self):
        self.clear()
        self.ui.menuTitleName.setText("Temperature Graph")
        self.temp_ui.setupUi(self.tempForm)
        self.layout.addWidget(self.tempForm)
        self.tempForm.plot(self.hour, self.temperature)
        self.gasForm.hide()
        self.otForm.hide()
        self.mulFormWindo.hide()
        # self.mulForm.hide()
        self.hisForm.hide()

    def showHumidityGraph(self):
        self.clear()
        self.ui.menuTitleName.setText("Humidity Graph")
        self.hum_ui.setupUi(self.humidityForm)
        self.layout.addWidget(self.humidityForm)
        self.humidityForm.plot(self.hour, self.humidity)
        self.gasForm.hide()
        self.otForm.hide()
        self.mulFormWindo.hide()
        # self.mulForm.hide()
        self.hisForm.hide()
        # self.unfill()

    def setLayout(self, layout):
        self.clearLayout(layout)
        QWidget.setLayout(self, layout)

    def clear(self):
        for i in reversed(range(self.layout.count())):
            widgetToRemove = self.layout.itemAt(i).widget()
            print("Mojank: " + str(i))
            # remove it from the layout list
            self.layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

    def clearAll(self):
        print("Object: " + self.layout.objectName())
        for i in reversed(range(self.layout.count())):
            self.layout.takeAt(i).widget().deleteLater()

    '''
    @staticmethod
    def clearLayout(layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()'''

    def clearLayout(self, layout):
        print("-- -- input layout: " + str(layout))
        for i in reversed(range(self.layout.count())):
            layoutItem = layout.itemAt(i)
            if layoutItem.widget() is not None:
                widgetToRemove = layoutItem.widget()
                print("found widget: " + str(widgetToRemove))
                widgetToRemove.setParent(None)
                layout.removeWidget(widgetToRemove)
            elif layoutItem.spacerItem() is not None:
                print("found spacer: " + str(layoutItem.spacerItem()))
            else:
                layoutToRemove = layout.itemAt(i)
                print("-- found Layout: " + str(layoutToRemove))
                self.clearLayout(layoutToRemove)

    @staticmethod
    def deleteItemsOfLayout(layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    layout.deleteItemsOfLayout(item.layout())

    '''
    @staticmethod
    def clearLayout(layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    layout.clearLayout(child.layout())
    '''

    def clearvbox(self, L=False):
        if not L:
            L = self.layout
        if L is not None:
            while L.count():
                item = L.takeAt(0)

                widget = item.widget()

                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearvbox(item.layout())

    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = mainwindow_auto.Ui_MainWindow()
        self.ui.setupUi(self)  # gets defined in the UI file
        # self.setStyleSheet("background-color: yellow;")
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        # self.viewer = QMainWindow()
        # =======================Temperature Graph======================================================================
        self.hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.humidity = [66, 73, 74, 79, 74, 73, 60, 71, 82, 85]
        '''
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y values
        self.graphWidget.plot(self.hour, self.temperature)'''
        # ============================ icon and label color settings ===================================================

        # ============================ end icon and label color settings ===============================================
        # ==============To create new widget============================================================================

        # =======================Temperature Graph======================================================================
        self.hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        '''
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y values
        self.graphWidget.plot(self.hour, self.temperature)'''
        # ==============To create new widget============================================================================
        # self.hisForm = QtWidgets.QWidget()
        self.mulForm = QtWidgets.QWidget()
        self.otForm = QtWidgets.QWidget()
        self.gasForm = QtWidgets.QWidget()
        self.tempForm = pg.PlotWidget()
        self.humidityForm = pg.PlotWidget()
        self.mulFormWindo = QMainWindow()
        self.toggleButtonForm = QtWidgets.QWidget()
        self.uiSecond = Ui_Form()
        self.multiMedia_ui = MultiMedia_Ui()

        self.ot_ui = Ot_Ui()
        self.gas_ui = Gas_Ui()
        self.temp_ui = Temp_Ui()
        self.hum_ui = Hum_Ui()
        self.multi_ui_media_player = Multi_Ui_Media()
        # self.timer_ui = TimerWidget()
        self.timer_set_ui = Ui_setTimer()
        self.clock_set_ui = Ui_setClockTime()
        self.setClockWidget = QtWidgets.QDialog()
        self.setTimerWidget = QtWidgets.QDialog()
        self.clock_set_ui.setupUi(self.setClockWidget)
        self.timer_set_ui.setupUi(self.setTimerWidget)
        self.gas_ui.setupUi(self.gasForm)

        # ================Start of settings button UI ==========================================
        self.settings_dialog_set_ui = Ui_SettingsQDialog()
        self.SettingsQDialog = QtWidgets.QDialog()
        self.settings_dialog_set_ui.setupUi(self.SettingsQDialog)

        # self.settings_dialog_set_ui.tab_7.setEnabled(False)
        # ----------------------___Start Login Dialog -----------------------------------------
        self.login_ui = Ui_loginDialog()
        self.loginDialogQtWidget = QtWidgets.QDialog()
        self.login_ui.setupUi(self.loginDialogQtWidget)
        self.loginDialogQtWidget.setWindowFlags(Qt.Dialog)
        # ==============================Start of Power Button====================================================
        self.shutDown_ui = Ui_shutDownDialog()
        self.shutDialog = QtWidgets.QDialog()
        self.shutDown_ui.setupUi(self.shutDialog)
        self.ui.powerButton.clicked.connect(self.shutdownManagement)
        self.shutDown_ui.shutDownButton.clicked.connect(self.shutDown)
        self.shutDown_ui.rebootButton.clicked.connect(self.reBoot)
        self.shutDown_ui.logoutButton.clicked.connect(self.suspend)
        self.shutDown_ui.cancelShutButton.clicked.connect(self.exitShutDownDialog)
        # ==============================End of Power Button============================================================

        self.labelNameFormWidget = QtWidgets.QWidget()
        self.label_ui_name_change = Ui_changeLabelName()
        self.label_ui_name_change.setupUi(self.labelNameFormWidget)
        # =====================================End Central Change Label Name ===========================================

        # ======================================Temperature and Humidity increment and decrement =======================
        self.t_i_d_count = 0
        self.hex_add_temp = 0
        self.hex_minus_temp = 0
        self.hex_add_humidity = 0
        self.hex_minus_humidity = 0
        self.ui.downTemperatureButton.pressed.connect(self.decrementTemperature)
        self.ui.upTemperatureButton.pressed.connect(self.incrementTemperature)
        self.ui.downTemperatureButton.setAutoRepeat(True)
        self.ui.upTemperatureButton.setAutoRepeat(True)

        self.h_i_d_count = 0
        self.ui.downHumidityButton.pressed.connect(self.decrementHumidity)
        self.ui.upHumidityButton.pressed.connect(self.incrementHumidity)
        self.ui.downHumidityButton.setAutoRepeat(True)
        self.ui.upHumidityButton.setAutoRepeat(True)

        self.tempDisplayLabel()
        self.humidityDisplayLabel()

        # self.ui.downTemperatureButton.triggered.connect(self.decrementTemperature)
        # ======================================End temperature and humidity increment and decrement ===================

        '''=============================================================================================================
              Telephone system
        ============================================================================================================='''
        self.telephone_ui = Ui_telephonePad()
        self.telephoneQtWidget = QtWidgets.QDialog()
        self.telephone_ui.setupUi(self.telephoneQtWidget)
        '''self.telephone_ui.lcdNumber.append("example")
        cursor = self.telephone_ui.lcdNumber.textCursor()
        textBlockFormat = cursor.blockFormat()
        textBlockFormat.setAlignment(Qt.AlignRight)
        cursor.mergeBlockFormat(textBlockFormat)
        self.telephone_ui.lcdNumber.setTextCursor(cursor)'''
        self.ui.phoneCallingButton.clicked.connect(self.telephoneDialogOpen)
        # =============================== Start Ventilation ==================================================================
        self.ventilationWidget = QtWidgets.QWidget()
        self.ventilation_ui = Ui_ventilationDetails()
        self.ventilation_ui.setupUi(self.ventilationWidget)
        self.ui.ventiLationDetails.clicked.connect(self.ventilationOpen)
        # =============================== End Ventilation ====================================================================
        '''
        self.viewer = ViewerWindow(self)
        # =====================To Hide  Close Button ===================================================================
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480, 360))
        self.viewer.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)'''
        # ==============================================================================================================

        # Hooks to for buttons
        # self.ui.btnOn.clicked.connect(lambda: self.pressedOnButton())
        # self.ui.btnOff.clicked.connect(lambda: self.AddFormWidget())
        self.num = 3

        self.layout = QtWidgets.QVBoxLayout(self.ui.centralwidget)
        # =======================Toggle Button ==================================================
        self.ot_ui.setupUi(self.otForm)
        # =========================Toggle Switch ===========================
        # ====================== Gas Color Changes using RX TX =========================================================
        # self.threadpoolRXTX = QThreadPool()
        threadRXTX = ThreadGasColorRXTX(self)
        #threadRXTX.signal.return_signal.connect(threadRXTX.function_thread)
        #self.threadpoolRXTX.start(threadRXTX)

        # ======================

        self.threadPoolSwitch = QThreadPool()
        self.serialWrapper = SerialWrapper('/dev/ttyUSB0', threadRXTX, self.threadpoolRXTX)
        print("starting...")
        self.rt = RepeatedTimer(1, self.serialWrapper.sendDataToSerialPort)  # it auto-starts, no need of rt.start()
        self.serialWrapper.setRepeater(self.rt)
        '''try:
            time.sleep(1)  # your long-running job goes here...
        finally:
            rt.stop()  # better in a try/finally block to make sure the program ends!'''

        self.add_sub_hex = 0
        self.switchContainer = QtWidgets.QVBoxLayout(self.ot_ui.toggleContainer)
        self.toggleSwitch = toggleButton.Switch(self.toggleButtonForm)
        self.toggleSwitch.setStyleSheet("background-color : #4c4c4c")
        self.switchContainer.addWidget(self.toggleSwitch)

        self.toggleSwitch.clicked.connect(self.startThreadSwitch4)

        self.switchContainerLaminar = QtWidgets.QVBoxLayout(self.ot_ui.toggleContainerLaminar)
        self.toggleSwitchLaminar = toggleButton.Switch(self.toggleButtonForm)
        self.toggleSwitchLaminar.setStyleSheet("background-color : #4c4c4c")
        self.switchContainerLaminar.addWidget(self.toggleSwitchLaminar)
        self.toggleSwitchLaminar.clicked.connect(self.startThreadSwitch5)

        self.switchContainerGasL1 = QtWidgets.QVBoxLayout(self.ot_ui.toggleContainerGasL1)
        self.toggleSwitchGasL1 = toggleButton.Switch(self.toggleButtonForm)
        self.toggleSwitchGasL1.setStyleSheet("background-color : #4c4c4c")
        self.switchContainerGasL1.addWidget(self.toggleSwitchGasL1)
        self.toggleSwitchGasL1.clicked.connect(self.startThreadSwitch1)

        self.switchContainerGasL2 = QtWidgets.QVBoxLayout(self.ot_ui.toggleContainerGasL2)
        self.toggleSwitchGasL2 = toggleButton.Switch(self.toggleButtonForm)
        self.toggleSwitchGasL2.setStyleSheet("background-color : #4c4c4c")
        self.switchContainerGasL2.addWidget(self.toggleSwitchGasL2)
        self.toggleSwitchGasL2.clicked.connect(self.startThreadSwitch2)

        self.switchContainerOT1 = QtWidgets.QVBoxLayout(self.ot_ui.toggleContainerOT1)
        self.toggleSwitchOT1 = toggleButton.Switch(self.toggleButtonForm)
        self.toggleSwitchOT1.setStyleSheet("background-color : #4c4c4c")
        self.switchContainerOT1.addWidget(self.toggleSwitchOT1)
        self.toggleSwitchOT1.clicked.connect(self.startThreadSwitch3)

        self.switchContainerOT2 = QtWidgets.QVBoxLayout(self.ot_ui.toggleContainerOT2)
        self.toggleSwitchOT2 = toggleButton.Switch(self.toggleButtonForm)
        self.toggleSwitchOT2.setStyleSheet("background-color : #4c4c4c")
        self.switchContainerOT2.addWidget(self.toggleSwitchOT2)
        self.toggleSwitchOT2.clicked.connect(self.startThreadSwitch6)

        # =========================End Toggle Switch ============================================

        # ==========Hooks for all Menu Item=========================================================================
        self.ui.otLighteningDetails.clicked.connect(self.AddOtLighteningWidget)
        self.ui.historyDetails.clicked.connect(self.AddHistoryWidget)
        self.ui.gasIndicator.clicked.connect(self.AddGasWidget)
        self.ui.temeratureGraph.clicked.connect(self.showTemperatureGraph)
        self.ui.humidityGraph.clicked.connect(self.showHumidityGraph)

        # ======================== Start Additional Chronos ========================================================
        self.additionChronos = QtWidgets.QWidget()
        self.additionChronos_ui = AdditionalChronos_Ui()
        self.additionChronos_ui.setupUi(self.additionChronos)
        self.ui.addAdditonalChronosButton.clicked.connect(self.additionalChronosWidget)

        # ======================== End Additional Chronos ==========================================================

        # ============================== Start of History details of data =============================================
        self.hisForm = QtWidgets.QWidget()
        self.history_ui = historydetailsofdata_ui()
        self.history_ui.setupUi(self.hisForm)
        self.tableWidget = QTableView()
        self.history_ui.historyhVerticalLayout.addWidget(self.tableWidget)

        # ============================== End of History details of data ===============================================
        # ========================Start of Database Management===============================================
        self.dataModel = DataModel()
        self.database_manage = database.DataBaseManagement()
        self.database_manage.init('datafile', 'QSQLITE')
        self.database_manage.queryThemeColorSettings(self.dataModel)
        self.queryGeneralSettingsDataAndSet()
        self.queryAppearanceSettingsDataAndSet(self.dataModel)
        self.populateThemeCombo()
        self.backgroundImagePath = str()
        self.logoImagePath = str()
        self.powerOnImagePath = str()
        self.themeColor_hex = str()
        self.themeColor_name = str()

        self.settings_dialog_set_ui.buttonApplyGeneral.clicked.connect(self.updateLabelName)
        self.settings_dialog_set_ui.chooseBackGroundImage.clicked.connect(self.selectBackgroundImageOpen)
        self.settings_dialog_set_ui.chooseLogo.clicked.connect(self.selectLogoImageOpen)
        self.settings_dialog_set_ui.choosePowerOnScreenImage.clicked.connect(self.selectPowerOnImageOpen)
        self.settings_dialog_set_ui.buttonApplyBackGroundImage.clicked.connect(self.updateBackgroundImage)
        self.settings_dialog_set_ui.buttonApplyLogo.clicked.connect(self.updateLogoImage)
        self.settings_dialog_set_ui.buttonApplyTheme.clicked.connect(self.updateThemeColor)
        self.settings_dialog_set_ui.buttonPowerOnScreenImage.clicked.connect(self.updatePowerOnImage)
        self.settings_dialog_set_ui.disableBackGroundImage.clicked.connect(self.disableBackGroundImage)
        self.settings_dialog_set_ui.enableBackGroundImage.clicked.connect(self.enableBackGroundImage)
        self.settings_dialog_set_ui.disableLogo.clicked.connect(self.disableLogo)
        self.settings_dialog_set_ui.enableLogo.clicked.connect(self.enableLogo)

        # ========================End of Database Management======================================================
        # ========================Icon Color Update =============================================================
        self.SettingsQDialog.closeEvent = self.CloseEvent

        self.IconColorControlObj = ToolButtonColorControl(self.settings_dialog_set_ui.iconColor, self.dataModel,
                                                          'icon_color')
        self.colorCborderColor = ToolButtonColorControl(self.settings_dialog_set_ui.borderColor, self.dataModel,
                                                        'border_color')
        self.colorCtextColor = ToolButtonColorControl(self.settings_dialog_set_ui.textColor, self.dataModel,
                                                      'text_color')
        self.colorCbackgroundColor = ToolButtonColorControl(self.settings_dialog_set_ui.backgroundColor, self.dataModel,
                                                            'background_color')
        self.settings_dialog_set_ui.borderColor.clicked.connect(self.colorCborderColor.processButton_DMX)
        self.settings_dialog_set_ui.textColor.clicked.connect(self.colorCtextColor.processButton_DMX)
        self.settings_dialog_set_ui.backgroundColor.clicked.connect(self.colorCbackgroundColor.processButton_DMX)
        self.settings_dialog_set_ui.iconColor.clicked.connect(self.IconColorControlObj.processButton_DMX)
        self.settings_dialog_set_ui.iconColor.icon().name()
        print("Icon Name:" + str(QtGui.QImage(
            self.settings_dialog_set_ui.iconColor.icon().pixmap(self.settings_dialog_set_ui.iconColor.iconSize()))))
        self.queryIconColorSettingsMain(self.dataModel, self.database_manage)
        self.alldisplayColorChangeObj = AllDisplayAttributeColor(self.dataModel)
        self.modifyGlobalVariablesObj = modifyGlobalVariables.ModifyGlobalVariables(self.alldisplayColorChangeObj,
                                                                                    self.ot_ui, self.dataModel)

        # --------------------------- Start Multimedia Player ------------------------------------------------------
        self.lastTime = ''
        self.lastDate = ''
        self.lastTimeHwclock = ''
        self.lastDateHwclock = ''
        self.changeTime = ''
        self.changeDate = ''
        self.int_count = False
        self.startThread1()
        self.setClockWidget.closeEvent = self.CloseEvent
        self.ui.setTimeSetting.clicked.connect(self.setClockDialog)
        self.clock_set_ui.timeEdit.timeChanged.connect(self.timeChange)
        self.clock_set_ui.dateEdit.dateChanged.connect(self.dateChange)
        self.clock_set_ui.buttonClockBox.accepted.connect(self.setClockOk)
        self.clock_set_ui.buttonClockBox.rejected.connect(self.rejectClock)
        #  print(pytz.all_timezones_set)
        # ------------------------------Start Stop Watch ------------------------------------
        self.dataCaptureThread = CounterThread(self.ui, self.alldisplayColorChangeObj)
        self.dataCaptureThread.start()

        # self.dateTimeShowThread = ShowTimeDateThread(self.ui, self.setClockWidget, self.dataModel, self.clock_set_ui)
        # self.dateTimeShowThread.start()

        self.timerCounterThread = TimerCounterThread(self.ui, self.timer_set_ui, self.alldisplayColorChangeObj,
                                                     self.dataModel, self.setTimerWidget)
        self.timerCounterThread.start()
        # -----------------------------End Stop Watch ---------------------------------------
        import sys
        self.player = Player(sys.argv[1:])
        self.ui.multiMediaDetails.clicked.connect(self.multimediaPlayer)
        # ---------------------------End Multimedia ----------------------------------------------------------------
        self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)

        #  ---------------------------------  Parallel ThreadClass Run UI Initial Setup  ---------------------------

        self.threadpool1 = QThreadPool()
        threadParallel = ThreadParallel(self)
        threadParallel.signal.return_signal.connect(threadParallel.function_thread)
        self.threadpool1.start(threadParallel)

        # self.threadpool2 = QThreadPool()
        # self.rtcThread = RTCThread(self)
        # self.rtcThread.signal.return_signal.connect(self.rtcThread.function_thread)
        # self.threadpool2.start(self.rtcThread)
        # self.result = subprocess.call(
        #   'echo pass | sudo hwclock -r',
        #    shell=True)
        # self.ui.day_date_show.setText(os.system('hwclock -r'))
        # --------------------------------- Parallel ThreadClass Run ---------------------------------------------------

        self.git_thread = CloneThread()  # This is the thread object
        # self.settings_dialog_set_ui.applyColor.clicked.connect(self.colorPushButton)  #
        # self.settings_dialog_set_ui.applyColor.clicked.connect(self.git_clone)
        self.settings_dialog_set_ui.applyColor.clicked.connect(self.clickCheckbox)

        # Connect the signal from the thread to the finished method
        self.git_thread.signal.connect(self.finished)
        # self.timer.moveToThread(self.thread)
        # self.timer_count_down.moveToThread(self.thread)
        # ---------------------------------- Additional Chronos ------------------------------------------------
        # self.chronosObject2 = chronos23.Chronos(self.additionChronos_ui.startChrono2,
        #                                     self.additionChronos_ui.resetChrono2, self.additionChronos_ui.chronos3)
        self.chronosObject2 = chronos2.Chronos2(self.additionChronos_ui, configVariables.play_changed_image,
                                                configVariables.pause_changed_image)
        self.chronosObject3 = chronos3.Chronos3(self.additionChronos_ui, configVariables.play_changed_image,
                                                configVariables.pause_changed_image)

        # --------------------------------------------------------------------------------------------------------------
        self.settings_dialog_set_ui.comboBoxTheme.activated.connect(self.handleActivated)
        self.applyThemeColor()
        self.applyBackGroundImage()
        self.applyLogoImage()
        self.makeBackTransparent()
        self.fontColorChangesName()
        self.s1 = threading.Thread(target=self.toggleSwitchColor)
        self.s1.daemon = True
        self.s1.start()
        self.s1.join()
        # self.toggleSwitchColor()
        self.s2 = threading.Thread(target=self.toggleSwitchLaminarColor)
        self.s2.daemon = True
        self.s2.start()
        self.s2.join()
        # self.toggleSwitchLaminarColor()
        self.s3 = threading.Thread(target=self.toggleSwitchGasL1Color)
        self.s3.daemon = True
        self.s3.start()
        self.s3.join()
        # self.toggleSwitchGasL1Color()
        self.s4 = threading.Thread(target=self.toggleSwitchGasL2Color)
        self.s4.daemon = True
        self.s4.start()
        self.s4.join()
        # self.toggleSwitchGasL2Color()
        self.s5 = threading.Thread(target=self.toggleSwitchOT1Color)
        self.s5.daemon = True
        self.s5.start()
        self.s5.join()
        # self.toggleSwitchOT1Color()
        self.s6 = threading.Thread(target=self.toggleSwitchOT2Color)
        self.s6.daemon = True
        self.s6.start()
        self.s6.join()
        # self.toggleSwitchOT2Color()

        # ========================Start light Dimming===============================================================
        self.lightBrightnessObject = lightBrightness.Brightness(self.ot_ui, self.dataModel)
        self.ot_ui.light1Increment.clicked.connect(self.lightBrightnessObject.otLightBrightIncrementControl)
        self.ot_ui.light1Decrement.clicked.connect(self.lightBrightnessObject.otLightBrightDecrementControl)
        self.ot_ui.light2Increment.clicked.connect(self.lightBrightnessObject.otLightBrightIncrementControl2)
        self.ot_ui.light2Decrement.clicked.connect(self.lightBrightnessObject.otLightBrightDecrementControl2)
        self.ot_ui.light3Increment.clicked.connect(self.lightBrightnessObject.otLightBrightIncrementControl3)
        self.ot_ui.light3Decrement.clicked.connect(self.lightBrightnessObject.otLightBrightDecrementControl3)
        self.ot_ui.light4Increment.clicked.connect(self.lightBrightnessObject.otLightBrightIncrementControl4)
        self.ot_ui.light4Decrement.clicked.connect(self.lightBrightnessObject.otLightBrightDecrementControl4)

        # ========================END Light Dimming=====================================================================

        self.mousePressSignal = pyqtSignal()

        # ==============================End Pop Up Keyboard======================================================
        # ===================================== Start of Login with keyboard =========================================================

        # self.loginDataModel = DataModel()
        self.userNameLineEdit = login_virtual_keyboard.cQLineEdit(self.login_ui.user_name, '', self.dataModel,
                                                                  "user_name")
        self.userPassLineEdit = login_virtual_keyboard.cQLineEdit(self.login_ui.user_pass, '', self.dataModel,
                                                                  "user_pass")
        # self.userPassLineEdit.setEchoMode(True)
        self.ui.settingsButton.clicked.connect(self.loginDialogOpen)
        self.login_ui.loginButton.clicked.connect(self.check_password)

        # ===================================== End of Login ===========================================================

    def setClockOk(self):
        subprocess.call(
            "sudo hwclock --set --date '" + str(self.changeDate) + " " + str(self.changeTime) + "'",
            shell=True)
        self.int_count = False

    def rejectClock(self):
        self.int_count = False

    def timeChange(self):
        print("Change Time: " + self.clock_set_ui.timeEdit.time().toString())
        self.changeTime = self.clock_set_ui.timeEdit.time().toString()

    def dateChange(self):
        print("Change Date: " + self.clock_set_ui.dateEdit.date().toString('MM/dd/yyyy'))
        self.changeDate = self.clock_set_ui.dateEdit.date().toString()

    def setClockDialog(self):
        self.int_count = True
        self.setClockWidget.setStyleSheet(
            "color:" + self.dataModel.get_text_col() + ";background-color:" + self.dataModel.get_theme_color() + ";")
        # current_time = QTime.currentTime()
        # self.clock_set_ui.timeEdit.setTime(current_time)
        self.clock_set_ui.timeEdit.setDisplayFormat("H:mm:ss")
        self.clock_set_ui.dateEdit.setDisplayFormat("dd/MM/yyyy")

        self.clock_set_ui.dateEdit.setDate(self.lastDate)
        self.clock_set_ui.timeEdit.setTime(self.lastTime)
        if self.ui.setTimeSetting.isChecked():
            # self.clock_set_ui.dateEdit.setDate(date)
            self.setClockWidget.show()
        else:
            self.setClockWidget.hide()
        self.setClockWidget.exec_()

    def startThread1(self):
        self.t1 = threading.Thread(target=self.loop1)
        self.t1.daemon = True
        self.t1.start()

    def loop1(self):
        while True:
            if self.int_count:
                pass
            else:
                # self.result = subprocess.call(
                # 'echo vishnu | sudo hwclock -r',
                # shell=True)
                print("INT_COUNT:" + str(self.int_count))
                # proc = subprocess.call('sudo hwclock -r', shell=True, stdout=subprocess.PIPE)

                proc = subprocess.getoutput('echo vishnu | sudo hwclock -r')
                # subprocess.call(shlex.split("sudo hwclock -r"))
                # list_result = self.insert_dash(proc, 10)
                # list_result = re.split(list_result, )

                try:
                    date_time_str = proc
                    # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
                    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f%z')
                    '''print('Date:', date_time_obj.date())
                    print('Time:', date_time_obj.time())
                    print('Date-time:', date_time_obj)'''
                    self.lastTime = date_time_obj.time()
                    self.lastDate = date_time_obj.date()
                    '''if self.ui.setTimeSetting.isChecked():
                        self.clock_set_ui.timeEdit.setTime(date_time_obj.time())'''
                    time_split = re.split(':', str(date_time_obj.time()))
                    self.ui.day_date_show.setText(str(date_time_obj.date().strftime('%d/%m/%Y')))
                    second = time_split[2].split('.', 1)[0]
                    self.ui.time_show.setText(
                        time_split[0] + ":" + time_split[1] + "" + "<b><font font size=12pt font weight:40>" +
                        ":" + "</font>" + "<b>< font size=12pt font weight:40>" +
                        second + "</font>")
                    self.lastTimeHwclock = time_split[0] + ":" + time_split[1] + ":" + second
                    '''splitted_string = re.split('\s+', proc)
                    time_split = re.split(':', splitted_string[1])
                    second = time_split[2].split('.', 1)[0]
                    self.ui.day_date_show.setText(splitted_string[0])
                    self.clock_set_ui.timeEdit.setTime(time_split[0] + ":" + time_split[1]+":"+second)
                    self.ui.time_show.setText(
                        time_split[0] + ":" + time_split[1] + "" + "<b><font font size=12pt font weight:40>" +
                        ":" + "</font>" + "<b>< font size=12pt font weight:40>" +
                        second + "</font>")'''
                except IndexError:
                    second = 'Please Connect rtc.'
                    print(second)
            # self.int_count = False
            # print(proc)
            # time.sleep(1)

    def insert_dash(self, string, index):
        return string[:index] + '-' + string[index:]

    def CloseEvent(self, event):
        self.int_count = False
        print("X is clicked")

    # ===============Start Color and Font =======================================================
    '''def threadFunctionForChanges(self):
        worker = mt.Worker(self.colorPushButton)  # Any other args, kwargs are passed to the run function
        # worker.signals.result.connect(self.print_output)
        # worker.signals.finished.connect(self.thread_complete)
        # worker.signals.progress.connect(self.progress_fn)
        # Execute
        self.threadpool.start(worker)'''

    def sleep5sec(self):
        self.settings_dialog_set_ui.applyColor.setEnabled(False)

    def clickCheckbox(self):
        self.sleep5sec()

        thread = Thread(self)
        thread.signal.return_signal.connect(self.function_thread)
        self.threadpool.start(thread)
        self.database_manage.updateIconColorSettings(self.dataModel)
        self.queryIconColorSettingsMain(self.dataModel, self.database_manage)
        # ----------------culprit below------------------------------------------------------------------------
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.previousButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.muteButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.rateBox, "QComboBox")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.volumeSlider, "QSlider")
        # self.alldisplayColorChangeObj.changePlayerAttributeColor(AutoCloseMessageBox())
        self.alldisplayColorChangeObj.changePlayerAttributeColor(self.player)  # 8 timer

        self.alldisplayColorChangeObj.changeTableViewAttributeColor(self.tableWidget, "QTableView")  # 1 timer
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.iconColor,
                                                           "QPushButton")  # 2 timer
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.comboBoxTheme,
                                                           "QComboBox")  # 2 timer

        self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)
        # self.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.shutDialog)
        # self.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.loginDialogQtWidget)
        # self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.setTimerWidget)
        # self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)  # 8 timer problem
        self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabWidget)
        # ---------------------New---------------------------------------------------------------------------
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabColor)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabGeneral)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabTheme)
        # ---------------------New---------------------------------------------------------------------------

        # =============================== Settings Dialog ==================================================
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light1,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light2,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light3,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light4,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light5,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light6,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit1,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit2,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit3,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit4,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit5,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit6,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit7,
                                                                   "QTextEdit")
        # =============================== Settings End =============================================================
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.login_ui.user_name,
                                                                   "QLineEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.login_ui.user_pass,
                                                                   "QLineEdit")
        # ----------------culprit Up------------------------------------------------------------------------

    def function_thread(self, signal):
        QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        # self.threadpool.destroyed()
        print(signal)

    def git_clone(self):
        self.git_thread.ui = self  # Get the git URL
        self.git_thread.database = self.database_manage
        self.git_thread.datamodel = self.dataModel
        self.git_thread.allObj = self.alldisplayColorChangeObj
        self.database_manage.updateIconColorSettings(self.dataModel)
        self.queryIconColorSettingsMain(self.dataModel, self.database_manage)
        # self.pushButton.setEnabled(False)  # Disables the pushButton
        # self.textEdit.setText("Started git clone operation.")  # Updates the UI
        self.git_thread.start()  # Finally starts the thread

    def finished(self):
        print("SErry")
        print(" Jusy " + str(self.git_thread.isFinished()))
        # self.git_thread.terminate()
        self.git_thread.finished()
        # self.git_thread.quit()
        # self.git_thread.exit()

    def colorPushButton(self):
        # self.dataModel = DataModel()
        self.database_manage.updateIconColorSettings(self.dataModel)
        self.queryIconColorSettingsMain(self.dataModel, self.database_manage)
        self.git_thread.start()
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)

    # ===============End Color and Font =========================================================
    def allChangeToolButtonAttributeColor(self, alldisplayColorChangeObj):
        ''' self.alldisplayColorChangeObj = alldisplayColorChangeObj
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.oxygen, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.ips, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.vacuum, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.cabonDiOxide, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.air7, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.air, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.nitrousOxide, "QToolButton") '''
        ''' # -----------------------Menu Tool Button ----------------------------------------------
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.otLighteningDetails, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.ventiLationDetails, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.gasIndicator, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.historyDetails, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.multiMediaDetails, "QToolButton")
        # --------------------------------Timer Control Color-------------------------------------------
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.start, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.reset, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.addAdditonalChronosButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.timerSet, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.startButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.resetButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.setTimeSetting, "QToolButton")
        # -------------------------------Miscellaneous---------------------------------------------------
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.powerButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.settingsButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.homeButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.phoneCallingButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.toolButton_9, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.upHumidityButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.downHumidityButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.upTemperatureButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.downTemperatureButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.temeratureGraph, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ui.humidityGraph, "QToolButton")
        # ------------------------------- Gas Label Color Changes ----------------------------------------
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.gas_ui.gasLabel_1, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.gas_ui.gasLabel_2, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.gas_ui.gasLabel_3, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.gas_ui.gasLabel_4, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.gas_ui.gasLabel_5, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.gas_ui.gasLabel_6, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_1_high, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_1_normal, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_1_low, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_2_high, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_2_normal, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_2_low, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_3_high, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_3_normal, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_3_low, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_4_high, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_4_normal, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_4_low, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_5_high, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_5_normal, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_5_low, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_6_normal, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.gas_ui.gasLabel_6_low, "QLabel")
        # ------------------------------- Label Color Changes --------------------------------------------
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.differentialLabel, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.hepaLabel, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.differentialPressureShow, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.hepaFilterStatus, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.tempLabelName, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.humidityLabelName, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.tempSetLabel, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.humiditySetLabel, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.tempSetShow, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.humiditySetShow, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.tempShow, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.humidityShow, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.anaesthesiaTimeLabel, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.elapsedTimeLabel, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.time_label, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ui.medicalGasLabelTitle, "QLabel")
        self.alldisplayColorChangeObj.changeDateTimeAttributeColor(self.ui.day_date_show, "QLabel")
        self.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.displayArea, "QLabel")
        self.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.lcd1, "QLabel")
        self.alldisplayColorChangeObj.changeTimeAttributeColor(self.ui.time_show, "QLabel")
        self.alldisplayColorChangeObj.changePixmapColor(self.ui.tempIcon)
        self.alldisplayColorChangeObj.changePixmapColor(self.ui.humidityIcon)'''
        # -------------------------------Icon color changes ----------------------------------------------
        '''self.alldisplayColorChangeObj.changeIconColor(self.ui.humidityGraph)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.powerButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.settingsButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.homeButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.phoneCallingButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.toolButton_9)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.upHumidityButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.downHumidityButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.upTemperatureButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.downTemperatureButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.temeratureGraph)

        self.alldisplayColorChangeObj.changeIconColor(self.ui.start)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.reset)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.addAdditonalChronosButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.timerSet)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.startButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.resetButton)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.setTimeSetting)

        # -----------------------Menu Tool Icon color changes----------------------------------------------
        self.alldisplayColorChangeObj.changeIconColor(self.ui.otLighteningDetails)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.ventiLationDetails)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.gasIndicator)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.historyDetails)
        self.alldisplayColorChangeObj.changeIconColor(self.ui.multiMediaDetails)
        
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.menuTitleName, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelBackgroundColor(self.ui.leftMenuTitleLine, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelBackgroundColor(self.ui.rightMenuTitleLine, "QLabel")'''
        # ----------------------Additional Chronos Label and Tool Button--------------------------------------------------
        '''self.alldisplayColorChangeObj.changeTimeAttributeColor(self.additionChronos_ui.chronos2, "QLabel")
        self.alldisplayColorChangeObj.changeTimeAttributeColor(self.additionChronos_ui.chronos3, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.additionChronos_ui.chronosLabel2, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.additionChronos_ui.chronosLabel3, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.additionChronos_ui.startChrono2, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.additionChronos_ui.resetChrono2, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.additionChronos_ui.startChrono3, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.additionChronos_ui.resetChrono3, "QToolButton")
        self.alldisplayColorChangeObj.changeIconColor(self.additionChronos_ui.startChrono2)
        self.alldisplayColorChangeObj.changeIconColor(self.additionChronos_ui.resetChrono2)
        self.alldisplayColorChangeObj.changeIconColor(self.additionChronos_ui.startChrono3)
        self.alldisplayColorChangeObj.changeIconColor(self.additionChronos_ui.resetChrono3)
        # -------------------------------------- OT Lightening --------------------------------------------
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ot_ui.lightLabel1, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ot_ui.lightLabel2, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ot_ui.lightLabel3, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ot_ui.lightLabel4, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ot_ui.lightLabel5, "QLabel")
        self.alldisplayColorChangeObj.changeDisplayAttributeColor(self.ot_ui.lightLabel6, "QLabel")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light1Decrement, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light1Increment, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light2Decrement, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light2Increment, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light3Decrement, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light3Increment, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light4Decrement, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.ot_ui.light4Increment, "QToolButton")'''

        self.modifyGlobalVariablesObj.setChangedImage()
        self.modifyGlobalVariablesObj.setChangedLightColor()
        # -------------- Start Change color of Icon -----------------------------------------------------------
        self.alldisplayColorChangeObj.changePlayerAttributeColor(self.player)
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.previousButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.muteButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.rateBox, "QComboBox")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.volumeSlider, "QSlider")
        # -------------------------- history menu data text color change ---------------------------
        self.alldisplayColorChangeObj.changeTableViewAttributeColor(self.tableWidget, "QTableView")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.iconColor,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.comboBoxTheme,
                                                           "QComboBox")
        self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)
        # ======================= Login UI ==========================================================================
        self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabWidget)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabTheme)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabColor)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabGeneral)
        # =============================== Login UI ==============================================================================================
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.login_ui.user_name,
                                                                   "QLineEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.login_ui.user_pass,
                                                                   "QLineEdit")
        '''self.modifyGlobalVariablesObj.setChangedImage()
        self.modifyGlobalVariablesObj.setChangedLightColor()
        # -------------- End Change Color of Icon -------------------------------------------------------
        
        # -------------------------- Multimedia Menu Color & Font Settings -------------------------
        
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.fullScreenButton, "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.colorButton, "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.openButton, "QPushButton")

        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.stopButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.playButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.stopButton, "QToolButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.player.controls.nextButton, "QToolButton")
        
        self.alldisplayColorChangeObj.changeIconColor(self.player.controls.stopButton)
        self.alldisplayColorChangeObj.changeIconColor(self.player.controls.playButton)
        self.alldisplayColorChangeObj.changeIconColor(self.player.controls.nextButton)
        self.alldisplayColorChangeObj.changeIconColor(self.player.controls.previousButton)
        self.alldisplayColorChangeObj.changeIconColor(self.player.controls.muteButton)
        # self.alldisplayColorChangeObj.changePlayerAttributeColor(AutoCloseMessageBox())
        # -------------------------- Login Dialog Color -----------------------------------------------------------------------------------------
        self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.buttonApplyGeneral,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.applyColor,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.buttonApplyBackGroundImage,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.buttonApplyLogo,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.buttonPowerOnScreenImage,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.buttonApplyTheme,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.iconColor,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.comboBoxTheme,
                                                           "QComboBox")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.chooseLogo,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.choosePowerOnScreenImage,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.settings_dialog_set_ui.chooseBackGroundImage,
                                                           "QPushButton")
        self.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.shutDialog)
        self.alldisplayColorChangeObj.changeAttributeColor(self.shutDown_ui.shutDownButton, "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.shutDown_ui.rebootButton, "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.shutDown_ui.cancelShutButton, "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.shutDown_ui.logoutButton, "QPushButton")
        self.alldisplayColorChangeObj.changeAttributeColor(self.login_ui.loginButton, "QPushButton")
        self.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.loginDialogQtWidget)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.setTimerWidget)
        # self.settings_dialog_set_ui.tabGeneral.setStyleSheet("color: " + self.dataModel.get_text_col() + ";")
        # self.settings_dialog_set_ui.tabColor.setStyleSheet("color: " + self.dataModel.get_text_col() + ";")
        # ++++++++++++++++++++++++++++++ Settings Dialog UI Color Changes ++++++++++++++++++++++++++++++++++
        # =============================== Settings Dialog ==================================================
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light1,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light2,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light3,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light4,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light5,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.light6,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit1,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit2,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit3,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit4,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit5,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit6,
                                                                   "QTextEdit")
        self.alldisplayColorChangeObj.changeEditTextAttributeColor(self.settings_dialog_set_ui.gasNameEdit7,
                                                                   "QTextEdit")

        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLight1,
                                                                   "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLight2,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLight3,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLight4,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLight5,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLight6,
                                                                        "QLabel")

        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxLight1,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxLight2,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxLight3,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxLight4,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxLight5,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxLight6,
                                                                        "QCheckBox")

        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxDim1,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxDim2,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxDim3,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxDim4,
                                                                        "QCheckBox")

        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxGas1,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxGas2,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxGas3,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxGas4,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxGas5,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxGas6,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxGas7,
                                                                        "QCheckBox")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.checkBoxDifferentialPressure,
                                                                        "QCheckBox")

        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelBorderColor,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelBackGroundColor,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelTextColor,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelIconColor,
                                                                        "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelTheme,
                                                                  "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelBackGroundImage,
                                                                  "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLogo,
                                                                  "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelPowerOnImage,
                                                                  "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelLightTitle,
                                                                  "QLabel")
        self.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.settings_dialog_set_ui.labelGasAlarmTitle,
                                                                  "QLabel")


        # =============================== Settings End ==========================================================================================
        
        
        # ---------------------New---------------------------------------------------------------------------
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabColor)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabGeneral)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabTheme)'''
        # ---------------------New---------------------------------------------------------------------------
        # self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabTheme)
        # self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabColor)
        # self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabGeneral)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def flashSplash(self):
        self.splash = QSplashScreen(QPixmap('/home/rnjn/RasberryProject/DigilineSystem/icon/medical-logo-plus.png'))

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        QTimer.singleShot(2000, self.splash.close)

    def popupVirtualKeyboard(self):
        self.keyboardF = KeyboardWidget(self.settings_dialog_set_ui.light1)

    def handleActivated(self, index):
        # self.dataModel = DataModel()
        print(self.settings_dialog_set_ui.comboBoxTheme.itemText(index))  # value
        print(self.settings_dialog_set_ui.comboBoxTheme.itemData(index))  # key
        self.themeColor_name = self.settings_dialog_set_ui.comboBoxTheme.itemText(index)  # value
        self.themeColor_hex = self.settings_dialog_set_ui.comboBoxTheme.itemData(index)  # key
        key = str(self.themeColor_hex).split(';#@;')
        self.dataModel.set_theme_color(key[0])  # Hex code of theme color
        self.dataModel.set_theme_preview_image_path(key[1])  # Theme image preview path
        self.dataModel.set_combo_theme_color_index(index)
        self.dataModel.set_appearance_theme_color_name(self.themeColor_name)
        # self.database_manage.updateThemeColorDb(self.dataModel)

    '''
    def selectionchange(self, i):
        print("Items in the list are :")
        for count in range(self.settings_dialog_set_ui.comboBoxTheme.count()):
            print(self.settings_dialog_set_ui.comboBoxTheme.itemData(count))

        print("Current index", i, "selection changed ", self.settings_dialog_set_ui.comboBoxTheme.currentText())
        thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    for x in thisdict:
      print(thisdict[x])'''

    def populateThemeCombo(self):
        # self.dataModel = DataModel()
        self.database_manage.queryThemeColorSettings(self.dataModel)
        self.database_manage.queryAppearanceSettingsData(self.dataModel)
        # print("Current Text: " + self.dataModel.get_theme_color() + ";#@;" + self.dataModel.get_theme_color_preview())
        items = self.database_manage.populate_cbo_from_tlkp_table()
        for x in items:
            self.settings_dialog_set_ui.comboBoxTheme.addItem(items[x], x)
        if self.dataModel.get_combo_theme_color_index():
            self.settings_dialog_set_ui.comboBoxTheme.setCurrentIndex(int(self.dataModel.get_combo_theme_color_index()))
        '''self.settings_dialog_set_ui.comboBoxTheme.setCurrentText(
            self.dataModel.get_theme_color() + ";#@;" + self.dataModel.get_theme_color_preview())'''

    def updateThemeColor(self):
        if self.dataModel.get_theme_color() != "Select":
            self.database_manage.updateThemeColorDb(self.dataModel)
            self.applyThemeColor()

    def applyThemeColor(self):
        # self.dataModel = DataModel()
        self.database_manage.queryAppearanceSettingsData(self.dataModel)
        # self.database_manage.queryAppearanceSettingsData(self.dataModel)
        # self.settings_dialog_set_ui.comboBoxTheme.setCurrentText(self.dataModel.get_theme_color_name())
        self.setStyleSheet("background-color: " + self.dataModel.get_theme_color() + ";")
        # self.loginDialogQtWidget.setStyleSheet("background-color: " + self.dataModel.get_theme_color() + ";")
        # self.SettingsQDialog.setStyleSheet("background-color: " + self.dataModel.get_theme_color() + ";")
        # self.shutDialog.setStyleSheet("background-color: " + self.dataModel.get_theme_color() + ";")
        print("Color Name: " + self.dataModel.get_appearance_theme_color_name())
        self.settings_dialog_set_ui.labelDisplayTheme.setPixmap(QtGui.QPixmap(self.dataModel.get_theme_color_preview()))
        # self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)
        self.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.shutDialog)
        self.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.loginDialogQtWidget)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.setTimerWidget)
        # ++++++++++++++++++++++++++++++ Settings Dialog UI Color Changes ++++++++++++++++++++++++++++++++++
        # self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabWidget)
        # self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabTheme)
        # self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabColor)
        # self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabGeneral)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabWidget)
        self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)
        # self.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.shutDialog)
        # self.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.loginDialogQtWidget)
        # self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.setTimerWidget)
        # self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)  # 8 timer problem
        self.alldisplayColorChangeObj.changeSettingsDialogTabColor(self.settings_dialog_set_ui.tabWidget)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabColor)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabGeneral)
        self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabTheme)
        # self.fontColorChanges()

    def fontColorChangesName(self):
        # self.dataModel = DataModel()
        self.database_manage.queryAppearanceSettingsData(self.dataModel)
        self.appearance_color_name = self.dataModel.get_appearance_theme_color_name()
        # self.ui.time_show.setStyleSheet("color:#000000")

    def updateBackgroundImage(self):
        # self.dataModel = DataModel()
        print(self.backgroundImagePath)
        if self.backgroundImagePath:
            self.dataModel.set_background_image_path(self.backgroundImagePath)
            self.database_manage.updateBackgroundImagePath(self.dataModel)
        self.queryAppearanceSettingsDataAndSet(self.dataModel)
        self.applyBackGroundImage()

    def applyBackGroundImage(self):
        # self.dataModel = DataModel()
        self.database_manage.queryAppearanceSettingsData(self.dataModel)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setStyleSheet("background:transparent;")
        if eval(self.dataModel.get_enable_disable_background_image()):
            self.setStyleSheet("background: url(" + self.dataModel.get_background_image_path() + ");")
        else:
            self.applyThemeColor()
        # self.setStyleSheet("background-color: " + self.dataModel.get_theme_color() + ";")

    def updateLogoImage(self):
        # self.dataModel = DataModel()
        if self.logoImagePath:
            self.dataModel.set_logo_image_path(self.logoImagePath)
            self.database_manage.updateLogoImagePath(self.dataModel)
        self.queryAppearanceSettingsDataAndSet(self.dataModel)
        self.applyLogoImage()

    def updatePowerOnImage(self):
        # self.dataModel = DataModel()
        if self.powerOnImagePath:
            self.dataModel.set_power_on_image_path(self.powerOnImagePath)
            self.database_manage.updatePowerOnImagePath(self.dataModel)
        self.queryAppearanceSettingsDataAndSet(self.dataModel)

    def enableBackGroundImage(self):
        # self.dataModel = DataModel()
        if self.settings_dialog_set_ui.enableBackGroundImage.isChecked():
            self.settings_dialog_set_ui.disableBackGroundImage.setChecked(False)
            self.dataModel.set_enable_disable_background_image("True")
            self.database_manage.updateEnableDisableBackgroundImage(self.dataModel)
        else:
            self.settings_dialog_set_ui.disableBackGroundImage.setChecked(True)
            self.dataModel.set_enable_disable_background_image("False")
            self.database_manage.updateEnableDisableBackgroundImage(self.dataModel)

    def disableBackGroundImage(self):
        # self.dataModel = DataModel()
        if self.settings_dialog_set_ui.disableBackGroundImage.isChecked():
            self.settings_dialog_set_ui.enableBackGroundImage.setChecked(False)
            self.dataModel.set_enable_disable_background_image("False")
            self.database_manage.updateEnableDisableBackgroundImage(self.dataModel)
        else:
            self.settings_dialog_set_ui.enableBackGroundImage.setChecked(True)
            self.dataModel.set_enable_disable_background_image("True")
            self.database_manage.updateEnableDisableBackgroundImage(self.dataModel)

    def applyLogoImage(self):
        # self.dataModel = DataModel()
        self.database_manage.queryAppearanceSettingsData(self.dataModel)
        if eval(self.dataModel.get_enable_disable_logo_image()):
            self.ui.logoDisplay.setPixmap(QtGui.QPixmap(self.dataModel.get_logo_image_path()))
        else:
            self.ui.logoDisplay.setPixmap(QtGui.QPixmap(""))
        # self.setStyleSheet("background-color: " + self.dataModel.get_theme_color() + ";")

    def enableLogo(self):
        # self.dataModel = DataModel()
        if self.settings_dialog_set_ui.enableLogo.isChecked():
            self.settings_dialog_set_ui.disableLogo.setChecked(False)
            self.dataModel.set_enable_disable_logo_image("True")
            self.database_manage.updateEnableDisableLogoImage(self.dataModel)
        else:
            self.settings_dialog_set_ui.disableLogo.setChecked(True)
            self.dataModel.set_enable_disable_logo_image("False")
            self.database_manage.updateEnableDisableLogoImage(self.dataModel)

    def disableLogo(self):
        # self.dataModel = DataModel()
        if self.settings_dialog_set_ui.disableLogo.isChecked():
            self.settings_dialog_set_ui.enableLogo.setChecked(False)
            self.dataModel.set_enable_disable_logo_image("False")
            self.database_manage.updateEnableDisableLogoImage(self.dataModel)
        else:
            self.settings_dialog_set_ui.enableLogo.setChecked(True)
            self.dataModel.set_enable_disable_logo_image("True")
            self.database_manage.updateEnableDisableLogoImage(self.dataModel)

    def selectBackgroundImageOpen(self):
        # self.dataModel = DataModel()
        self.backgroundImagePath, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                                  "Image PNG (*.png);Image JPG (*.jpg);All files (*.*)")
        # self.settings_dialog_set_ui.displayBackGroundImagePath.setStyleSheet("word-wrap: break-word;")
        # self.dataModel.set_background_image_path(path)
        if self.backgroundImagePath:
            self.dataModel.set_background_image_path(self.backgroundImagePath)
            self.settings_dialog_set_ui.displayBackGroundImagePath.setText(self.backgroundImagePath)
        else:
            self.queryAppearanceSettingsDataAndSet(self.dataModel)

    def selectLogoImageOpen(self):
        # self.dataModel = DataModel()
        self.logoImagePath, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                            "Image PNG (*.png);Image JPG (*.jpg);All files (*.*)")
        if self.logoImagePath:
            self.dataModel.set_logo_image_path(self.logoImagePath)
            self.settings_dialog_set_ui.displayLogoPath.setText(self.logoImagePath)
        else:
            self.queryAppearanceSettingsDataAndSet(self.dataModel)

    def selectPowerOnImageOpen(self):
        # self.dataModel = DataModel()
        self.powerOnImagePath, _ = QFileDialog.getOpenFileName(self, "Open file", "",

                                                               "Image PNG (*.png);Image JPG (*.jpg);All files (*.*)")
        if self.powerOnImagePath:
            self.dataModel.set_power_on_image_path(self.powerOnImagePath)
            self.settings_dialog_set_ui.labelDisplayPowerOnScreenImage.setText(self.powerOnImagePath)
        else:
            self.queryAppearanceSettingsDataAndSet(self.dataModel)

    def changeGasNameDatabase(self, db):
        self.ui.nitrousOxide.setText(db.get_gas_name_1())
        if eval(db.get_checkbox_gas_1()):
            self.ui.nitrousOxide.show()
        else:
            self.ui.nitrousOxide.hide()
        self.ui.air.setText(db.get_gas_name_2())
        if eval(db.get_checkbox_gas_2()):
            self.ui.air.show()
        else:
            self.ui.air.hide()
        self.ui.air7.setText(db.get_gas_name_3())
        if eval(db.get_checkbox_gas_3()):
            self.ui.air7.show()
        else:
            self.ui.air7.hide()
        self.ui.cabonDiOxide.setText(db.get_gas_name_4())
        if eval(db.get_checkbox_gas_4()):
            self.ui.cabonDiOxide.show()
        else:
            self.ui.cabonDiOxide.hide()
        self.ui.oxygen.setText(db.get_gas_name_5())
        if eval(db.get_checkbox_gas_5()):
            self.ui.oxygen.show()
        else:
            self.ui.oxygen.hide()
        self.ui.vacuum.setText(db.get_gas_name_6())
        if eval(db.get_checkbox_gas_6()):
            self.ui.vacuum.show()
        else:
            self.ui.vacuum.hide()
        self.ui.ips.setText(db.get_gas_name_7())
        if eval(db.get_checkbox_gas_7()):
            self.ui.ips.show()
        else:
            self.ui.ips.hide()

    def changeLightNameDatabase(self, db):
        self.ot_ui.lightLabel1.setText(db.get_light_name_1())
        if eval(db.get_light_checkbox_1()):
            self.ot_ui.lightLabel1.show()
            self.ot_ui.lightBulb1.show()
            self.ot_ui.toggleContainerGasL1.show()
        else:
            self.ot_ui.lightLabel1.hide()
            self.ot_ui.lightBulb1.hide()
            self.ot_ui.toggleContainerGasL1.hide()
        self.ot_ui.lightLabel2.setText(db.get_light_name_2())
        if eval(db.get_light_checkbox_2()):
            self.ot_ui.lightLabel2.show()
            self.ot_ui.lightBulb2.show()
            self.ot_ui.toggleContainerGasL2.show()
        else:
            self.ot_ui.lightLabel2.hide()
            self.ot_ui.lightBulb2.hide()
            self.ot_ui.toggleContainerGasL2.hide()
        self.ot_ui.lightLabel3.setText(db.get_light_name_3())
        if eval(db.get_light_checkbox_3()):
            self.ot_ui.lightLabel3.show()
            self.ot_ui.otLightBulb1.show()
            self.ot_ui.toggleContainerOT1.show()
        else:
            self.ot_ui.lightLabel3.hide()
            self.ot_ui.otLightBulb1.hide()
            self.ot_ui.toggleContainerOT1.hide()
        self.ot_ui.lightLabel4.setText(db.get_light_name_4())
        if eval(db.get_light_checkbox_4()):
            self.ot_ui.lightLabel4.show()
            self.ot_ui.lightBulb3.show()
            self.ot_ui.toggleContainer.show()
        else:
            self.ot_ui.lightLabel4.hide()
            self.ot_ui.lightBulb3.hide()
            self.ot_ui.toggleContainer.hide()
        self.ot_ui.lightLabel5.setText(db.get_light_name_5())
        if eval(db.get_light_checkbox_5()):
            self.ot_ui.lightLabel5.show()
            self.ot_ui.lightBulb4.show()
            self.ot_ui.toggleContainerLaminar.show()
        else:
            self.ot_ui.lightLabel5.hide()
            self.ot_ui.lightBulb4.hide()
            self.ot_ui.toggleContainerLaminar.hide()
        self.ot_ui.lightLabel6.setText(db.get_light_name_6())
        if eval(db.get_light_checkbox_6()):
            self.ot_ui.lightLabel6.show()
            self.ot_ui.otLightBulb2.show()
            self.ot_ui.toggleContainerOT2.show()
        else:
            self.ot_ui.lightLabel6.hide()
            self.ot_ui.otLightBulb2.hide()
            self.ot_ui.toggleContainerOT2.hide()

    def showHideLightDimming(self, db):
        if eval(db.get_light_dim_checkbox_1()):
            self.ot_ui.light1Increment.show()
            self.ot_ui.light1Decrement.show()
            self.ot_ui.light1_1.show()
            self.ot_ui.light1_2.show()
            self.ot_ui.light1_3.show()
            self.ot_ui.light1_4.show()
            self.ot_ui.light1_5.show()
            self.ot_ui.light1_6.show()
            self.ot_ui.light1_7.show()
            self.ot_ui.light1_8.show()
            self.ot_ui.light1_9.show()
            self.ot_ui.light1_10.show()
        else:
            self.ot_ui.light1Increment.hide()
            self.ot_ui.light1Decrement.hide()
            self.ot_ui.light1_1.hide()
            self.ot_ui.light1_2.hide()
            self.ot_ui.light1_3.hide()
            self.ot_ui.light1_4.hide()
            self.ot_ui.light1_5.hide()
            self.ot_ui.light1_6.hide()
            self.ot_ui.light1_7.hide()
            self.ot_ui.light1_8.hide()
            self.ot_ui.light1_9.hide()
            self.ot_ui.light1_10.hide()
        if eval(db.get_light_dim_checkbox_2()):
            self.ot_ui.light2Increment.show()
            self.ot_ui.light2Decrement.show()
            self.ot_ui.light2_1.show()
            self.ot_ui.light2_2.show()
            self.ot_ui.light2_3.show()
            self.ot_ui.light2_4.show()
            self.ot_ui.light2_5.show()
            self.ot_ui.light2_6.show()
            self.ot_ui.light2_7.show()
            self.ot_ui.light2_8.show()
            self.ot_ui.light2_9.show()
            self.ot_ui.light2_10.show()
        else:
            self.ot_ui.light2Increment.hide()
            self.ot_ui.light2Decrement.hide()
            self.ot_ui.light2_1.hide()
            self.ot_ui.light2_2.hide()
            self.ot_ui.light2_3.hide()
            self.ot_ui.light2_4.hide()
            self.ot_ui.light2_5.hide()
            self.ot_ui.light2_6.hide()
            self.ot_ui.light2_7.hide()
            self.ot_ui.light2_8.hide()
            self.ot_ui.light2_9.hide()
            self.ot_ui.light2_10.hide()
        if eval(db.get_light_dim_checkbox_3()):
            self.ot_ui.light3Increment.show()
            self.ot_ui.light3Decrement.show()
            self.ot_ui.light3_1.show()
            self.ot_ui.light3_2.show()
            self.ot_ui.light3_3.show()
            self.ot_ui.light3_4.show()
            self.ot_ui.light3_5.show()
            self.ot_ui.light3_6.show()
            self.ot_ui.light3_7.show()
            self.ot_ui.light3_8.show()
            self.ot_ui.light3_9.show()
            self.ot_ui.light3_10.show()
        else:
            self.ot_ui.light3Increment.hide()
            self.ot_ui.light3Decrement.hide()
            self.ot_ui.light3_1.hide()
            self.ot_ui.light3_2.hide()
            self.ot_ui.light3_3.hide()
            self.ot_ui.light3_4.hide()
            self.ot_ui.light3_5.hide()
            self.ot_ui.light3_6.hide()
            self.ot_ui.light3_7.hide()
            self.ot_ui.light3_8.hide()
            self.ot_ui.light3_9.hide()
            self.ot_ui.light3_10.hide()
        if eval(db.get_light_dim_checkbox_4()):
            self.ot_ui.light4Increment.show()
            self.ot_ui.light4Decrement.show()
            self.ot_ui.light4_1.show()
            self.ot_ui.light4_2.show()
            self.ot_ui.light4_3.show()
            self.ot_ui.light4_4.show()
            self.ot_ui.light4_5.show()
            self.ot_ui.light4_6.show()
            self.ot_ui.light4_7.show()
            self.ot_ui.light4_8.show()
            self.ot_ui.light4_9.show()
            self.ot_ui.light4_10.show()
        else:
            self.ot_ui.light4Increment.hide()
            self.ot_ui.light4Decrement.hide()
            self.ot_ui.light4_1.hide()
            self.ot_ui.light4_2.hide()
            self.ot_ui.light4_3.hide()
            self.ot_ui.light4_4.hide()
            self.ot_ui.light4_5.hide()
            self.ot_ui.light4_6.hide()
            self.ot_ui.light4_7.hide()
            self.ot_ui.light4_8.hide()
            self.ot_ui.light4_9.hide()
            self.ot_ui.light4_10.hide()

    def changGasUiGasName(self, db):
        self.gas_ui.gasLabel_1.setText(db.get_gas_name_1())
        self.gas_ui.gasLabel_2.setText(db.get_gas_name_2())
        self.gas_ui.gasLabel_3.setText(db.get_gas_name_3())
        self.gas_ui.gasLabel_4.setText(db.get_gas_name_4())
        self.gas_ui.gasLabel_5.setText(db.get_gas_name_5())
        self.gas_ui.gasLabel_6.setText(db.get_gas_name_6())
        if eval(db.get_checkbox_gas_1()):
            self.gas_ui.gasLabel_1.show()
            self.gas_ui.gasLabel_1_high.show()
            self.gas_ui.gasLabel_1_normal.show()
            self.gas_ui.gasLabel_1_low.show()
        else:
            self.gas_ui.gasLabel_1.hide()
            self.gas_ui.gasLabel_1_high.hide()
            self.gas_ui.gasLabel_1_normal.hide()
            self.gas_ui.gasLabel_1_low.hide()
        if eval(db.get_checkbox_gas_2()):
            self.gas_ui.gasLabel_2.show()
            self.gas_ui.gasLabel_2_high.show()
            self.gas_ui.gasLabel_2_normal.show()
            self.gas_ui.gasLabel_2_low.show()
        else:
            self.gas_ui.gasLabel_2.hide()
            self.gas_ui.gasLabel_2_high.hide()
            self.gas_ui.gasLabel_2_normal.hide()
            self.gas_ui.gasLabel_2_low.hide()
        if eval(db.get_checkbox_gas_3()):
            self.gas_ui.gasLabel_3.show()
            self.gas_ui.gasLabel_3_high.show()
            self.gas_ui.gasLabel_3_normal.show()
            self.gas_ui.gasLabel_3_low.show()
        else:
            self.gas_ui.gasLabel_3.hide()
            self.gas_ui.gasLabel_3_high.hide()
            self.gas_ui.gasLabel_3_normal.hide()
            self.gas_ui.gasLabel_3_low.hide()
        if eval(db.get_checkbox_gas_4()):
            self.gas_ui.gasLabel_4.show()
            self.gas_ui.gasLabel_4_high.show()
            self.gas_ui.gasLabel_4_normal.show()
            self.gas_ui.gasLabel_4_low.show()
        else:
            self.gas_ui.gasLabel_4.hide()
            self.gas_ui.gasLabel_4_high.hide()
            self.gas_ui.gasLabel_4_normal.hide()
            self.gas_ui.gasLabel_4_low.hide()
        if eval(db.get_checkbox_gas_5()):
            self.gas_ui.gasLabel_5.show()
            self.gas_ui.gasLabel_5_high.show()
            self.gas_ui.gasLabel_5_normal.show()
            self.gas_ui.gasLabel_5_low.show()
        else:
            self.gas_ui.gasLabel_5.hide()
            self.gas_ui.gasLabel_5_high.hide()
            self.gas_ui.gasLabel_5_normal.hide()
            self.gas_ui.gasLabel_5_low.hide()
        if eval(db.get_checkbox_gas_6()):
            self.gas_ui.gasLabel_6.show()
            self.gas_ui.gasLabel_6_normal.show()
            self.gas_ui.gasLabel_6_low.show()
        else:
            self.gas_ui.gasLabel_6.hide()
            self.gas_ui.gasLabel_6_normal.hide()
            self.gas_ui.gasLabel_6_low.hide()

    def queryIconColorSettingsMain(self, model, database):
        database.queryIconColorSettings(model)

    def queryAppearanceSettingsDataAndSet(self, dataModel):
        # self.dataModel = DataModel()
        self.database_manage.queryAppearanceSettingsData(dataModel)
        # print("Now:" + str(eval(self.dataModel.get_light_dim_checkbox_1())))
        self.settings_dialog_set_ui.displayBackGroundImagePath.setText(dataModel.get_background_image_path())
        self.settings_dialog_set_ui.displayLogoPath.setText(dataModel.get_logo_image_path())
        self.settings_dialog_set_ui.labelDisplayPowerOnScreenImage.setText(dataModel.get_power_on_image_path())
        if eval(dataModel.get_enable_disable_background_image()):
            self.settings_dialog_set_ui.enableBackGroundImage.setChecked(True)
        else:
            self.settings_dialog_set_ui.disableBackGroundImage.setChecked(True)

        if eval(dataModel.get_enable_disable_logo_image()):
            self.settings_dialog_set_ui.enableLogo.setChecked(True)
        else:
            self.settings_dialog_set_ui.disableLogo.setChecked(True)
        # self.settings_dialog_set_ui.comboBoxTheme.setText(self.dataModel.get_light_name_4())
        # self.settings_dialog_set_ui.light5.setText(self.dataModel.get_light_name_5())
        # self.settings_dialog_set_ui.light6.setText(self.dataModel.get_light_name_6())
        self.setPixMapToLabel(dataModel)

    def setPixMapToLabel(self, datamodel):
        if datamodel.get_background_image_path():
            self.settings_dialog_set_ui.labelDisplayBackGroundImage.setPixmap(
                QtGui.QPixmap(datamodel.get_background_image_path()))
        if datamodel.get_logo_image_path():
            self.settings_dialog_set_ui.labelDisplayLogo.setPixmap(
                QtGui.QPixmap(datamodel.get_logo_image_path()))
        if datamodel.get_power_on_image_path():
            self.settings_dialog_set_ui.labelDisplayPowerOnScreenImage_2.setPixmap(
                QtGui.QPixmap(datamodel.get_power_on_image_path()))

    def queryGeneralSettingsDataAndSet(self):
        # self.dataModel = DataModel()
        self.database_manage.queryGeneralSettingsData(self.dataModel)
        print("Now:" + str(eval(self.dataModel.get_light_dim_checkbox_1())))
        self.settings_dialog_set_ui.light1.setText(self.dataModel.get_light_name_1())
        self.settings_dialog_set_ui.light2.setText(self.dataModel.get_light_name_2())
        self.settings_dialog_set_ui.light3.setText(self.dataModel.get_light_name_3())
        self.settings_dialog_set_ui.light4.setText(self.dataModel.get_light_name_4())
        self.settings_dialog_set_ui.light5.setText(self.dataModel.get_light_name_5())
        self.settings_dialog_set_ui.light6.setText(self.dataModel.get_light_name_6())
        self.settings_dialog_set_ui.gasNameEdit1.setText(self.dataModel.get_gas_name_1())
        self.settings_dialog_set_ui.gasNameEdit2.setText(self.dataModel.get_gas_name_2())
        self.settings_dialog_set_ui.gasNameEdit3.setText(self.dataModel.get_gas_name_3())
        self.settings_dialog_set_ui.gasNameEdit4.setText(self.dataModel.get_gas_name_4())
        self.settings_dialog_set_ui.gasNameEdit5.setText(self.dataModel.get_gas_name_5())
        self.settings_dialog_set_ui.gasNameEdit6.setText(self.dataModel.get_gas_name_6())
        self.settings_dialog_set_ui.gasNameEdit7.setText(self.dataModel.get_gas_name_7())
        self.settings_dialog_set_ui.checkBoxLight1.setChecked(eval(self.dataModel.get_light_checkbox_1()))
        self.settings_dialog_set_ui.checkBoxLight2.setChecked(eval(self.dataModel.get_light_checkbox_2()))
        self.settings_dialog_set_ui.checkBoxLight3.setChecked(eval(self.dataModel.get_light_checkbox_3()))
        self.settings_dialog_set_ui.checkBoxLight4.setChecked(eval(self.dataModel.get_light_checkbox_4()))
        self.settings_dialog_set_ui.checkBoxLight5.setChecked(eval(self.dataModel.get_light_checkbox_5()))
        self.settings_dialog_set_ui.checkBoxLight6.setChecked(eval(self.dataModel.get_light_checkbox_6()))
        self.settings_dialog_set_ui.checkBoxGas1.setChecked(eval(self.dataModel.get_checkbox_gas_1()))
        self.settings_dialog_set_ui.checkBoxGas2.setChecked(eval(self.dataModel.get_checkbox_gas_2()))
        self.settings_dialog_set_ui.checkBoxGas3.setChecked(eval(self.dataModel.get_checkbox_gas_3()))
        self.settings_dialog_set_ui.checkBoxGas4.setChecked(eval(self.dataModel.get_checkbox_gas_4()))
        self.settings_dialog_set_ui.checkBoxGas5.setChecked(eval(self.dataModel.get_checkbox_gas_5()))
        self.settings_dialog_set_ui.checkBoxGas6.setChecked(eval(self.dataModel.get_checkbox_gas_6()))
        self.settings_dialog_set_ui.checkBoxGas7.setChecked(eval(self.dataModel.get_checkbox_gas_7()))
        self.settings_dialog_set_ui.checkBoxDim1.setChecked(eval(self.dataModel.get_light_dim_checkbox_1()))
        self.settings_dialog_set_ui.checkBoxDim2.setChecked(eval(self.dataModel.get_light_dim_checkbox_2()))
        self.settings_dialog_set_ui.checkBoxDim3.setChecked(eval(self.dataModel.get_light_dim_checkbox_3()))
        self.settings_dialog_set_ui.checkBoxDim4.setChecked(eval(self.dataModel.get_light_dim_checkbox_4()))
        self.settings_dialog_set_ui.checkBoxDifferentialPressure.setChecked(
            eval(self.dataModel.get_differential_gas_pressure_checkbox()))
        self.changeGasNameDatabase(self.dataModel)
        self.changeLightNameDatabase(self.dataModel)
        self.showHideLightDimming(self.dataModel)
        self.changGasUiGasName(self.dataModel)

        cQLineEdit(self.settings_dialog_set_ui.light1, self.dataModel.get_light_name_1(), self.dataModel, "light_1")
        cQLineEdit(self.settings_dialog_set_ui.light2, self.dataModel.get_light_name_2(), self.dataModel, "light_2")
        cQLineEdit(self.settings_dialog_set_ui.light3, self.dataModel.get_light_name_3(), self.dataModel, "light_3")
        cQLineEdit(self.settings_dialog_set_ui.light4, self.dataModel.get_light_name_4(), self.dataModel, "light_4")
        cQLineEdit(self.settings_dialog_set_ui.light5, self.dataModel.get_light_name_5(), self.dataModel, "light_5")
        cQLineEdit(self.settings_dialog_set_ui.light6, self.dataModel.get_light_name_6(), self.dataModel, "light_6")

        cQLineEdit(self.settings_dialog_set_ui.gasNameEdit1, self.dataModel.get_gas_name_1(), self.dataModel, "gas_1")
        cQLineEdit(self.settings_dialog_set_ui.gasNameEdit2, self.dataModel.get_gas_name_2(), self.dataModel, "gas_2")
        cQLineEdit(self.settings_dialog_set_ui.gasNameEdit3, self.dataModel.get_gas_name_3(), self.dataModel, "gas_3")
        cQLineEdit(self.settings_dialog_set_ui.gasNameEdit4, self.dataModel.get_gas_name_4(), self.dataModel, "gas_4")
        cQLineEdit(self.settings_dialog_set_ui.gasNameEdit5, self.dataModel.get_gas_name_5(), self.dataModel, "gas_5")
        cQLineEdit(self.settings_dialog_set_ui.gasNameEdit6, self.dataModel.get_gas_name_6(), self.dataModel, "gas_6")
        cQLineEdit(self.settings_dialog_set_ui.gasNameEdit7, self.dataModel.get_gas_name_7(), self.dataModel, "gas_7")

    def updateLabelName(self):
        # self.dataModel = DataModel()
        print("EditText: " + str(self.settings_dialog_set_ui.checkBoxLight1.isChecked()))
        if self.dataModel.get_light_name_1() is None:
            self.dataModel.set_light_name_1(self.settings_dialog_set_ui.light1.toPlainText())
        if self.dataModel.get_light_name_2() is None:
            self.dataModel.set_light_name_2(self.settings_dialog_set_ui.light2.toPlainText())
        if self.dataModel.get_light_name_3() is None:
            self.dataModel.set_light_name_3(self.settings_dialog_set_ui.light3.toPlainText())
        if self.dataModel.get_light_name_4() is None:
            self.dataModel.set_light_name_4(self.settings_dialog_set_ui.light4.toPlainText())
        if self.dataModel.get_light_name_5() is None:
            self.dataModel.set_light_name_5(self.settings_dialog_set_ui.light5.toPlainText())
        if self.dataModel.get_light_name_6() is None:
            self.dataModel.set_light_name_6(self.settings_dialog_set_ui.light6.toPlainText())

        self.dataModel.set_light_checkbox_1(self.settings_dialog_set_ui.checkBoxLight1.isChecked())
        self.dataModel.set_light_checkbox_2(self.settings_dialog_set_ui.checkBoxLight2.isChecked())
        self.dataModel.set_light_checkbox_3(self.settings_dialog_set_ui.checkBoxLight3.isChecked())
        self.dataModel.set_light_checkbox_4(self.settings_dialog_set_ui.checkBoxLight4.isChecked())
        self.dataModel.set_light_checkbox_5(self.settings_dialog_set_ui.checkBoxLight5.isChecked())
        self.dataModel.set_light_checkbox_6(self.settings_dialog_set_ui.checkBoxLight6.isChecked())
        if self.dataModel.get_gas_name_1() is None:
            self.dataModel.set_gas_name_1(self.settings_dialog_set_ui.gasNameEdit1.toPlainText())
        if self.dataModel.get_gas_name_2() is None:
            self.dataModel.set_gas_name_2(self.settings_dialog_set_ui.gasNameEdit2.toPlainText())
        if self.dataModel.get_gas_name_3() is None:
            self.dataModel.set_gas_name_3(self.settings_dialog_set_ui.gasNameEdit3.toPlainText())
        if self.dataModel.get_gas_name_4() is None:
            self.dataModel.set_gas_name_4(self.settings_dialog_set_ui.gasNameEdit4.toPlainText())
        if self.dataModel.get_gas_name_5() is None:
            self.dataModel.set_gas_name_5(self.settings_dialog_set_ui.gasNameEdit5.toPlainText())
        if self.dataModel.get_gas_name_6() is None:
            self.dataModel.set_gas_name_6(self.settings_dialog_set_ui.gasNameEdit6.toPlainText())
        if self.dataModel.get_gas_name_7() is None:
            self.dataModel.set_gas_name_7(self.settings_dialog_set_ui.gasNameEdit7.toPlainText())

        self.dataModel.set_checkbox_gas_1(self.settings_dialog_set_ui.checkBoxGas1.isChecked())
        self.dataModel.set_checkbox_gas_2(self.settings_dialog_set_ui.checkBoxGas2.isChecked())
        self.dataModel.set_checkbox_gas_3(self.settings_dialog_set_ui.checkBoxGas3.isChecked())
        self.dataModel.set_checkbox_gas_4(self.settings_dialog_set_ui.checkBoxGas4.isChecked())
        self.dataModel.set_checkbox_gas_5(self.settings_dialog_set_ui.checkBoxGas5.isChecked())
        self.dataModel.set_checkbox_gas_6(self.settings_dialog_set_ui.checkBoxGas6.isChecked())
        self.dataModel.set_checkbox_gas_7(self.settings_dialog_set_ui.checkBoxGas7.isChecked())
        self.dataModel.set_light_dim_1(self.settings_dialog_set_ui.checkBoxDim1.isChecked())
        self.dataModel.set_light_dim_2(self.settings_dialog_set_ui.checkBoxDim2.isChecked())
        self.dataModel.set_light_dim_3(self.settings_dialog_set_ui.checkBoxDim3.isChecked())
        self.dataModel.set_light_dim_4(self.settings_dialog_set_ui.checkBoxDim4.isChecked())
        self.dataModel.set_checkbox_differential_pressure_name(
            self.settings_dialog_set_ui.checkBoxDifferentialPressure.isChecked())
        '''print("GAS_1: " + self.dataModel.get_gas_name_1())
        print("GAS_2: " + self.dataModel.get_gas_name_2())
        print("GAS_3: " + self.dataModel.get_gas_name_3())
        print("GAS_4: " + self.dataModel.get_gas_name_4())
        print("GAS_5: " + self.dataModel.get_gas_name_5())
        print("GAS_6: " + self.dataModel.get_gas_name_6())
        print("GAS_7: " + self.dataModel.get_gas_name_7())'''
        self.database_manage.updateGeneralSettingsData(self.dataModel)
        self.queryGeneralSettingsDataAndSet()

    # ==============================xxxxxxxxxxxxxxxxxxxxxxxxxx===========================================================

    def decrementTemperature(self):
        if self.t_i_d_count > 0:
            self.t_i_d_count = self.t_i_d_count - 1
        print(str(self.t_i_d_count))
        self.tempDisplayLabel()
        # while self.ui.downTemperatureButton.isDown():
        self.startThreadSwitch7()
        #  i = i + 1
        # print(str(i))

    def incrementTemperature(self):
        self.t_i_d_count = self.t_i_d_count + 1
        print(str(self.t_i_d_count))
        self.tempDisplayLabel()
        self.startThreadSwitch7()

    def decrementHumidity(self):
        if self.h_i_d_count > 0:
            self.h_i_d_count = self.h_i_d_count - 1
        print(str(self.h_i_d_count))
        self.humidityDisplayLabel()
        self.startThreadSwitch8()
        # while self.ui.downTemperatureButton.isDown():
        #  i = i + 1
        # print(str(i))

    def incrementHumidity(self):
        self.h_i_d_count = self.h_i_d_count + 1
        print(str(self.h_i_d_count))
        self.humidityDisplayLabel()
        self.startThreadSwitch8()

    def tempDisplayLabel(self):
        # self.ui.tempSetShow.setStyleSheet("QLabel { color: yellow ;}")
        self.ui.tempSetShow.setText(str("%02d" % self.t_i_d_count) + " " + "°C")

    def humidityDisplayLabel(self):
        # self.ui.humiditySetShow.setStyleSheet("QLabel { color: yellow ;}")
        self.ui.humiditySetShow.setText(str("%02d" % self.h_i_d_count) + " " + "%")

    # ========================+++++++++++++End Database++++++++++++++++==================
    #                        method called by button
    # ========================+++++++++++++Make All QWidget transparent =================
    def makeBackTransparent(self):
        self.ui.centralWidget.setStyleSheet("background:transparent;")
        '''self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.time_show.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.tick_show.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.day_date_show.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.lcd1.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.ui.horizontalLayout_10.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.time_label.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.elapsedTimeLabel.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.ui.verticalLayout.setStylesheet("QWidget{background-color: rgba(100,100,100,100")
        self.ui.centralWidget.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.tempIcon.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.tempShow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.humidityIcon.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.humidityShow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.tempSetLabel.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.humiditySetLabel.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.tempSetShow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.humiditySetShow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.anaesthesiaTimeLabel.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.humidityLabelName.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.tempLabelName.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.differentialLabel.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.hepaLabel.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.hepaFilterStatus.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.differentialPressureShow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.displayArea.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.label_8.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.label_9.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.medicalGasLabelTitle.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.ui.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.otLighteningDetails.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.ventiLationDetails.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.gasIndicator.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.historyDetails.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.multiMediaDetails.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.btnOn.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.btnOff.setAttribute(Qt.WA_TranslucentBackground, True)'''
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.verticalLayout.setStyleSheet("background:transparent;")
        # self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        # self.ui.verticalLayout.setStylesheet("QWidget{background-color: rgba(100,100,100,100")
        # self.ui.verticalLayout.setAttribute(Qt.WA_TranslucentBackground, True)

    '''def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.lbl1.setText(text)'''

    def hexAdd(self, hex_code):
        print("hexAdd: " + str(hex_code))
        self.add_sub_hex += int(hex_code, 16)
        configVariables.totalHex = hex(self.add_sub_hex)
        # return configVariables.totalHex

    def hexSub(self, hex_code):
        if self.add_sub_hex >= int(hex_code, 16):
            self.add_sub_hex -= int(hex_code, 16)
            configVariables.totalHex = hex(self.add_sub_hex)
        # return configVariables.totalHex

    def startThreadSwitch1(self):
        # self.rt.stop()
        self.swt1 = threading.Thread(target=self.switch1)
        self.swt1.daemon = True
        self.swt1.start()
        # self.swt1.join()

    def switch1(self):
        self.toggleSwitchGasL1Color()
        # self.rt.start()

    def startThreadSwitch2(self):
        # self.rt.stop()
        self.swt2 = threading.Thread(target=self.switch2)
        self.swt2.daemon = True
        self.swt2.start()
        # self.swt2.join()

    def switch2(self):
        self.toggleSwitchGasL2Color()
        # self.rt.start()

    def startThreadSwitch3(self):
        # self.rt.stop()
        self.swt3 = threading.Thread(target=self.switch3)
        self.swt3.daemon = True
        self.swt3.start()
        # self.swt3.join()

    def switch3(self):
        self.toggleSwitchOT1Color()
        # self.rt.start()

    def startThreadSwitch4(self):
        # self.rt.stop()
        self.swt4 = threading.Thread(target=self.switch4)
        self.swt4.daemon = True
        self.swt4.start()
        # self.swt4.join()

    def switch4(self):
        self.toggleSwitchColor()
        # self.rt.start()

    def startThreadSwitch5(self):
        # self.rt.stop()
        self.swt5 = threading.Thread(target=self.switch5)
        self.swt5.daemon = True
        self.swt5.start()
        # self.swt5.join()

    def switch5(self):
        self.toggleSwitchLaminarColor()
        # self.rt.start()

    def startThreadSwitch6(self):
        # self.rt.stop()
        self.swt6 = threading.Thread(target=self.switch6)
        self.swt6.daemon = True
        self.swt6.start()
        # self.swt6.join()

    def switch6(self):
        self.toggleSwitchOT2Color()
        # self.rt.start()

    def startThreadSwitch7(self):
        # self.rt.stop()
        self.swt7 = threading.Thread(target=self.switch7)
        self.swt7.daemon = True
        self.swt7.start()
        # self.swt7.join()

    def switch7(self):
        self.tempSwitch()
        # self.rt.start()

    def startThreadSwitch8(self):
        # self.rt.stop()
        self.swt8 = threading.Thread(target=self.switch8)
        self.swt8.daemon = True
        self.swt8.start()
        # self.swt8.join()

    def switch8(self):
        self.humidSwitch()
        # self.rt.start()

    def tempSwitch(self):
        # if button is checked
        if self.t_i_d_count > 15.1 and self.hex_add_temp == 0:
            self.hexAdd("0x40")
            self.hex_add_temp = 1
            self.hex_minus_temp = 0
            # setting background color to light-blue
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            self.rt.start()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # if it is unchecked
        elif self.t_i_d_count < 15.1 and self.hex_minus_temp == 0:
            # set background color back to light-grey
            self.hexSub("0x40")
            self.hex_minus_temp = 1
            self.hex_add_temp = 0
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            self.rt.start()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))

    def humidSwitch(self):
        # if button is checked
        if self.h_i_d_count > 64.0 and self.hex_add_humidity == 0:
            self.hexAdd("0x80")
            self.hex_add_humidity = 1
            self.hex_minus_humidity = 0
            # setting background color to light-blue
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            self.rt.start()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # if it is unchecked
        elif self.h_i_d_count < 64.0 and self.hex_minus_humidity == 0:
            # set background color back to light-grey
            self.hexSub("0x80")
            self.hex_add_humidity = 0
            self.hex_minus_humidity = 1
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            self.rt.start()

    def toggleSwitchColor(self):
        # if button is checked
        if self.toggleSwitch.isChecked():
            print("Check: " + str(self.toggleSwitch.isChecked()))
            self.hexAdd("0x8")
            # setting background color to light-blue
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            try:
                self.toggleSwitch.setStyleSheet("background-color : #FFFFFF")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb3.setPixmap(configVariables.changed_light_bulb)
            self.rt.start()
            '''self.threadDataSwitchData = ThreadDataSwitchData(self)
            self.threadDataSwitchData.signal.return_signal.connect(self.threadDataSwitchData.function_thread)
            self.threadPoolSwitch.start(self.threadDataSwitchData)'''

            # if it is unchecked
        else:
            # set background color back to light-grey
            print("Uncheck: " + str(self.toggleSwitch.isChecked()))
            self.hexSub("0x8")
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            try:
                self.toggleSwitch.setStyleSheet("background-color : #4c4c4c")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb3.setPixmap(configVariables.low_light_bulb)
            self.rt.start()

    def toggleSwitchLaminarColor(self):
        # if button is checked
        if self.toggleSwitchLaminar.isChecked():

            # setting background color to light-blue
            self.hexAdd("0x10")
            self.rt.stop()
            # setting background color to light-blue
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            try:
                self.toggleSwitchLaminar.setStyleSheet("background-color : #FFFFFF")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb4.setPixmap(configVariables.changed_light_bulb)
            self.rt.start()
            # if it is unchecked
        else:
            self.hexSub("0x10")
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # set background color back to light-grey
            try:
                self.toggleSwitchLaminar.setStyleSheet("background-color : #4c4c4c")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb4.setPixmap(configVariables.low_light_bulb)
            self.rt.start()

    def toggleSwitchGasL1Color(self):
        # if button is checked
        if self.toggleSwitchGasL1.isChecked():
            self.hexAdd("0x1")
            # setting background color to light-blue
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # setting background color to light-blue
            # self.ot_ui.light1Increment.setEnabled(True)
            try:
                self.toggleSwitchGasL1.setStyleSheet("background-color : #FFFFFF")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb1.setPixmap(configVariables.changed_light_bulb)
            self.rt.start()
            # if it is unchecked
        else:
            # self.ot_ui.light1Increment.setEnabled(False)
            self.hexSub("0x1")
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # set background color back to light-grey
            try:
                self.toggleSwitchGasL1.setStyleSheet("background-color : #4c4c4c")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb1.setPixmap(configVariables.low_light_bulb)
            self.rt.start()

    def toggleSwitchGasL2Color(self):
        # if button is checked
        if self.toggleSwitchGasL2.isChecked():
            self.hexAdd("0x2")
            # setting background color to light-blue
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # setting background color to light-blue
            try:
                self.toggleSwitchGasL2.setStyleSheet("background-color : #FFFFFF")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb2.setPixmap(configVariables.changed_light_bulb)
            # if it is unchecked
            self.rt.start()
        else:
            self.hexSub("0x2")
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # set background color back to light-grey
            try:
                self.toggleSwitchGasL2.setStyleSheet("background-color : #4c4c4c")
            except IndexError:
                print("Color")
            self.ot_ui.lightBulb2.setPixmap(configVariables.low_light_bulb)
            self.rt.start()

    def toggleSwitchOT1Color(self):
        # if button is checked
        if self.toggleSwitchOT1.isChecked():
            self.hexAdd("0x4")
            # setting background color to light-blue
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # setting background color to light-blue
            try:
                self.toggleSwitchOT1.setStyleSheet("background-color : #FFFFFF")
            except IndexError:
                print("Color")
            self.ot_ui.otLightBulb1.setPixmap(configVariables.changed_ot_light)
            self.rt.start()
            # if it is unchecked
        else:
            self.hexSub("0x4")
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # set background color back to light-grey
            try:
                self.toggleSwitchOT1.setStyleSheet("background-color : #4c4c4c")
            except IndexError:
                print("Color")
            self.ot_ui.otLightBulb1.setPixmap(configVariables.low_ot_light)
            self.rt.start()

    def toggleSwitchOT2Color(self):
        # if button is checked
        if self.toggleSwitchOT2.isChecked():
            self.hexAdd("0x20")
            # setting background color to light-blue
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # setting background color to light-blue
            try:
                self.toggleSwitchOT2.setStyleSheet("background-color : #FFFFFF")
            except IndexError:
                print("Color")
            self.ot_ui.otLightBulb2.setPixmap(configVariables.changed_ot_light)
            self.rt.start()
            # if it is unchecked
        else:
            self.hexSub("0x20")
            self.rt.stop()
            self.serialWrapper.sendDataToSerialPort()
            # self.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
            # set background color back to light-grey
            try:
                self.toggleSwitchOT2.setStyleSheet("background-color : #4c4c4c")
            except IndexError:
                print("Color")
            self.ot_ui.otLightBulb2.setPixmap(configVariables.low_ot_light)
            self.rt.start()

    # ================= Start Media Player ================================
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.model.layoutChanged.emit()

        # If not playing, seeking to first of newly added + play.
        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "mp3 Audio (*.mp3);mp4 Video (*.mp4);Movie files (*.mov);All files (*.*)")

        if path:
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(path)
                )
            )

        self.model.layoutChanged.emit()

    def update_duration(self, duration):
        print("!", duration)
        print("?", self.player.duration())

        self.multi_ui_media_player.timeSlider.setMaximum(duration)

        if duration >= 0:
            self.multi_ui_media_player.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.multi_ui_media_player.currentTimeLabel.setText(hhmmss(position))

        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.multi_ui_media_player.timeSlider.blockSignals(True)
        self.multi_ui_media_player.timeSlider.setValue(position)
        self.multi_ui_media_player.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.multi_ui_media_player.playlistView.setCurrentIndex(ix)

    def toggle_viewer(self, state):
        # self.viewer.setMinimumSize(QSize(480, 360))
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()
        # self.videoWidget = QVideoWidget(self)

    def erroralert(self, *args):
        print(args)

    # =================End Media Player ================================

    # =====================Start of Settings Dialog===========================================shutdown Management =====
    def shutdownManagement(self):
        if self.ui.powerButton.isChecked():
            self.shutDialog.show()
        else:
            self.shutDialog.hide()
        self.shutDialog.exec_()

    def shutDown(self):
        subprocess.call(["systemctl", "poweroff"])

    def reBoot(self):
        subprocess.call(["systemctl", "reboot"])

    def exitShutDownDialog(self):
        self.shutDialog.close()

    def logOut(self):
        pass

    def suspend(self):
        subprocess.call(["systemctl", "suspend"])  # 6777754577 5677

    def loginDialogOpen(self):
        isVis = self.SettingsQDialog.isVisible()
        if isVis:
            AutoCloseMessageBox.showWithTimeout(3, "All ready user granted", "Login Form",
                                                QMessageBox.Warning)
            print("Login Pass: " + str(isVis))
        else:
            self.login_ui.user_pass.setEchoMode(QLineEdit.Password)
            self.queryGeneralSettingsDataAndSet()
            if self.login_ui.loginButton.isChecked():
                self.loginDialogQtWidget.show()
            else:
                self.loginDialogQtWidget.hide()
            self.loginDialogQtWidget.exec_()

    def check_password(self):
        # print('Lovb: ' + self.loginDataModel.get_user_name() + ' ' + self.loginDataModel.get_user_pass())
        if self.dataModel.get_user_name() == '' and self.dataModel.get_user_pass() == '':
            AutoCloseMessageBox.showWithTimeout(1, "Successfully Login", "Login Form",
                                                QMessageBox.Warning)
            self.userNameLineEdit.setText('')
            self.userPassLineEdit.setText('')
            '''self.login_ui.user_name.setText('')
            self.login_ui.user_pass.setText('')'''
            self.loginDialogQtWidget.close()
            self.settingsDialogOpen()
        else:
            AutoCloseMessageBox.showWithTimeout(3, "Incorrect Password", "Login Form",
                                                QMessageBox.Warning)
            '''self.login_ui.user_name.setText('')
            self.login_ui.user_pass.setText('')'''
            self.userNameLineEdit.setText('')
            self.userPassLineEdit.setText('')

        '''
            def check_password(self):
        if self.login_ui.user_name.text() == 'admin' and self.login_ui.user_pass.text() == 'pass':
            AutoCloseMessageBox.showWithTimeout(1, "Successfully Login", "Login Form",
                                                QMessageBox.Warning)
            self.login_ui.user_name.setText('')
            self.login_ui.user_pass.setText('')
            self.loginDialogQtWidget.close()
            self.settingsDialogOpen()
        else:
            AutoCloseMessageBox.showWithTimeout(3, "Incorrect Password", "Login Form",
                                                QMessageBox.Warning)
            self.login_ui.user_name.setText('')
            self.login_ui.user_pass.setText('')
        '''
        # self.doAnim()

    '''def doAnim(self):
        self.anim = QPropertyAnimation(self.loginDialogQtWidget, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(150, 30, 100, 100))
        self.anim.setEndValue(QRect(150, 30, 200, 200))
        self.anim.start()'''

    def settingsDialogOpen(self):
        self.queryGeneralSettingsDataAndSet()
        # ======== Icon Color Set from database ====================================================
        self.database_manage.queryIconColorSettings(self.dataModel)
        self.colorCborderColor.default_color_database(self.dataModel)
        self.colorCbackgroundColor.default_color_database(self.dataModel)
        self.colorCtextColor.default_color_database(self.dataModel)
        self.IconColorControlObj.default_color_database(self.dataModel)
        # ==========================================================================================
        if self.ui.settingsButton.isChecked():
            self.SettingsQDialog.show()
        else:
            self.SettingsQDialog.hide()

        self.SettingsQDialog.exec_()

    def telephoneDialogOpen(self):
        window = TelephoneDialog()
        # self.telephoneQtWidget.exec_()

    def changeNameLabel(self):
        self.clear()
        self.layoutCentralSettingsWidget.addWidget(self.labelNameFormWidget)
        self.labelNameFormWidget.show()
        # self.hisForm.hide()
        # self.otForm.show()
        # self.mulFormWindo.hide()
        # self.mulForm.hide()
        # self.gasForm.hide()

    '''def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        path = QPainterPath()
        path.moveTo(15, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        qp.drawPath(path)'''

    '''def paintEvent(self, event):
        rgb = self.hex_to_rgb(self.dataModel.get_text_col())

        print("My Color:"+self.dataModel.get_text_col()+" "+str(rgb[0])+" "+str(rgb[1])+" "+str(rgb[2]))
        self.myLineColor = QColor(rgb[0], rgb[1], rgb[2])
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setPen(QPen(self.myLineColor, 1, Qt.SolidLine))
        self.painter.setBrush(QBrush(self.myLineColor, Qt.SolidPattern))
        # self.painter.drawEllipse(40, 40, 400, 400)
        self.painter.drawLine(750, 280, 250, 280)
        self.painter.drawLine(1350, 280, 900, 280)
        # self.painter.drawArc(300, 70, 300, 300, 0 * 16, 90 * 16)
        self.painter.end()'''

    def hex_to_rgb(self, hx, hsl=False):
        """Converts a HEX code into RGB or HSL.
        Args:
            hx (str): Takes both short as well as long HEX codes.
            hsl (bool): Converts the given HEX code into HSL value if True.
        Return:
            Tuple of length 3 consisting of either int or float values."""
        if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
            div = 255.0 if hsl else 0
            if len(hx) <= 4:
                return tuple(int(hx[i] * 2, 16) / div if div else
                             int(hx[i] * 2, 16) for i in (1, 2, 3))
            else:
                return tuple(int(hx[i:i + 2], 16) / div if div else
                             int(hx[i:i + 2], 16) for i in (1, 3, 5))
        else:
            raise ValueError(f'"{hx}" is not a valid HEX code.')

    # ===================== End of Settings Dialog ===========================================


'''
    def changSystemTime(self):
        try:
            subprocess.check_call("ntpdate")  # Non-zero exit code means it was unable to get network time
        except subprocess.CalledProcessError:
            dt = getRTCTime()  # Get time from RTC as a datetime object
            subprocess.call(['sudo', 'date', '-s', '{:}'.format(dt.strftime('%Y/%m/%d %H:%M:%S'))],
                            shell=True)  # Sets system time (Requires root, obviously)'''


# =================End Set Clock ===============================================================


# I feel better having one of these
def main():
    # a new app instance
    import time
    app = QApplication(sys.argv)
    app.setStyle("QtCurve")  # dataModel.get_power_on_image_path()
    dataModel = DataModel()
    database_manage = database.DataBaseManagement()
    database_manage.init('datafile', 'QSQLITE')
    database_manage.queryAppearanceSettingsData(dataModel)
    splash_pix = QPixmap(dataModel.get_power_on_image_path())
    # -------------------------Splash screeen Image ----------------------------------------------------------
    # self.splash_pix = QPixmap(self.dataModel.get_power_on_image_path())
    # from.splash_pix
    # -------------------------Splash Screen Image ----------------------------------------------------------
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # splash = QSplashScreen(splash_pix, Qt.WindowMinimizeButtonHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    # splash = QSplashScreen(splash_pix)
    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)

    splash.setMask(splash_pix.mask())

    splash.showFullScreen()
    splash.showMessage("<h1><font color='green'>Welcome to Digiline System Pvt. Ltd!</font></h1>",
                       Qt.AlignTop | Qt.AlignCenter, Qt.black)

    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    # Simulate something that takes time
    time.sleep(1)
    '''
    movie = QMovie(dataModel.get_power_on_image_path())
    # movie = QMovie("animation.gif")
    splash = MovieSplashScreen(movie)
    splash.showFullScreen()
    start = time.time()
    while movie.state() == QMovie.Running and time.time() < start + 10:
        app.processEvents()
    '''

    form = MainWindow()
    form.showFullScreen()
    splash.finish(form)
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
