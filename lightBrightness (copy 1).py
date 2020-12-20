
class Brightness:
    def __init__(self, ot_ui):
        self.ot_ui = ot_ui
        self.light1Brightness = 0
        self.light1Brightness_2 = 0
        self.light1Brightness_3 = 0
        self.light1Brightness_4 = 0

    def otLightBrightIncrementControl(self):
        if 0 <= self.light1Brightness < 10:
            self.light1Brightness = self.light1Brightness + 1
        print(str(self.light1Brightness))

        if self.light1Brightness == 1:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 2:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 3:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 4:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 5:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 6:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 7:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 8:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 9:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 10:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")

    ''' self.count = self.light1Brightness
     print(str(self.count))
     while self.count > 0:
         self.label12 = QtWidgets.QLabel()
         self.label12.setObjectName("light1_" + str(self.count))
         self.ot_ui.light1_11 = QLabel("light1_" + str(self.count))
         self.label12.setStyleSheet(
             "border-style: outset; padding:2px;border-radius:4px;"
             "border-width: 2px;min-height: 15px;max-height: "
             "15px;background-color:#FFFFFF;border-color:#FFFFFF")
         print("light1_" + str(self.count))
         print(str(self.ot_ui.light1_11))
         self.count = self.count - 1'''

    def otLightBrightDecrementControl(self):
        if 0 < self.light1Brightness <= 10:
            self.light1Brightness = self.light1Brightness - 1
        print("Decrement: " + str(self.light1Brightness))

        if self.light1Brightness == 0:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 1:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 2:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 3:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 4:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 5:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 6:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 7:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 8:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 9:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness == 10:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")

    def otLightBrightIncrementControl2(self):
        if 0 <= self.light1Brightness_2 < 10:
            self.light1Brightness_2 = self.light1Brightness_2 + 1

        if self.light1Brightness_2 == 1:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 2:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 3:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 4:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 5:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 6:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 7:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 8:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 9:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 10:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")

    ''' self.count = self.light1Brightness
     print(str(self.count))
     while self.count > 0:
         self.label12 = QtWidgets.QLabel()
         self.label12.setObjectName("light1_" + str(self.count))
         self.ot_ui.light1_11 = QLabel("light1_" + str(self.count))
         self.label12.setStyleSheet(
             "border-style: outset; padding:2px;border-radius:4px;"
             "border-width: 2px;min-height: 15px;max-height: "
             "15px;background-color:#FFFFFF;border-color:#FFFFFF")
         print("light1_" + str(self.count))
         print(str(self.ot_ui.light1_11))
         self.count = self.count - 1'''

    def otLightBrightDecrementControl2(self):
        if 0 < self.light1Brightness_2 <= 10:
            self.light1Brightness_2 = self.light1Brightness_2 - 1

        if self.light1Brightness_2 == 0:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 1:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 2:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 3:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 4:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 5:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 6:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 7:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 8:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 9:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_2 == 10:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")

    def otLightBrightIncrementControl3(self):
        if 0 <= self.light1Brightness_3 < 10:
            self.light1Brightness_3 = self.light1Brightness_3 + 1

        if self.light1Brightness_3 == 1:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 2:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 3:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 4:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 5:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 6:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 7:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 8:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 9:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 10:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")

    ''' self.count = self.light1Brightness
     print(str(self.count))
     while self.count > 0:
         self.label12 = QtWidgets.QLabel()
         self.label12.setObjectName("light1_" + str(self.count))
         self.ot_ui.light1_11 = QLabel("light1_" + str(self.count))
         self.label12.setStyleSheet(
             "border-style: outset; padding:2px;border-radius:4px;"
             "border-width: 2px;min-height: 15px;max-height: "
             "15px;background-color:#FFFFFF;border-color:#FFFFFF")
         print("light1_" + str(self.count))
         print(str(self.ot_ui.light1_11))
         self.count = self.count - 1'''

    def otLightBrightDecrementControl3(self):
        if 0 < self.light1Brightness_3 <= 10:
            self.light1Brightness_3 = self.light1Brightness_3 - 1

        if self.light1Brightness_3 == 0:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 1:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 2:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 3:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 4:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 5:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 6:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 7:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 8:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 9:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_3 == 10:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")

    def otLightBrightIncrementControl4(self):
        if 0 <= self.light1Brightness_4 < 10:
            self.light1Brightness_4 = self.light1Brightness_4 + 1

        if self.light1Brightness_4 == 1:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 2:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 3:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 4:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 5:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 6:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 7:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 8:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 9:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 10:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")

    ''' self.count = self.light1Brightness
     print(str(self.count))
     while self.count > 0:
         self.label12 = QtWidgets.QLabel()
         self.label12.setObjectName("light1_" + str(self.count))
         self.ot_ui.light1_11 = QLabel("light1_" + str(self.count))
         self.label12.setStyleSheet(
             "border-style: outset; padding:2px;border-radius:4px;"
             "border-width: 2px;min-height: 15px;max-height: "
             "15px;background-color:#FFFFFF;border-color:#FFFFFF")
         print("light1_" + str(self.count))
         print(str(self.ot_ui.light1_11))
         self.count = self.count - 1'''

    def otLightBrightDecrementControl4(self):
        if 0 < self.light1Brightness_4 <= 10:
            self.light1Brightness_4 = self.light1Brightness_4 - 1

        if self.light1Brightness_4 == 0:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 1:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 2:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 3:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 4:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 5:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 6:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 7:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 8:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#000000;border-color:#000000")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 9:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#000000;border-color:#000000")
        if self.light1Brightness_4 == 10:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 15px;max-height: "
                                              "15px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 20px;max-height: "
                                              "20px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 25px;max-height: "
                                              "25px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 30px;max-height: "
                                              "30px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 35px;max-height: "
                                              "35px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 40px;max-height: "
                                              "40px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 45px;max-height: "
                                              "45px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 50px;max-height: "
                                              "50px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;min-height: 55px;max-height: "
                                              "55px;background-color:#FFFFFF;border-color:#FFFFFF")
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;min-height: 60px;max-height: "
                                               "60px;background-color:#FFFFFF;border-color:#FFFFFF")
