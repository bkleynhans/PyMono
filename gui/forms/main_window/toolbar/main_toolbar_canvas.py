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
        self.status_button = ttk.Button(
            master.canvases[self.canvas_name],
            text="Connect",
            command=lambda: self.process_connect_disconnect_button(master)
        )
        self.status_button.pack(
            side=LEFT,
            padx=(15, 0)
        )

        master.canvases[self.canvas_name].pack(anchor='w', fill='both', expand=True)


    # Process the Connect/Disconnect button operation
    def process_connect_disconnect_button(self, master):

        if self.status_button['text'] == "Connect":
            self.status_button['text'] = "Disconnect"

            self.close_connection(master)
        else:
            self.status_button['text'] = "Connect"

            self.open_connection(master)


    # Open connection to OL750
    def open_connection(self, master):

        self.change_color(master)
        try:
            # We connect to the OL750 with the number of the serial port only eg. 07
            com_port = self.root.preferences['ol750']['connection']['com']
            status = self.root.preferences['ol750']['obj'].SerialOpen(com_port)

            if status == 0:
                self.change_color(master)
        except:
            print('Unable to connect.  Please check the cable connection')


    # Close connection to OL750
    def close_connection(self, master):

        self.change_color(master)
        try:
            # Disconnect from the OL750
            status = self.root.preferences['ol750']['connection']['com']

            if status == 0:
                self.change_color(master)
        except:
            print('Unable to disconnect.  Please wait.')


    # Change the color of the activity monitor
    def change_color(self, master):

        if self.button_color == "red":
            self.button_color = "green"
            self.process_now(master, "green")
            print("green")

        else:
            self.button_color = "red"
            self.process_now(master, "red")

            print("red")


    # Change the button color and determine the process to execute based on the color
    def process_now(self, master, color):

        # Change the color of the connected/disconnected button
        master.canvases[self.canvas_name].itemconfig(self.oval_connected, fill=self.button_color)

        # Only open the sample processing window if we are connecting, not when we are disconnecting
        if (color == "green"):
            Sample_Window(self.root, master)