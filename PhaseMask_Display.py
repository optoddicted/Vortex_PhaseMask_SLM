# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:05:11 2017

@author: pravin vaity
""" 
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
This code generates window for phase mask display. This must be called from Vortex_ Beam_PhaseMask (Main code) 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

import matplotlib
matplotlib.use('TkAgg')
import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def FigureGUI(Ph,window):
    window.wm_title("Phase Mask")
    
    f = Figure(figsize=(5, 5))
    f.subplots_adjust(left=0,right=1,bottom=0,top=1)
    a = f.add_subplot(111) 

    a.axis('off')
    a.imshow(Ph,cmap='gray')

    canvas = FigureCanvasTkAgg(f, master=window)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


    Tk.mainloop()
    
    return window