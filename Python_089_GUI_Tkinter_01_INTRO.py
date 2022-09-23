# Title: Python GUI Programming With TKinter - INTRO
# Author: C. S. Germany 02/05/2022

# Link = https://realpython.com/python-gui-tkinter/

# Tkinter is the only framework that’s built into the Python standard library. Tkinter has several strengths. It’s cross-platform, so the same code works on Windows, macOS, and Linux. 
# Visual elements are rendered using native operating system elements, so applications built with Tkinter look like they belong on the platform where they’re run.
# Although Tkinter is considered the de facto Python GUI framework, it’s not without criticism. One notable criticism is that GUIs built with Tkinter look outdated. 
# If you want a shiny, modern interface, then Tkinter may not be what you’re looking for.

# The foundational element of a Tkinter GUI is the window. Windows are the containers in which all other GUI elements live. 
# These other GUI elements, such as text boxes, labels, and buttons, are known as widgets. Widgets are contained inside of windows.
# Note: Default version of the Python interpreter that's pre-installed on some Ubuntu versions leaves it out. So install with: apt-get install python3-tk

# Note: After importing from tkinter and adding widgets, you need to call mainloop() on the TK instance to get the window to display.


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def First_GUI_Function():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("450x300");
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------     


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
  
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#Invocations
First_GUI_Function();