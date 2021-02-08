class DataModel:
    def __init__(self):
        self._light_name_1 = str()
        self._light_name_2 = str()  # real code might use an enum
        self._light_name_3 = str()
        self._light_name_4 = str()
        self._light_name_5 = str()  # real code might use an enum
        self._light_name_6 = str()
        self._light_checkbox_1 = str()
        self._light_checkbox_2 = str()  # real code might use an enum
        self._light_checkbox_3 = str()
        self._light_checkbox_4 = str()
        self._light_checkbox_5 = str()  # real code might use an enum
        self._light_checkbox_6 = str()
        self._checkbox_gas_1 = str()
        self._checkbox_gas_2 = str()  # real code might use an enum
        self._checkbox_gas_3 = str()
        self._checkbox_gas_4 = str()
        self._checkbox_gas_5 = str()  # real code might use an enum
        self._checkbox_gas_6 = str()
        self._checkbox_gas_7 = str()
        self._gas_name_1 = str()
        self._gas_name_2 = str()  # real code might use an enum
        self._gas_name_3 = str()
        self._gas_name_4 = str()
        self._gas_name_5 = str()  # real code might use an enum
        self._gas_name_6 = str()
        self._gas_name_7 = str()
        self._light_dim_1 = str()
        self._light_dim_2 = str()  # real code might use an enum
        self._light_dim_3 = str()
        self._light_dim_4 = str()
        self._differential_gas_pressure_checkbox = str()  # real code might use an enum
        # =================== Icon Color Settings =====================================
        self._border_color = str()
        self._background_color = str()
        self._text_color = str()
        self._icon_color = str()

        # =================== +++++++++++++++++++ =====================================
        # ===========================++++++++++++++++++++++++++++++====================
        self._theme_color = str()
        self._theme_preview_image_path = str()
        self._background_image_path = str()
        self._logo_image_path = str()
        self._power_on_image_path = str()
        self._enable_disable_background_image = str()
        self._enable_disable_logo_image = str()
        # ===========================++++++++++++Theme Color Settings++++++++++++++++++===============================
        self._theme_color_hex = str()
        self._theme_color_name = str()
        self._appearance_theme_color_name = str()
        self._theme_active_inactive = str()
        self._theme_color_preview = str()
        self._combo_theme_color_index = str()
        self._user_name = str()
        self._user_pass = str()

        # ++++++++++++++++++++++++ Start Alarm History Data Model Variable +++++++++++++++++++++++++++
        self.date_time = str()
        self.alarm_history = str()
        self.temp_date_time = str()
        self.hum_date_time = str()
        self.temp_value = str()
        self.hum_value = str()
        self._date_time = str()


    # ++++++++++++++++++++++++ End Alarm History Data Model ++++++++++++++++++++++++++++++++++++++

    # ================================Icon Color Settings Method =====================================================
    def set_border_col(self, name):
        self._border_color = name

    def get_border_col(self):
        return self._border_color

    def set_background_col(self, name):
        self._background_color = name

    def get_background_col(self):
        return self._background_color

    def set_text_col(self, name):
        self._text_color = name

    def get_text_col(self):
        return self._text_color

    def set_icon_col(self, name):
        self._icon_color = name

    def get_icon_col(self):
        return self._icon_color

    # ================================+++++++++++++++++++++++++++=====================================================
    # ================================ Login Form user name and password =============================================

    def set_user_name(self, name):
        self._user_name = name

    def get_user_name(self):
        return self._user_name

    def set_user_pass(self, name):
        self._user_pass = name

    def get_user_pass(self):
        return self._user_pass

    # ================================ End Login user name and password  =============================================

    # ==============================Start of Appearance Settings getter and setter====================================
    def set_combo_theme_color_index(self, name):
        self._combo_theme_color_index = name

    def get_combo_theme_color_index(self):
        return self._combo_theme_color_index

    def set_theme_color(self, name):
        self._theme_color = name

    def set_theme_color_preview(self, name):
        self._theme_color_preview = name

    def set_theme_color_name(self, name):
        self._theme_color_name = name

    def set_theme_color_hex(self, name):
        self._theme_color_hex = name

    def set_theme_active_inactive(self, name):
        self._theme_active_inactive = name

    def set_theme_preview_image_path(self, name):
        self._theme_preview_image_path = name

    def get_theme_color_name(self):
        return self._theme_color_name

    def get_theme_color_hex(self):
        return self._theme_color_hex

    def get_theme_active_inactive(self):
        return self._theme_active_inactive

    def get_theme_color_preview(self):
        return self._theme_color_preview

    # ==================================================================================================================

    def set_background_image_path(self, name):
        self._background_image_path = name

    def set_logo_image_path(self, name):
        self._logo_image_path = name

    def set_power_on_image_path(self, name):
        self._power_on_image_path = name

    def set_enable_disable_background_image(self, name):
        self._enable_disable_background_image = name

    def set_enable_disable_logo_image(self, name):
        self._enable_disable_logo_image = name

    def get_theme_color(self):
        return self._theme_color

    def get_theme_preview_image_path(self):
        return self._theme_preview_image_path

    def get_background_image_path(self):
        return self._background_image_path

    def get_logo_image_path(self):
        return self._logo_image_path

    def get_power_on_image_path(self):
        return self._power_on_image_path

    def get_enable_disable_background_image(self):
        return self._enable_disable_background_image

    def get_enable_disable_logo_image(self):
        return self._enable_disable_logo_image

    def get_appearance_theme_color_name(self):
        return self._appearance_theme_color_name

    def set_appearance_theme_color_name(self, name):
        self._appearance_theme_color_name = name

    # ==============================End of Appearance Settings getter and setter==============
    # real code would define a lot more class variables
    # ============================+Light======================================================
    def set_light_name_1(self, name):
        self._light_name_1 = name

    def set_light_name_2(self, name):
        self._light_name_2 = name

    def set_light_name_3(self, name):
        self._light_name_3 = name

    def set_light_name_4(self, name):
        self._light_name_4 = name

    def set_light_name_5(self, name):
        self._light_name_5 = name

    def set_light_name_6(self, name):
        self._light_name_6 = name

    def set_light_checkbox_1(self, name):
        self._light_checkbox_1 = name

    def set_light_checkbox_2(self, name):
        self._light_checkbox_2 = name

    def set_light_checkbox_3(self, name):
        self._light_checkbox_3 = name

    def set_light_checkbox_4(self, name):
        self._light_checkbox_4 = name

    def set_light_checkbox_5(self, name):
        self._light_checkbox_5 = name

    def set_light_checkbox_6(self, name):
        self._light_checkbox_6 = name

    # ======================================Gas=====================================
    def set_checkbox_gas_1(self, name):
        self._checkbox_gas_1 = name

    def set_checkbox_gas_2(self, name):
        self._checkbox_gas_2 = name

    def set_checkbox_gas_3(self, name):
        self._checkbox_gas_3 = name

    def set_checkbox_gas_4(self, name):
        self._checkbox_gas_4 = name

    def set_checkbox_gas_5(self, name):
        self._checkbox_gas_5 = name

    def set_checkbox_gas_6(self, name):
        self._checkbox_gas_6 = name

    def set_checkbox_gas_7(self, name):
        self._checkbox_gas_7 = name

    def set_gas_name_1(self, name):
        self._gas_name_1 = name

    def set_gas_name_2(self, name):
        self._gas_name_2 = name

    def set_gas_name_3(self, name):
        self._gas_name_3 = name

    def set_gas_name_4(self, name):
        self._gas_name_4 = name

    def set_gas_name_5(self, name):
        self._gas_name_5 = name

    def set_gas_name_6(self, name):
        self._gas_name_6 = name

    def set_gas_name_7(self, name):
        self._gas_name_7 = name

    # ======================================Dimming=====================================
    def set_light_dim_1(self, name):
        self._light_dim_1 = name

    def set_light_dim_2(self, name):
        self._light_dim_2 = name

    def set_light_dim_3(self, name):
        self._light_dim_3 = name

    def set_light_dim_4(self, name):
        self._light_dim_4 = name

    def set_checkbox_differential_pressure_name(self, name):
        self._differential_gas_pressure_checkbox = name

    # ===========================================Get=============================
    # ===========================================Light===========================
    def get_light_name_1(self):
        return self._light_name_1

    def get_light_name_2(self):
        return self._light_name_2

    def get_light_name_3(self):
        return self._light_name_3

    def get_light_name_4(self):
        return self._light_name_4

    def get_light_name_5(self):
        return self._light_name_5

    def get_light_name_6(self):
        return self._light_name_6

    def get_light_checkbox_1(self):
        return self._light_checkbox_1

    def get_light_checkbox_2(self):
        return self._light_checkbox_2

    def get_light_checkbox_3(self):
        return self._light_checkbox_3

    def get_light_checkbox_4(self):
        return self._light_checkbox_4

    def get_light_checkbox_5(self):
        return self._light_checkbox_5

    def get_light_checkbox_6(self):
        return self._light_checkbox_6

    # ====================================Gas ============================================
    def get_checkbox_gas_1(self):
        return self._checkbox_gas_1

    def get_checkbox_gas_2(self):
        return self._checkbox_gas_2

    def get_checkbox_gas_3(self):
        return self._checkbox_gas_3

    def get_checkbox_gas_4(self):
        return self._checkbox_gas_4

    def get_checkbox_gas_5(self):
        return self._checkbox_gas_5

    def get_checkbox_gas_6(self):
        return self._checkbox_gas_6

    def get_checkbox_gas_7(self):
        return self._checkbox_gas_7

    def get_gas_name_1(self):
        return self._gas_name_1

    def get_gas_name_2(self):
        return self._gas_name_2

    def get_gas_name_3(self):
        return self._gas_name_3

    def get_gas_name_4(self):
        return self._gas_name_4

    def get_gas_name_5(self):
        return self._gas_name_5

    def get_gas_name_6(self):
        return self._gas_name_6

    def get_gas_name_7(self):
        return self._gas_name_7

    # ==================================  Dimming  ===============================
    def get_light_dim_checkbox_1(self):
        return self._light_dim_1

    def get_light_dim_checkbox_2(self):
        return self._light_dim_2

    def get_light_dim_checkbox_3(self):
        return self._light_dim_3

    def get_light_dim_checkbox_4(self):
        return self._light_dim_4

    def get_differential_gas_pressure_checkbox(self):
        return self._differential_gas_pressure_checkbox

    # ++++++++++++++++++++++++ Start Alarm History Data Model Getter and Setter ++++++++++++++++++
    def set_alarm_date_time(self, date_time):
        self.date_time = date_time

    def set_alarm_history(self, alarm_history):
        self.alarm_history = alarm_history

    def get_alarm_date_time(self):
        return self.date_time

    def get_alarm_history(self):
        return self.alarm_history

    # ++++++++++++++++++++++++ End Alarm History Data Model ++++++++++++++++++++++++++++++++++++++

    # ++++++++++++++++++++++++ Start Temperature and Humidity Data Model Getter and Setter +++++++

    def set_date_time(self, _date_time):
        self._date_time = _date_time

    def get_date_time(self):
        return self._date_time

    def set_temp_value(self, temp_value):
        self.temp_value = temp_value

    def get_temp_value(self):
        return self.temp_value

    def set_hum_value(self, hum_value):
        self.hum_value = hum_value

    def get_hum_value(self):
        return self.hum_value

    # ++++++++++++++++++++++++ End Temperature and Humidity Data Model Getter and Setter +++++++++
