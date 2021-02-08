from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111)
        plt.show()
        super(MplCanvas, self).__init__(self.fig)
