# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:37:45 2017

@author: pravin vaity
"""
"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
" This fuction code create subframe with multiple entry labals for input and as well as for output "
" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

from tkinter import ttk

"------------------------------------------------------------------------------"
" Input label " 
def Sub_Frame_Entry(frame,title,title_heigth, title_width, T,Text,textvar,Entry):
#    T = xo,yo,height,width,array_x,array_y, space_up, space_down, space_mid
#Text = ["Beam Waist", "Wavelength","A","B"]
#textvar= [a,b,c,d]
    xo = T[0]
    yo = T[1]
    h  = T[2]
    w  = T[3]
    ax = T[4]
    ay = T[5]
    su = T[6]
    sd = T[7]
    sm = T[8]
    
    ttk.Label(frame,text=title,font="bold",anchor="center",background="#1E90FF").place(x=xo,y=yo,height=title_heigth,width=title_width)
    
    xo = xo+su
    yo = yo +title_heigth+sd
    kk = 0;
    
    for ii in range(ax):
        xi = xo
        for jj in range(ay):            
            Entry[kk]= Entry_Label(frame,Text[kk],xi,yo,h,w,sd,textvar[kk])
            kk = kk+1
            xi = xi+w+sm
        yo = yo+ 2*h+2*sd
        
    return Entry, xi, yo        
            
            
            
def Entry_Label(frame,txt,x1,y1,h,w,sd,textvar):
    
    ttk.Label(frame,text=txt,anchor="center").place(x=x1,y=y1,height=h,width=w)
    y1= y1 +h+sd/2;
    entry=ttk.Entry(frame,textvariable=textvar,justify="center").place(x=x1,y=y1,height=h,width=w)
    return entry
"------------------------------------------------------------------------------"
" Output label "
def Sub_Frame_Output(frame,title,title_heigth, title_width, T,Text,textvar):
#    T = xo,yo,height,width,array_x,array_y, space_up, space_down, space_mid
#Text = ["Beam Waist", "Wavelength","A","B"]
#textvar= [a,b,c,d]
    xo = T[0]
    yo = T[1]
    h  = T[2]
    w  = T[3]
    ax = T[4]
    ay = T[5]
    su = T[6]
    sd = T[7]
    sm = T[8]
    
    ttk.Label(frame,text=title,font="bold",anchor="center",background="#1E90FF").place(x=xo,y=yo,height=title_heigth,width=title_width)
    
    xo = xo+su
    yo = yo +title_heigth+sd
    kk = 0;
    
    for ii in range(ax):
        xi = xo
        for jj in range(ay):            
            Output_Label(frame,Text[kk],xi,yo,h,w,sd,textvar[kk])
            kk = kk+1
            xi = xi+w+sm
        yo = yo+ 2*h+2*sd
    return xi,yo
    
def Output_Label(frame,txt,x1,y1,h,w,sd,textvar):
    
    ttk.Label(frame,text=txt,anchor="center").place(x=x1,y=y1,height=h,width=w)
    y1= y1 +h+sd/2;
    ttk.Label(frame,textvariable=textvar,anchor="center",background ="#E6E6FA").place(x=x1,y=y1,height=h,width=w)
"----------------------------------- End --------------------------------------"