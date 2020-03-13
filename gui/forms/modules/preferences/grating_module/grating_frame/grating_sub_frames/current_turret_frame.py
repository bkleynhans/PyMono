###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : February 18, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 18, 2020
# Filename            : current_turret_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Current_Turret_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "current_turret_frame", "Current Turret")
        self.create_current_turret_frame(master)


    # Create the actual frame as a separate window
    def create_current_turret_frame(self, master):

        self.current_turret_selection = StringVar()
        self.current_turret_selection.set('Turret 1')

        # Add Radio button for Turret 1 selection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Turret 1',
                variable = self.current_turret_selection,
                value = 'turret_1',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.current_turret_selection)).grid(
                        row = 0,
                        column = 0
        )

        # Add Radio button for Turret 2 selection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Turret 2',
                variable = self.current_turret_selection,
                value = 'turret_2',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.current_turret_selection)).grid(
                        row = 1,
                        column = 0)
                    
        # Add Radio button for Turret 13selection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Turret 3',
                variable = self.current_turret_selection,
                value = 'turret_3',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.current_turret_selection)).grid(
                        row = 2,
                        column = 0)


        master.frames[self.frame_name].pack(side=TOP, fill=BOTH, expand=True, anchor = 'w', padx = 10, pady = (20, 0))

    def toggle_active_selection(self, master, selection):

        self.root.preferences['connection']['current_turret'] = selection.get()