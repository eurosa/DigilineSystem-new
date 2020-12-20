class Color:
    def __init__(self, ot_ui):
        self.ot_ui = ot_ui

    def toolButtonSettings(self):
        self.ui.oxygen.setStyleSheet("QToolButton{\n"
                                  "    border-style: outset;\n"
                                  "    border-width: 1px;\n"
                                  "    border-radius: 10px;\n"
                                  "    border-color: #000000;\n"
                                  "    font: bold 14px;\n"
                                  "\n"
                                  "    padding: 6px;\n"
                                  "    background-color: #FFFFFF;\n"
                                  "    color:#000000;\n"
                                  "}\n"
                                  "QToolButton:pressed {\n"
                                  "    background-color: gray;\n"
                                  "    border-style: inset;\n"
                                  "}")