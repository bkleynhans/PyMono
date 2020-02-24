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
        self.create_sample_frame(master)


    # Create the actual frame as a separate window
    def create_sample_frame(self, master):

        # # Add the sample notebook to the frame
        # Sample_Notebook(self.root, master.frames[self.frame_name])

        # Add the sample subframe to the sample frame
        Sample1_Frame(self.root, master.frames[self.frame_name])

        master.frames[self.frame_name].pack(anchor='w', fill=BOTH, expand=True, padx=10, pady=10)