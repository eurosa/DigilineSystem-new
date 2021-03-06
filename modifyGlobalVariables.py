from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
from PyQt5.QtGui import QImage, QPixmap, QIcon

import configVariables

configVariables.x = 1
configVariables.y = 2
configVariables.z = "geeksforgeeks"


class ModifyGlobalVariables:
    def __init__(self, alldisplayobj, ot_ui, model, _database):
        self.alldisplayobj = alldisplayobj
        self.database = _database
        self.ot_ui = ot_ui
        self.dataModel = model
        self.play_wh = QImage(QPixmap("icon/play_white.png"))
        self.pause_wh = QImage(QPixmap("icon/pause_white.png"))
        self.light_bulb = QImage(QPixmap("icon/light-bulb.png"))
        self.ot_light = QImage(QPixmap("icon/lights.png"))
        self.on_speaker = QImage(QPixmap("icon/speaker-on-white.png"))
        self.off_speaker = QImage(QPixmap("icon/speaker-off-white.png"))

    def setChangedImage(self):
        play_qpixmap_image = self.alldisplayobj.changedQPixMapColorImage(self.play_wh)
        pause_qpixmap_image = self.alldisplayobj.changedQPixMapColorImage(self.pause_wh)
        play_qpixmap_byte = self.convertQPixMapToByteArray(play_qpixmap_image)
        pause_qpixmap_byte = self.convertQPixMapToByteArray(pause_qpixmap_image)

        configVariables.play_changed_image = QIcon(play_qpixmap_image)
        configVariables.pause_changed_image = QIcon(pause_qpixmap_image)

        self.dataModel.set_changed_play(play_qpixmap_byte)
        self.dataModel.set_changed_pause(pause_qpixmap_byte)

    def setChangedLightColor(self):
        play_qpixmap_image = self.alldisplayobj.changedQPixMapColorImage(self.play_wh)
        pause_qpixmap_image = self.alldisplayobj.changedQPixMapColorImage(self.pause_wh)
        play_qpixmap_byte = self.convertQPixMapToByteArray(play_qpixmap_image)
        pause_qpixmap_byte = self.convertQPixMapToByteArray(pause_qpixmap_image)

        on_speaker_qpixmap_image = self.alldisplayobj.changedQPixMapColorImage(self.on_speaker)
        off_speaker_qpixmap_image = self.alldisplayobj.changedQPixMapColorImage(self.off_speaker)
        on_speaker_qpixmap_byte = self.convertQPixMapToByteArray(on_speaker_qpixmap_image)
        off_speaker_qpixmap_byte = self.convertQPixMapToByteArray(off_speaker_qpixmap_image)

        configVariables.changed_on_speaker = QIcon(on_speaker_qpixmap_image)
        configVariables.changed_off_speaker = QIcon(off_speaker_qpixmap_image)
        configVariables.play_changed_image = QIcon(play_qpixmap_image)
        configVariables.pause_changed_image = QIcon(pause_qpixmap_image)

        self.dataModel.set_changed_play(play_qpixmap_byte)
        self.dataModel.set_changed_pause(pause_qpixmap_byte)
        self.dataModel.set_changed_on_speaker(on_speaker_qpixmap_byte)
        self.dataModel.set_changed_off_speaker(off_speaker_qpixmap_byte)

        '''configVariables.changed_light1Decrement = self.alldisplayobj.changeIconColor(self.ot_ui.light1Decrement)
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
        configVariables.changed_otLightBulb2 = self.alldisplayobj.changePixmapColor(self.ot_ui.otLightBulb2) '''

        configVariables.changed_light_bulb = self.alldisplayobj.returnPixmapColorImage(self.light_bulb)
        configVariables.changed_ot_light = self.alldisplayobj.returnPixmapColorImage(self.ot_light)
        configVariables.low_light_bulb = self.alldisplayobj.returnPixmapColorImageLowLight(self.light_bulb)
        configVariables.low_ot_light = self.alldisplayobj.returnPixmapColorImageLowLight(self.ot_light)
        configVariables.changed_low_color = self.alldisplayobj.color_variant_inc_dec(self.dataModel.get_icon_col(), 87)

        changed_light_bulb = self.convertQPixMapToByteArray(configVariables.changed_light_bulb)
        self.dataModel.set_changed_light_bulb(changed_light_bulb)
        # self.convertByteToPixMap(self.dataModel.get_changed_light_bulb())

        changed_ot_light = self.convertQPixMapToByteArray(configVariables.changed_ot_light)
        self.dataModel.set_changed_ot_light(changed_ot_light)

        # self.convertByteToPixMap(self.dataModel.get_changed_ot_light())

        low_light_bulb = self.convertQPixMapToByteArray(configVariables.low_light_bulb)
        self.dataModel.set_low_light_bulb(low_light_bulb)
        # self.convertByteToPixMap(self.dataModel.get_low_light_bulb())

        low_ot_light = self.convertQPixMapToByteArray(configVariables.low_ot_light)
        self.dataModel.set_low_ot_light(low_ot_light)
        # self.convertByteToPixMap(self.dataModel.get_low_ot_light())

        # changed_low_color = self.convertQPixMapToByteArray(configVariables.changed_low_color)
        self.dataModel.set_changed_low_color(configVariables.changed_low_color)
        # self.convertByteToPixMap(self.dataModel.get_changed_low_color())
        print("Changed Light Bulb: " + str(changed_light_bulb))
        # configVariables.light_database.insertPixMapByteArray(self.dataModel)

        if configVariables.light_database.tableRowCount("image_table") > 0:
            configVariables.light_database.updatePixMapByteArray(self.dataModel)
        else:
            configVariables.light_database.insertPixMapByteArray(self.dataModel)

    def getChangedImage(self):
        '''configVariables.play_changed_image = self.alldisplayobj.changedIconColorImage(self.play_wh)
        configVariables.pause_changed_image = self.alldisplayobj.changedIconColorImage(self.pause_wh)'''
        configVariables.play_changed_image = QIcon(self.convertByteToPixMap(self.dataModel.get_changed_play()))
        configVariables.pause_changed_image = QIcon(self.convertByteToPixMap(self.dataModel.get_changed_pause()))

    def getChangedLightColor(self):
        '''configVariables.changed_light1Decrement = self.alldisplayobj.changeIconColor(self.ot_ui.light1Decrement)
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
        configVariables.changed_otLightBulb2 = self.alldisplayobj.changePixmapColor(self.ot_ui.otLightBulb2)'''

        configVariables.play_changed_image = QIcon(self.convertByteToPixMap(self.dataModel.get_changed_play()))
        configVariables.pause_changed_image = QIcon(self.convertByteToPixMap(self.dataModel.get_changed_pause()))

        configVariables.changed_light_bulb = self.convertByteToPixMap(self.dataModel.get_changed_light_bulb())
        configVariables.changed_ot_light = self.convertByteToPixMap(self.dataModel.get_changed_ot_light())
        configVariables.low_light_bulb = self.convertByteToPixMap(self.dataModel.get_low_light_bulb())
        configVariables.low_ot_light = self.convertByteToPixMap(self.dataModel.get_low_ot_light())
        configVariables.changed_low_color = self.dataModel.get_changed_low_color()
        configVariables.changed_on_speaker = QIcon(self.convertByteToPixMap(self.dataModel.get_changed_on_speaker()))
        configVariables.changed_off_speaker = QIcon(self.convertByteToPixMap(self.dataModel.get_changed_off_speaker()))
        # configVariables.changed_low_color = self.alldisplayobj.color_variant_inc_dec(self.dataModel.get_icon_col(), 87)
        print("changed_low_color:" + configVariables.changed_low_color+"  From Database : "+ self.dataModel.get_changed_low_color())


        '''configVariables.changed_light_bulb = self.alldisplayobj.returnPixmapColorImage(self.light_bulb)
        configVariables.changed_ot_light = self.alldisplayobj.returnPixmapColorImage(self.ot_light)
        configVariables.low_light_bulb = self.alldisplayobj.returnPixmapColorImageLowLight(self.light_bulb)
        configVariables.low_ot_light = self.alldisplayobj.returnPixmapColorImageLowLight(self.ot_light)
        configVariables.changed_low_color = self.alldisplayobj.color_variant_inc_dec(self.dataModel.get_icon_col(), 87)'''

    def convertQPixMapToByteArray(self, pixmap):
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.WriteOnly)
        ok = pixmap.save(buff, "PNG")
        assert ok
        pixmap_bytes = ba
        # pixmap_bytes = ba.data()
        return pixmap_bytes
        # print("PIX_MAP_BYTE" + str(pixmap_bytes))

    def convertByteToPixMap(self, pixmap_bytes):
        # convert bytes to QPixmap
        ba = pixmap_bytes
        pixmap = QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok
        print("PIX_MAP" + str(pixmap))
        return pixmap

    '''def convertByteToPixMap(self, pixmap_bytes):
        # convert bytes to QPixmap
        ba = QByteArray(pixmap_bytes)
        pixmap = QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok
        print("PIX_MAP" + str(pixmap))
        return pixmap'''
