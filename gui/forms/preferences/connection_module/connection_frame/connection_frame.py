###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : GUI for the Landsat Buoy Calibration program
# Created By          : Benjamin Kleynhans
# Creation Date       : February 18, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 18, 2020
# Filename            : connection_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
from gui.forms.preferences.connection_module.connection_frame.connection_notebook import Connection_Notebook
import pdb

class Connection_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, master):

        Gui_Label_Frame.__init__(self, master, "connection_frame", "OL-750 Connection Properties")
        self.create_connection_frame(master)


    # Create the actual frame as a separate window
    def create_connection_frame(self, master):

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)

        # Add the connection notebook to the frame
        Connection_Notebook(master.frames[self.frame_name])
