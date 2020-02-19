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
# Filename            : general_connection_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_frame import Gui_Frame
import pdb

class General_Connection_Frame(Gui_Frame):

    # connection Frame constructor
    def __init__(self, master):

        Gui_Frame.__init__(self, master, "general_connection_frame")

        self.create_connection_frame(master)


    # Create the actual frame as a separate window
    def create_connection_frame(self, master):

        #master.add(master.frames[self.frame_name], text = "general")

        # Read in the scene id
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Clean Folders : ',
            width = 20).grid(
                row = 0,
                column = 0,
                padx = 10,
                pady = 10,
                sticky = 'w'
            )

        master.preferences['general']['clean_folders'] = ttk.Entry(master.frames[self.frame_name], width = 30)
        master.preferences['general']['clean_folders'].grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'e')

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)