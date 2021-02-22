import datetime

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

import configVariables


class LightSwitchDataBase:
    def __init__(self):
        configVariables.db = ""
        configVariables.db_history = ""
        configVariables.db_light = ""
        configVariables.db_image = ""
        self.hwclock_time = ""
        self.hwclock_date = ""

    def init(self, filename, server, connection):
        import os
        if not os.path.exists(filename):
            self.db_connect(filename, server, connection)
            self.db_create()
        else:
            self.db_connect(filename, server, connection)
        print("Real Path: " + os.path.realpath('icon') + "/")

    def close(self):
        print("sery")

    '''def insertHistoryData(self, gas_name, date_time, high_low):
        query = QSqlQuery(self.db_history)
        query.exec_("insert into history_table values('{1}', '{2}', '{3}')".format(date_time, high_low, gas_name))'''

    def insertHistoryData(self, date_time, gas_name, high_low):
        query = QSqlQuery(configVariables.db_history)
        if date_time:
            date_time_obj = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f%z')
            date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f%z').strftime('%d/%m/%Y '
                                                                                                 '%H:%M:%S')
            self.hwclock_time = date_time_obj.time().strftime("%H:%M:%S")
            self.hwclock_date = date_time_obj.date().strftime('%d/%m/%Y')

        print("Hw Time: " + str(self.hwclock_time) + " Hw Date: " + str(self.hwclock_date))

        query.exec_(f"""insert into history_table(date_time, alarm_history, gas_name, hwclock_date, hwclock_time) 
        values('{date_time}', '{high_low}', '{gas_name}', '{self.hwclock_date}', '{self.hwclock_time}')""")

        '''query.exec_("DELETE FROM history_table WHERE  id NOT IN ( SELECT TOP ( 2 ) id FROM  "
                    "history_table ORDER BY date_time)")'''

    def historydata(self):
        query = QSqlQuery(configVariables.db_history)
        query.exec_("DELETE FROM history_table WHERE  id NOT IN ( SELECT id FROM history_table ORDER BY id desc limit "
                    "500)")
        '''query.exec_("DELETE FROM history_table WHERE  id NOT IN ( SELECT TOP ( 2 ) id FROM  "
                    "history_table ORDER BY date_time)")'''
        query_select = "SELECT date_time, alarm_history, gas_name  FROM history_table  ORDER BY date_time DESC"
        return query_select

    def graphDataSelect(self, model):
        query = QSqlQuery(configVariables.db_history)
        query.exec_("DELETE FROM graph_table WHERE  id NOT IN ( SELECT id FROM graph_table ORDER BY id desc limit "
                    "500)")
        '''query.exec_("DELETE FROM history_table WHERE  id NOT IN ( SELECT TOP ( 2 ) id FROM  "
                    "history_table ORDER BY date_time)")'''
        query_select = "SELECT date_time, id, temp_value, hum_value FROM graph_table  ORDER BY " \
                       "id  ASC "
        query.exec_(query_select)

        while query.next():
            if query.value('date_time'):
                date_time_obj = datetime.datetime.strptime(query.value('date_time'), '%Y-%m-%d %H:%M:%S.%f%z')
                # configVariables.my_time_list.append(date_time_obj.time().strftime("%H:%M"))
                hours, minutes = date_time_obj.time().strftime("%H:%M").split(':')
                minutes_total = int(hours) * 60 + int(minutes)
                configVariables.my_time_list[query.value('id')] = date_time_obj.time().strftime(
                    "%H:%M") + "\n " + date_time_obj.date().strftime('%d/%m/%Y')
                configVariables.my_temp_list[query.value('id')] = (query.value('temp_value'))
                configVariables.my_hum_list[query.value('id')] = float(query.value('hum_value'))
                configVariables.my_id_list[query.value('id')] = float(query.value('id'))
                # [configVariables.my_time_list.append(graph_time) for graph_time in configVariables.my_time_list if
                # graph_time not in configVariables.my_time_list]

                # configVariables.my_time_list.append(configVariables.my_time_list)
                # configVariables.my_temp_list.append(query.value('temp_value'))
                # configVariables.my_temp_list.append(query.value('hum_value'))
        print("Hello Time: " + str(configVariables.my_time_list))

    def insertGraphData(self, temp_value, hum_value, running_pass_time, date_time):
        query = QSqlQuery(configVariables.db_history)
        '''if date_time:
                    date_time_obj = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f%z')
                    date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f%z').strftime('%d/%m/%Y '
                                                                                                         '%H:%M:%S')
                    self.hwclock_time = date_time_obj.time().strftime("%H:%M:%S")
                    self.hwclock_date = date_time_obj.date().strftime('%d/%m/%Y')

        print("Hw Time: "+str(self.hwclock_time)+" Hw Date: "+str(self.hwclock_date))'''

        query.exec_(f"""insert into graph_table(date_time, temp_value,
         hum_value, running_pass_time) values('{date_time}', '{temp_value}', '{hum_value}', '{running_pass_time}')""")

    def insertPixMapByteArray(self, datamodel):
        changed_light_bulb = datamodel.get_changed_light_bulb()
        changed_ot_light = datamodel.get_changed_ot_light()
        low_light_bulb = datamodel.get_low_light_bulb()
        low_ot_light = datamodel.get_low_ot_light()
        changed_low_color = datamodel.get_changed_low_color()
        play_pixmap_byte = datamodel.get_changed_play()
        pause_pixmap_byte = datamodel.get_changed_pause()
        # print("Changed Light Bulb: "+str(changed_light_bulb))
        # print("Changed Low Light Color: " + str(changed_low_color))
        query = QSqlQuery(configVariables.db_history)
        # query.exec_(f"""insert into image_table( changed_light_bulb)
        #       values(  '{ckjk}')""")
        query.prepare("INSERT INTO image_table (changed_light_bulb, changed_ot_light, "
                      "low_light_bulb, low_ot_light, changed_low_color, play_wh, pause_wh) "
                      "VALUES ( :changed_light_bulb, :changed_ot_light, :low_light_bulb,"
                      " :low_ot_light, :changed_low_color, :play_wh, :pause_wh)")
        query.bindValue(":changed_light_bulb", changed_light_bulb)
        query.bindValue(":changed_ot_light", changed_ot_light)
        query.bindValue(":low_light_bulb", low_light_bulb)
        query.bindValue(":low_ot_light", low_ot_light)
        query.bindValue(":changed_low_color", changed_low_color)
        query.bindValue(":play_wh", play_pixmap_byte)
        query.bindValue(":pause_wh", pause_pixmap_byte)
        if not query.exec():
            qDebug() << "Error inserting image into table:\n" << query.lastError()

    def updatePixMapByteArray(self, datamodel):
        changed_light_bulb = datamodel.get_changed_light_bulb()
        changed_ot_light = datamodel.get_changed_ot_light()
        low_light_bulb = datamodel.get_low_light_bulb()
        low_ot_light = datamodel.get_low_ot_light()
        changed_low_color = datamodel.get_changed_low_color()
        play_pixmap_byte = datamodel.get_changed_play()
        pause_pixmap_byte = datamodel.get_changed_pause()
        # print("Changed Light Bulb: "+str(changed_light_bulb))
        # print("Changed Low Light Color: " + str(changed_low_color))
        query = QSqlQuery(configVariables.db_history)
        # query.exec_(f"""insert into image_table( changed_light_bulb)
        #       values(  '{ckjk}')""")
        # query.prepare('UPDATE "%s" SET value=:val WHERE property=:var' % tbl)
        query.prepare('UPDATE image_table SET changed_light_bulb=:changed_light_bulb,'
                      ' changed_ot_light=:changed_ot_light, low_light_bulb=:low_light_bulb,'
                      ' low_ot_light=:low_ot_light, changed_low_color=:changed_low_color, '
                      'play_wh=:play_wh, pause_wh=:pause_wh'
                      ' WHERE id=:var')

        query.bindValue(":changed_light_bulb", changed_light_bulb)
        query.bindValue(":changed_ot_light", changed_ot_light)
        query.bindValue(":low_light_bulb", low_light_bulb)
        query.bindValue(":low_ot_light", low_ot_light)
        query.bindValue(":changed_low_color", changed_low_color)
        query.bindValue(":play_wh", play_pixmap_byte)
        query.bindValue(":pause_wh", pause_pixmap_byte)
        query.bindValue(':var', 1)

        if not query.exec():
            qDebug() << "Error updating image into table:\n" << query.lastError()
        '''
        query.exec_(f"""insert into image_table(changed_light_bulb, changed_ot_light, low_light_bulb, low_ot_light, changed_low_color) 
                values('{changed_light_bulb}', '{changed_ot_light}', '{low_light_bulb}', '{low_ot_light}', '{changed_low_color}')""")

        '''

        # qDebug() << "Error inserting image into table:\n" << query.lastError()

    def queryChangedIconColorData(self, model):
        query = QSqlQuery(configVariables.db_history)
        query.exec_("SELECT * FROM image_table where 1")
        while query.next():
            # print(query.value('theme_color_preview'))
            model.set_changed_light_bulb(query.value('changed_light_bulb'))
            model.set_changed_ot_light(query.value('changed_ot_light'))
            model.set_low_light_bulb(query.value('low_light_bulb'))
            model.set_low_ot_light(query.value('low_ot_light'))
            model.set_changed_low_color(query.value('changed_low_color'))
            model.set_changed_play(query.value('play_wh'))
            model.set_changed_pause(query.value('pause_wh'))

    def tableRowCount(self, table_name):
        row_count = 0
        query = QSqlQuery(configVariables.db_history)
        query.exec("SELECT COUNT(*) FROM " + table_name + "")

        if query.first():
            row_count = query.value(0)
        return row_count

    # ++++++++++++++++++++++++++++++++++++++ Toggle Switch Status +++++++++++++++++++++++++++++++
    def queryToggleSwitchStatus(self, model):
        query = QSqlQuery(configVariables.db_history)
        query.exec_("SELECT toggle_switch_1, toggle_switch_2, toggle_switch_3, toggle_switch_4,"
                    " toggle_switch_5, toggle_switch_6, set_hum, set_temp"
                    " FROM switchControl where 1")
        while query.next():
            # print(query.value('theme_color_preview'))
            model.set_toggle_switch_1(query.value('toggle_switch_1'))
            model.set_toggle_switch_2(query.value('toggle_switch_2'))
            model.set_toggle_switch_3(query.value('toggle_switch_3'))
            model.set_toggle_switch_4(query.value('toggle_switch_4'))
            model.set_toggle_switch_5(query.value('toggle_switch_5'))
            model.set_toggle_switch_6(query.value('toggle_switch_6'))
            model.set_switch_hum_ctrl(query.value('set_hum'))
            model.set_switch_temp_ctrl(query.value('set_temp'))

    def queryCountDownTimerData(self, model):
        query = QSqlQuery(configVariables.db_history)
        query.exec_("SELECT hours_cnt, minutes_cnt, seconds_cnt"
                    " FROM switchControl where 1")
        while query.next():
            # print(query.value('theme_color_preview'))
            model.set_hours_cnt(query.value('hours_cnt'))
            model.set_minutes_cnt(query.value('minutes_cnt'))
            model.set_seconds_cnt(query.value('seconds_cnt'))

    def updateCntDwnTimer(self, model):
        # ids = int(model.get_light_name_1())
        _hours_cnt = model.get_hours_cnt()
        _minutes_cnt = model.get_minutes_cnt()
        _seconds_cnt = model.get_seconds_cnt()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET hours_cnt ='" + str(_hours_cnt) + "' "
                    ",minutes_cnt ='" + str(_minutes_cnt) + "'"
                    ",seconds_cnt ='" + str(_seconds_cnt) + "' WHERE id= 1")

    def updateToggleSwitchOne(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_1 = model.get_toggle_switch_1()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET toggle_switch_1 ='" + str(_toggle_switch_1) + "' WHERE id= 1")

    def updateToggleSwitchTwo(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_2 = model.get_toggle_switch_2()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET toggle_switch_2 ='" + str(_toggle_switch_2) + "' WHERE id= 1")

    def updateToggleSwitchThree(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_3 = model.get_toggle_switch_3()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET toggle_switch_3 ='" + str(_toggle_switch_3) + "' WHERE id= 1")

    def updateToggleSwitchFour(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_4 = model.get_toggle_switch_4()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET toggle_switch_4 ='" + str(_toggle_switch_4) + "' WHERE id= 1")

    def updateToggleSwitchFive(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_5 = model.get_toggle_switch_5()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET toggle_switch_5 ='" + str(_toggle_switch_5) + "' WHERE id= 1")

    def updateToggleSwitchSix(self, model):
        # ids = int(model.get_light_name_1())
        _toggle_switch_6 = model.get_toggle_switch_6()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET toggle_switch_6 ='" + str(_toggle_switch_6) + "' WHERE id= 1")

    def updateTempSwitchData(self, model):
        # ids = int(model.get_light_name_1())
        _switch_temp_ctrl = model.get_switch_temp_ctrl()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET set_temp ='" + str(_switch_temp_ctrl) + "' WHERE id= 1")

    def updateHumSwitchData(self, model):
        # ids = int(model.get_light_name_1())
        _switch_hum_ctrl = model.get_switch_hum_ctrl()
        query = QSqlQuery(configVariables.db_history)
        query.exec_("UPDATE switchControl SET set_hum ='" + str(_switch_hum_ctrl) + "' WHERE id= 1")

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def db_connect(self, filename, server, connection):
        configVariables.db = QSqlDatabase.addDatabase(server, connection)
        configVariables.db.setDatabaseName(filename)
        configVariables.db_history = configVariables.db.database("history", open=True)
        # configVariables.db_image = configVariables.db.database("image_con", open=True)
        # self.db_history = self.db.database("history", open=True)
        if not configVariables.db_history.open():
            QMessageBox.critical(None, "Cannot open database",
                                 "Unable to establish a database connection.\n"
                                 "This example needs SQLite support. Please read the Qt SQL "
                                 "driver documentation for information how to build it.\n\n"
                                 "Click Cancel to exit.", QMessageBox.Cancel)
            return False
        return True

    def db_create(self):
        print("DB_create:" + str(configVariables.db_history.open()))
        query = QSqlQuery(configVariables.db_history)
        query.exec_("create table history_table(id INTEGER PRIMARY KEY , "
                    "date_time varchar(60), hwclock_date, hwclock_time, "
                    "alarm_history varchar(20) , gas_name varchar(60))")

        query.exec_("create table graph_table(id INTEGER PRIMARY KEY , "
                    "temp_value varchar(60), "
                    "date_time varchar(60) ,running_pass_time varchar(20) , hum_value varchar(60))")

        '''query = QSqlQuery(configVariables.db_light)
        query.exec_("create table light_table(id INTEGER PRIMARY KEY , "
                    " sw_1 varchar(20), sw_2 varchar(20), sw_3 varchar(20), sw_4 varchar(20), sw_5 varchar(20),"
                    " sw_6 varchar(20),  intensity_1 varchar(20), intensity_2 varchar(20), intensity_3 varchar(20), "
                    " intensity_4 varchar(20))")'''

        query_image = QSqlQuery(configVariables.db_image)
        query.exec_("create table image_table(id INTEGER PRIMARY KEY , "
                    "play_wh BLOB, pause_wh BLOB, changed_light_bulb BLOB,"
                    "changed_ot_light BLOB, low_light_bulb BLOB, low_ot_light BLOB,"
                    "changed_low_color varchar(80))")

        query.exec_("create table switchControl(id INTEGER PRIMARY KEY ,"
                    "toggle_switch_1 varchar(10), toggle_switch_2 varchar(10),"
                    "toggle_switch_3 varchar(10), toggle_switch_4 varchar(10),"
                    "toggle_switch_5 varchar(10), toggle_switch_6 varchar(10),"
                    "hours_cnt INTEGER, minutes_cnt INTEGER, seconds_cnt INTEGER, set_hum INTEGER, "
                    "set_temp INTEGER)")

        query.exec_("insert into switchControl(toggle_switch_1, toggle_switch_2, "
                    "toggle_switch_3, toggle_switch_4,"
                    "toggle_switch_5, toggle_switch_6,"
                    "hours_cnt, minutes_cnt, seconds_cnt,"
                    "set_hum, set_temp) values("
                    " 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")

        '''query.exec_("create table GeneralSettings(id INTEGER PRIMARY KEY , "
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
                    "varchar(20))")'''
        '''
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

        '''

        ''' if __name__ == "__main__":
                app = QCoreApplication(sys.argv)
                createDB()
                sys.exit(app.exec_())'''
