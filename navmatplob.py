import sys
import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_size_inches(100, 100, forward=True)
        self.axes = self.fig.add_subplot(111)
        #self.axes.set_xlabel("Time(H)")
        #self.axes.set_ylabel("Temperature(°C)")
        self.axes.xaxis.label.set_size(100)
        self.axes.yaxis.label.set_size(100)
        self.axes.grid(axis="x", color="green", alpha=.3, linewidth=2, linestyle=":")
        self.axes.grid(axis="y", color="black", alpha=.5, linewidth=.5)
        super(MplCanvas, self).__init__(self.fig)


'''class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()'''