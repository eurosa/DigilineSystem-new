import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation


xs = []
ys = []


class RealtimeGraph:
    def __init__(self, ui):
        super(RealtimeGraph, self).__init__()
        self.ui = ui

    # This function is called periodically from FuncAnimation
    def animate(self, i, xs, ys):
        # Read temperature (Celsius) from TMP102
        # temp_c = round("", 2)
        # temp_c = round(tmp102.read_temp(), 2)

        # Add x and y to lists
        # xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        # ys.append(temp_c)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        self.ui.tempForm.axes.clear()
        self.ui.tempForm.fig.autofmt_xdate()
        # self.ui.tempForm.axes.cla()
        self.ui.tempForm.axes.plot(xs, ys)
        self.ui.tempForm.axes.set_ylabel("Temp")
        # self.ui.tempForm.axes.set_xlim(xmin=0, xmax=10)
        # self.ui.tempForm.axes.set_ylim(ymin=0, ymax=10)
        # self.ui.tempForm.fig.tight_layout()
        # self.ui.tempForm.axes.show()
        # Format plot
        # self.ui.tempForm.xticks(rotation=45, ha='right')
        # self.ui.tempForm.subplots_adjust(bottom=0.30)
        # self.ui.tempForm.title('TMP102 Temperature over Time')
        # self.ui.tempForm.ylabel('Temperature (deg C)')

        # Set up plot to call animate() function periodically
        # ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
        # plt.show()

    def animateHumid(self, i, xs, ys):
        # Read temperature (Celsius) from TMP102
        # temp_c = round("", 2)
        # temp_c = round(tmp102.read_temp(), 2)

        # Add x and y to lists
        # xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        # ys.append(temp_c)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        self.ui.tempForm.axes.clear()
        self.ui.tempForm.fig.autofmt_xdate()
        # self.ui.tempForm.axes.cla()
        self.ui.humForm.axes.plot(xs, ys)
        self.ui.humForm.axes.set_ylabel("Humidity(%)")
        # self.ui.tempForm.axes.set_xlim(xmin=0, xmax=10)
        # self.ui.tempForm.axes.set_ylim(ymin=0, ymax=10)
        # self.ui.tempForm.fig.tight_layout()
        # self.ui.tempForm.axes.show()
        # Format plot
        # self.ui.tempForm.xticks(rotation=45, ha='right')
        # self.ui.tempForm.subplots_adjust(bottom=0.30)
        # self.ui.tempForm.title('TMP102 Temperature over Time')
        # self.ui.tempForm.ylabel('Temperature (deg C)')

        # Set up plot to call animate() function periodically
        # ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
        # plt.show()

