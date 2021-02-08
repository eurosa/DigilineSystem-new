import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QScrollArea
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


class ScrollableWindow(QMainWindow):
    def __init__(self, fig):
        self.qapp = QApplication([])

        QMainWindow.__init__(self)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QVBoxLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.canvas.mpl_connect("scroll_event", self.scrolling)

        self.show()
        exit(self.qapp.exec_())

    def scrolling(self, event):
        val = self.scroll.verticalScrollBar().value()
        if event.button == "down":
            self.scroll.verticalScrollBar().setValue(val + 100)
        else:
            self.scroll.verticalScrollBar().setValue(val - 100)


# create a figure and some subplots
fig, axes = plt.subplots(ncols=4, nrows=5, figsize=(16, 16))
for ax in axes.flatten():
    ax.plot([2, 3, 5, 1])

# pass the figure to the custom window
a = ScrollableWindow(fig)
