import math
import threading
import time
from multiprocessing.pool import ThreadPool

import serial
from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor

import configVariables
from Database import switchdatabase
from repeatedTimer import RepeatedTimer


class SerialWrapper:
    def __init__(self, device, ui):
        self.s = None
        self.port = device
        self.ui = ui
        # self.ser = serial.Serial(device, 115200)
        # self.ser1 = serial.Serial(device, 9600)
        self.cw = [0x02, 0x31, 0x43, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46,
                   0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x20]

        '''self.database_manage = switchdatabase.DataBaseManagement()
        self.database_manage.init('switchcontrol', 'QSQLITE')
        self.database_manage.queryThemeColorSettings(self.dataModel)'''

        '''self.ser1 = serial.Serial(
            port=device,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)'''

    '''def sendData(self, data):
        data += "\r\n"
        self.ser.write(data.encode())'''

    # def sendDataToSerialPort(self, hex_code):
    def setRepeater(self, repeater):
        self.repeater = repeater

    def getRepeater(self):
        return self.repeater

    def sendDataToSerialPort(self):

        self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)

        # print("Converted Hex: " + str(hex_code))
        light_hex = int(configVariables.totalHex, 16)
        # ================================== Intensity Control Start 1==========================================
        # print("Light Intensity:" + str(configVariables.intensity_hex_1))
        # print("Converted Hex: " + hex(configVariables.intensity_hex_1))
        low_1, high_1 = self.bytes1(int(hex(configVariables.intensity_hex_1), 16))

        # int_low = bin(int(low, 16)).replace("0b", "")
        # int_high = bin(int(high, 16)).replace("0b", "")
        # binary_low = "{0:b}".format(int_low)
        # binary_high = "{0:b}".format(int_high)
        # print("Low Hex: " + low + " Int Low: " + int_low)
        # print("High Hex: " + high + " Int High: " + int_high)
        hex_low_int_1 = int(low_1, 16)
        hex_high_int_1 = int(high_1, 16)
        # print("Low Hex: " + str(hex_low) + " Int Low: " + str(int_low))
        # print("High Hex: " + str(hex_high) + " Int High: " + str(int_high))
        # ================================== Intensity Control Start 2==========================================
        # print("Light Intensity:" + str(configVariables.intensity_hex_1))
        # print("Converted Hex: " + hex(configVariables.intensity_hex_1))
        low_2, high_2 = self.bytes1(int(hex(configVariables.intensity_hex_2), 16))

        # int_low = bin(int(low, 16)).replace("0b", "")
        # int_high = bin(int(high, 16)).replace("0b", "")
        # binary_low = "{0:b}".format(int_low)
        # binary_high = "{0:b}".format(int_high)
        # print("Low Hex: " + low + " Int Low: " + int_low)
        # print("High Hex: " + high + " Int High: " + int_high)
        hex_low_int_2 = int(low_2, 16)
        hex_high_int_2 = int(high_2, 16)
        # print("Low Hex: " + str(hex_low) + " Int Low: " + str(int_low))
        # print("High Hex: " + str(hex_high) + " Int High: " + str(int_high))
        # ================================== Intensity Control End ==================================================
        # ================================== Intensity Control Start 3==========================================
        # print("Light Intensity:" + str(configVariables.intensity_hex_1))
        # print("Converted Hex: " + hex(configVariables.intensity_hex_1))
        low_3, high_3 = self.bytes1(int(hex(configVariables.intensity_hex_3), 16))

        # int_low = bin(int(low, 16)).replace("0b", "")
        # int_high = bin(int(high, 16)).replace("0b", "")
        # binary_low = "{0:b}".format(int_low)
        # binary_high = "{0:b}".format(int_high)
        # print("Low Hex: " + low + " Int Low: " + int_low)
        # print("High Hex: " + high + " Int High: " + int_high)
        hex_low_int_3 = int(low_3, 16)
        hex_high_int_3 = int(high_3, 16)
        # print("Low Hex: " + str(hex_low) + " Int Low: " + str(int_low))
        # print("High Hex: " + str(hex_high) + " Int High: " + str(int_high))
        # ================================== Intensity Control End ==================================================
        # ================================== Intensity Control Start 4==========================================
        # print("Light Intensity:" + str(configVariables.intensity_hex_1))
        # print("Converted Hex: " + hex(configVariables.intensity_hex_1))
        low_4, high_4 = self.bytes1(int(hex(configVariables.intensity_hex_4), 16))

        # int_low = bin(int(low, 16)).replace("0b", "")
        # int_high = bin(int(high, 16)).replace("0b", "")
        # binary_low = "{0:b}".format(int_low)
        # binary_high = "{0:b}".format(int_high)
        # print("Low Hex: " + low + " Int Low: " + int_low)
        # print("High Hex: " + high + " Int High: " + int_high)
        hex_low_int_4 = int(low_4, 16)
        hex_high_int_4 = int(high_4, 16)
        # print("Low Hex: " + str(hex_low) + " Int Low: " + str(int_low))
        # print("High Hex: " + str(hex_high) + " Int High: " + str(int_high))
        # ================================== Intensity Control End ==================================================
        # ================================== Temperature and Humidity Control Start =================================
        print("Temp: " + str(configVariables.temp_send_data) + " Hum: " + str(configVariables.hum_send_data))
        low_5, high_5 = self.bytes1(int(hex(configVariables.temp_send_data), 16))
        low_6, high_6 = self.bytes1(int(hex(configVariables.hum_send_data), 16))
        hex_low_temp_5 = int(low_5, 16)
        hex_high_temp_5 = int(high_5, 16)
        hex_low_hum_6 = int(low_6, 16)
        hex_high_hum_6 = int(high_6, 16)
        # ================================== Temperature and Humidity Control End ===================================
        # ================================== Buzzer Control ========================================================
        buzzer_hex = (configVariables.buzzer_hex_gas_1 | configVariables.buzzer_hex_gas_2 |
                      configVariables.buzzer_hex_gas_3 | configVariables.buzzer_hex_gas_4 |
                      configVariables.buzzer_hex_gas_5 | configVariables.buzzer_hex_gas_6 |
                      configVariables.buzzer_hex_gas_7 | configVariables.buzzer_hex_gas_8)

        print("Buzzer Hex: " + " " + str(configVariables.buzzer_hex_gas_1 | configVariables.buzzer_hex_gas_2 |
                                         configVariables.buzzer_hex_gas_3 | configVariables.buzzer_hex_gas_4 |
                                         configVariables.buzzer_hex_gas_5 | configVariables.buzzer_hex_gas_6))

        # misc code here
        # thestring = "\x02\x31\x43\x46\xFF\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20"
        # command = b'\x02\x31\x43\x02\x0F\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20\n'
        cw = [0x02, 0x31, 0x43, buzzer_hex, light_hex,
              hex_low_int_1, hex_high_int_1,
              hex_low_int_2, hex_high_int_2,
              hex_low_int_3, hex_high_int_3,
              0x0, 0x0, 0x0, 0x0,
              hex_low_int_4, hex_high_int_4,
              hex_low_temp_5, hex_high_temp_5,
              hex_low_hum_6, hex_high_hum_6, 0x20]

        '''while True:
            cc = str(self.ser1.read_all())
            print(cc[0:])'''
        try:
            # self.getRepeater().stop()
            self.ser1.write(serial.to_bytes(cw))
            self.s = self.ser1.read(22)
            '''
            pool = ThreadPool(processes=1)

            async_result = pool.apply_async(self.ser1.read, (22,))  # tuple of args for foo

            # do some other stuff in the main process

            self.s = async_result.get()  # get the return value from your function.
            '''
            # self.getRepeater().start()
            # print("Read RX")
        except Exception as e:
            print("--- abnormal ---：", e)
        time.sleep(0.5)  # Sleep for 3 seconds
        self.ser1.close()
        configVariables.hex_string = self.s
        # time.sleep(1)
        # =================================== Thread to color changes ====================

        if self.s:
            print(str(self.s[0]) + " " +
                  str(self.s[1]) + " " +
                  str(self.s[2]) + " " +
                  str(self.s[3]) + " " +
                  str(self.s[4]) + " " +
                  str(self.s[5]) + " " +
                  str(self.s[6]) + " " +
                  str(self.s[7]) + " " +
                  str(self.s[8]) + " " +
                  str(self.s[9]) + " " +
                  str(self.s[10]) + " " +
                  str(self.s[11]) + " " +
                  str(self.s[12]) + " " +
                  str(self.s[13]) + " " +
                  str(self.s[14]) + " " +
                  str(self.s[15]) + " " +
                  str(self.s[16]) + " " +
                  str(self.s[17]) + " " +
                  str(self.s[18]) + " " +
                  str(self.s[19]) + " " +
                  str(self.s[20]) + " " +
                  str(self.s[21]))
            print(str(hex(self.s[0])) + " " +
                  str(hex(self.s[1])) + " " +
                  str(hex(self.s[2])) + " " +
                  str(hex(self.s[3])) + " " +
                  str(hex(self.s[4])) + " " +
                  str(hex(self.s[5])) + " " +
                  str(hex(self.s[6])) + " " +
                  str(hex(self.s[7])) + " " +
                  str(hex(self.s[8])) + " " +
                  str(hex(self.s[9])) + " " +
                  str(hex(self.s[10])) + " " +
                  str(hex(self.s[11])) + " " +
                  str(hex(self.s[12])) + " " +
                  str(hex(self.s[13])) + " " +
                  str(hex(self.s[14])) + " " +
                  str(hex(self.s[15])) + " " +
                  str(hex(self.s[16])) + " " +
                  str(hex(self.s[17])) + " " +
                  str(hex(self.s[18])) + " " +
                  str(hex(self.s[19])) + " " +
                  str(hex(self.s[20])) + " " +
                  str(hex(self.s[21])))
            if configVariables.hex_string[0] == 0x2 and configVariables.hex_string[1] == 0x31 and \
                    configVariables.hex_string[2] == 0x43 and configVariables.hex_string[21] == 0x20:
                temp_data_read_hex = self.joinHex(self.s[5], self.s[6])
                hum_data_read_hex = self.joinHex(self.s[7], self.s[8])
                air_pressure_data_read_hex = self.joinHex(self.s[9], self.s[10])
                # shifts decimal place left
                temp_data_read = int(hex(temp_data_read_hex), 16) / 10
                # shifts decimal place left
                hum_data_read = int(hex(hum_data_read_hex), 16) / 10
                air_pressure_data_read = int(hex(air_pressure_data_read_hex), 16)

                # ++++++++++++++++++++ Temp , Humidity, Pressure UI update +++++++++++++++++++
                self.ui.ui.tempShow.setText(str(temp_data_read))
                self.ui.ui.humidityShow.setText(str(hum_data_read))
                self.ui.ui.differentialPressureShow.setText(str(air_pressure_data_read))

                configVariables.temp_read_value = temp_data_read
                configVariables.hum_read_value = hum_data_read
                configVariables.air_pressure_value = air_pressure_data_read
                # ++++++++++++++++++++ Temp , Humidity, Pressure UI update +++++++++++++++++++

                self.ui.startThreadSwitch7()
                self.ui.startThreadSwitch8()
        '''if self.s:
            print("01: " + self.s[0])
            print("02: " + str(self.s[1]))
            print("03: " + str(self.s[2]))
            print("04: " + str(self.s[3]))
            print("05: " + str(self.s[4]))
            print("06: " + str(self.s[5]))
            print("07: " + str(self.s[6]))
            print("08: " + str(self.s[7]))
            print("09: " + str(self.s[8]))
            print("10: " + str(self.s[9]))
            print("11: " + str(self.s[10]))
            print("12: " + str(self.s[11]))
            print("13: " + str(self.s[12]))
            print("14: " + str(self.s[13]))
            print("15: " + str(self.s[14]))
            print("16: " + str(self.s[15]))
            print("17: " + str(self.s[16]))
            print("18: " + str(self.s[17]))
            print("19: " + str(self.s[18]))
            print("20: " + str(self.s[19]))
            print("21: " + str(self.s[20]))
            print("22: " + str(self.s[21]))'''

        # time.sleep(1)  # Sleep for 1 seconds

    def joinHex(self, low, high):
        sizeof_high = 0
        # get size of b in bits
        while int(hex(high), 16) >> sizeof_high > 0:
            sizeof_high += 1

        # every position in hex in represented by 4 bits
        sizeof_high_hex = math.ceil(sizeof_high / 4) * 4
        low_data = int(hex(low), 16)
        high_data = int(hex(high), 16)
        hex_data = hex((low_data << sizeof_high_hex) | high_data)
        print(str(hex_data))
        return int(hex_data, 16)

    def bytes1(self, num):
        return hex(num >> 8), hex(num & 0xFF)

    def sendDataToSerialPortIntensity(self, lightintensity):
        print("Light Intensity:" + str(lightintensity))
        print("Converted Hex: " + hex(lightintensity))
        low, high = self.bytes1(int(hex(lightintensity), 16))

        new_hex = int(configVariables.totalHex, 16)
        int_low = bin(int(low, 16)).replace("0b", "")
        int_high = bin(int(high, 16)).replace("0b", "")
        # binary_low = "{0:b}".format(int_low)
        # binary_high = "{0:b}".format(int_high)
        # print("Low Hex: " + low + " Int Low: " + int_low)
        # print("High Hex: " + high + " Int High: " + int_high)
        hex_low = int(low, 16)
        hex_high = int(high, 16)
        print("Low Hex: " + low + " Int Low: " + str(hex_low))
        print("High Hex: " + high + " Int High: " + str(int_high))
        # misc code here
        thestring = "\x02\x31\x43\x46\xFF\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20"
        command = b'\x02\x31\x43\x02\x0F\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20\n'
        cw = [0x02, 0x31, 0x43, 0x46, new_hex, hex(hex_low), hex(hex_high), 0x46, 0x46, 0x46, 0x46,
              0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x20]

        self.ser1.write(serial.to_bytes(cw))
        '''while True:
            cc = str(self.ser1.read_all())
            print(cc[0:])'''
        try:
            # self.getRepeater().stop()
            self.s = self.ser1.read(22)
            # self.getRepeater().start()
            # print("Read RX")
        except IOError as exc:
            print("HELLO IO")
        configVariables.hex_string = self.s
        time.sleep(1)
        # =================================== Thread to color changes ====================
        if self.s:
            print(str(hex(self.s[0])) + " " +
                  str(hex(self.s[1])) + " " +
                  str(hex(self.s[2])) + " " +
                  str(hex(self.s[3])) + " " +
                  str(hex(self.s[4])) + " " +
                  str(hex(self.s[5])) + " " +
                  str(hex(self.s[6])) + " " +
                  str(hex(self.s[7])) + " " +
                  str(hex(self.s[8])) + " " +
                  str(hex(self.s[9])) + " " +
                  str(hex(self.s[10])) + " " +
                  str(hex(self.s[11])) + " " +
                  str(hex(self.s[12])) + " " +
                  str(hex(self.s[13])) + " " +
                  str(hex(self.s[14])) + " " +
                  str(hex(self.s[15])) + " " +
                  str(hex(self.s[16])) + " " +
                  str(hex(self.s[17])) + " " +
                  str(hex(self.s[18])) + " " +
                  str(hex(self.s[19])) + " " +
                  str(hex(self.s[20])) + " " +
                  str(hex(self.s[21])))
        '''if self.s:
            print("01: " + self.s[0])
            print("02: " + str(self.s[1]))
            print("03: " + str(self.s[2]))
            print("04: " + str(self.s[3]))
            print("05: " + str(self.s[4]))
            print("06: " + str(self.s[5]))
            print("07: " + str(self.s[6]))
            print("08: " + str(self.s[7]))
            print("09: " + str(self.s[8]))
            print("10: " + str(self.s[9]))
            print("11: " + str(self.s[10]))
            print("12: " + str(self.s[11]))
            print("13: " + str(self.s[12]))
            print("14: " + str(self.s[13]))
            print("15: " + str(self.s[14]))
            print("16: " + str(self.s[15]))
            print("17: " + str(self.s[16]))
            print("18: " + str(self.s[17]))
            print("19: " + str(self.s[18]))
            print("20: " + str(self.s[19]))
            print("21: " + str(self.s[20]))
            print("22: " + str(self.s[21]))'''

        # time.sleep(1)  # Sleep for 1 seconds

    def graphData(self):
        # ----------------------- Send to Database Temp and Hum ----------------------------------------
        '''if date_time:
                    date_time_obj = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f%z')
                    date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f%z').strftime('%d/%m/%Y '
                                                                                                         '%H:%M:%S')
                    self.hwclock_time = date_time_obj.time().strftime("%H:%M:%S")
                    self.hwclock_date = date_time_obj.date().strftime('%d/%m/%Y')

        print("Hw Time: "+str(self.hwclock_time)+" Hw Date: "+str(self.hwclock_date))'''

        self.ui.dataModel.set_hum_value(configVariables.hum_read_value)
        self.ui.dataModel.set_temp_value(configVariables.temp_read_value)
        print("Time and Date Inserting time in Database:"+str(self.ui.proc))
        if self.ui.proc:
            configVariables.light_database.insertGraphData(self.ui.dataModel.get_temp_value(),
                                                           self.ui.dataModel.get_hum_value(), '', self.ui.proc)

        # if configVariables.graph_data_flag:
        configVariables.light_database.graphDataSelect(self.ui.dataModel)

        # self.ui.drawRealTimeData()

    def colorChned1(self, ui):
        if self.s:
            if self.s[4] == 2:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.oxygen_hex)
            elif self.s[4] == 1:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.oxygen_hex)
            elif self.s[4] == 0:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.oxygen, "QToolButton",
                                                                    configVariables.oxygen_hex)

        '''pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 0, 0))
        ui.ui.oxygen.setPalette(pal)
        ui.ui.oxygen.setAutoFillBackground(True)'''
        # ui.alldisplayColorChangeObj.changeGasColorRXTX(ui.ui.oxygen, "QToolButton")
        # ui.ui.oxygen.setStyleSheet("background-color : #FF4c4c")
        # ui.ui.oxygen.setStyleSheet("QToolButton { background-color : #FF0000}")
        time.sleep(1)

    def colorChned2(self, ui):
        if self.s:
            if self.s[4] == 8:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.nitrous_hex)
            elif self.s[4] == 4:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.nitrous_hex)
            elif self.s[4] == 0:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.nitrousOxide, "QToolButton",
                                                                    configVariables.nitrous_hex)

        '''pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 0, 0))
        ui.ui.oxygen.setPalette(pal)
        ui.ui.oxygen.setAutoFillBackground(True)'''
        # ui.alldisplayColorChangeObj.changeGasColorRXTX(ui.ui.oxygen, "QToolButton")
        # ui.ui.oxygen.setStyleSheet("background-color : #FF4c4c")
        # ui.ui.oxygen.setStyleSheet("QToolButton { background-color : #FF0000}")
        time.sleep(1)

    def colorChned3(self, ui):
        if self.s:
            if self.s[4] == 32:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.carbondioxide_hex)
            elif self.s[4] == 16:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.carbondioxide_hex)
            elif self.s[4] == 0:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.cabonDiOxide, "QToolButton",
                                                                    configVariables.carbondioxide_hex)
        '''pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 0, 0))
        ui.ui.oxygen.setPalette(pal)
        ui.ui.oxygen.setAutoFillBackground(True)'''
        # ui.alldisplayColorChangeObj.changeGasColorRXTX(ui.ui.oxygen, "QToolButton")
        # ui.ui.oxygen.setStyleSheet("background-color : #FF4c4c")
        # ui.ui.oxygen.setStyleSheet("QToolButton { background-color : #FF0000}")
        time.sleep(1)

    def colorChned4(self, ui):
        if self.s:
            if self.s[4] == 128:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.air4_hex)
            elif self.s[4] == 64:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.air4_hex)
            elif self.s[4] == 0:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air, "QToolButton",
                                                                    configVariables.air4_hex)
        '''pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 0, 0))
        ui.ui.oxygen.setPalette(pal)
        ui.ui.oxygen.setAutoFillBackground(True)'''
        # ui.alldisplayColorChangeObj.changeGasColorRXTX(ui.ui.oxygen, "QToolButton")
        # ui.ui.oxygen.setStyleSheet("background-color : #FF4c4c")
        # ui.ui.oxygen.setStyleSheet("QToolButton { background-color : #FF0000}")
        time.sleep(1)

    def colorChned5(self, ui):
        if self.s:
            if self.s[3] == 2:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.air7_hex)
            elif self.s[3] == 1:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.air7_hex)
            elif self.s[3] == 0:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.air7, "QToolButton",
                                                                    configVariables.air7_hex)
        '''pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 0, 0))
        ui.ui.oxygen.setPalette(pal)
        ui.ui.oxygen.setAutoFillBackground(True)'''
        # ui.alldisplayColorChangeObj.changeGasColorRXTX(ui.ui.oxygen, "QToolButton")
        # ui.ui.oxygen.setStyleSheet("background-color : #FF4c4c")
        # ui.ui.oxygen.setStyleSheet("QToolButton { background-color : #FF0000}")
        time.sleep(1)

    def colorChned6(self, ui):
        if self.s:
            if self.s[3] == 8:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.vacuum_hex)
            elif self.s[3] == 4:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.vacuum_hex)
            elif self.s[3] == 0:
                self.ui.alldisplayColorChangeObj.changeGasColorRXTX(self.ui.ui.vacuum, "QToolButton",
                                                                    configVariables.vacuum_hex)
        '''pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 0, 0))
        ui.ui.oxygen.setPalette(pal)
        ui.ui.oxygen.setAutoFillBackground(True)'''
        # ui.alldisplayColorChangeObj.changeGasColorRXTX(ui.ui.oxygen, "QToolButton")
        # ui.ui.oxygen.setStyleSheet("background-color : #FF4c4c")
        # ui.ui.oxygen.setStyleSheet("QToolButton { background-color : #FF0000}")
        time.sleep(1)


def main():
    SerialWrapper('/dev/ttyUSB0')
    # ser = SerialWrapper('/dev/ttyUSB0')
    # ser1 = serial.Serial("COM5", 9600)

    # sudo usermod -a -G dialout $USER
    '''
    
sudo usermod -a -G dialout $USER
and reboot the system 

The device is most likely attached to user group dialout. Just add your user to the dialout group so you have appropriate permissions on the device.

sudo usermod -a -G dialout $USER

(You may need to logout and back in for the new group to take effect.)

No need to mess around with permissions or udev rules.

sudo adduser <the user you want to add> dialout
sudo reboot

Mentioned by "Try now" worked for me. Check that You have dialout as group for ttyUSB0:

ls -l /dev/ttyUSB0

in my case the output is:

crw-rw---T 1 root dialout 188, 0 Feb 12 12:01 /dev/ttyUSB0



    '''
    '''while 1:
        # misc code here
        thestring = "\x02\x31\x43\x46\xFF\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20"
        command = b'\x02\x31\x43\x46\xFF\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20'
        cw = [0x02, 0x31, 0x43, 0x46, 0xFF, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46,
              0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x20]

        ser1.write(serial.to_bytes(command))
        # ser.sendData(cw)
        s = ser1.read(9)
        print(s)
        time.sleep(1)  # Sleep for 3 seconds'''

# 02314346464646464646464646464646464646464620 #--------Relay Control---------
# 023143464046464646464646464646464646464620   #--------Relay Control---------
# 02314346FF4646464646464646464646464646464620 #--------Relay Control---------
# https://www.ascii-code.com/
# if __name__ == '__main__':
#    main()
