import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class DataBaseManagement:
    def __init__(self):
        pass

    def init(self, filename, server):
        import os
        if not os.path.exists(filename):
            self.db_connect(filename, server)
            self.db_create()
        else:
            self.db_connect(filename, server)
        print("Real Path: " + os.path.realpath('icon') + "/")

    '''
    def cargarDatos(self, event):
        index = 0
        query = QSqlQuery()
        query.exec_("select * from person")

        while query.next():
            ids = query.value(0)
            nombre = query.value(1)
            apellido = query.value(2)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(ids)))
            self.table.setItem(index, 1, QTableWidgetItem(nombre))
            self.table.setItem(index, 2, QTableWidgetItem(apellido))

            index += 1'''

    def close(self):
        print("sery")

    def insertarDatos(self, model):
        ids = int(model.get_label_name_1())
        nombre = str(model.get_label_name_2())
        apellido = str(model.get_label_name_3())

        query = QSqlQuery()
        query.exec_("insert into person values({0}, '{1}', '{2}')".format(ids, nombre, apellido))

    '''def eliminarDatos(self, event):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            return

        ids = self.table.selectedItems()[0]
        query = QSqlQuery()
        query.exec_("delete from person where id = " + ids.text())

        self.table.removeRow(selected.row())
        self.table.setCurrentIndex(QModelIndex())'''

    def updateIconColorSettings(self, model):
        # ids = int(model.get_light_name_1())
        border_color = model.get_border_col()
        background_color = model.get_background_col()
        text_color = model.get_text_col()
        print("" + border_color + "" + background_color + "" + text_color)
        icon_color = model.get_icon_col()
        query = QSqlQuery()
        query.exec_("UPDATE iconColorControl SET border_color ='"
                    + border_color + "',background_color ='"
                    + background_color + "',text_color ='"
                    + text_color + "',icon_color ='"
                    + icon_color + "' WHERE id= 1")

    def queryIconColorSettings(self, model):
        query = QSqlQuery()
        query.exec_("SELECT * FROM iconColorControl where 1")
        while query.next():
            # print(query.value('theme_color_preview'))
            model.set_border_col(query.value('border_color'))
            model.set_background_col(query.value('background_color'))
            model.set_text_col(query.value('text_color'))
            model.set_icon_col(query.value('icon_color'))

    def queryThemeColorSettings(self, model):
        query = QSqlQuery()
        query.exec_("SELECT * FROM themeColorSettings where 1")
        while query.next():
            # print(query.value('theme_color_preview'))
            model.set_theme_color_hex(query.value('theme_color_hex'))
            model.set_theme_color_name(query.value('theme_color_name'))
            model.set_theme_active_inactive(query.value('active_inactive'))
            model.set_theme_preview_image_path(query.value('theme_color_preview'))

    def populate_cbo_from_tlkp_table(self):
        query = QSqlQuery()
        query.exec_("SELECT * FROM themeColorSettings where 1")
        dict = {'Select': 'Select'}
        while query.next():
            dict[query.value('theme_color_hex') + ";#@;" + query.value('theme_color_preview')] = query.value(
                'theme_color_name')
        return dict

    def insertPixMapByteArray(self, datamodel):
        changed_light_bulb = datamodel.get_changed_light_bulb()
        changed_ot_light = datamodel.get_changed_ot_light()
        low_light_bulb = datamodel.get_low_light_bulb()
        low_ot_light = datamodel.get_low_ot_light()
        changed_low_color = datamodel.get_changed_low_color()
        # print("Changed Light Bulb: "+str(changed_light_bulb))
        # print("Changed Low Light Color: " + str(changed_low_color))
        query = QSqlQuery()
        # query.exec_(f"""insert into image_table( changed_light_bulb)
        #       values(  '{ckjk}')""")
        query.prepare("INSERT INTO image_table (changed_light_bulb, changed_ot_light, "
                      "low_light_bulb, low_ot_light, changed_low_color) "
                      "VALUES ( :changed_light_bulb, :changed_ot_light, :low_light_bulb,"
                      " :low_ot_light, :changed_low_color)")
        query.bindValue(":changed_light_bulb", changed_light_bulb)
        query.bindValue(":changed_ot_light", changed_ot_light)
        query.bindValue(":low_light_bulb", low_light_bulb)
        query.bindValue(":low_ot_light", low_ot_light)
        query.bindValue(":changed_low_color", changed_low_color)
        if not query.exec():
            qDebug() << "Error inserting image into table:\n" << query.lastError()

        '''
        query.exec_(f"""insert into image_table(changed_light_bulb, changed_ot_light, low_light_bulb, low_ot_light, changed_low_color) 
                values('{changed_light_bulb}', '{changed_ot_light}', '{low_light_bulb}', '{low_ot_light}', '{changed_low_color}')""")

        '''

        # qDebug() << "Error inserting image into table:\n" << query.lastError()

    def queryGeneralSettingsData(self, model):
        query = QSqlQuery()
        query.exec_("SELECT * FROM GeneralSettings where id=1")
        while query.next():
            model.set_light_name_1(query.value('light_name_1'))
            model.set_light_name_2(query.value('light_name_2'))
            model.set_light_name_3(query.value('light_name_3'))
            model.set_light_name_4(query.value('light_name_4'))
            model.set_light_name_5(query.value('light_name_5'))
            model.set_light_name_6(query.value('light_name_6'))
            model.set_gas_name_1(query.value('gas_name_1'))
            model.set_gas_name_2(query.value('gas_name_2'))
            model.set_gas_name_3(query.value('gas_name_3'))
            model.set_gas_name_4(query.value('gas_name_4'))
            model.set_gas_name_5(query.value('gas_name_5'))
            model.set_gas_name_6(query.value('gas_name_6'))
            model.set_gas_name_7(query.value('gas_name_7'))
            model.set_light_checkbox_1(query.value('light_checkbox_1'))
            model.set_light_checkbox_2(query.value('light_checkbox_2'))
            model.set_light_checkbox_3(query.value('light_checkbox_3'))
            model.set_light_checkbox_4(query.value('light_checkbox_4'))
            model.set_light_checkbox_5(query.value('light_checkbox_5'))
            model.set_light_checkbox_6(query.value('light_checkbox_6'))
            model.set_checkbox_gas_1(query.value('gas_checkbox_1'))
            model.set_checkbox_gas_2(query.value('gas_checkbox_2'))
            model.set_checkbox_gas_3(query.value('gas_checkbox_3'))
            model.set_checkbox_gas_4(query.value('gas_checkbox_4'))
            model.set_checkbox_gas_5(query.value('gas_checkbox_5'))
            model.set_checkbox_gas_6(query.value('gas_checkbox_6'))
            model.set_checkbox_gas_7(query.value('gas_checkbox_7'))
            model.set_light_dim_1(query.value('dim_checkbox_1'))
            model.set_light_dim_2(query.value('dim_checkbox_2'))
            model.set_light_dim_3(query.value('dim_checkbox_3'))
            model.set_light_dim_4(query.value('dim_checkbox_4'))
            model.set_checkbox_differential_pressure_name(query.value('differential_gas_pressure_checkbox'))
            print(query.value('dim_checkbox_4'))

    def updateGeneralSettingsData(self, model):
        # ids = int(model.get_light_name_1())
        print("Light: " + model.get_light_name_1())
        light_name_1 = model.get_light_name_1()
        light_name_2 = model.get_light_name_2()
        light_name_3 = model.get_light_name_3()
        light_name_4 = model.get_light_name_4()
        light_name_5 = model.get_light_name_5()
        light_name_6 = model.get_light_name_6()
        gas_name_1 = model.get_gas_name_1()
        gas_name_2 = model.get_gas_name_2()
        gas_name_3 = model.get_gas_name_3()
        gas_name_4 = model.get_gas_name_4()
        gas_name_5 = model.get_gas_name_5()
        gas_name_6 = model.get_gas_name_6()
        gas_name_7 = model.get_gas_name_7()
        light_checkbox_1 = model.get_light_checkbox_1()
        light_checkbox_2 = model.get_light_checkbox_2()
        light_checkbox_3 = model.get_light_checkbox_3()
        light_checkbox_4 = model.get_light_checkbox_4()
        light_checkbox_5 = model.get_light_checkbox_5()
        light_checkbox_6 = model.get_light_checkbox_6()
        gas_checkbox_1 = model.get_checkbox_gas_1()
        gas_checkbox_2 = model.get_checkbox_gas_2()
        gas_checkbox_3 = model.get_checkbox_gas_3()
        gas_checkbox_4 = model.get_checkbox_gas_4()
        gas_checkbox_5 = model.get_checkbox_gas_5()
        gas_checkbox_6 = model.get_checkbox_gas_6()
        gas_checkbox_7 = model.get_checkbox_gas_7()
        dim_checkbox_1 = model.get_light_dim_checkbox_1()
        dim_checkbox_2 = model.get_light_dim_checkbox_2()
        dim_checkbox_3 = model.get_light_dim_checkbox_3()
        dim_checkbox_4 = model.get_light_dim_checkbox_4()
        differential_gas_pressure_checkbox = model.get_differential_gas_pressure_checkbox()

        query = QSqlQuery()
        print("Update: " + light_name_1)
        query.exec_("UPDATE GeneralSettings SET light_name_1 ='" + light_name_1 +
                    "', light_name_2 ='" + light_name_2 +
                    "', light_name_3 ='" + light_name_3 +
                    "', light_name_4 = '" + light_name_4 +
                    "', light_name_5 = '" + light_name_5 +
                    "', light_name_6 = '" + light_name_6 +
                    "', gas_name_1 ='" + gas_name_1 +
                    "', gas_name_2 ='" + gas_name_2 +
                    "', gas_name_3 ='" + gas_name_3 +
                    "', gas_name_4 = '" + gas_name_4 +
                    "', gas_name_5 = '" + gas_name_5 +
                    "', gas_name_6 = '" + gas_name_6 +
                    "', gas_name_7 = '" + gas_name_7 +
                    "', light_checkbox_1 ='" + str(light_checkbox_1) +
                    "', light_checkbox_2 ='" + str(light_checkbox_2) +
                    "', light_checkbox_3 ='" + str(light_checkbox_3) +
                    "', light_checkbox_4 = '" + str(light_checkbox_4) +
                    "', light_checkbox_5 = '" + str(light_checkbox_5) +
                    "', light_checkbox_6 = '" + str(light_checkbox_6) +
                    "', gas_checkbox_1 ='" + str(gas_checkbox_1) +
                    "', gas_checkbox_2 ='" + str(gas_checkbox_2) +
                    "', gas_checkbox_3 ='" + str(gas_checkbox_3) +
                    "', gas_checkbox_4 = '" + str(gas_checkbox_4) +
                    "', gas_checkbox_5 = '" + str(gas_checkbox_5) +
                    "', gas_checkbox_6 = '" + str(gas_checkbox_6) +
                    "', gas_checkbox_7 = '" + str(gas_checkbox_7) +
                    "', dim_checkbox_1 ='" + str(dim_checkbox_1) +
                    "', dim_checkbox_2 ='" + str(dim_checkbox_2) +
                    "', dim_checkbox_3 ='" + str(dim_checkbox_3) +
                    "', dim_checkbox_4 = '" + str(dim_checkbox_4) +
                    "', differential_gas_pressure_checkbox = '" + str(differential_gas_pressure_checkbox) +
                    "' WHERE id= 1")

    def queryAppearanceSettingsData(self, model):
        query = QSqlQuery()
        query.exec_("SELECT * FROM AppearanceSettings where id=1")
        while query.next():
            model.set_theme_color(query.value('theme_color'))
            model.set_appearance_theme_color_name(query.value('appearance_color_name'))
            model.set_theme_color_preview(query.value('theme_color_preview_image_path'))
            model.set_enable_disable_background_image(query.value('back_image_enable_disable'))
            model.set_background_image_path(query.value('background_image_path'))
            print("Query: " + query.value('background_image_path'))
            model.set_enable_disable_logo_image(query.value('logo_enable_disable'))
            model.set_logo_image_path(query.value('logo_path'))
            model.set_power_on_image_path(query.value('power_on_image_path'))
            model.set_combo_theme_color_index(query.value('theme_color_index'))

    def updateBackgroundImagePath(self, model):
        # ids = int(model.get_light_name_1())
        _background_image_path = model.get_background_image_path()
        query = QSqlQuery()
        query.exec_("UPDATE AppearanceSettings SET background_image_path ='" + _background_image_path + "' WHERE id= 1")

    def updateLogoImagePath(self, model):
        # ids = int(model.get_light_name_1())
        _logo_image_path = model.get_logo_image_path()
        query = QSqlQuery()
        query.exec_("UPDATE AppearanceSettings SET logo_path ='" + _logo_image_path + "' WHERE id= 1")

    def updatePowerOnImagePath(self, model):
        # ids = int(model.get_light_name_1())
        _power_on_image_path = model.get_power_on_image_path()
        query = QSqlQuery()
        query.exec_("UPDATE AppearanceSettings SET power_on_image_path ='" + _power_on_image_path + "' WHERE id= 1")

    def updateEnableDisableBackgroundImage(self, model):
        # ids = int(model.get_light_name_1())
        _enable_disable_background_image = model.get_enable_disable_background_image()
        query = QSqlQuery()
        query.exec_(
            "UPDATE AppearanceSettings SET back_image_enable_disable ='" + _enable_disable_background_image + "' WHERE id= 1")

    def updateEnableDisableLogoImage(self, model):
        # ids = int(model.get_light_name_1())
        _enable_disable_logo_image = model.get_enable_disable_logo_image()
        query = QSqlQuery()
        query.exec_(
            "UPDATE AppearanceSettings SET logo_enable_disable ='" + _enable_disable_logo_image + "' WHERE id= 1")

    def updateThemeColorDb(self, model):
        # ids = int(model.get_light_name_1())
        _theme_color = model.get_theme_color()
        _theme_color_name = model.get_appearance_theme_color_name()
        _theme_preview_image_path = model.get_theme_preview_image_path()
        _theme_color_index = model.get_combo_theme_color_index()
        query = QSqlQuery()
        query.exec_("UPDATE AppearanceSettings SET theme_color ='" + _theme_color
                    + "',theme_color_preview_image_path ='" + _theme_preview_image_path
                    + "',appearance_color_name ='" + _theme_color_name
                    + "', theme_color_index='" + str(_theme_color_index) + "' WHERE id= 1")

    def queryofhistorydata(self):
        query = "SELECT * FROM historyDetails where 1"
        return query

    def db_connect(self, filename, server):
        db = QSqlDatabase.addDatabase(server)
        db.setDatabaseName(filename)
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                                 "Unable to establish a database connection.\n"
                                 "This example needs SQLite support. Please read the Qt SQL "
                                 "driver documentation for information how to build it.\n\n"
                                 "Click Cancel to exit.", QMessageBox.Cancel)
            return False
        return True

    def querySwitchControlData(self, model):
        query = QSqlQuery()
        query.exec_("SELECT * FROM switchControl where 1")
        while query.next():
            model.set_light_brightness(query.value('lightBrightness'))
            model.set_light_brightness_original(query.value('lightBrightness_original'))
            model.set_light1Brightness_2(query.value('light1Brightness_2'))
            model.set_light1Brightness_2_original(query.value('light1Brightness_2_original'))
            model.set_light1Brightness_3(query.value('light1Brightness_3'))
            model.set_light1Brightness_3_original(query.value('light1Brightness_3_original'))
            model.set_light1Brightness_4(query.value('light1Brightness_4'))
            model.set_light1Brightness_4_original(query.value('light1Brightness_4_original'))

    def updateLight1BrightnessControl(self, model):
        # ids = int(model.get_light_name_1())
        _light_brightness = model.get_light_brightness()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET lightBrightness ='" + str(_light_brightness) + "'"
                    ", lightBrightness_original ='" + str(_light_brightness)+ "' WHERE id= 1")

    def updateLight1Brightness(self, model):
        # ids = int(model.get_light_name_1())
        _light_brightness = model.get_light_brightness()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET lightBrightness ='" + str(_light_brightness)
                    + "' WHERE id= 1")

    # ++++++++++++++++++++++++++++Light Brightness control update switch two++++++++++++++++++++++++++++++++++++++++++++
    def updateLight_two_BrightnessControl(self, model):
        # ids = int(model.get_light_name_1())
        _light_brightness_2 = model.get_light1Brightness_2()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET light1Brightness_2 ='" + str(_light_brightness_2) + "'"
                                                                                                  ", light1Brightness_2_original ='" + str(
            _light_brightness_2) + "' WHERE id= 1")

    def updateLight_two_Brightness(self, model):
        # ids = int(model.get_light_name_1())
        _light1Brightness_2 = model.get_light1Brightness_2()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET light1Brightness_2 ='" + str(_light1Brightness_2)
                    + "' WHERE id= 1")

    # ++++++++++++++++++++++++++++Light Brightness control update switch three++++++++++++++++++++++++++++++++++++++

    def updateLight_three_BrightnessControl(self, model):
        # ids = int(model.get_light_name_1())
        _light1Brightness_3 = model.get_light1Brightness_3()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET light1Brightness_3 ='" + str(_light1Brightness_3) + "'"
                                                                                                  ", light1Brightness_3_original ='" + str(
            _light1Brightness_3) + "' WHERE id= 1")

    def updateLight_three_Brightness(self, model):
        # ids = int(model.get_light_name_1())
        _light1Brightness_3 = model.get_light1Brightness_3()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET light1Brightness_3 ='" + str(_light1Brightness_3)
                    + "' WHERE id= 1")

    # ++++++++++++++++++++++++++++Light Brightness control update switch four++++++++++++++++++++++++++++++++++++++

    def updateLight_four_BrightnessControl(self, model):
        # ids = int(model.get_light_name_1())
        _light1Brightness_4 = model.get_light1Brightness_4()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET light1Brightness_4 ='" + str(_light1Brightness_4) + "'"
                    ", light1Brightness_4_original ='" + str(_light1Brightness_4) + "' WHERE id= 1")

    def updateLight_four_Brightness(self, model):
        # ids = int(model.get_light_name_1())
        _light1Brightness_4 = model.get_light1Brightness_4()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET light1Brightness_4 ='" + str(_light1Brightness_4)
                    + "' WHERE id= 1")

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++Toggle Switch Status++++++++++++++++++++++++++++++++++++++++++++++++
    '''def queryToggleSwitchStatus(self, model):
        query = QSqlQuery()
        query.exec_("SELECT toggle_switch_1, toggle_switch_2, toggle_switch_3, toggle_switch_4,"
                    " toggle_switch_5, toggle_switch_6 FROM switchControl where 1")
        while query.next():
            # print(query.value('theme_color_preview'))
            model.set_toggle_switch_1(query.value('toggle_switch_1'))
            model.set_toggle_switch_2(query.value('toggle_switch_2'))
            model.set_toggle_switch_3(query.value('toggle_switch_3'))
            model.set_toggle_switch_4(query.value('toggle_switch_4'))
            model.set_toggle_switch_5(query.value('toggle_switch_5'))
            model.set_toggle_switch_6(query.value('toggle_switch_6'))

    def updateToggleSwitchOne(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_1 = model.get_toggle_switch_1()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET toggle_switch_1 ='" + str(_toggle_switch_1) + "' WHERE id= 1")

    def updateToggleSwitchTwo(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_2 = model.get_toggle_switch_2()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET toggle_switch_2 ='" + str(_toggle_switch_2) + "' WHERE id= 1")

    def updateToggleSwitchThree(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_3 = model.get_toggle_switch_3()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET toggle_switch_3 ='" + str(_toggle_switch_3) + "' WHERE id= 1")

    def updateToggleSwitchFour(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_4 = model.get_toggle_switch_4()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET toggle_switch_4 ='" + str(_toggle_switch_4) + "' WHERE id= 1")

    def updateToggleSwitchFive(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_5 = model.get_toggle_switch_5()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET toggle_switch_5 ='" + str(_toggle_switch_5) + "' WHERE id= 1")

    def updateToggleSwitchSix(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_6 = model.get_toggle_switch_6()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET toggle_switch_6 ='" + str(_toggle_switch_6) + "' WHERE id= 1")'''

    def updateCountDownTimer(self, model):
        # ids = int(model.get_light_name_1())
        _count_down_timer_value = model.get_count_down_timer_value()
        query = QSqlQuery()
        query.exec_("UPDATE switchControl SET count_down_timer_value ='" + str(_count_down_timer_value) + "' WHERE id= 1")

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def db_create(self):
        query = QSqlQuery()
        query.exec_("create table GeneralSettings(id INTEGER PRIMARY KEY , "
                    "light_name_1 varchar(20), light_name_2 varchar(20), light_name_3 varchar(20), light_name_4 "
                    "varchar(20), light_name_5 varchar(20), light_name_6 varchar(20), light_checkbox_1 varchar(20), "
                    "light_checkbox_2 varchar(20), light_checkbox_3 varchar(20), light_checkbox_4 varchar(20), "
                    "light_checkbox_5 varchar(20), light_checkbox_6 varchar(20),gas_name_1 "
                    "varchar(20), gas_name_2 varchar(20), gas_name_3 varchar(20), gas_name_4 varchar(20), gas_name_5 "
                    "varchar(20), gas_name_6 varchar(20),gas_name_7 varchar(20), gas_checkbox_1 varchar(20), "
                    "gas_checkbox_2 varchar(20), "
                    "gas_checkbox_3 varchar(20), gas_checkbox_4 varchar(20), gas_checkbox_5 varchar(20), "
                    "gas_checkbox_6 varchar(20), gas_checkbox_7 varchar(20),dim_checkbox_1 varchar(20), "
                    "dim_checkbox_2 varchar(20), "
                    "dim_checkbox_3 varchar(20), dim_checkbox_4 varchar(20), differential_gas_pressure_checkbox "
                    "varchar(20))")

        query.exec_("create table AppearanceSettings(id INTEGER PRIMARY KEY , "
                    "theme_color varchar(20), back_image_enable_disable varchar(20), "
                    "background_image_path varchar(80),logo_enable_disable varchar(20), "
                    "logo_path varchar(80),appearance_color_name varchar(80),power_on_image_path varchar(80),"
                    "theme_color_preview_image_path varchar( "
                    "200), theme_color_index varchar(10))")

        query.exec_("create table themeColorSettings(id INTEGER PRIMARY KEY , "
                    "theme_color_hex varchar(20), theme_color_name varchar(20), active_inactive varchar(20),"
                    "theme_color_preview varchar(200))")

        query.exec_("create table image_table(id INTEGER PRIMARY KEY , "
                    "play_wh BLOB, pause_wh BLOB, changed_light_bulb BLOB,"
                    "changed_ot_light BLOB, low_light_bulb BLOB, low_ot_light BLOB,"
                    "changed_low_color varchar(80))")

        query.exec_("insert into themeColorSettings(theme_color_hex, theme_color_name, "
                    "active_inactive,theme_color_preview) values('#000000','Dark','True',"
                    "'/home/rnjn/RasberryProject/DigilineSystem/icon/theme-preview-image/dark-theme-preview.png')")
        query.exec_("insert into themeColorSettings(theme_color_hex, theme_color_name, "
                    "active_inactive,theme_color_preview) values('#FFFFFF','White','True',"
                    "'/home/rnjn/RasberryProject/DigilineSystem/icon/theme-preview-image/white-theme-preview.png')")
        query.exec_("insert into themeColorSettings(theme_color_hex, theme_color_name, "
                    "active_inactive,theme_color_preview) values('#808080','Gray','True',"
                    "'/home/rnjn/RasberryProject/DigilineSystem/icon/theme-preview-image/gray-theme-preview.png')")
        query.exec_("insert into themeColorSettings(theme_color_hex, theme_color_name, "
                    "active_inactive,theme_color_preview) values('#C0C0C0','Silver','True',"
                    "'/home/rnjn/RasberryProject/DigilineSystem/icon/theme-preview-image/silver-theme-preview.png')")

        query.exec_("insert into AppearanceSettings(theme_color, back_image_enable_disable, "
                    "background_image_path,logo_enable_disable, "
                    "logo_path, power_on_image_path,theme_color_preview_image_path,appearance_color_name) values("
                    "'#000000','False','', "
                    "'False','','','','Dark')")

        '''query.exec_("insert into GeneralSettings( light_name_1, light_name_2 ,light_name_3,light_name_4,"
                    "light_name_5,light_name_6,light_checkbox_1,light_checkbox_2,light_checkbox_3,light_checkbox_4,"
                    "light_checkbox_5,light_checkbox_6,gas_name_1,gas_name_2,gas_name_3,gas_name_4,gas_name_5,"
                    "gas_name_6,gas_checkbox_1,gas_checkbox_2,gas_checkbox_3,gas_checkbox_4,gas_checkbox_5,"
                    "gas_checkbox_6,dim_checkbox_1,dim_checkbox_2,dim_checkbox_3,dim_checkbox_4,"
                    "differential_gas_pressure_checkbox) values('2','3','3','3','3','3','3','3','3','3','3','3','3',"
                    "'3','3','3','3','3','3','3','3','3','3')")'''
        query.exec_("insert into GeneralSettings( light_name_1, light_name_2 ,light_name_3,light_name_4,light_name_5,"
                    "light_name_6,light_checkbox_1,light_checkbox_2,light_checkbox_3,light_checkbox_4,"
                    "light_checkbox_5,light_checkbox_6,gas_name_1,gas_name_2,gas_name_3,gas_name_4,gas_name_5,"
                    "gas_name_6,gas_checkbox_1,gas_checkbox_2,gas_checkbox_3,gas_checkbox_4,gas_checkbox_5,"
                    "gas_checkbox_6,dim_checkbox_1,dim_checkbox_2,dim_checkbox_3,dim_checkbox_4,"
                    "differential_gas_pressure_checkbox,gas_name_7,gas_checkbox_7) values('Gen Light - 1','Gen Light "
                    "- 2','OT 1','OT 2', "
                    "'Peripheral','Laminar','True','True','True','True','True','True','Oxygen', "
                    "'Nitrous Oxide','Medical Air','Instrument Air','Carbon Dioxide','Vacuum','True','True','True',"
                    "'True','True','True','True','True','True','True','True','IPS','True')")

        query.exec_("create table historyDetails(id INTEGER PRIMARY KEY , "
                    "date_time varchar(200), alarm_details varchar(100))")

        query.exec_("insert into historyDetails(date_time, alarm_details) values('20/12/2020','Oxygen Low')")
        query.exec_("insert into historyDetails(date_time, alarm_details) values('20/12/2020','Hydrogen Low')")

        query.exec_("create table userTable(id INTEGER PRIMARY KEY , "
                    "user_name varchar(200), user_password varchar(100))")

        query.exec_("create table switchControl(id INTEGER PRIMARY KEY , "
                    "lightBrightness varchar(100), lightBrightness_original varchar(100),"
                    "light1Brightness_2 varchar(100), light1Brightness_2_original varchar(100),"
                    "light1Brightness_3 varchar(100), light1Brightness_3_original varchar(100),"
                    "light1Brightness_4 varchar(100), light1Brightness_4_original varchar(100)," 
                    "count_down_timer_value varchar(100))")

        query.exec_("insert into switchControl(lightBrightness, lightBrightness_original, "
                    "light1Brightness_2, light1Brightness_2_original,"
                    "light1Brightness_3, light1Brightness_3_original,"
                    "light1Brightness_4, light1Brightness_4_original,"
                    "count_down_timer_value) values("
                    " 0, 0, 0, 0, 0, 0, 0, 0, 0)")

        query.exec_("insert into userTable(user_name, user_password) values('admin','pass')")

        query.exec_("create table iconColorControl(id INTEGER PRIMARY KEY , "
                    "border_color varchar(60), background_color varchar(60), text_color varchar(60),icon_color "
                    "varchar(60))")

        query.exec_("insert into iconColorControl(border_color, background_color,text_color,icon_color) values("
                    "'#FFFFFF','#000000','#FFFFFF','#FFFFFF')")

        ''' if __name__ == "__main__":
                app = QCoreApplication(sys.argv)
                createDB()
                sys.exit(app.exec_())'''
