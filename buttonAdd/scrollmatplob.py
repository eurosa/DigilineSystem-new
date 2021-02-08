import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import EllipseSelector


def onselect(eclick, erelease):
    "eclick and erelease are matplotlib events at press and release."
    print('startposition: (%f, %f)' % (eclick.xdata, eclick.ydata))
    print('endposition  : (%f, %f)' % (erelease.xdata, erelease.ydata))
    print('used button  : ', eclick.button)


def toggle_selector(event):
    print(' Key pressed.')
    if event.key in ['Q', 'q'] and _toggle_selector.active:
        print('EllipseSelector deactivated.')
        _toggle_selector.set_active(False)
    if event.key in ['A', 'a'] and not _toggle_selector.active:
        print('EllipseSelector activated.')
        _toggle_selector.set_active(True)


x = np.arange(100.) / 99
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

_toggle_selector = EllipseSelector(ax, onselect, drawtype='line')
fig.canvas.mpl_connect('key_press_event', toggle_selector)
plt.show()
