###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : GUI for the Landsat Buoy Calibration program
# Module Description  : Creates the connection_notebook that exists on the connection Frame.  Also
#                       handles all data input from the connection Frame
# Created By          : Benjamin Kleynhans
# Creation Date       : May 30, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : October 30, 2019
# Filename            : connection_notebook.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from gui.forms.base_classes.gui_notebook import Gui_Notebook
from gui.forms.preferences.connection_module.connection_frame.connection_sub_frames.general_connection_frame import General_Connection_Frame
import pdb

class Connection_Notebook(Gui_Notebook):

    # Connection Notebook constructor
    def __init__(self, master):

        # Preferences
        self.preferences = {
                    'general': {
                            'clean_folders': 'False',
                            'folder_size': '500'},
                    'scene_id': '',
                    'date_frame_container': {
                        'frame': '',
                        'date_picker': '',
                        'date_label': '',
                        'date': ''},
                    'lat': '',
                    'lon': '',
                    'surface_temp': ''
            }

        Gui_Notebook.__init__(self, master, "connection_notebook")

        # Add local preferences dictionary to the object
        master.notebooks[self.notebook_name].preferences = self.preferences

        self.create_connection_notebook(master)


    # Create the connection_notebook object that will contain all the tabs
    def create_connection_notebook(self, master):

        # Add the General frame to the notebook
        General_Connection_Frame(master.notebooks[self.notebook_name])

        master.notebooks[self.notebook_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)