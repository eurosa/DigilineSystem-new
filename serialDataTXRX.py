import time
import serial


class SerialWrapper:
    def __init__(self, device):
        self.ser = serial.Serial(device, 115200)
        self.ser1 = serial.Serial(device, 9600)
        self.sendDataToSerialPort()

    def sendData(self, data):
        data += "\r\n"
        self.ser.write(data.encode())

    def sendDataToSerialPort(self, hex_code=0x46):
        print("Converted Hex: "+str(hex_code))
        # misc code here
        thestring = "\x02\x31\x43\x46\xFF\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20"
        # command = b'\x02\x31\x43\x02\x0F\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x46\x20'
        cw = [0x02, 0x31, 0x43, 0x46, hex_code, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46,
              0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x46, 0x20]

        self.ser1.write(serial.to_bytes(cw))
        s = self.ser1.read(22)
        print(s)
        time.sleep(1)  # Sleep for 1 seconds


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
#if __name__ == '__main__':
#    main()
