from Window import ConverterGUI, Gtk
from file_functions import * 

win = ConverterGUI()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
