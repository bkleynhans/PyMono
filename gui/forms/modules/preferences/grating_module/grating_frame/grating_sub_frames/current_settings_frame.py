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
# Filename            : current_settings_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Current_Settings_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "current_settings_frame", "Frame Title")

        self.master = master

        self.create_current_settings_frame(master)


    # Create the actual frame as a separate window
    def create_current_settings_frame(self, master):

        self.current_grating_selection = StringVar()
        self.current_grating_selection.set('Turret 1')

        # Add Radio button for Turret 1 selection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Grating 1',
                variable = self.current_grating_selection,
                value = 'grating_1',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.current_grating_selection)).grid(
                        row = 0,
                        column = 0
        )

        # Read in the scene id
        ttk.Label(
                master.frames[self.frame_name],
                text = 'Lower Effective Wavelength ',
                width = 10).grid(
                        row = 0,
                        column = 0,
                        padx = 10,
                        pady = 10,
                        sticky = 'nsew'
                )
        
        master.frames[self.frame_name].input_values['scene_id'] = ttk.Entry(master.frames[self.frame_name], width = 80)
        master.frames[self.frame_name].input_values['scene_id'].grid(
                row = 0, 
                column = 1, 
                columnspan = 3,
                padx = 10,
                pady = 10,
                sticky = 'nsew'
        )

        master.frames[self.frame_name].pack(side=RIGHT, fill=BOTH, expand=True, anchor='e', padx=10, pady=(20, 20))