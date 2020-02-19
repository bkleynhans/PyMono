###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : GUI for the Landsat Buoy Calibration program
# Module Description  : Creates the connection_notebook that exists on the connection Frame.  Also
#                       handles all data input from the connection Frame
# Created By          : Benjamin Kleynhans
# Creation Date       : February 15, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 18, 2020
# Filename            : connection_notebook.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from gui.forms.base_classes.gui_notebook import Gui_Notebook
from gui.forms.preferences.connection_module.connection_frame.connection_sub_frames.interface_frame import Interface_Frame
from gui.forms.preferences.connection_module.connection_frame.connection_sub_frames.com_port_frame import COM_Port_Frame
from gui.forms.preferences.connection_module.connection_frame.connection_sub_frames.gpib_address_frame import GPIB_Address_Frame
import pdb

class Connection_Notebook(Gui_Notebook):

    # Connection Notebook constructor
    def __init__(self, master):

        Gui_Notebook.__init__(self, master, "connection_notebook")

        self.create_connection_notebook(master)


    # Create the connection_notebook object that will contain all the tabs
    def create_connection_notebook(self, master):

        # Add the connection notebook to the frame
        Connection_Notebook(master.frames[self.frame_name])

        master.notebooks[self.notebook_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)