import re


class Brightness:
    def __init__(self, ot_ui, datamodel):
        self.ot_ui = ot_ui
        self.datamodel = datamodel
        self.changed_low_color = self.color_variant_inc_dec(self.datamodel.get_icon_col(), 87)
        self.light1Brightness = 0
        self.light1Brightness_2 = 0
        self.light1Brightness_3 = 0
        self.light1Brightness_4 = 0
        self.allLightBarInitialSetup(ot_ui)

    def otLightBrightIncrementControl(self):
        if 0 <= self.light1Brightness < 10:
            self.light1Brightness = self.light1Brightness + 1
        print(str(self.light1Brightness))

        if self.light1Brightness == 1:
            self.ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")
            '''self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
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
                                               "60px;background-color:#000000;border-color:#000000")'''
        if self.light1Brightness == 2:
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 3:
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 4:
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 5:
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 6:
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 7:
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 8:
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 9:
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness == 10:
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

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
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 1:
            self.ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 2:
            self.ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 3:
            self.ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 4:
            self.ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 5:
            self.ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 6:
            self.ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 7:
            self.ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 8:
            self.ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness == 9:
            self.ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

    def otLightBrightIncrementControl2(self):
        if 0 <= self.light1Brightness_2 < 10:
            self.light1Brightness_2 = self.light1Brightness_2 + 1

        if self.light1Brightness_2 == 1:
            self.ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 2:
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 3:
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 4:
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 5:
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 6:
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 7:
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 8:
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 9:
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_2 == 10:
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

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
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 1:
            self.ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 2:
            self.ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 3:
            self.ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 4:
            self.ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 5:
            self.ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 6:
            self.ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 7:
            self.ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 8:
            self.ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_2 == 9:
            self.ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

    def otLightBrightIncrementControl3(self):
        if 0 <= self.light1Brightness_3 < 10:
            self.light1Brightness_3 = self.light1Brightness_3 + 1

        if self.light1Brightness_3 == 1:
            self.ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 2:
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 3:
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 4:
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 5:
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 6:
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 7:
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 8:
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 9:
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_3 == 10:
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

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
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 1:
            self.ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 2:
            self.ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 3:
            self.ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 4:
            self.ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 5:
            self.ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 6:
            self.ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 7:
            self.ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 8:
            self.ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_3 == 9:
            self.ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

    def otLightBrightIncrementControl4(self):
        if 0 <= self.light1Brightness_4 < 10:
            self.light1Brightness_4 = self.light1Brightness_4 + 1

        if self.light1Brightness_4 == 1:
            self.ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 2:
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 3:
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 4:
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 5:
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 6:
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 7:
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 8:
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 9:
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

        if self.light1Brightness_4 == 10:
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

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
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 1:
            self.ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 2:
            self.ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 3:
            self.ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 4:
            self.ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 5:
            self.ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 6:
            self.ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 7:
            self.ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 8:
            self.ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                              "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")

        if self.light1Brightness_4 == 9:
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
            '''
                    if self.light1Brightness_4 == 9:
            self.ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                               "border-width: 2px;background-color:#000000;border-color:#000000")
            '''

    def color_variant_inc_dec(self, hex_color, brightness_offset=1):
        print("Original Hex: " + str(hex_color))
        R, G, B = self.hex_to_rgb(hex_color)
        Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
        if Y > 128:
            h = self.get_complementary(hex_color)
            print("Complementary color", h)
            # h = h.lstrip('#')
            # print('RGB =', tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)))
            hex_color = h
        else:
            hex_color
        '''R, G, B = self.hex_to_rgb(hex_color)
        Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
        if Y < 128:
            print("Black")
        else:
            print("White")'''
        print("Red" + str(R) + " Green" + str(G) + " Blue" + str(B))
        """ takes a color like #87c95f and produces a lighter or darker variant """
        if len(hex_color) != 7:
            raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
        rgb_hex = [hex_color[x:x + 2] for x in [1, 3, 5]]
        new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
        new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int]  # make sure new values are between 0 and 255
        # hex() produces "0x88", we want just "88"
        return "#" + "".join([hex(i)[2:] for i in new_rgb_int])

    def get_complementary(self, color):
        color = color[1:]
        color = int(color, 16)
        comp_color = 0xFFFFFF ^ color
        comp_color = "#%06X" % comp_color
        return comp_color

    def hex_to_rgb(self, hx, hsl=False):
        """Converts a HEX code into RGB or HSL.
        Args:
            hx (str): Takes both short as well as long HEX codes.
            hsl (bool): Converts the given HEX code into HSL value if True.
        Return:
            Tuple of length 3 consisting of either int or float values."""
        if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
            div = 255.0 if hsl else 0
            if len(hx) <= 4:
                return tuple(int(hx[i] * 2, 16) / div if div else
                             int(hx[i] * 2, 16) for i in (1, 2, 3))
            else:
                return tuple(int(hx[i:i + 2], 16) / div if div else
                             int(hx[i:i + 2], 16) for i in (1, 3, 5))
        else:
            raise ValueError(f'"{hx}" is not a valid HEX code.')

    def initialBarColor(self, attribute):
        attribute.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                "border-width: 2px;background-color:" + self.datamodel.get_icon_col() + ";border-color:" + self.datamodel.get_icon_col() + "")

    def allLightBarInitialSetup(self, ot_ui):
        ot_ui.light1_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light1_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                      "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light2_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                      "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light3_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                      "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_1.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_2.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_3.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_4.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_5.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_6.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_7.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_8.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_9.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                     "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
        ot_ui.light4_10.setStyleSheet("border-style: outset; padding:2px;border-radius:4px;"
                                      "border-width: 2px;background-color:" + self.changed_low_color + ";border-color:" + self.changed_low_color + "")
