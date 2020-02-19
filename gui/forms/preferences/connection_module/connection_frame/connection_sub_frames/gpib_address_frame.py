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
# Filename            : gpib_address_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class GPIB_Address_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, master):

        Gui_Label_Frame.__init__(self, master, "gpib_address_frame", "GPIB Address")

        self.create_gpib_address_frame(master)


    # Create the actual frame as a separate window
    def create_gpib_address_frame(self, master):

        # # Read in the scene id
        # ttk.Label(
        #     master.frames[self.frame_name],
        #     text = 'Clean Folders : ',
        #     width = 20).grid(
        #         row = 0,
        #         column = 0,
        #         padx = 10,
        #         pady = 10,
        #         sticky = 'w'
        #     )

        # master.master.master.master.preferences['general']['clean_folders'] = ttk.Entry(master.frames[self.frame_name], width = 30)
        # master.master.master.master.preferences['general']['clean_folders'].grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'e')

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)