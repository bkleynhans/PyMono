###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : The input frame consists of multiple tabs and takes all the input for the program. Different tabs are enabled and disabled
#                       based on selections made by the user on the header frame.
# Created By          : Benjamin Kleynhans
# Creation Date       : May 28, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : November 8, 2019
# Filename            : input_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys
import datetime
import time
import threading
from gui.forms.general.progress_bar import Progress_Bar
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
# from gui.forms.main_window.input_module.input_notebook import Input_Notebook
from gui.forms.general.error_module.error_window import Error_Window
# from modules.core import menu
# from modules.core.model import Model
# from tools import test_paths
import pdb


class Input_Frame(Gui_Label_Frame):
    
    # Input Frame constructor
    def __init__(self, master):
                
        self.current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
                    
        Gui_Label_Frame.__init__(self, master, "input_frame", "Input")
        self.create_input_frame(master)
        
    
    # Create the actual Frame
    def create_input_frame(self, master):        
        
        master.frames[self.frame_name].pack(anchor = 'w', fill = 'both', expand = True, padx = 10, pady = 10)
        
        # # Add the input notebook to the frame
        # Input_Notebook(master.frames[self.frame_name], self.frame_name)
        
        # self.add_process_button(master)