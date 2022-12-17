import gi
from file_functions import * 

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GLib

class ConverterGUI(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gif to Pointer")

        box = Gtk.Box(spacing=6)
        self.add(box)

        chooser = Gtk.Button(label="Choose File")
        chooser.connect("clicked", self.on_file_clicked)
        box.add(chooser)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a gif", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open")
            Insert_to_file(dialog.get_filename())

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")

        dialog.destroy()

    def add_filters(self, dialog):

        filter_gif = Gtk.FileFilter()
        filter_gif.set_name(".gif file")
        filter_gif.add_mime_type("text/x-gif")
        filter_gif.add_pattern("*.gif")
        dialog.add_filter(filter_gif)
    
