from PyQt5.QtGui import QImage, QPixmap

import configVariables

configVariables.x = 1
configVariables.y = 2
configVariables.z = "geeksforgeeks"


class ModifyGlobalVariables:
    def __init__(self, alldisplayobj, ot_ui, model):
        self.alldisplayobj = alldisplayobj
        self.ot_ui = ot_ui
        self.dataModel = model
        self.play_wh = QImage(QPixmap("icon/play_white.png"))
        self.pause_wh = QImage(QPixmap("icon/pause_white.png"))
        self.light_bulb = QImage(QPixmap("icon/light-bulb.png"))
        self.ot_light = QImage(QPixmap("icon/lights.png"))

    def setChangedImage(self):
        configVariables.play_changed_image = self.alldisplayobj.changedIconColorImage(self.play_wh)
        configVariables.pause_changed_image = self.alldisplayobj.changedIconColorImage(self.pause_wh)

    def setChangedLightColor(self):
        configVariables.changed_light1Decrement = self.alldisplayobj.changeIconColor(self.ot_ui.light1Decrement)
        configVariables.changed_light1Increment = self.alldisplayobj.changeIconColor(self.ot_ui.light1Increment)
        configVariables.changed_light2Decrement = self.alldisplayobj.changeIconColor(self.ot_ui.light2Decrement)
        configVariables.changed_light2Increment = self.alldisplayobj.changeIconColor(self.ot_ui.light2Increment)
        configVariables.changed_light3Decrement = self.alldisplayobj.changeIconColor(self.ot_ui.light3Decrement)
        configVariables.changed_light3Increment = self.alldisplayobj.changeIconColor(self.ot_ui.light3Increment)
        configVariables.changed_light4Decrement = self.alldisplayobj.changeIconColor(self.ot_ui.light4Decrement)
        configVariables.changed_light4Increment = self.alldisplayobj.changeIconColor(self.ot_ui.light4Increment)
        configVariables.changed_lightBulb1 = self.alldisplayobj.changePixmapColor(self.ot_ui.lightBulb1)
        configVariables.changed_lightBulb2 = self.alldisplayobj.changePixmapColor(self.ot_ui.lightBulb2)
        configVariables.changed_otLightBulb1 = self.alldisplayobj.changePixmapColor(self.ot_ui.otLightBulb1)
        configVariables.changed_lightBulb3 = self.alldisplayobj.changePixmapColor(self.ot_ui.lightBulb3)
        configVariables.changed_lightBulb4 = self.alldisplayobj.changePixmapColor(self.ot_ui.lightBulb4)
        configVariables.changed_otLightBulb2 = self.alldisplayobj.changePixmapColor(self.ot_ui.otLightBulb2)

        configVariables.changed_light_bulb = self.alldisplayobj.returnPixmapColorImage(self.light_bulb)
        configVariables.changed_ot_light = self.alldisplayobj.returnPixmapColorImage(self.ot_light)
        configVariables.low_light_bulb = self.alldisplayobj.returnPixmapColorImageLowLight(self.light_bulb)
        configVariables.low_ot_light = self.alldisplayobj.returnPixmapColorImageLowLight(self.ot_light)
        configVariables.changed_low_color = self.alldisplayobj.color_variant_inc_dec(self.dataModel.get_icon_col(), 87)

    def getChangedPlayImage(self):
        return configVariables.play_changed_image

    def getChangedPauseImage(self):
        return configVariables.pause_changed_image
