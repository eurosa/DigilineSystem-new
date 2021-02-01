from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

import configVariables


class LightSwitchDataBase:
    def __init__(self):
        configVariables.db = ""
        configVariables.db_history = ""
        configVariables.db_light = ""

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
        query.exec_(f"""insert into history_table(date_time, alarm_history, gas_name) 
        values('{date_time}', '{high_low}', '{gas_name}')""")

    def historydata(self):
        query = "SELECT * FROM history_table where 1"
        return query

    def db_connect(self, filename, server, connection):
        configVariables.db = QSqlDatabase.addDatabase(server, connection)
        configVariables.db.setDatabaseName(filename)
        configVariables.db_history = configVariables.db.database("history", open=True)
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
                    "date_time varchar(60), alarm_history varchar(20) , gas_name varchar(60))")

        query = QSqlQuery(configVariables.db_light)
        query.exec_("create table light_table(id INTEGER PRIMARY KEY , "
                    " sw_1 varchar(20), sw_2 varchar(20), sw_3 varchar(20), sw_4 varchar(20), sw_5 varchar(20),"
                    " sw_6 varchar(20),  intensity_1 varchar(20), intensity_2 varchar(20), intensity_3 varchar(20), "
                    " intensity_4 varchar(20))")

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
