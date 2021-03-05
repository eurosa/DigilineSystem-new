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

        # +++++++++++++++++++++++++++ Image byte array variable ++++++++++++++++++++++++++++++++++++++
        self._changed_light_bulb = bytearray
        self._changed_ot_light = bytearray
        self._low_light_bulb = bytearray
        self._low_ot_light = bytearray
        self._changed_low_color = str()
        self._changed_play = bytearray
        self._changed_pause = bytearray
        self._changed_on_speaker = bytearray
        self._changed_off_speaker = bytearray
        self._sound_on_off_flag = 1

        # ++++++++++++++++++++++++ End Alarm History Data Model ++++++++++++++++++++++++++++++++++++++
        #  Light Brightness control during initial value
        self._lightBrightness = str()
        self._lightBrightness_original = str()
        self._light1Brightness_2 = str()
        self._light1Brightness_2_original = str()
        self._light1Brightness_3 = str()
        self._light1Brightness_3_original = str()
        self._light1Brightness_4 = str()
        self._light1Brightness_4_original = str()
        # ++++++++++++++++++++++++++++++++++++++++Switch Control +++++++++++++++++++++++++++++++++++++++++
        self._toggle_switch_1 = str()
        self._toggle_switch_2 = str()
        self._toggle_switch_3 = str()
        self._toggle_switch_4 = str()
        self._toggle_switch_5 = str()
        self._toggle_switch_6 = str()
        # ++++++++++++++++++++++++++++++++++++++++++
        self._hours_cnt = int()
        self._minutes_cnt = int()
        self._seconds_cnt = int()
        # ++++++++++++++++++++++++++++++++++++++++++
        self._switch_temp_ctrl = int()
        self._switch_hum_ctrl = int()

    # ++++++++++++++++++++++++++++++++++++ Count Down Timer Counter value status ++++++++++++++++++++++++++
    def set_hours_cnt(self, _hours_cnt):
        self._hours_cnt = _hours_cnt

    def set_minutes_cnt(self, _minutes_cnt):
        self._minutes_cnt = _minutes_cnt

    def set_seconds_cnt(self, _seconds_cnt):
        self._seconds_cnt = _seconds_cnt

    def get_hours_cnt(self):
        return self._hours_cnt

    def get_minutes_cnt(self):
        return self._minutes_cnt

    def get_seconds_cnt(self):
        return self._seconds_cnt

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def set_switch_temp_ctrl(self, _switch_temp_ctrl):
        self._switch_temp_ctrl = _switch_temp_ctrl

    def set_switch_hum_ctrl(self, _switch_hum_ctrl):
        self._switch_hum_ctrl = _switch_hum_ctrl

    def get_switch_hum_ctrl(self):
        return self._switch_hum_ctrl

    def get_switch_temp_ctrl(self):
        return self._switch_temp_ctrl

    def set_toggle_switch_1(self, _toggle_switch_1):
        self._toggle_switch_1 = _toggle_switch_1

    def get_toggle_switch_1(self):
        return self._toggle_switch_1

    def set_toggle_switch_2(self, _toggle_switch_2):
        self._toggle_switch_2 = _toggle_switch_2

    def get_toggle_switch_2(self):
        return self._toggle_switch_2

    def set_toggle_switch_3(self, _toggle_switch_3):
        self._toggle_switch_3 = _toggle_switch_3

    def get_toggle_switch_3(self):
        return self._toggle_switch_3

    def set_toggle_switch_4(self, _toggle_switch_4):
        self._toggle_switch_4 = _toggle_switch_4

    def get_toggle_switch_4(self):
        return self._toggle_switch_4

    def set_toggle_switch_5(self, _toggle_switch_5):
        self._toggle_switch_5 = _toggle_switch_5

    def get_toggle_switch_5(self):
        return self._toggle_switch_5

    def set_toggle_switch_6(self, _toggle_switch_6):
        self._toggle_switch_6 = _toggle_switch_6

    def get_toggle_switch_6(self):
        return self._toggle_switch_6

    def set_count_down_timer_value(self, _count_down_timer_value):
        self._count_down_timer_value = _count_down_timer_value

    def get_count_down_timer_value(self):
        return self._count_down_timer_value

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def set_light_brightness(self, _lightBrightness):
        self._lightBrightness = _lightBrightness

    def get_light_brightness(self):
        return self._lightBrightness

    def set_light_brightness_original(self, _lightBrightness_original):
        self._lightBrightness_original = _lightBrightness_original

    def get_light_brightness_original(self):
        return self._lightBrightness_original

    # +++++++++++++ Light Brightness 2 +++++++++++++++++++++++++++++++
    def set_light1Brightness_2(self, _light1Brightness_2):
        self._light1Brightness_2 = _light1Brightness_2

    def get_light1Brightness_2(self):
        return self._light1Brightness_2

    def set_light1Brightness_2_original(self, _light1Brightness_2_original):
        self._light1Brightness_2_original = _light1Brightness_2_original

    def get_light1Brightness_2_original(self):
        return self._light1Brightness_2_original

        # +++++++++++++ Light Brightness 3 +++++++++++++++++++++++++++++++

    def set_light1Brightness_3(self, _light1Brightness_3):
        self._light1Brightness_3 = _light1Brightness_3

    def get_light1Brightness_3(self):
        return self._light1Brightness_3

    def set_light1Brightness_3_original(self, _light1Brightness_3_original):
        self._light1Brightness_3_original = _light1Brightness_3_original

    def get_light1Brightness_3_original(self):
        return self._light1Brightness_3_original

    # +++++++++++++ Light Brightness 4 +++++++++++++++++++++++++++++++

    def set_light1Brightness_4(self, _light1Brightness_4):
        self._light1Brightness_4 = _light1Brightness_4

    def get_light1Brightness_4(self):
        return self._light1Brightness_4

    def set_light1Brightness_4_original(self, _light1Brightness_4_original):
        self._light1Brightness_4_original = _light1Brightness_4_original

    def get_light1Brightness_4_original(self):
        return self._light1Brightness_4_original

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
    # ==============+Store QPixMap Image in Database+=============================================
    def set_changed_light_bulb(self, _changed_light_bulb):
        self._changed_light_bulb = _changed_light_bulb

    def get_changed_light_bulb(self):
        return self._changed_light_bulb

    def set_changed_ot_light(self, _changed_ot_light):
        self._changed_ot_light = _changed_ot_light

    def get_changed_ot_light(self):
        return self._changed_ot_light

    def set_low_light_bulb(self, _low_light_bulb):
        self._low_light_bulb = _low_light_bulb

    def get_low_light_bulb(self):
        return self._low_light_bulb

    def set_low_ot_light(self, _low_ot_light):
        self._low_ot_light = _low_ot_light

    def get_low_ot_light(self):
        return self._low_ot_light

    def set_changed_low_color(self, _changed_low_color):
        self._changed_low_color = _changed_low_color

    def get_changed_low_color(self):
        return self._changed_low_color

    def set_changed_play(self, _changed_play):
        self._changed_play = _changed_play

    def get_changed_play(self):
        return self._changed_play

    def set_changed_pause(self, _changed_pause):
        self._changed_pause = _changed_pause

    def get_changed_pause(self):
        return self._changed_pause

    def set_changed_on_speaker(self, _changed_on_speaker):
        self._changed_on_speaker = _changed_on_speaker

    def get_changed_on_speaker(self):
        return self._changed_on_speaker

    def set_changed_off_speaker(self, _changed_off_speaker):
        self._changed_off_speaker = _changed_off_speaker

    def get_changed_off_speaker(self):
        return self._changed_off_speaker

    def set_sound_on_off_flag(self, _set_sound_on_off_flag):
        self._sound_on_off_flag = _set_sound_on_off_flag

    def get_sound_on_off_flag(self):
        return self._sound_on_off_flag

