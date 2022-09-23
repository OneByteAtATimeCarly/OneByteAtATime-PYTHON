# Title: Python GUI Programming With TKinter - Widgets - SCROLLBARS
# Author: C. S. Germany 02/05/2022

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add Vertical Scrollbar to Window
def ScrollBars_Vertical_01_Add_to_Window():
    import tkinter as TK;
    window = TK.Tk();
    window.title("0. Vertical Scrollbar to window");
    window.geometry("300x250");
    window.configure(bg='white');

    #Event Handler for Show Selected Button
    def Show_Selected_Ponies_Handler():
        LBL_Selected.config(text=Lbox_Numbers.get(TK.ANCHOR));

    #Scrollbar
    SB_Vert_Lbox_Numbers = TK.Scrollbar(window, orient = TK.VERTICAL);
    SB_Vert_Lbox_Numbers.pack(side=TK.RIGHT, fill=TK.Y);

    #Listbox
    Lbox_Numbers = TK.Listbox(window, yscrollcommand = SB_Vert_Lbox_Numbers.set);
    for Listbox_Item in range(445):
        Lbox_Numbers.insert(TK.END, "Pony number " + str(Listbox_Item))
    Lbox_Numbers.pack();

    SB_Vert_Lbox_Numbers.config(command=Lbox_Numbers.yview);

    BTN_Show_Selected = TK.Button(window, text='Show Selected Ponies', command=Show_Selected_Ponies_Handler).pack(pady=10);
    LBL_Selected = TK.Label(window);
    LBL_Selected.pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add Horizontal Scrollbar to Window
def ScrollBars_Horizontal_02_Add_to_Window():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Horizontal Scrollbar to window");
    window.geometry("300x250");
    window.configure(bg='white');

    #Event Handler for Show Selected Button
    def Show_Selected_Ponies_Handler():
        LBL_Selected.config(text=Lbox_Numbers.get(TK.ANCHOR));

    #Scrollbar
    SB_Horz_Lbox_Numbers = TK.Scrollbar(window, orient = TK.HORIZONTAL);
    SB_Horz_Lbox_Numbers.pack(side=TK.BOTTOM, fill=TK.X);

    #Listbox
    Lbox_Numbers = TK.Listbox(window, xscrollcommand = SB_Horz_Lbox_Numbers.set);
    for Listbox_Item in range(445):
        Lbox_Numbers.insert(TK.END, "What is this pony number? Everypony? Who could it be? The pony number is: " + str(Listbox_Item))
    Lbox_Numbers.pack();

    SB_Horz_Lbox_Numbers.config(command=Lbox_Numbers.xview);

    BTN_Show_Selected = TK.Button(window, text='Show Selected Ponies', command=Show_Selected_Ponies_Handler).pack(pady=10);
    LBL_Selected = TK.Label(window);
    LBL_Selected.pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add Vertical AND Horizontal Scrollbar to Window
def ScrollBars_Vertical_And_Horizontal_03_Add_to_Window():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Horizontal Scrollbar to window");
    window.geometry("300x250");
    window.configure(bg='white');

    #Event Handler for Show Selected Button
    def Show_Selected_Ponies_Handler():
        LBL_Selected.config(text=Lbox_Numbers.get(TK.ANCHOR));

    #Scrollbar - Horizontal 
    SB_Horz_Lbox_Numbers = TK.Scrollbar(window, orient = TK.HORIZONTAL);
    SB_Horz_Lbox_Numbers.pack(side=TK.BOTTOM, fill=TK.X);

    #Scrollbar - Vertical 
    SB_Vert_Lbox_Numbers = TK.Scrollbar(window, orient = TK.VERTICAL);
    SB_Vert_Lbox_Numbers.pack(side=TK.LEFT, fill=TK.Y);   

    #Listbox
    Lbox_Numbers = TK.Listbox(window, xscrollcommand=SB_Horz_Lbox_Numbers.set, yscrollcommand=SB_Vert_Lbox_Numbers.set);
    for Listbox_Item in range(445):
        Lbox_Numbers.insert(TK.END, "What is this pony number? Everypony? Who could it be? The pony number is: " + str(Listbox_Item))
    Lbox_Numbers.pack(fill = TK.BOTH, expand=0);

    SB_Horz_Lbox_Numbers.config(command=Lbox_Numbers.xview);
    SB_Vert_Lbox_Numbers.config(command=Lbox_Numbers.yview);

    BTN_Show_Selected = TK.Button(window, text='Show Selected Ponies', command=Show_Selected_Ponies_Handler).pack(pady=10);
    LBL_Selected = TK.Label(window);
    LBL_Selected.pack();

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add Vertical Scrollbar to Listbox
def Vertical_ScrollBars_04_Add_to_Listbox():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Listbox Example 0 - Getting Selected Item");
    window.geometry("300x250");
    window.configure(bg='white');

    #Event Handler for Show Selected Button
    def Show_Selected_Ponies_Handler():
        LBL_Selected.config(text=Lbox_Numbers.get(TK.ANCHOR));

    #1. Add Frame for Scrollbar to window
    FRM_Lbox_Numbers = TK.Frame(window);
    FRM_Lbox_Numbers.pack();

    #2. Add Vertical Scrollbar to Frame
    SB_Vert_Lbox_Numbers = TK.Scrollbar(FRM_Lbox_Numbers, orient=TK.VERTICAL);
    SB_Vert_Lbox_Numbers.pack(side=TK.RIGHT,fill=TK.Y);

    #3. Add Listbox to Frame
    Lbox_Numbers = TK.Listbox(FRM_Lbox_Numbers, yscrollcommand=SB_Vert_Lbox_Numbers.set);
    for Listbox_Item in range(445):
        Lbox_Numbers.insert(TK.END, "Pony number " + str(Listbox_Item))
    Lbox_Numbers.pack(expand=True,fill=TK.Y);

    #Set behavior for VERTICAL scrollbar
    SB_Vert_Lbox_Numbers.config(command=Lbox_Numbers.yview);

    BTN_Show_Selected = TK.Button(window, text='Show Selected Ponies', command=Show_Selected_Ponies_Handler).pack(pady=10);
    LBL_Selected = TK.Label(window);
    LBL_Selected.pack();

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add Horizontal Scrollbar to Listbox
def Horizontal_ScrollBars_05_Add_to_Listbox():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Listbox Example 0 - Getting Selected Item");
    window.geometry("300x250");
    window.configure(bg='white');

    #Event Handler for Show Selected Button
    def Show_Selected_Ponies_Handler():
        LBL_Selected.config(text=Lbox_Numbers.get(TK.ANCHOR));

    #1. Add Frame for Scrollbar to window
    FRM_Lbox_Numbers = TK.Frame(window);
    FRM_Lbox_Numbers.pack();

    #2. Add Horizontal Scrollbar to Frame
    SB_Horz_Lbox_Numbers = TK.Scrollbar(FRM_Lbox_Numbers, orient=TK.HORIZONTAL);
    SB_Horz_Lbox_Numbers.pack(side=TK.BOTTOM,fill=TK.X);

    #3. Add Listbox to Frame
    Lbox_Numbers = TK.Listbox(FRM_Lbox_Numbers, xscrollcommand=SB_Horz_Lbox_Numbers.set);
    for Listbox_Item in range(445):
        Lbox_Numbers.insert(TK.END, "What is this pony number? Everypony? Who could it be? The pony number is: " + str(Listbox_Item))
    Lbox_Numbers.pack(expand=True,fill=TK.Y);

    #Set behavior for VERTICAL scrollbar
    SB_Horz_Lbox_Numbers.config(command=Lbox_Numbers.xview);

    BTN_Show_Selected = TK.Button(window, text='Show Selected Ponies', command=Show_Selected_Ponies_Handler).pack(pady=10);
    LBL_Selected = TK.Label(window);
    LBL_Selected.pack();

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add Vertical Scrollbar to Text Object
def Vertical_ScrollBars_06_Add_to_Text_Object():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Adding Vertical Scrollbars to Entry Objects");
    window.geometry("320x550");
    window.configure(bg='white');

    #Event Handler to Show text in Text object
    def Show_Selected_Ponies_Handler():
        LBL_Output.config(text=TXT_Input.get("1.0",TK.END));

    #1. Add Frames for Scrollbars to window
    FRM_Main_Text = TK.Frame(window,relief=TK.SUNKEN);
    FRM_Main_Text.place(x=60, y=10, height=300, width=200); 
    FRM_Output_Label = TK.Frame(window,relief=TK.RIDGE);
    FRM_Output_Label.place(x=30, y=360, height=150, width=250);     

    #2. Create and add VERTICAL Scrollbar to Frame (orient=TK.VERTICAL and pack() side=TK.RIGHT and fill=TK.Y)
    SB_Vert_TXT_Input  = TK.Scrollbar(FRM_Main_Text, orient=TK.VERTICAL);
    SB_Vert_TXT_Input .pack(side=TK.RIGHT,fill=TK.Y);   

    #3. Add Text object to Frames (for VERTICAL use yscrollcommand=)
    TXT_Input = TK.Text(FRM_Main_Text, font=("Comic Sans MS", 15, "bold"), yscrollcommand=SB_Vert_TXT_Input.set);
    for Entry_Line_Item in range(445):
        TXT_Input.insert(TK.END, "Pony number " + str(Entry_Line_Item) + "\n");
    TXT_Input.pack(expand=True,fill=TK.Y);

    LBL_Output = TK.Label(FRM_Output_Label,font=("Comic Sans MS", 15, "bold"), background="black", foreground="white");
    LBL_Output.pack(expand=True,fill=TK.BOTH);      

    #Set behavior for VERTICAL scrollbar (use .yview for VERTICAL)
    SB_Vert_TXT_Input.config(command=TXT_Input.yview);

    BTN_Show_Selected = TK.Button(window, font=("Comic Sans MS", 12, "bold"), text='Show Selected Ponies', command=Show_Selected_Ponies_Handler, background="green", foreground="white");
    BTN_Show_Selected.place(x=55, y=320, height=30, width=200);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add Horizontal Scrollbar to Text Object
def Horizontal_ScrollBars_07_Add_to_Text_Object():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Adding Vertical Scrollbars to Entry Objects");
    window.geometry("320x550");
    window.configure(bg='white');

    #Event Handler to Show text in Text object
    def Show_Selected_Ponies_Handler():
        LBL_Output.config(text=TXT_Input.get("1.0",TK.END));

    #1. Add Frames for Scrollbars to window
    FRM_Main_Text = TK.Frame(window,relief=TK.SUNKEN);
    FRM_Main_Text.place(x=60, y=10, height=300, width=200); 
    FRM_Output_Label = TK.Frame(window,relief=TK.RIDGE);
    FRM_Output_Label.place(x=30, y=360, height=150, width=250);     

    #2. Create and add HORIZONTAL Scrollbar to Frame (orient=TK.HORIZONTAL and pack() side=TK.BOTTOM and fill=TK.X)
    SB_Horz_TXT_Input  = TK.Scrollbar(FRM_Main_Text, orient=TK.HORIZONTAL);
    SB_Horz_TXT_Input.pack(side=TK.BOTTOM,fill=TK.X);   

    #3. Add Entry to Frames (set wrap=TK.NONE for HORIZONTAL scrolls and use xscrollcommand=)
    TXT_Input = TK.Text(FRM_Main_Text, font=("Comic Sans MS", 15, "bold"), xscrollcommand=SB_Horz_TXT_Input.set, wrap=TK.NONE);
    for Entry_Line_Item in range(445):
        TXT_Input.insert(TK.END, "This pony is everypony. And this text will go on and on. And this Pony number is " + str(Entry_Line_Item) + "\n");
    TXT_Input.pack(expand=True,fill=TK.X);

    LBL_Output = TK.Label(FRM_Output_Label,font=("Comic Sans MS", 15, "bold"), background="black", foreground="white");
    LBL_Output.pack(expand=True,fill=TK.BOTH);      

    #Set behavior for HORIZONTAL scrollbar (use .xview for HORIZONTAL)
    SB_Horz_TXT_Input.config(command=TXT_Input.xview);

    BTN_Show_Selected = TK.Button(window, font=("Comic Sans MS", 12, "bold"), text='Show Selected Ponies', command=Show_Selected_Ponies_Handler, background="green", foreground="white");
    BTN_Show_Selected.place(x=55, y=320, height=30, width=200);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Vertical Scrollbars - Get Only Selected Text
def Vertical_ScrollBars_08_Get_Only_Selected_Text():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Vertical Scrollbars - Get Only Selected Text");
    window.geometry("320x550");
    window.configure(bg='white');

    #Event Handler to Show text in Text object
    def Show_Selected_Ponies_Handler():
        LBL_Output.config(text=TXT_Input.selection_get());

    #1. Add Frames for Scrollbars to window
    FRM_Main_Text = TK.Frame(window,relief=TK.SUNKEN);
    FRM_Main_Text.place(x=60, y=10, height=300, width=200); 
    FRM_Output_Label = TK.Frame(window,relief=TK.RIDGE);
    FRM_Output_Label.place(x=30, y=360, height=150, width=250);     

    #2. Create and add VERTICAL Scrollbar to Frame (orient=TK.VERTICAL and pack() side=TK.RIGHT and fill=TK.Y)
    SB_Vert_TXT_Input  = TK.Scrollbar(FRM_Main_Text, orient=TK.VERTICAL);
    SB_Vert_TXT_Input .pack(side=TK.RIGHT,fill=TK.Y);   

    #3. Add Text object to Frames (for VERTICAL use yscrollcommand=)
    TXT_Input = TK.Text(FRM_Main_Text, font=("Comic Sans MS", 15, "bold"), yscrollcommand=SB_Vert_TXT_Input.set);
    for Entry_Line_Item in range(445):
        TXT_Input.insert(TK.END, "Pony number " + str(Entry_Line_Item) + "\n");
    TXT_Input.pack(expand=True,fill=TK.Y);

    LBL_Output = TK.Label(FRM_Output_Label,font=("Comic Sans MS", 15, "bold"), background="black", foreground="white");
    LBL_Output.pack(expand=True,fill=TK.BOTH);      

    #Set behavior for VERTICAL scrollbar (use .yview for VERTICAL)
    SB_Vert_TXT_Input.config(command=TXT_Input.yview);

    BTN_Show_Selected = TK.Button(window, font=("Comic Sans MS", 12, "bold"), text='Show Selected Ponies', command=Show_Selected_Ponies_Handler, background="green", foreground="white");
    BTN_Show_Selected.place(x=55, y=320, height=30, width=200);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add HORIZONTAL Scrollbar to ENTRY Object (HORIZONTAL only, no VERTICAL since ENTRY object is for one line of text)
# If you want to VERTICAL scroll, use a TEXT object instead of an ENTRY object
def HORIZONTAL_ScrollBars_09_Adding_to_ENTRY():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Vertical Scrollbars - Get Only Selected Text");
    window.geometry("320x550");
    window.configure(bg='white');

    #Event Handler to Show text in Text object
    def Show_Selected_Ponies_Handler():
        The_Message = TXT_Input.get("1.0",TK.END);
        ENT_Output.insert(0,The_Message);

    #1. Add Frames for Scrollbars to window. To add scroobar to a LABEL, FIRST create a Canvas and add Frame to that.
    FRM_Main_Text = TK.Frame(window,relief=TK.SUNKEN);
    FRM_Main_Text.place(x=60, y=10, height=300, width=200);

    #2. Create and add VERTICAL Scrollbar to Frame (orient=TK.VERTICAL and pack() side=TK.RIGHT and fill=TK.Y)
    SB_Vert_TXT_Input  = TK.Scrollbar(FRM_Main_Text, orient=TK.VERTICAL);
    SB_Vert_TXT_Input .pack(side=TK.RIGHT,fill=TK.Y);

    #For Output Entry Object, add HORIZONTAL scrollbar
    FRM_Output_Entry = TK.Frame(window);
    FRM_Output_Entry.place(x=30, y=360, height=150, width=250);   

    ENT_Output = TK.Entry(FRM_Output_Entry,font=("Comic Sans MS", 15, "bold"), background="black", foreground="white");
    ENT_Output.pack(expand=True,fill=TK.BOTH);

    SB_Vert_Output_Entry  = TK.Scrollbar(FRM_Output_Entry, orient='horizontal', command=ENT_Output.xview);
    SB_Vert_Output_Entry.pack(side=TK.BOTTOM,fill=TK.X); 
    ENT_Output.config(xscrollcommand=SB_Vert_Output_Entry.set);
          
    #3. Add Text object to Frames (for VERTICAL use yscrollcommand=)
    TXT_Input = TK.Text(FRM_Main_Text, font=("Comic Sans MS", 15, "bold"), yscrollcommand=SB_Vert_TXT_Input.set);
    for Entry_Line_Item in range(445):
        TXT_Input.insert(TK.END, "Pony number " + str(Entry_Line_Item) + "\n");
    TXT_Input.pack(expand=True,fill=TK.Y);      

    #Set behavior for VERTICAL scrollbar (use .yview for VERTICAL)
    SB_Vert_TXT_Input.config(command=TXT_Input.yview);

    BTN_Show_Selected = TK.Button(window, font=("Comic Sans MS", 12, "bold"), text='Show Selected Ponies', command=Show_Selected_Ponies_Handler, background="green", foreground="white");
    BTN_Show_Selected.place(x=55, y=320, height=30, width=200);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#10. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add HORIZONTAL Scrollbar to LABEL Object Using a Canvas
def HORIZONTAL_ScrollBars_10_Adding_to_LABEL_Using_A_Canvas():
    import tkinter as TK;
    from tkinter import ttk; #In this instance, you MUST create scrollbar from ttk instead of TK instance
    window = TK.Tk();
    window.title("Vertical Scrollbars - Get Only Selected Text");
    #window.geometry("400x400");
    #window.configure(bg='white');

    #Frame
    FRM_Output_Label_Outer = TK.Frame(window); 
    CANV_Output_Label = TK.Canvas(FRM_Output_Label_Outer, height=150, width=250);
    FRM_Output_Label_Inner = TK.Frame(CANV_Output_Label);
  
    #In this instance, you MUST create scrollbar from ttk instead of TK instance
    SB_Output_Label = ttk.Scrollbar(FRM_Output_Label_Outer, orient='horizontal', command=CANV_Output_Label.xview);

    CANV_Output_Label.configure(xscrollcommand=SB_Output_Label.set);

    FRM_Output_Label_Outer.grid();
    CANV_Output_Label.grid(row=1, sticky='nesw');
    SB_Output_Label.grid(row=2, sticky='ew');
    CANV_Output_Label.create_window(0, 0, window=FRM_Output_Label_Inner, anchor='nw');

    LAB_Output = TK.Label(FRM_Output_Label_Inner, font=("Comic Sans MS", 20, "bold"), background="black", foreground="white");
    LAB_Output.grid(sticky='w');

    LAB_Output['text'] = 'test ' * 100;          

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#11. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Add VERTICAL Scrollbar to LABEL Object Using a Canvas
def VERTICAL_ScrollBars_11_Adding_to_LABEL_Using_A_Canvas():
    import tkinter as TK;
    from tkinter import ttk; #In this instance, you MUST create scrollbar from ttk instead of TK instance
    window = TK.Tk();
    window.title("Vertical Scrollbars - Get Only Selected Text");
    #window.geometry("400x400");
    #window.configure(bg='white');

    #Frame
    FRM_Output_Label_Outer = TK.Frame(window); 
    CANV_Output_Label = TK.Canvas(FRM_Output_Label_Outer, height=150, width=250);
    FRM_Output_Label_Inner = TK.Frame(CANV_Output_Label);
  
    #In this instance, you MUST create scrollbar from ttk instead of TK instance
    SB_Output_Label = ttk.Scrollbar(FRM_Output_Label_Outer, orient='vertical', command=CANV_Output_Label.yview);

    CANV_Output_Label.configure(yscrollcommand=SB_Output_Label.set);

    FRM_Output_Label_Outer.grid();
    CANV_Output_Label.grid(row=1, sticky='nesw');
    SB_Output_Label.grid(row=1, sticky='e');
    CANV_Output_Label.create_window(0, 0, window=FRM_Output_Label_Inner, anchor='w');

    LAB_Output = TK.Label(FRM_Output_Label_Inner, font=("Comic Sans MS", 20, "bold"), background="black", foreground="white");
    LAB_Output.grid(sticky='w');

    LAB_Output['text'] = 'test test test \n' * 100;          

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#ScrollBars_Vertical_01_Add_to_Window();
#ScrollBars_Horizontal_02_Add_to_Window();
#ScrollBars_Vertical_And_Horizontal_03_Add_to_Window();
#Vertical_ScrollBars_04_Add_to_Listbox();
#Horizontal_ScrollBars_05_Add_to_Listbox();
#Vertical_ScrollBars_06_Add_to_Text_Object();
#Horizontal_ScrollBars_07_Add_to_Text_Object();
#Vertical_ScrollBars_08_Get_Only_Selected_Text();
#HORIZONTAL_ScrollBars_09_Adding_to_ENTRY();
#HORIZONTAL_ScrollBars_10_Adding_to_LABEL_Using_A_Canvas();
VERTICAL_ScrollBars_11_Adding_to_LABEL_Using_A_Canvas();



