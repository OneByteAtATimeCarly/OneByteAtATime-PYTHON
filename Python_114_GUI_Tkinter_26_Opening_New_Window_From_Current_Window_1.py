# Title: Python GUI Programming With TKinter - Opening a New Window from the Current Window 1
# Author: C. S. Germany 02/05/2022

#Import tkinter library
import tkinter as tk;
from tkinter import *;
from tkinter import ttk;
win = Tk();
win.geometry("600x300");

#Define a new function to open the window
def Open_New_Name_Window():
    
    Name_Data = tk.StringVar();

    def SUBMIT_Button_Handler():
        The_Name = Entry_NAM.get();
        print("Name =",The_Name);
        Name_Window.destroy();

    Name_Window = tk.Tk();
    Name_Window.configure(bg='black'); 
    Name_Window.title("Please enter your name.");
    Name_Window_Width = 300;
    Name_Window_Height = 150;
    ScreenWidth = Name_Window.winfo_screenwidth();
    ScreenHeight = Name_Window.winfo_screenheight();
    Appear_in_the_Middle = '%dx%d+%d+%d' % (Name_Window_Width, Name_Window_Height, (ScreenWidth - Name_Window_Width) / 2, (ScreenHeight - Name_Window_Height) / 2);
    Name_Window.geometry(Appear_in_the_Middle);
    Name_Window.resizable(width=False, height=False);
    Label_NAM = Label(Name_Window, text="Please enter your name below, player.", font=('Helvetica 12'), bg='black', fg='white').pack(pady=10);
    Entry_NAM = tk.Entry(Name_Window, width=25, font=('Helvetica 12'),textvariable=Name_Data).pack(pady=10);
    Button_NAM = Button(Name_Window, width=15, height=10, font=('Helvetica 11'), text="SUBMIT", bg='red', command=SUBMIT_Button_Handler).pack(pady=10);

#Create a label
Label(win, text= "Click button below to open new Window", font= ('Helvetica 17 bold')).pack(pady=30);
#Create a button to open a New Window
ttk.Button(win, text="Open", command=Open_New_Name_Window).pack();
win.mainloop();
