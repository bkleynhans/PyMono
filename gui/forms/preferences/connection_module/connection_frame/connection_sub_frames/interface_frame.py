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
# Filename            : interface_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Interface_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, master):

        Gui_Label_Frame.__init__(self, master, "interface_frame", "Device Interface")

        self.create_interface_frame(master)


    # Create the actual frame as a separate window
    def create_interface_frame(self, master):

        self.interface_selection = StringVar()
        self.interface_selection.set('serial')

        # Add Radio button for Serial connection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Serial',
                variable = self.interface_selection,
                value = 'serial',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.interface_selection)).grid(
                        row = 0,
                        column = 0
        )

        # Add Radio button for GPIB connection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'GPIB',
                variable = self.interface_selection,
                value = 'gpib',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.interface_selection)).grid(
                        row = 0,
                        column = 1)


        master.frames[self.frame_name].pack(padx = 10, pady = (20, 0))
        # master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)

    def toggle_active_connection(self, master, selection):

        pdb.set_trace()

        master.master.master.master.preferences['connection']['interface'] = selection.get()