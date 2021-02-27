import time

from PyQt5.QtCore import pyqtSlot, QRunnable, QObject, pyqtSignal

import configVariables
from Database import switchdatabase


class Signals(QObject):
    return_signal = pyqtSignal(str)


class ThreadGasColorRXTX(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(ThreadGasColorRXTX, self).__init__()
        self.signal = Signals()
        self.ui = ui
        # =========+Alarm History Details Database Manage+=============================================
        configVariables.light_database = switchdatabase.LightSwitchDataBase()
        configVariables.light_database.init('lighthistory', 'QSQLITE', 'history')
        # configVariables.light_database.init('lighthistory', 'QSQLITE', 'image_con')

    @pyqtSlot()
    def run(self):
        # time.sleep(5)
        result = "RXTX"
        while True:
            self.signal.return_signal.emit(result)
            time.sleep(1)
        # ------------------------------------------------------
        # self.ui.settings_dialog_set_ui.labelDisplayTheme.setPixmap(QtGui.QPixmap(self.ui.dataModel.get_theme_color_preview()))
        # self.ui.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.ui.SettingsQDialog)

        # self.signal.return_signal.emit(result)

    def function_thread(self, signal):
        # self.ui.drawRealTimeData()
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj) self.threadpool.destroyed() Index out
        # of range error if configVariables.hex_string[0] == 0x2 and configVariables.hex_string[1] == 0x31 \ in
        # rasberry pi
        # Aborted in rasberry pi
        if configVariables.hex_string[0] == 0x2 and configVariables.hex_string[1] == 0x31 and \
                configVariables.hex_string[2] == 0x43 and configVariables.hex_string[21] == 0x20:
            x7 = bin(0b10000000)
            x6 = bin(0b01000000)
            x5 = bin(0b00100000)
            x4 = bin(0b00010000)
            x3 = bin(0b00001000)
            x2 = bin(0b00000100)
            x1 = bin(0b00000010)
            x0 = bin(0b00000001)
            x8 = bin(0b0001)
            x9 = bin(0b0010)
            x10 = bin(0b0100)
            x11 = bin(0b1000)
            x12 = bin(0b00100000)# 100000
            x13 = bin(0b00010000)  # 10000

            # bit8 = bool(x & 0b01000000)
            binary_value = "{0:b}".format(configVariables.hex_string[4])
            binary_value1 = "{0:b}".format(configVariables.hex_string[3])
            # binary_value = bin(configVariables.hex_string[4])
            bit7 = bool(int(binary_value, 2) & int(x7, 2))
            bit6 = bool(int(binary_value, 2) & int(x6, 2))
            bit5 = bool(int(binary_value, 2) & int(x5, 2))
            bit4 = bool(int(binary_value, 2) & int(x4, 2))
            bit3 = bool(int(binary_value, 2) & int(x3, 2))
            bit2 = bool(int(binary_value, 2) & int(x2, 2))
            bit1 = bool(int(binary_value, 2) & int(x1, 2))
            bit0 = bool(int(binary_value, 2) & int(x0, 2))

            bit8 = bool(int(binary_value1, 2) & int(x8, 2))
            bit9 = bool(int(binary_value1, 2) & int(x9, 2))
            bit10 = bool(int(binary_value1, 2) & int(x10, 2))
            bit11 = bool(int(binary_value1, 2) & int(x11, 2))
            bit12 = bool(int(binary_value1, 2) & int(x12, 2))
            bit13 = bool(int(binary_value1, 2) & int(x13, 2))
            print("-----bit12--------"+str(bit12)+"-----------------bit13----------------"+str(bit13)+"-----------------")

            # bit8 = bool(binary_value >> 8)
            # print("Bit: " + str(bit7))

            '''if configVariables.hex_string[0] == 0x2 and configVariables.hex_string[1] == 0x31 and \
                configVariables.hex_string[2] == 0x43 and configVariables.hex_string[21] == 0x20:'''

            if bit1:
                # Low
                configVariables.buzzer_hex_gas_2 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu----------------------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_high, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_1(), "Low")

                # ++++++++++++++++++++++++ High Alarm Data Save in History Table +++++++++++++++++++++++++++

            elif bit0:
                # High
                configVariables.buzzer_hex_gas_2 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_low, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_1(), "High")
                # ++++++++++++++++++++++++ High Alarm Data Save in History Table +++++++++++++++++++++++++++

            elif not bit1 and not bit0:
                configVariables.buzzer_hex_gas_2 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.green_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit3:
                # Low
                configVariables.buzzer_hex_gas_4 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_normal, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_2(), "Low")
            elif bit2:
                # High
                configVariables.buzzer_hex_gas_4 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_low, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_2(), "High")
                # +++++++++++++++++++ gas_name_1 is oxygen +++++++++++++++++++++++++++++++++++++++++++++++++

            elif not bit3 and not bit2:
                configVariables.buzzer_hex_gas_4 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit5:
                # Low
                configVariables.buzzer_hex_gas_5 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.red_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_high, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_3(), "Low")

            elif bit4:
                # High
                configVariables.buzzer_hex_gas_5 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_low, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_normal, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_3(), "High")
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif not bit5 and not bit4:
                configVariables.buzzer_hex_gas_5 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit7:
                # Low
                configVariables.buzzer_hex_gas_3 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_high, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_4(), "Low")

            elif bit6:
                # High
                configVariables.buzzer_hex_gas_3 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_low, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_4(), "High")

            elif not bit7 and not bit6:
                configVariables.buzzer_hex_gas_3 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_low, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_normal, "QLabel",
                                                                    configVariables.green_color_hex)

            if bit9:
                # Low
                configVariables.buzzer_hex_gas_1 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_high, "QLabel",
                                                                    configVariables.white_color_hex)
                # ++++++++++++++++++++++++ Low Alarm Data Save in History Table ++++++++++++++++++++++++++++
                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                self.ui.dataModel.get_gas_name_5()
                print("Gas Name 1 Low: " + self.ui.dataModel.get_gas_name_5() + " Date Time: " + self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_5(), "Low")
            elif bit8:
                # High
                configVariables.buzzer_hex_gas_1 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ----------------------------------Gas pad menu--------------------------------------------
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_low, "QLabel",
                                                                    configVariables.white_color_hex)
                # ++++++++++++++++++++++++ High Alarm Data Save in History Table +++++++++++++++++++++++++++
                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                self.ui.dataModel.get_gas_name_5()
                print("Gas Name 1 High: " + self.ui.dataModel.get_gas_name_5() + " Date Time: " + self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_5(), "High")
                # +++++++++++++++ Gas Five Carbondioxide +++++++++++++++++++++++++++++++++++++++++++++++++++

            elif not bit8 and not bit9:
                configVariables.buzzer_hex_gas_1 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.green_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_high, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit11:
                # High
                configVariables.buzzer_hex_gas_6 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.red_color_hex)
                # self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_high, "QLabel",
                #  configVariables.vacuum_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                # configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                #                                                 self.ui.dataModel.get_gas_name_6(), "High")
            elif bit10:
                # Low
                configVariables.buzzer_hex_gas_6 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.red_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_normal, "QLabel",
                                                                    configVariables.white_color_hex)

                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_6(), "Low")
            elif not bit11 and not bit10:
                configVariables.buzzer_hex_gas_6 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_low, "QLabel",
                                                                    configVariables.white_color_hex)
            '''if bit12:
                configVariables.buzzer_hex_gas_6 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.ips, "QToolButton",
                                                                    configVariables.red_color_hex)'''

            if bit12:
                configVariables.buzzer_hex_gas_7 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.ips, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ++++++++++++++++++++++++ High Alarm Data Save in History Table +++++++++++++++++++++++++++
                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                self.ui.dataModel.get_gas_name_7()
                print("Gas Name 7 High: " + self.ui.dataModel.get_gas_name_7() + " Date Time: " + self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 self.ui.dataModel.get_gas_name_7(), "High")

            elif not bit12:
                configVariables.buzzer_hex_gas_7 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.ips, "QToolButton",
                                                                    configVariables.green_color_hex)

            if bit13:
                configVariables.buzzer_hex_gas_8 = 0x01
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.hepa, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ++++++++++++++++++++++++ High Alarm Data Save in History Table +++++++++++++++++++++++++++
                self.ui.dataModel.set_alarm_date_time(self.ui.proc)
                # self.ui.dataModel.get_gas_name_8()
                # print("Gas Name 7 High: " + self.ui.dataModel.get_gas_name_8() + " Date Time: " + self.ui.proc)
                configVariables.light_database.insertHistoryData(self.ui.dataModel.get_alarm_date_time(),
                                                                 "Hepa", "High")

            elif not bit13:
                configVariables.buzzer_hex_gas_8 = 0x00
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.hepa, "QToolButton",
                                                                    configVariables.green_color_hex)

                # High

        # print(configVariables.hex_string)
        # print(signal)
