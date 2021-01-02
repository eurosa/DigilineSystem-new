from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, QTimer


class Signals(QObject):
    return_signal = pyqtSignal(str)


class ThreadParallel(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(ThreadParallel, self).__init__()
        self.signal = Signals()
        self.ui = ui

    def run(self):
        # time.sleep(5)
        result = "Some String"
        # ======================= Login UI ==========================================================================
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

        # -------------------------- history menu data text color change ---------------------------
        self.ui.alldisplayColorChangeObj.changeTableViewAttributeColor(self.ui.tableWidget, "QTableView")
        # -------------------------- Multimedia Menu Color & Font Settings -------------------------

        # -------------------------------------------------------------------------
        # ----------------culprit below------------------------------------------------------------------------

        # self.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.shutDialog)
        # self.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.loginDialogQtWidget)
        # self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.setTimerWidget)
        # self.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.SettingsQDialog)  # 8 timer problem

        #---------------------------------------------------------------------

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
        # self.alldisplayColorChangeObj.changePlayerAttributeColor(AutoCloseMessageBox())
        # -------------------------- Login Dialog Color -----------------------------------------------------------------------------------------

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

        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.chooseLogo,
                                                           "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.choosePowerOnScreenImage,
                                                           "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.settings_dialog_set_ui.chooseBackGroundImage,
                                                           "QPushButton")
        self.ui.alldisplayColorChangeObj.changeShutDownDialogAttributeColor(self.ui.shutDialog)
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.shutDownButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.rebootButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.cancelShutButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.shutDown_ui.logoutButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeAttributeColor(self.ui.login_ui.loginButton, "QPushButton")
        self.ui.alldisplayColorChangeObj.changeLoginDialogAttributeColor(self.ui.loginDialogQtWidget)
        self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.setTimerWidget)
        # self.settings_dialog_set_ui.tabGeneral.setStyleSheet("color: " + self.dataModel.get_text_col() + ";")
        # self.settings_dialog_set_ui.tabColor.setStyleSheet("color: " + self.dataModel.get_text_col() + ";")
        # ++++++++++++++++++++++++++++++ Settings Dialog UI Color Changes ++++++++++++++++++++++++++++++++++
        # =============================== Settings Dialog ==================================================
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.settings_dialog_set_ui.light1,
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
                                                                   "QTextEdit")

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
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelBackGroundColor,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelTextColor,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelIconColor,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelTheme,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelBackGroundImage,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLogo,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelPowerOnImage,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelLightTitle,
                                                                  "QLabel")
        self.ui.alldisplayColorChangeObj.changeDisplayLabelTextColor(self.ui.settings_dialog_set_ui.labelGasAlarmTitle,
                                                                  "QLabel")

        # =============================== Settings End ==========================================================================================
        # =============================== Login UI ==============================================================================================
        '''self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.login_ui.user_name,
                                                                   "QLineEdit")
        self.ui.alldisplayColorChangeObj.changeEditTextAttributeColor(self.ui.login_ui.user_pass,
                                                                   "QLineEdit")'''

        # ---------------------New---------------------------------------------------------------------------
        '''self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.settings_dialog_set_ui.tabColor)
        self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.settings_dialog_set_ui.tabGeneral)
        self.ui.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.ui.settings_dialog_set_ui.tabTheme)'''
        # ---------------------New---------------------------------------------------------------------------
        # self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabTheme)
        # self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabColor)
        # self.alldisplayColorChangeObj.changeTimerDialogAttributeColor(self.settings_dialog_set_ui.tabGeneral)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        # self.ui.modifyGlobalVariablesObj.setChangedImage()
        # self.ui.modifyGlobalVariablesObj.setChangedLightColor()
        # self.ui.lightBrightnessObject.allLightBarInitialSetup(self.ui.ot_ui)
        self.signal.return_signal.emit(result)

    def function_thread(self, signal):
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        # self.threadpool.destroyed()
        print("My Goodness")
        print(signal)
