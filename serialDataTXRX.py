import threading
import time
import serial
from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor

import configVariables
from Database import switchdatabase
from repeatedTimer import RepeatedTimer


class SerialWrapper:
    def __init__(self, device, ui):
        self.s = None
        self.ui = ui
        # self.ser = serial.Serial(device, 115200)
        self.ser1 = serial.Serial(device, 9600)
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
        # print("Converted Hex: " + str(hex_code))
        new_hex = int(configVariables.totalHex, 16)
        # misc code here
        thestring = "\x02\x31\x43\x46\xFF\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20"
        command = b'\x02\x31\x43\x02\x0F\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20\n'
        cw = [0x02, 0x31, 0x43, 0x46, new_hex, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46,
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
