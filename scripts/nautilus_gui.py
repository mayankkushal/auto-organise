import os

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')

from gi.repository import Nautilus, GObject

class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):

    def menu_activate_cb(self, menu, file):
        os.system('organise -p {}'.format(file.get_location().get_path()))

    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        
        file = files[0]

        item = Nautilus.MenuItem(
            name="OrganiseExtension::Organise_Files",
            label="Organise",
            tip="Organise your folder"
        )
        item.connect('activate', self.menu_activate_cb, file)
        
        return [item]