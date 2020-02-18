###
#
# Entry file for 3D Math using Python and PyGame
#
# Program Description : This is the launcher file which initiates the OpenGL
#   renderer window.
# Created By          : Benjamin Kleynhans
# Creation Date       : January 25, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : January 25, 2020
# Filename            : launcher.py
#
###

# System Imports
import sys, os, inspect
import subprocess as sp
import pdb

# Module Imports
from lib.ol750_420_python_api import Ol750_420_Python_Api
from gui import mono750_gui

# Definitions
ERASE_LINE = '\x1b[2k'      # defines ASCII code to clear a Linux terminal
__PROJECT_ROOT = ''           # defines the root directory of the project for portability


# Calculate fully qualified path to location of program execution
def get_module_path():

    filename = inspect.getfile(inspect.currentframe())
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    return path, filename


# Set environment variables to locate current execution path
def set_path_variables():

    path, filename = get_module_path()

    sys.path.append(path)

    # Automatically build the path
    for element in os.walk(path):
        if ('/' in element[0]):
            ind = element[0].rindex('/')
            index_value = element[0][ind + 1]

            # If the directory does not start with a '_' or a '.' append it to the path
            if (index_value != '_') and (index_value != '.'):
                sys.path.append(element[0])

        elif ('\\' in element[0]):
            ind = element[0].rindex('\\')
            index_value = element[0][ind + 1]

            # If the directory does not start with a '_' or a '.' append it to the path
            if (index_value != '_') and (index_value != '.'):
                sys.path.append(element[0])


def main(args):

    global __PROJECT_ROOT

    __PROJECT_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    sp.call('clear', shell = True)

    set_path_variables()

    # args = {'project_root' : __PROJECT_ROOT}

    # ol750 = Ol750_420_Python_Api(args)
    mono750_gui.main(__PROJECT_ROOT)

    sp.call('clear', shell = True)


if __name__ == '__main__':
    args = main(sys.argv[1:])
