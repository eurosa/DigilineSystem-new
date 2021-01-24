import time

from PyQt5.QtCore import pyqtSlot, QRunnable, QObject, pyqtSignal

import configVariables


class Signals(QObject):
    return_signal = pyqtSignal(str)


class ThreadGasColorRXTX(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(ThreadGasColorRXTX, self).__init__()
        self.signal = Signals()
        self.ui = ui

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
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        # self.threadpool.destroyed()
        if configVariables.hex_string:
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

            # bit8 = bool(binary_value >> 8)
            # print("Bit: " + str(bit7))

        if configVariables.hex_string:
            if bit1:
                # High
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_low, "QLabel",
                                                                    configVariables.white_color_hex)

            elif bit0:
                # Low
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_high, "QLabel",
                                                                    configVariables.white_color_hex)

            elif not bit1 and not bit0:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.green_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_5_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit3:
                # High
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_low, "QLabel",
                                                                    configVariables.white_color_hex)
            elif bit2:
                # Low
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_high, "QLabel",
                                                                    configVariables.white_color_hex)

            elif not bit3 and not bit2:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.green_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_1_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit5:
                # High
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_low, "QLabel",
                                                                    configVariables.white_color_hex)

            elif bit4:
                # Low
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_high, "QLabel",
                                                                    configVariables.white_color_hex)
            elif not bit5 and not bit4:

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_low, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_4_normal, "QLabel",
                                                                    configVariables.green_color_hex)

            if bit7:
                # High
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_low, "QLabel",
                                                                    configVariables.white_color_hex)

            elif bit6:
                # Low
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.red_color_hex)
                # ---------Gas pad menu---------------------------------------------------------

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_normal, "QLabel",
                                                                    configVariables.white_color_hex)

            elif not bit7 and not bit6:

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_2_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit9:
                # High
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_high, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_low, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_normal, "QLabel",
                                                                    configVariables.white_color_hex)
            elif bit8:
                # Low
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.red_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_normal, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_high, "QLabel",
                                                                    configVariables.white_color_hex)

            elif not bit8 and not bit9:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_high, "QLabel",
                                                                    configVariables.white_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_3_low, "QLabel",
                                                                    configVariables.white_color_hex)

            if bit11:
                # High
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.red_color_hex)
                # self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_high, "QLabel",
                #  configVariables.vacuum_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_normal, "QLabel",
                                                                    configVariables.white_color_hex)
            elif bit10:
                # Low
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.red_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_low, "QLabel",
                                                                    configVariables.red_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_normal, "QLabel",
                                                                    configVariables.white_color_hex)
            elif not bit11 and not bit10:

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.green_color_hex)

                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_normal, "QLabel",
                                                                    configVariables.green_color_hex)
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.gas_ui.gasLabel_6_low, "QLabel",
                                                                    configVariables.white_color_hex)
        # print(configVariables.hex_string)
        # print(signal)
