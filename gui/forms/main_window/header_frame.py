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
# Last Modified Date  : October 29, 2019
# Filename            : header_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from gui.forms.base_classes.gui_frame import Gui_Frame
import pdb

class Header_Frame(Gui_Frame):

    # Header Frame constructor
    def __init__(self, root, master):

        Gui_Frame.__init__(self, root, master, "header_frame")
        self.create_header(master)


    # Create header frame object
    def create_header(self, master):

        master.frames[self.frame_name].pack(padx = 10, pady = (20, 0))

