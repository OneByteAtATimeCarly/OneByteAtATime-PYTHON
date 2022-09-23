# Title: Python GUI Programming With TKinter - Widgets - PROGRESSBARS
# Author: C. S. Germany 02/05/2022

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# HORIZONTAL Progressbar
def Progressbar_01_Horizontal_Set():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    window = TK.Tk();
    window.title("tkinter Progressbar Objects");
    window.geometry("300x160");
    window.configure(bg='white');              

    #Create and place Progressbar Object
    The_Bar = ttk.Progressbar(window, orient='horizontal', mode='determinate', length=280);
    The_Bar.grid(column=0, row=0, columnspan=2, padx=10, pady=20);  

    The_Bar['value'] = 50;

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# VERTICAL Progressbar
def Progressbar_02_Vertical_Set():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    window = TK.Tk();
    window.title("tkinter Progressbar Objects");
    window.geometry("25x380");
    window.configure(bg='white');              

    #Create and place Progressbar Object
    The_Bar = ttk.Progressbar(window, orient='vertical', mode='determinate', length=280);
    The_Bar.grid(column=0, row=0, columnspan=2, padx=10, pady=20);  

    The_Bar['value'] = 50;

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# HORIZONTAL Progressbar
def Progressbar_03_Horizontal():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("tkinter Progressbar Objects");
    window.geometry("300x160");
    window.configure(bg='white');   

    #Event Handlers for Progressbar Buttons
    def BTN_Progress_Handler():
     if The_Bar['value'] < 100:
        The_Bar['value'] += 20;
        value_label['text'] = update_progress_label();
     else:
           TK.messagebox.showinfo(message='Operation completed!');  

    def BTN_Reset_Handler():
        The_Bar.stop();
        value_label['text'] = update_progress_label();     

    def update_progress_label():
        return f"Current Progress: {The_Bar['value']}%";              

    #Create and place Progressbar Object
    The_Bar = ttk.Progressbar(window, orient='horizontal', mode='determinate', length=280);
    The_Bar.grid(column=0, row=0, columnspan=2, padx=10, pady=20);

    BTN_Progress = TK.Button(window, text="Make Progress", command=BTN_Progress_Handler);
    BTN_Progress.grid(column=0, row=2, padx=10, pady=10, sticky=TK.E);

    BTN_Reset = TK.Button(window, text="Reset", command=BTN_Reset_Handler);
    BTN_Reset.grid(column=1, row=2, padx=10, pady=10, sticky=TK.W); 

    value_label = TK.Label(window, text=update_progress_label())
    value_label.grid(column=0, row=1, columnspan=2);       

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# VERTICAL Progressbar
def Progressbar_04_Vertical():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("tkinter Progressbar Objects");
    window.geometry("170x425");
    window.configure(bg='white');   

    #Event Handlers for Progressbar Buttons
    def BTN_Progress_Handler():
     if The_Bar['value'] < 100:
        The_Bar['value'] += 20;
        value_label['text'] = update_progress_label();
     else:
           TK.messagebox.showinfo(message='Operation completed!');  

    def BTN_Reset_Handler():
        The_Bar.stop();
        value_label['text'] = update_progress_label();     

    def update_progress_label():
        return f"Current Progress: {The_Bar['value']}%";              

    #Create and place Progressbar Object
    The_Bar = ttk.Progressbar(window, orient='vertical', mode='determinate', length=280);
    The_Bar.grid(column=0, row=0, columnspan=2, padx=10, pady=20);

    BTN_Progress = TK.Button(window, text="Make Progress", command=BTN_Progress_Handler);
    BTN_Progress.grid(column=0, row=2, padx=10, pady=10, sticky=TK.E);

    BTN_Reset = TK.Button(window, text="Reset", command=BTN_Reset_Handler);
    BTN_Reset.grid(column=1, row=2, padx=10, pady=10, sticky=TK.W); 

    value_label = TK.Label(window, text=update_progress_label())
    value_label.grid(column=0, row=1, columnspan=2);       

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----Invocations-----
#Progressbar_01_Horizontal_Set();
#Progressbar_02_Vertical_Set();
Progressbar_03_Horizontal();
#Progressbar_04_Vertical();





