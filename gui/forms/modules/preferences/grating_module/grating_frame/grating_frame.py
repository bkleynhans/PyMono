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
# Filename            : grating_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
from gui.forms.modules.preferences.grating_module.grating_frame.grating_notebook import Grating_Notebook
from gui.forms.modules.preferences.grating_module.grating_frame.grating_sub_frames.current_turret_frame import Current_Turret_Frame
from gui.forms.modules.preferences.grating_module.grating_frame.grating_sub_frames.current_grating_frame import Current_Grating_Frame
from gui.forms.modules.preferences.grating_module.grating_frame.grating_sub_frames.current_settings_frame import Current_Settings_Frame
import pdb

class Grating_Frame(Gui_Label_Frame):

    # template Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "grating_frame", "OL-750 Template Properties")
        self.create_grating_frame(master)


    # Create the actual frame as a separate window
    def create_grating_frame(self, master):

        # # Add the template notebook to the frame
        # Template_Notebook(self.root, master.frames[self.frame_name])

        # Add the Template1 Frame to the notebook
        Current_Turret_Frame(self.root, master.frames[self.frame_name])

        # Add the Template2 Frame to the notebook
        Current_Grating_Frame(self.root, master.frames[self.frame_name])

        # Add the Template3 Frame to the notebook
        Current_Settings_Frame(self.root, master.frames[self.frame_name])

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)
