# Title: Python GUI Programming With TKinter - Widgets - MENUS
# Author: C. S. Germany 02/05/2022

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Basic Menu
def Menus_01_Basic_Menu():
    import tkinter as TK;
    window = TK.Tk();
    window.title("tkinter Menu Objects");
    window.geometry("300x250");
    window.configure(bg='white');

    #Empty event handlers for menu items
    def File_Menu_Handler():
        pass;

    def Edit_Menu_Handler():
        pass;    

    def View_Menu_Handler():
        pass;

    def Help_Menu_Handler():
        pass;        

    Main_Menu_Bar = TK.Menu(window);

    #File Menu
    File_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    File_Menu.add_command(label="New", command=File_Menu_Handler);
    File_Menu.add_command(label="Open", command=File_Menu_Handler);
    File_Menu.add_command(label="Save", command=File_Menu_Handler);
    File_Menu.add_command(label="Save as...", command=File_Menu_Handler);
    File_Menu.add_command(label="Close", command=File_Menu_Handler);    
    File_Menu.add_separator(); # Add separator line to menu
    File_Menu.add_command(label="Exit", command=window.quit); #built-in method closes window
    Main_Menu_Bar.add_cascade(label="File", menu=File_Menu); #adds menu File_Menu to Main_Menu_Bar   

    #Edit Menu
    Edit_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    Edit_Menu.add_command(label="Undo", command=Edit_Menu_Handler);
    Edit_Menu.add_command(label="Redo", command=Edit_Menu_Handler);
    Edit_Menu.add_command(label="Cut", command=Edit_Menu_Handler);
    Edit_Menu.add_command(label="Copy", command=Edit_Menu_Handler);
    Edit_Menu.add_command(label="Paste", command=Edit_Menu_Handler);
    Edit_Menu.add_command(label="Delete", command=Edit_Menu_Handler);
    Edit_Menu.add_command(label="Select All", command=Edit_Menu_Handler);    
    Main_Menu_Bar.add_cascade(label="Edit", menu=Edit_Menu); #adds menu File_Menu to Main_Menu_Bar      

    #View Menu
    View_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    View_Menu.add_command(label="Zoom In +", command=View_Menu_Handler);
    View_Menu.add_command(label="Zoom Out -", command=View_Menu_Handler);
    View_Menu.add_command(label="Status Bar", command=View_Menu_Handler);
    Main_Menu_Bar.add_cascade(label="View", menu=View_Menu); #adds menu File_Menu to Main_Menu_Bar    

    #Help Menu
    Help_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    Help_Menu.add_command(label="Help", command=Help_Menu_Handler);
    Help_Menu.add_command(label="Help Index", command=Help_Menu_Handler);
    Help_Menu.add_command(label="About", command=Help_Menu_Handler);
    Main_Menu_Bar.add_cascade(label="Help", menu=Help_Menu); #adds menu File_Menu to Main_Menu_Bar         

    #Add complmeted menu structure to window
    window.config(menu=Main_Menu_Bar);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Menu - Handling Events
def Menus_02_Basic_Menu_Handling_Events():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("tkinter Menu Objects");
    window.geometry("300x250");
    window.configure(bg='white');

    #Event handlers for File menu items
    def File_Menu_NEW_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From FILE menu clicked NEW");
    def File_Menu_OPEN_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From FILE menu clicked OPEN"); 
    def File_Menu_CLOSE_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From FILE menu clicked CLOSE"); 
    def File_Menu_SAVE_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From FILE menu clicked SAVE"); 
    def File_Menu_SAVEAS_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From FILE menu clicked SAVE AS"); 

    #Event handlers for Edit menu items
    def Edit_Menu_UNDO_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked UNDO");
    def Edit_Menu_REDO_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked REDO"); 
    def Edit_Menu_CUT_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked CUT"); 
    def Edit_Menu_COPY_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked COPY"); 
    def Edit_Menu_PASTE_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked PASTE");
    def Edit_Menu_DELETE_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked DELETE"); 
    def Edit_Menu_SELECTALL_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From EDIT menu clicked SELECT ALL");

    #Event handlers for View menu items
    def View_Menu_ZOOMIN_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM IN");
    def View_Menu_ZOOMOUT_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM OUT"); 
    def View_Menu_STATUSBAR_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked STATUS BAR");

    #Event handlers for Help menu items
    def Help_Menu_HELP_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From HELP menu clicked HELP");
    def Help_Menu_HELPINDEX_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From HELP menu clicked HELP INDEX"); 
    def Help_Menu_ABOUT_Handler(): TK.messagebox.showinfo(title='Menu Event Triggered: ', message="From HELP menu clicked ABOUT");     

    #Create main Menu Bar
    Main_Menu_Bar = TK.Menu(window);

    #File Menu
    File_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    File_Menu.add_command(label="New", command=File_Menu_NEW_Handler);
    File_Menu.add_command(label="Open", command=File_Menu_OPEN_Handler);
    File_Menu.add_command(label="Close", command=File_Menu_CLOSE_Handler);
    File_Menu.add_command(label="Save", command=File_Menu_SAVE_Handler);
    File_Menu.add_command(label="Save as...", command=File_Menu_SAVEAS_Handler);       
    File_Menu.add_separator(); # Add separator line to menu
    File_Menu.add_command(label="Exit", command=window.quit); #built-in method closes window
    Main_Menu_Bar.add_cascade(label="File", menu=File_Menu); #adds menu File_Menu to Main_Menu_Bar   

    #Edit Menu
    Edit_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    Edit_Menu.add_command(label="Undo", command=Edit_Menu_UNDO_Handler);
    Edit_Menu.add_command(label="Redo", command=Edit_Menu_REDO_Handler);
    Edit_Menu.add_command(label="Cut", command=Edit_Menu_CUT_Handler);
    Edit_Menu.add_command(label="Copy", command=Edit_Menu_COPY_Handler);
    Edit_Menu.add_command(label="Paste", command=Edit_Menu_PASTE_Handler);
    Edit_Menu.add_command(label="Delete", command=Edit_Menu_DELETE_Handler);
    Edit_Menu.add_command(label="Select All", command=Edit_Menu_SELECTALL_Handler);    
    Main_Menu_Bar.add_cascade(label="Edit", menu=Edit_Menu); #adds menu File_Menu to Main_Menu_Bar      

    #View Menu
    View_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    View_Menu.add_command(label="Zoom In +", command=View_Menu_ZOOMIN_Handler);
    View_Menu.add_command(label="Zoom Out -", command=View_Menu_ZOOMOUT_Handler);
    View_Menu.add_command(label="Status Bar", command=View_Menu_STATUSBAR_Handler);
    Main_Menu_Bar.add_cascade(label="View", menu=View_Menu); #adds menu File_Menu to Main_Menu_Bar    

    #Help Menu
    Help_Menu = TK.Menu(Main_Menu_Bar, tearoff=0);
    Help_Menu.add_command(label="Help", command=Help_Menu_HELP_Handler);
    Help_Menu.add_command(label="Help Index", command=Help_Menu_HELPINDEX_Handler);
    Help_Menu.add_command(label="About", command=Help_Menu_ABOUT_Handler);
    Main_Menu_Bar.add_cascade(label="Help", menu=Help_Menu); #adds menu File_Menu to Main_Menu_Bar         

    #Add complmeted menu structure to window
    window.config(menu=Main_Menu_Bar);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  

#-----Invocations-----
#Menus_01_Basic_Menu();
Menus_02_Basic_Menu_Handling_Events();




