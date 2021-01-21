import threading
import time
import serial

import configVariables
from Database import switchdatabase
from repeatedTimer import RepeatedTimer


class SerialWrapper:
    def __init__(self, device, threadrxtx):
        self.threadrxtx = threadrxtx
        self.s = None
        self.ser = serial.Serial(device, 115200)
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

    def sendData(self, data):
        data += "\r\n"
        self.ser.write(data.encode())

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

        if self.s:
            if self.s[4] == 1 or self.s[4] == 2:
                configVariables.oxygen_hex = self.s[4]
            if self.s[4] == 4 or self.s[4] == 8:
                configVariables.nitrous_hex = self.s[4]
            if self.s[4] == 16 or self.s[4] == 32:
                configVariables.carbondioxide_hex = self.s[4]
            if self.s[4] == 54 or self.s[4] == 128:
                configVariables.air4_hex = self.s[4]
            if self.s[4] == 1 or self.s[4] == 2:
                configVariables.air7_hex = self.s[3]
            if self.s[4] == 1 or self.s[4] == 2:
                configVariables.air7_hex = self.s[3]
            if self.s[4] == 4 or self.s[4] == 8:
                configVariables.vacuum_hex = self.s[3]
            # =================================== Thread to color changes ====================
            #self.threadrxtx.signal.return_signal.connect(self.threadrxtx.function_thread)
            #self.threadpoolRXTX.start(self.threadrxtx)

            self.threadrxtx .start()


            # =================================== Thread to color changes ====================
            print(str(self.s[0]) + " " + str(self.s[1]) + " " + str(self.s[2]) + " "
                                                                                 "" + str(self.s[3]) + " " + str(
                self.s[4]) + " " + str(
                self.s[5]) + " " + str(self.s[6]) + " " + str(self.s[7]) + " " + str(self.s[8]) + " "
                                                                                                  " " + str(
                self.s[9]) + " " + str(
                self.s[10]) + " " + str(
                self.s[11]) + " " + str(
                self.s[12]) + " " + str(self.s[13]) + " "
                                                      "" + str(self.s[14]) + " " + str(self.s[15]) + " " + str(
                self.s[16]) + " " + str(
                self.s[17]) + " " + str(self.s[18]) + " "
                                                      "" + str(self.s[19]) + " " + str(self.s[20]) + " " + str(
                self.s[21]))

        '''print("01: "+str(s[0]))
                        print("02: "+str(s[1]))
                        print("03: "+str(s[2]))
                        print("04: "+str(s[3]))
                        print("05: "+str(s[4]))
                        print("06: "+str(s[5]))
                        print("07: "+str(s[6]))
                        print("08: "+str(s[7]))
                        print("09: "+str(s[8]))
                        print("10: "+str(s[9]))
                        print("11: "+str(s[10]))
                        print("12: "+str(s[11]))
                        print("13: "+str(s[12]))
                        print("14: "+str(s[13]))
                        print("15: "+str(s[14]))
                        print("16: "+str(s[15]))
                        print("17: "+str(s[16]))
                        print("18: "+str(s[17]))
                        print("19: "+str(s[18]))
                        print("20: "+str(s[19]))
                        print("21: "+str(s[20]))
                        print("22: "+str(s[21]))'''

        # time.sleep(1)  # Sleep for 1 seconds


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
