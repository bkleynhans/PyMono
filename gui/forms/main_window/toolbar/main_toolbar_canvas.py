###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : February 22, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 22, 2020
# Filename            : toolbar_canvas.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from gui.forms.base_classes.gui_canvas import Gui_Canvas
from gui.forms.modules.sample.sample_window import Sample_Window
import pdb

class Main_Toolbar_Canvas(Gui_Canvas):

    # Canvas constructor
    def __init__(self, root, master):

        Gui_Canvas.__init__(self, root, master, "toolbar_canvas")
        self.create_canvas(master)


    # Create the actual Frame
    def create_canvas(self, master):

        self.canvas = Canvas(master, bg="white")

        # Create connection indicator (red/green dot)
        self.oval_connected = master.canvases[self.canvas_name].create_oval(2, 8, 12, 18, fill="")

        self.button_color = "red"
        master.canvases[self.canvas_name].itemconfig(self.oval_connected, fill=self.button_color)

        # Add connection button
        connect_button = ttk.Button(
            master.canvases[self.canvas_name],
            text="Connect",
            command=lambda: self.connect_to_ol750(master)
            ).pack(
                side=LEFT,
                padx=(15, 0)
        )

        master.canvases[self.canvas_name].pack(anchor='w', fill='both', expand=True)


    # Connect to OL750
    def connect_to_ol750(self, master):

        # self.change_color(master)
        try:
            pdb.set_trace()
            com_port = self.root.preferences['ol750']['connection']['com']
            status = self.root.preferences['ol750']['obj'].SerialOpen(com_port)

            if status == 0:
                self.change_color(master)
        except:
            print('Unable to connect.  Please check the cable connection')


    # Change the color of the activity monitor
    def change_color(self, master):

        if self.button_color == "red":
            self.button_color = "green"
            print("green")
            
        else:
            self.button_color = "red"
            print("red")


        self.change_now(master)

    # The color needs to be explicitely forced
    def change_now(self, master):

        master.canvases[self.canvas_name].itemconfig(self.oval_connected, fill=self.button_color)
        Sample_Window(self.root, master)