# Title: Python GUI Programming With TKinter - Widgets - PANEDWINDOWS
# Author: C. S. Germany 02/05/2022

# Panedwindow Objects. Let you stack 2 or more resizable widgets above and below each other (or to the left and right). 
# Users can adjust their relative heights (or widths) by dragging a sash located between the panes. 
# Typically widgets you're adding to a panedwindow will be frames containing other widgets.
# Panewindows can also be added to each other.

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Panedwindow - Instantiating
def Panedwindow_0l():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Panewindow Objects");
    window.geometry("600x600");
    window.configure(bg='white');         

    #LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rarity's Perfect Panewindow"); 
    #LAB_Title.place(x=45,y=10,height=30,width=360);

    #1. Create 1st Panewindow and pack it
    PW_Panedwindow_1 = TK.PanedWindow();
    PW_Panedwindow_1.pack(fill=TK.BOTH, expand=1);

    #2. Create label and add it to 1st Panewindow
    LB_Left = TK.Label(PW_Panedwindow_1, text="Left Pane");
    PW_Panedwindow_1.add(LB_Left);

    #3. Create 2nd Panewindow and add it to 1st Panewindow
    PW_Panedwindow_2 = TK.PanedWindow(PW_Panedwindow_1, orient=TK.VERTICAL);
    PW_Panedwindow_1.add(PW_Panedwindow_2);

    #4. Create label and add it to 1st Panewindow
    LB_Top = TK.Label(PW_Panedwindow_2, text="Top Pane");
    PW_Panedwindow_2.add(LB_Top);

    #5. Create label and add it to 2nd Panewindow
    LB_Bottom = TK.Label(PW_Panedwindow_2, text="Bottom Pane")
    PW_Panedwindow_2.add(LB_Bottom);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Panedwindow - Instantiating
def Panedwindow_02():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Panewindow Objects");
    window.geometry("300x300");
    window.configure(bg='white');         

    #LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rarity's Perfect Panewindow"); 
    #LAB_Title.place(x=45,y=10,height=30,width=360);

    #1. Create 1st Panedwindow
    PW_Panedwindow_1 = TK.PanedWindow();
    PW_Panedwindow_1.pack(fill = TK.BOTH, expand = 1);

    #2. Create Entry and add it to Panedwindow 
    ENT_Left = TK.Entry(PW_Panedwindow_1, bd = 5);
    PW_Panedwindow_1.add(ENT_Left);

    #3. Create 2nd Panedwindow and add it to 1st Panedwindow
    PW_Panedwindow_2 = TK.PanedWindow(PW_Panedwindow_1, orient = TK.VERTICAL);
    PW_Panedwindow_1.add(PW_Panedwindow_2);
    
    #4. Create Scale and add it to 2nd Panedwindow
    SCL_Top = TK.Scale( PW_Panedwindow_2, orient = TK.HORIZONTAL);
    PW_Panedwindow_2.add(SCL_Top);

    #4. Create Button and add it to 2nd Panedwindow
    BTN_Bottom = TK.Button(PW_Panedwindow_2, text = "OK");
    PW_Panedwindow_2.add(BTN_Bottom);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#-----Invocations-----
#Panedwindow_0l();
Panedwindow_02();









