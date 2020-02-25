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
# Filename            : sample_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
# from gui.forms.modules.sample.sample_frame.sample_notebooks.sample_notebook import Sample_Notebook
from gui.forms.modules.sample.sample_frame.sample_notebooks.sample_sub_frames.sample1_frame import Sample1_Frame
import pdb

class Sample_Frame(Gui_Label_Frame):

    # sample Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "sample_frame", "OL-750 Sample Properties")

        self.button_state = "Start"

        self.create_sample_frame(master)


    # Create the actual frame as a separate window
    def create_sample_frame(self, master):

        # Add the sample subframe to the sample frame
        Sample1_Frame(self.root, master.frames[self.frame_name])

        self.add_process_button(master)

        master.frames[self.frame_name].pack(anchor='w', fill=BOTH, expand=True, padx=10, pady=10)


    # Add the button that can be used to start/stop/pause operation
    def add_process_button(self, master):

        # Instantiate a start/pause button
        self.process_button = ttk.Button(
            master.frames[self.frame_name],
            text = "Start",
            command = lambda: self.process_start_pause_button(master)
        )
        # Pack the button as a seperate process in order to access its value
        self.process_button.pack(
                anchor='w',
                side=LEFT,
                fill=BOTH,
                expand=True,
                padx=10,
                pady=10
        )

        # Instantiate a stop button
        self.stop_button = ttk.Button(
            master.frames[self.frame_name],
            text = "Stop", #unicode for lamda
            command = lambda: self.process_stop_button(master)
        )
        # Pack the button as a seperate process in order to access its value
        self.stop_button.pack(
                anchor='w',
                side=RIGHT,
                fill=BOTH,
                expand=True,
                padx=10,
                pady=10
        )


    # Process the Start/Pause button operation
    def process_start_pause_button(self, master):

        if self.process_button['text'] == "Start":
            self.process_button['text'] = "Pause"
        else:
            self.process_button['text'] = "Start"


    # Process the stop button
    def process_stop_button(self, master):
        pass