#!/usr/bin/env python3
###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : May 23, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : September 8, 2019
# Filename            : mono750_gui.py
#
###

# Imports
import json
import os

from tkinter import *
from tkinter import messagebox

from lib.ol750_420_python_api import Ol750_420_Python_Api


class Mono750_Gui:

    def __init__(self, master, args):

        self.root = master

        # Import gui paths
        from forms.main_window.menu_bar import Menu_Bar
        from forms.main_window.main_toolbar import Main_Toolbar
        from forms.main_window.header_frame import Header_Frame
        # from forms.main_window.input_module.input_frame import Input_Frame
        # from forms.main_window.status_module.status_frame import Status_Frame

        # Create the root Tkinter object
        master.title('CIS Mono750 System Interface')
        master.geometry('1024x768')
        master.resizable(False, False)
        #master.configure(background = '#FFFFFF')

        # Ensure the master frame cannot be detached from the main program
        master.option_add('*tearOff', False)

        # Create a dictionary of preferences which will contain all the program settings
        preferences = {
            'connection': {
                'interface': 'serial',
                'com': '07',
                'gpib': {
                    'pc_controller': 'gpib-00',
                    '750_device': 'gpib-03'
                }
            },
            'os_details': {
                'os': args['os'],
            },
            'project_root': args['project_root']
        }
        master.preferences = preferences

        # Create a dictionary to contain all the custom user settings
        user_options = {
            'sample1_frame': {
                'starting_wavelength': '',
                'ending_wavelength': '',
                'change_in_wavelength': '',
                'time_between_wavelengths': ''
            }
        }
        master.user_options = user_options

        # Create notebook container to easily access notebooks from other areas in the gui
        notebooks = {}
        master.notebooks = notebooks

        # Create frame container to easily access frames from other areas in the gui
        frames = {}
        master.frames = frames

        # Create widgets container to easily access widgets from other areas in the gui
        widgets = {}
        master.widgets = widgets

         # Create widgets container to easily access widgets from other areas in the gui
        canvases = {}
        master.canvases = canvases

        # Create toolbar container to easily access toolbars from other areas in the gui
        toolbars = {}
        master.toolbars = toolbars

        # Create window container to easily access windows from other areas in the gui
        windows = {}
        master.windows = windows

        # Create the Menubar - accessed via master.menu_bar
        Menu_Bar(self.root, master)

        # Create the Toolbar - accessed via master.menu_bar
        Main_Toolbar(self.root, master)

        # Create the Header - accessed via master.header_frame
        Header_Frame(self.root, master)

        # Connect to the OL750 API
        ol750 = Ol750_420_Python_Api(args)


# Ask the user to confirm if they want to close the program
def on_closing(root):

    pass
    if messagebox.askyesno("Quit", "Do you really wish to quit?"):
        root.destroy()


# Main entry to the GUI program
def main(project_root, args):

    root = Tk()
    root.project_root = project_root

    args['project_root'] = project_root
    # root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

    mono750_gui = Mono750_Gui(root, args)

    root.mainloop()
