import gi
from file_functions import * 

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GLib

class ConverterGUI(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gif to Pointer")

        grid = Gtk.Grid()
        #box_chooser = Gtk.Box(spacing=10)
        #self.add(box_chooser)

        #box_convertButton = Gtk.Box(spacing=10)
        #self.add(box_convertButton)

        chooser = Gtk.Button(label="Choose File")
        chooser.connect("clicked", self.on_file_clicked)
        #box_chooser.add(chooser)
        grid.add(chooser)

        convert_button = Gtk.Button.new_with_label("Click Me")
        convert_button.connect("clicked", self.on_click_convert)
        #box_convertButton.pack_start(convert_button, True, True, 0)
        grid.attach(convert_button,5,5,3,1)

        self.add(grid)

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
    
    def on_click_convert(self, button):
        run_bashConverter()
