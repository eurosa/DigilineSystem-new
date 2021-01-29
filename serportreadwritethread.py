import serial  # import module
import threading

STRGLO = ""  # read data
BOOL = True  # read flag


class SerialWrapper1:
    def __init__(self, device, ui):
        self.s = None
        self.ui = ui
        # self.ser = serial.Serial(device, 115200)
        ser, ret = self.DOpenPort(device, 9600, None)
        if ret:  # determine if the serial port is successfully opened.
            count = self.DWritePort(ser, " i am dong xiaodong, haha. ")
            print(" number of bytes written ：", count)
            # DReadPort() # read serial data
            # DColsePort(ser)  # close the serial port'''

    # reading code ontology implementation
    def ReadData(self, ser):
        global STRGLO, BOOL
        #  loop receiving data, this is an infinite loop ， available thread
        while BOOL:
            if ser.in_waiting:
                STRGLO = ser.read(ser.in_waiting).decode("gbk")
                print(STRGLO)

    # open serial port port, GNU / Linux up / dev / ttyUSB0  wait or  Windows up  COM3  wait baud rate, one of the
    # standard values ：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200 timeout
    # setting, None： waiting for operation forever, 0 to return the result of the request immediately,
    # the other values are waiting timeouts ( in seconds ）
    def DOpenPort(self, portx, bps, timeout):
        ret = False
        try:
            #  open the serial port and get the serial port object
            ser = serial.Serial(portx, bps, timeout=timeout)
            # determine whether it is open successfully
            if ser.is_open:
                ret = True
                threading.Thread(target=self.ReadData, args=(ser,)).start()
        except Exception as e:
            print("--- abnormal ---：", e)
        return ser, ret

    # close the serial port
    def DColsePort(self, ser):
        global BOOL
        BOOL = False
        ser.close()

    # write data
    def DWritePort(self, ser, text):
        result = ser.write(text.encode("gbk"))  # write data
        return result

    # reading data
    def DReadPort(self):
        global STRGLO
        str = STRGLO
        STRGLO = ""  # clear the current reading
        return str


'''if __name__ == "__main__":
    ser, ret = self.DOpenPort("COM6", 115200, None)
    if ret == True:  # determine if the serial port is successfully opened.
        count = self.DWritePort(ser, " i am dong xiaodong, haha. ")
        print(" number of bytes written ：", count)
        # DReadPort() # read serial data
        # DColsePort(ser)  # close the serial port'''
