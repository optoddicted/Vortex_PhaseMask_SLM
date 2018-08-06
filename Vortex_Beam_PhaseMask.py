# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 18:18:42 2017

@author: pravin vaity
"""
""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Optical Vortex beam can be generated from Spatial Light Modulators (SLM) by uploading required phase mask. This GUI based code can be used to generate such a phase mask. If you someone find it useful and use it in their reserch work then please cite my paper: Pravin Vaity and R. P. Singh, Topological charge dependent propagation of optical vortices under quadratic phase transformation, Opt. Lett. 37, 1301-1303 (2012)
https://doi.org/10.1364/OL.37.001301 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
  
"------------------------------------------------------------------------------"
" Modules uploading "
import tkinter as Tk
import numpy as np
import FrameWork
import PhaseMask_Display

"------------------------------------------------------------------------------"
" Main GUI Window class "  
class WinDow:

    def __init__(self):
              
        self.button1 = Tk.Button(frame,text='Run', command=self._display, bg="green");
        self.button1.place(x=55,y=465,height=25,width=80)
        
        self.button2 = Tk.Button(frame, text='Quit', command=_quit,bg="red")
        self.button2.place(x=155,y=465,height=25,width=80)
        
        self.button3 = Tk.Button(frame,text='\u039b', command=self.increament_x);
        self.button3.place(x=126,y=413,height=13,width=13)
        
        self.button4 = Tk.Button(frame,text='V', command=self.decreament_x);
        self.button4.place(x=126,y=426,height=13,width=13)
        
        self.button5 = Tk.Button(frame,text='\u039b', command=self.increament_y);
        self.button5.place(x=256,y=413,height=13,width=13)
        
        self.button6 = Tk.Button(frame,text='V', command=self.decreament_y);
        self.button6.place(x=256,y=426,height=13,width=13)
        
        self.window = Tk.Tk()
        
    def increament_x(self):
        xs = xs_in.get()+1
        xs_in.set(xs)

    def decreament_x(self):
        xs = xs_in.get()-1
        xs_in.set(xs)
       
    def increament_y(self):
        ys = ys_in.get()+1
        ys_in.set(ys)

    def decreament_y(self):
        ys = ys_in.get()-1
        ys_in.set(ys)
      
        
    def _display(self):    
        wp = wp_in.get()
        Fn = Fn_in.get()
        th = th_in.get()*np.pi/180
        Pn = Pn_in.get()
        Ps = Ps_in.get()
        l  = l_in.get()
        xs = xs_in.get()
        ys = ys_in.get()
        
        W  = Pn*Ps
        wp = wp*Ps;
        
        Phase = tkvar.get()

        
        xy    = np.linspace(-Pn/2,Pn/2,Pn);  xy = xy*Ps;
        x, y  = np.meshgrid(xy,xy)
        phs   = np.angle(np.exp(1j*l*np.arctan2(y,x)))
        x     = x*np.cos(th)-y*np.sin(th)
        y     = x*np.sin(th)+y*np.cos(th)
        
        
        options = {"Vortex_Phase"   : Vortex_Phase,
               "Sinusoidal_Grating" : Sinusoidal,
               "Sinusoidal_Gauss"   : Sinusoidal_Gauss,
               "Blazed_Grating"     : Blazed,
               }
               
        Ph  =  options[Phase](phs,x,y,W,Fn,wp)
        
        self.window.quit()
        self.window.destroy()
        self.window = Tk.Tk()
        self.window.geometry('%dx%d+%d+%d' % (Pn, Pn, xs, ys))   
        self.window = PhaseMask_Display.FigureGUI(Ph,self.window)
        
    
def Vortex_Phase(phs,x,y,W,Fn,wp):
    Ph = phs
    return Ph

def Sinusoidal(phs,x,y,W,Fn,wp):
    Ph = (1+np.sin(2*np.pi*Fn*x/W+phs))/2
    return Ph  

def Blazed(phs,x,y,W,Fn,wp):
    Ph = np.exp(1j*(2*np.pi*Fn*x/W+phs))
    Ph = np.angle(Ph)
    return Ph 

def Sinusoidal_Gauss(phs,x,y,W,Fn,wp):
    Ph = (1+np.sin(2*np.pi*Fn*x/W+phs))*np.exp(-2*(x*x+y*y)/wp**2)/2
    return Ph      

def _quit():    
    root.quit()     # Stops & Exit Mainloop
    root.destroy()  # To Avoid python error 
               
        
"------------------------------------------------------------------------------"
"Initilization of main Window "                       
    
root = Tk.Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

root.geometry('%dx%d+%d+%d' % (290, 500, 5, 5))
root.title('Phase Mask for Vortex Beam')

"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
" DECLERATION of VARIABLES "
" --------------------------- Input Beam Parameter  --------------------------"
wp_in = Tk.DoubleVar(); wp_in.set(100);     " Beam Radius of input Gauss beam "
#lm_in = Tk.DoubleVar(); lm_in.set(405);     " Pump Wavelength "

"  ---------------------------- Grating Parameter ------------------------------ "
Fn_in = Tk.DoubleVar(); Fn_in.set(10);        # Fringes Number
th_in = Tk.DoubleVar(); th_in.set(0)      # Angle of rotation

"  ------------------------------ SLM Parameter -------------------------------- "
Pn_in = Tk.DoubleVar(); Pn_in.set(500);     # Pixel Numbers 
Ps_in = Tk.DoubleVar(); Ps_in.set(19);      # Pixel Size

"  ------------------------- Vortex Beam Parameter ----------------------------- "
l_in  = Tk.DoubleVar(); l_in.set(1);     # Topological Charge 

" --------------------------- Shifting Parameter  -------------------------------"
xs_in = Tk.DoubleVar(); xs_in.set(ws/2);
ys_in = Tk.DoubleVar(); ys_in.set(hs/2);

# Create a List variable
tkvar = Tk.StringVar(root);     # List variable 

"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"  FRAMES: Frame for lables & input  "
" --------------------------------- Main Frame ---------------------------------- "
xo = 10; yo = 0;
frame = Tk.Frame(root, bg='grey',height=450,width=270).place(x=xo,y=yo,height=460,width=270)

" ---------------------------  SLM Parameters ---------------------------"
x1 = xo+5; y1 = yo +5;
frame1  = Tk.Frame(root, bg='white').place(x=x1,y=y1,height=95,width=260)

Text    = ["Pixel Number", "Pixel Size (\u03bcm)"]
textvar = [Pn_in,Ps_in]
#T = xo,yo,height,width,array_x,array_y, space_up, space_down, space_mid
T       = x1,y1, 25,120,1,2,5,5,10     # Various values
entry   = [0,0]                   # Empty matrix to get entry data
#Sub_Frame_Entry(frame,title,title_heigth, title_width, T,Text,textvar,Entry)
Entry,x1,y1 = FrameWork.Sub_Frame_Entry(frame1,"SLM Parameters",30,260, T,Text,textvar,entry)

" --------------------------- Grating Parameters  --------------------------- "
x1 = xo+5; y1 = y1 +10; 
frame2  = Tk.Frame(root, bg='white').place(x=x1,y=y1,height=155,width=260)

Text    = ["No. of Fringes", "Rotation Angle (\u00b0)","Beam Radius (\u03bcm)","Vortex Charge"]
textvar = [Fn_in,th_in,wp_in,l_in]
#T = xo,yo,height,width,array_x,array_y, space_up, space_down, space_mid
T       = x1,y1, 25,120,2,2,5,5,10     # Various values
entry   = [0,0,0,0]                   # Empty matrix to get entry data

Entry,x1,y1 = FrameWork.Sub_Frame_Entry(frame2,"Grating Parameters",30,260, T,Text,textvar,entry)


" --------------------------- Menu Bar  ---------------------------"

x1 = xo+5; y1 = y1 + 10;
frame3  = Tk.Frame(root, bg='white').place(x=x1,y=y1,height=65,width=260)
# Dictionary with options
choices = { 'Vortex_Phase','Sinusoidal_Grating','Sinusoidal_Gauss','Blazed_Grating'}

tkvar.set('Vortex_Phase') # set the default option

x1 = xo+5; 
popupMenu = Tk.OptionMenu(frame3, tkvar, *choices)
Tk.Label(frame3, text="Choose Mask",font="bold",anchor="center",background="#1E90FF").place(x=x1,y=y1,height=30,width=260)
x1 =xo  + 35; y1 = y1+35
popupMenu.place(x=x1,y=y1,height=25,width=200)

" --------------------------- Shifting Parameters ---------------------------"
x1 = xo+5; y1 = y1 +40; 
frame2  = Tk.Frame(root, bg='white').place(x=x1,y=y1,height=100,width=260)

Text    = ["X-axis", "Y-axis"]
textvar = [xs_in,ys_in]
#T = xo,yo,height,width,array_x,array_y, space_up, space_down, space_mid
T       = x1,y1, 25,120,1,2,5,5,10     # Various values
entry   = [0,0]                   # Empty matrix to get entry data

Entry,x1,y1 = FrameWork.Sub_Frame_Entry(frame2,"Shifting Parameters",30,260, T,Text,textvar,entry)
#print(y1)

"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
" Main loop "
WinDow()            # Calling class window
root.mainloop()
"----------------------------------- END --------------------------------------"