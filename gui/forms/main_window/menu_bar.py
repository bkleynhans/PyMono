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
# Last Modified Date  : October 23, 2019
# Filename            : menu_bar.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from gui import mono750_gui
from gui.forms.main_window.help_menu import Help_Menu
from gui.forms.modules.preferences.connection_module.connection_window import Connection_Window
from gui.forms.modules.preferences.filter_wheel_module.filter_wheel_window import Filter_Wheel_Window
from gui.forms.modules.preferences.grating_module.grating_window import Grating_Window


class Menu_Bar():

    # Menu Bar constructor
    def __init__(self, root, master):

        self.root = root

        self.create_menu_bar(master)


    # Create Menu Bar object
    def create_menu_bar(self, master):

        # Create menubar
        self.menu_bar = Menu(master)
        master.config(menu = self.menu_bar)
        master.menu_bar = self.menu_bar

        # Define the main menu options
        self.file_menu = Menu(self.menu_bar)
        self.edit_menu = Menu(self.menu_bar)
        self.help_menu = Menu(self.menu_bar)

        self.menu_bar.add_cascade(menu = self.file_menu, label = 'File')
        self.menu_bar.add_cascade(menu = self.edit_menu, label = 'Edit')

         # Define the File menu options
        self.file_menu.add_command(label = 'Exit', command = lambda: mono750_gui.on_closing(master))
        self.file_menu.entryconfig('Exit', accelerator = 'Ctrl+Q')

        # Define the Edit menu options
        self.preferences_menu = Menu(self.edit_menu)
        
        self.edit_menu.add_cascade(label='Preferences', menu = self.preferences_menu)
        
        # Define the Preferences sub-menu options
        self.preferences_menu.add_command(label = 'Connection', command = lambda: Connection_Window(self.root, master))
        self.preferences_menu.add_command(label = 'Filter Wheel Wavelengths', command = lambda: Filter_Wheel_Window(self.root, master))
        self.preferences_menu.add_command(label = 'Setup Gratings', command = lambda: Grating_Window(self.root, master))

        # Define the Help menu options
        self.menu_bar.add_command(label = 'Help', command = lambda: Help_Menu(master)) # Open the readme file on the GitHub page for the project