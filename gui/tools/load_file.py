# -*- coding: utf-8 -*-
#!/usr/bin/env python3
###
#
# Python Monochrometer Interface
#
# Program Description : GUI master for the Landsat Buoy Calibration program
# Created By          : Benjamin Kleynhans
# Creation Date       : February 22, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 22, 2019
# Filename            : load_file.py
#
###

### Usage ###
# source_file = os.path.join(self.root.preferences['project_root'], 'gui', 'etc', 'ol750.cfg')
# loader = Load_File(self.root, master)
# my_data = loader.load(source_file)
###

# Imports
import json
import os
import pdb

from tkinter import *
from tkinter import filedialog


class Load_File:

    def __init__(self, root, master):

        self.root = root
        self.master = master


    def load(self, file):

        self.data = {}

        with open(file) as json_file:
            self.data = json.load(json_file)

        return self.data