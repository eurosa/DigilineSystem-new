import re

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QPixmap, QIcon, QImage


class AllDisplayAttributeColor:
    def __init__(self, model):
        self.datamodel = model
        self.color_name = str()

    def changeAttributeColor(self, attribute_name, Attribute):
        print("Login background color: " + self.datamodel.get_background_col())
        attribute_name.setStyleSheet("" + Attribute + " {\n"
                                                      "    border-style: outset;\n"
                                                      "    border-width: 1px;\n"
                                                      "    border-radius: 10px;\n"
                                                      "    border-color: " + self.datamodel.get_border_col() + ";\n"
                                                                                                               "    font: bold 14px;\n"
                                                                                                               "     \n"
                                                                                                               "    padding: 6px;\n"
                                                                                                               "    background-color: " + self.datamodel.get_background_col() + ";\n"
                                                                                                                                                                                "    color:" + self.datamodel.get_text_col() + ";\n"
                                                                                                                                                                                                                               "   \n"
                                                                                                                                                                                                                               "}\n"
                                                                                                                                                                                                                               "" + Attribute + ":pressed {\n"
                                                                                                                                                                                                                                                "    background-color: gray;\n"
                                                                                                                                                                                                                                                "    border-style: inset;\n"
                                                                                                                                                                                                                                                "}\n"
                                                                                                                                                                                                                                                "")

    def changeDisplayAttributeColor(self, attribute_name, Attribute):
        attribute_name.setStyleSheet("" + Attribute + " {\n"
                                                      "    border-color: " + self.datamodel.get_border_col() + ";\n"

                                                                                                               "     \n"
                                                                                                               "    padding: 0px;\n"
                                                                                                               "    background-color: " ";\n"
                                                                                                               "    color:" + self.datamodel.get_text_col() + ";\n"
                                                                                                                                                              "   \n"
                                                                                                                                                              "}\n"
                                                                                                                                                              "")

    def changeDisplayLabelTextColor(self, attribute_name, Attribute):
        attribute_name.setStyleSheet("" + Attribute + " {\n"
                                                      "    border-color: " ";\n"

                                                      "     \n"
                                                      "    padding: 0px;\n"
                                                      "    background-color: " ";\n"
                                                      "    color:" + self.datamodel.get_text_col() + ";\n"
                                                                                                     "   \n"
                                                                                                     "}\n"
                                                                                                     "")

    def changeDisplayLabelBackgroundColor(self, attribute_name, Attribute):
        attribute_name.setStyleSheet("" + Attribute + " {\n"
                                                      "    border-color: " ";\n"

                                                      "     \n"
                                                      "    padding: 0px;\n"
                                                      "    background-color: " + self.datamodel.get_text_col() + ";\n"
                                                                                                                 "    color:" ";\n"
                                                                                                                 "   \n"
                                                                                                                 "}\n"
                                                                                                                 "")

    def changeDateTimeAttributeColor(self, attribute_name, Attribute):
        attribute_name.setStyleSheet("" + Attribute + " {\n"
                                                      "    border-color: " + self.datamodel.get_border_col() + ";\n"
                                                                                                               "    font: bold 33px;\n"
                                                                                                               "     \n"
                                                                                                               "    padding: 0px;\n"
                                                                                                               "    background-color: " ";\n"
                                                                                                               "    color:" + self.datamodel.get_text_col() + ";\n"
                                                                                                                                                              "   \n"
                                                                                                                                                              "}\n"
                                                                                                                                                              "")

    def changeTimeAttributeColor(self, attribute_name, Attribute):
        attribute_name.setStyleSheet("" + Attribute + " {\n"
                                                      "    border-color: " + self.datamodel.get_border_col() + ";\n"
                                                                                                               "    font: bold 160px;\n"
                                                                                                               "     \n"
                                                                                                               "    padding: 0px;\n"
                                                                                                               "    background-color: " ";\n"
                                                                                                               "    color:" + self.datamodel.get_text_col() + ";\n"
                                                                                                                                                              "   \n"
                                                                                                                                                              "}\n"
                                                                                                                                                              "")

    def changeTableViewAttributeColor(self, attribute_name, attribute):
        attribute_name.setStyleSheet(
            "color:" + self.datamodel.get_text_col() + "; background-color:" + self.datamodel.get_background_col() + ";")

    def changePlayerAttributeColor(self, attribute_name):
        attribute_name.setStyleSheet(
            "color:" + self.datamodel.get_text_col() + "; background-color:" + self.datamodel.get_background_col() + ";")

    def changeSettingsDialogAttributeColor(self, attribute_name):
        attribute_name.setStyleSheet(
            "color:" + self.datamodel.get_text_col() + ";background-color:" + self.datamodel.get_theme_color() + ";")

    def changeEditTextAttributeColor(self, attribute_name, Attribute):
        attribute_name.setStyleSheet("" + Attribute + " {\n"
                                                      "    border-style: outset;\n"
                                                      "    border-width: 1px;\n"
                                                      "    border-radius: 10px;\n"
                                                      "    border-color: " + self.datamodel.get_border_col() + ";\n"
                                                                                                               "    font: bold 14px;\n"
                                                                                                               "    background-color: " + self.datamodel.get_background_col() + ";\n"
                                                                                                                                                                                "    color:" + self.datamodel.get_text_col() + ";\n"
                                                                                                                                                                                                                               "}\n"
                                                                                                                                                                                                                               "")

    def changeSettingsDialogTabColor(self, attribute_name):
        attribute_name.setStyleSheet(
            "QTabBar::tab{"
            "    border-style: outset;"
            "    border-width: 1px;"
            "    border-radius: 10px;"
            "    padding: 6px;"
            "    background-color: " + self.datamodel.get_theme_color() + ";"
                                                                          "    color:" + self.datamodel.get_text_col() + ";"
                                                                                                                         "}"
                                                                                                                         "    QTabBar::tab:hover {"
                                                                                                                         "background-color: " + self.datamodel.get_border_col() + ";"
                                                                                                                                                                                  "border-style: outset;"
                                                                                                                                                                                  "padding: 6px;"
                                                                                                                                                                                  "}"
        )

    '''def changeSettingsDialogTabColor(self, attribute_name):
        attribute_name.setStyleSheet("QTabBar::tabWidget:selected {background: " + self.datamodel.get_theme_color() + ";}"
        " QTabWidget>QWidget>QWidget{background: " + self.datamodel.get_theme_color() + ";""}")'''

    def changeLoginDialogAttributeColor(self, attribute_name):
        attribute_name.setStyleSheet(
            "color:" + self.datamodel.get_text_col() + ";background-color:" + self.datamodel.get_theme_color() + ";")

    def changeShutDownDialogAttributeColor(self, attribute_name):
        attribute_name.setStyleSheet(
            "color:" + self.datamodel.get_text_col() + ";background-color:" + self.datamodel.get_theme_color() + ";")

    def changeTimerDialogAttributeColor(self, attribute_name):
        attribute_name.setStyleSheet(
            "color:" + self.datamodel.get_text_col() + ";background-color:" + self.datamodel.get_theme_color() + ";")

    def changeIconColor(self, attribute_name):
        self.image = QImage(attribute_name.icon().pixmap(attribute_name.iconSize()))
        for x in range(self.image.width()):
            for y in range(self.image.height()):
                pcolor = self.image.pixelColor(x, y)
                if pcolor.alpha() > 0:
                    n_color = QColor(self.datamodel.get_icon_col())
                    n_color.setAlpha(pcolor.alpha())
                    self.image.setPixelColor(x, y, n_color)
        attribute_name.setIcon(QIcon(QPixmap.fromImage(self.image)))
        # attribute_name.setIconSize(QSize(31, 31))\

    def changePixmapColor(self, attribute_name):
        self.image = QImage(attribute_name.pixmap())
        for x in range(self.image.width()):
            for y in range(self.image.height()):
                pcolor = self.image.pixelColor(x, y)
                if pcolor.alpha() > 0:
                    n_color = QColor(self.datamodel.get_icon_col())
                    n_color.setAlpha(pcolor.alpha())
                    self.image.setPixelColor(x, y, n_color)
        attribute_name.setPixmap(QPixmap.fromImage(self.image))
        # attribute_name.setIconSize(QSize(31, 31))

    def changeIconColorOfTimer(self, attribute_name, image):
        self.image = image
        for x in range(self.image.width()):
            for y in range(self.image.height()):
                pcolor = self.image.pixelColor(x, y)
                if pcolor.alpha() > 0:
                    n_color = QColor(self.datamodel.get_icon_col())
                    n_color.setAlpha(pcolor.alpha())
                    self.image.setPixelColor(x, y, n_color)
        attribute_name.setIcon(QIcon(QPixmap.fromImage(self.image)))
        # attribute_name.setIconSize(QSize(31, 31))

    def returnPixmapColorImage(self, image):
        self.image = image
        for x in range(self.image.width()):
            for y in range(self.image.height()):
                pcolor = self.image.pixelColor(x, y)
                if pcolor.alpha() > 0:
                    n_color = QColor(self.datamodel.get_icon_col())
                    n_color.setAlpha(pcolor.alpha())
                    self.image.setPixelColor(x, y, n_color)
        return QPixmap.fromImage(self.image)

    def returnPixmapColorImageLowLight(self, image):
        self.image = image
        for x in range(self.image.width()):
            for y in range(self.image.height()):
                pcolor = self.image.pixelColor(x, y)
                if pcolor.alpha() > 0:
                    n_color = QColor(self.color_variant(self.datamodel.get_icon_col(), 87))
                    print("Converted Hex: " + self.color_variant(self.datamodel.get_icon_col(), 87))
                    n_color.setAlpha(pcolor.alpha())
                    self.image.setPixelColor(x, y, n_color)
        return QPixmap.fromImage(self.image)

    def color_variant(self, hex_color, brightness_offset=1):
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
        '''
        if Y < 128:
            print("Black")
        else:
            print("White")'''
        print("Red" + str(R) + " Green" + str(G) + " Blue" + str(B))
        # https://stackoverflow.com/questions/9780632/how-do-i-determine-if-a-color-is-closer-to-white-or-black
        #
        """ takes a color like #87c95f and produces a lighter or darker variant """
        if len(hex_color) != 7:
            raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
        rgb_hex = [hex_color[x:x + 2] for x in [1, 3, 5]]
        new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
        new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int]  # make sure new values are between 0 and 255
        # hex() produces "0x88", we want just "88"
        return "#" + "".join([hex(i)[2:] for i in new_rgb_int])

    def changedIconColorImage(self, image):
        self.image = image
        for x in range(self.image.width()):
            for y in range(self.image.height()):
                pcolor = self.image.pixelColor(x, y)
                if pcolor.alpha() > 0:
                    n_color = QColor(self.datamodel.get_icon_col())
                    n_color.setAlpha(pcolor.alpha())
                    self.image.setPixelColor(x, y, n_color)
        return QIcon(QPixmap.fromImage(self.image))
        # attribute_name.setIconSize(QSize(31, 31))
        # attribute_name.setIcon(QIcon(QPixmap.fromImage(self.image)))

    '''def get_complementary(self, color):
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
            raise ValueError(f'"{hx}" is not a valid HEX code.')'''

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
