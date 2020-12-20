#!/usr/bin/env python2

import pygtk
pygtk.require('2.0')
import gtk
from subprocess import call

label = gtk.Label("Shutdown computer?")
dialog = gtk.Dialog(
	"Shutdown computer?",
	None,
	gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
	(
		"Suspend", 1,
		"Hybrid Sleep", 4,
		"Hibernate", 2,
		"Shutdown", 8,
		"Reboot", 9,
		gtk.STOCK_CANCEL, 0
	)
)
dialog.set_position(gtk.WIN_POS_CENTER)

dialog.vbox.pack_start(label)
label.show()
response = dialog.run()
dialog.destroy()

action = "nothing"

if response == 1:
	action = "suspend"
elif response == 2:
	action = "hibernate"
elif response == 4:
	action = "hybrid-sleep"
elif response == 8:
	action = "poweroff"
elif response == 9:
	action = "reboot"


print (*"Got %d, executing %s ..." % (response, action))

if response > 0:
	call(["systemctl", action])
