###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : GUI for the Landsat Buoy Calibration program
# Created By          : Benjamin Kleynhans
# Creation Date       : May 28, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : May 28, 2019
# Filename            : notebook.py
#
###

###
# tkcalendar available at https://pypi.org/project/tkcalendar/#files
# python module installation (Windows) : python -m pip install tkcalendar
###

from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date

class MyDateEntry(DateEntry):
    
    def __init__(self, master=None, **kw):
        #DateEntry.__init__(self, master=None, **kw)
        self.this_calendar = DateEntry()#.__init__(self, master = None, **kw)
        # add black border around drop-down calendar
        self._top_cal.configure(bg='black', bd=1)
        # add label displaying today's date below
        date_label = Label(
                self._top_cal,
                bg='gray90',
                anchor='w',
                text='Today: %s' % date.today().strftime('%x'))
        date_label.pack(fill='x')
        date_label.bind("<Button-1>", lambda e : self.this_calendar.set_date(date.today()))
        

root = Tk()
# change ttk theme to 'clam' to fix issue with downarrow button
style = ttk.Style(root)
style.theme_use('clam')

# create the entry and configure the calendar colors
de = MyDateEntry(root)

de.pack()
root.mainloop()