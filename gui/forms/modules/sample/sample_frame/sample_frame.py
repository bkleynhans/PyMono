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
import threading

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
# from gui.forms.modules.sample.sample_frame.sample_notebooks.sample_notebook import Sample_Notebook
from gui.forms.modules.sample.sample_frame.sample_notebooks.sample_sub_frames.sample_definition_frame import Sample_Definition_Frame
import pdb

class Sample_Frame(Gui_Label_Frame):

    # sample Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "sample_frame", "OL-750 Sample Properties")

        self.button_state = "Start"
        self.root.preferences['sample_status'] = "stopped"

        self.sample_thread = None

        self.create_sample_frame(master)


    # Create the actual frame as a separate window
    def create_sample_frame(self, master):

        # Add the sample subframe to the sample frame
        Sample_Definition_Frame(self.root, master.frames[self.frame_name])

        self.add_process_button(master)

        master.frames[self.frame_name].pack(anchor='w', fill=BOTH, expand=True, padx=10, pady=10)


    # Add the button that can be used to start/stop/pause operation
    def add_process_button(self, master):

        # Instantiate a start/pause button
        master.frames[self.frame_name].widgets['process_button'] = ttk.Button(
            master.frames[self.frame_name],
            text = "Start",
            command = lambda: self.process_start_pause_button(master)
        )
        # Pack the button as a seperate process in order to access its value
        master.frames[self.frame_name].widgets['process_button'].pack(
                anchor='w',
                side=LEFT,
                fill=BOTH,
                expand=True,
                padx=10,
                pady=10
        )

        # Instantiate a stop button
        master.frames[self.frame_name].widgets['stop_button'] = ttk.Button(
            master.frames[self.frame_name],
            text = "Stop", #unicode for lamda
            command = lambda: self.process_stop_button(master)
        )
        # Pack the button as a seperate process in order to access its value
        master.frames[self.frame_name].widgets['stop_button'].pack(
                anchor='w',
                side=RIGHT,
                fill=BOTH,
                expand=True,
                padx=10,
                pady=10
        )


    # Process the Start/Pause button operation
    def process_start_pause_button(self, master):

        process_button = master.frames[self.frame_name].widgets['process_button']

        if process_button['text'] == "Start":
            master.frames[self.frame_name].widgets['process_button']['text'] = "Pause"
            master.frames[self.frame_name].widgets['process_button']['state'] = "disabled"

            if self.root.preferences['sample_status'] == "stopped":
                self.process_start(master)
            else:
                self.root.preferences['sample_status'] = "running"
        else:
            master.frames[self.frame_name].widgets['process_button']['text'] = "Start"
            master.frames[self.frame_name].widgets['process_button']['state'] = "enable"

            self.process_pause(master)


    # Process the stop button
    def process_stop_button(self, master):
        print("stopped")
        self.root.preferences['sample_status'] = "stopped"


    def process_start(self, master):
        print("started")
        self.root.preferences['sample_status'] = "running"

        self.read_sample_definition(master)

        self.sample_thread = threading.Thread(target=self.root.ol750.start_sampling, args=())
        self.sample_thread.start()


    def process_pause(self, master):
        self.root.preferences['sample_status'] = "paused"
        print("paused")


    def read_sample_definition(self, master):

        sample_definition_frame = self.root.frames['sample_definition_frame']

        starting_nm = sample_definition_frame.widgets['starting_wavelength'].get()
        ending_nm = sample_definition_frame.widgets['ending_wavelength'].get()
        delta_nm = sample_definition_frame.widgets['change_in_wavelength'].get()
        delta_t = sample_definition_frame.widgets['time_between_wavelengths'].get()

        self.root.user_options['sample_definition']['starting_wavelength'] = starting_nm
        self.root.user_options['sample_definition']['ending_wavelengths'] = ending_nm
        self.root.user_options['sample_definition']['change_in_wavelength'] = delta_nm
        self.root.user_options['sample_definition']['time_between_wavelengths'] = delta_t


    # Destructor.  Usually not needed but in this case required to get rid of threads
    def __del__(self):

        if self.sample_thread != None:
            if self.sample_thread.isAlive():
                self.sample_thread.join()