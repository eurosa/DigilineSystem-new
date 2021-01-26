import threading


class LightIntensityControlThread:
    def __init__(self, serialwrapper):
        self.serialWrapper = serialwrapper

    def lightIntensityThread1(self):
        self.s1 = threading.Thread(target=self.serialWrapper.sendDataToSerialPort)
        # self.s1 = threading.Thread(target=self.serialWrapper.sendDataToSerialPortIntensity, args=[light1Brightness1])
        self.s1.daemon = True
        self.s1.start()

    def lightIntensityThread2(self):
        self.s2 = threading.Thread(target=self.serialWrapper.sendDataToSerialPort)
        self.s2.daemon = True
        self.s2.start()

    def lightIntensityThread3(self):
        self.s3 = threading.Thread(target=self.serialWrapper.sendDataToSerialPort)
        self.s3.daemon = True
        self.s3.start()

    def lightIntensityThread4(self):
        self.s4 = threading.Thread(target=self.serialWrapper.sendDataToSerialPort)
        self.s4.daemon = True
        self.s4.start()
