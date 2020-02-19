###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : GUI for the Landsat Buoy Calibration program
# Created By          : Benjamin Kleynhans
# Creation Date       : May 30, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : November 18, 2019
# Filename            : connection_window.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_window import Gui_Window
from gui.forms.preferences.connection_module.connection_frame.connection_frame import Connection_Frame
import pdb

class Connection_Window(Gui_Window):

    # connection Window constructor
    def __init__(self, master):

        Gui_Window.__init__(self, master, "connection_window", "Connection")
        self.create_connection_window(master)


    # Create the actual window as a separate window
    def create_connection_window(self, master):

        master.windows[self.window_name].protocol("WM_DELETE_WINDOW", lambda: self.on_closing(master))

        # Add the connection frame to the window
        Connection_Frame(master.windows[self.window_name])


    # Save changes made to connection
    def save_changes(self, master):

        pass
        master.windows[self.window_name].destroy()

    # Action to perform when connection window is closed
    def on_closing(self, master):

        if messagebox.askyesno("Save Preferences", "Do you wish to save your changes?"):
            self.save_changes(master)
        else:
            master.windows[self.window_name].destroy()