# Title: Python GUI Programming With TKinter - Widgets - LISTBOXES
# Author: C. S. Germany 02/05/2022

# For Listboxes, you must use "from tkinter import ttk".

#0. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Get selected item from Listbox and adding items to selection
def Listboxes_0_Basic():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Listbox Example 0 - Getting Selected Item");
    window.geometry("300x250");
    window.configure(bg='white');

    def showSelected():
        LBL_Selected.config(text=Lbox_Colors.get(TK.ANCHOR));

    Lbox_Colors = TK.Listbox(window);
    Lbox_Colors.insert(0, 'red');
    Lbox_Colors.insert(1, 'green');
    Lbox_Colors.insert(2, 'blue');
    Lbox_Colors.insert(3, 'pink');
    Lbox_Colors.pack();

    BTN_Show_Selected = TK.Button(window, text='Show Selected', command=showSelected).pack(pady=10);
    LBL_Selected = TK.Label(window);
    LBL_Selected.pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - Using Calendar
def Listboxes_1_Calendar():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    from calendar import month_name;
    window = TK.Tk();
    window.title("Listbox Example 1 - Using Calendar");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Month_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Month_Changed_Handler(event):
        Selected_Items = ListBox_Month.curselection();
        The_Selection = ",".join([ListBox_Month.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);    

    label = TK.Label(text="Please select a month:");
    label.pack(fill=TK.X, padx=5, pady=5);

    ListBox_Month = TK.Listbox(window, listvariable=Month_Selection);

    #Get 1st 10 letters of every month
    #ListBox_Month['listvariable'] = [month_name[m][0:10] for m in range(1, 13)];
    MONTHS = [month_name[m][0:10] for m in range(1, 13)];
    MONTHS_var = TK.StringVar(value=MONTHS);
    ListBox_Month['listvariable'] = MONTHS_var;

    #Another example to populate Listbox with simple strings
    #PONIES = ("Twilight Sparkle","Rainbow Dash","Fluttershy");
    #PONIES_var = TK.StringVar(value=PONIES);
    #ListBox_Month['listvariable'] = PONIES_var;

    ListBox_Month.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    ListBox_Month.bind('<<ListboxSelect>>', Month_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Listboxes - Using Calendar - Selecting a default item
def Listboxes_2_Calendar():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    from calendar import month_name;
    from datetime import date; #to get current date    
    window = TK.Tk();
    window.title("Listbox Example 2 - Using Calendar");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Month_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Month_Changed_Handler(event):
        Selected_Items = ListBox_Month.curselection();
        The_Selection = ",".join([ListBox_Month.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);    

    label = TK.Label(text="Please select a month:");
    label.pack(fill=TK.X, padx=5, pady=5);

    ListBox_Month = TK.Listbox(window, listvariable=Month_Selection);

    #Get 1st 10 letters of every month
    #ListBox_Month['listvariable'] = [month_name[m][0:10] for m in range(1, 13)];
    MONTHS = [month_name[m][0:10] for m in range(1, 13)];
    MONTHS_var = TK.StringVar(value=MONTHS);
    ListBox_Month['listvariable'] = MONTHS_var;

    ListBox_Month.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    ListBox_Month.bind('<<ListboxSelect>>', Month_Changed_Handler);

    Current_Month = date.today();
    ListBox_Month.select_set((Current_Month.month-1));
    #ListBox_Month.select_set(0);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - Adding Choices
def Listboxes_3_Adding_Choices_Using_Arrays():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 3 - Adding Listbox Choices Using Arrays");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Character_Changed_Handler(event):
        Selected_Items = LBox_Fav_Char.curselection();
        The_Selection = ",".join([LBox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message); 

    Lab_Fav_Char = TK.Label(text="Who is your favorite MLP character?");
    Lab_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    LBox_Fav_Char = TK.Listbox(window, listvariable=Character_Selection);
    Array_Fav_Chars = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia']; #Set cmbbox choices as string array
    
    Array_Fav_Chars_Counter = 0;
    for x in Array_Fav_Chars:
        LBox_Fav_Char.insert(Array_Fav_Chars_Counter,x);
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1; 

    LBox_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    LBox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - Adding Choices Alternate Way
def Listboxes_4_Adding_Choices_Alternate_Way():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 4 - Adding Listbox Choices Alternate Way");
    window.geometry("375x250");
    window.configure(bg='white');

    #Event Handler for Combobox
    def Character_Changed_Handler(event):
        Selected_Items = LBox_Fav_Char.curselection();
        The_Selection = ",".join([LBox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message); 

    Lab_Fav_Char = TK.Label(text="Who is your favorite MLP character?");
    Lab_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    Fav_Chars = TK.StringVar();
    Fav_Chars.set(['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia']);
    LBox_Fav_Char = TK.Listbox(window, listvariable=Fav_Chars);

    LBox_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    LBox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - Autonumbering - Adding Choices
def Listboxes_5_AutoNumbering():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 5 - Auto-Numbering");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Character_Changed_Handler(event):
        Selected_Items = LBox_Fav_Char.curselection();
        The_Selection = ",".join([LBox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message); 

    Lab_Fav_Char = TK.Label(text="Who is your favorite MLP character?");
    Lab_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    LBox_Fav_Char = TK.Listbox(window, listvariable=Character_Selection);
    Array_Fav_Chars = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia']; #Set cmbbox choices as string array
    
    Array_Fav_Chars_Counter = 0;
    for x in range(len(Array_Fav_Chars)):
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1;
        Array_Fav_Chars[x] = str(Array_Fav_Chars_Counter) + ". " + Array_Fav_Chars[x];

    Array_Fav_Chars_Counter = 0;
    for y in Array_Fav_Chars:
        LBox_Fav_Char.insert(Array_Fav_Chars_Counter,y);
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1; 

    LBox_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    LBox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - In Frames
def Listboxes_6_Multiple_Listboxes_In_Frames():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 6 - Listboxes in Frames");
    window.geometry("570x240");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar(); 
    Antagonist_Selection = TK.StringVar();

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Char.curselection();
        The_Selection = ",".join([Lbox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);

    def Antagonist_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Antag.curselection();
        The_Selection = ",".join([Lbox_Fav_Antag.get(h) for h in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);      

    FRM_Fav_Chars = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=210  
                            );

    FRM_Fav_Antag = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=210  
                            );

    FRM_Fav_Chars.place(x=15, y=10, height=205, width=255); 
    FRM_Fav_Antag.place(x=280, y=10, height=205, width=255);

    Lab_Fav_Chars = TK.Label( master=FRM_Fav_Chars,
                              text="Favorite MLP FIM Characters:",
                              font=("Comic Sans MS", 10, "bold"),
                              justify="center",
                              foreground="white",
                              background="gray",
                              width=40,
                              height=3  
                            );

    Lab_Fav_Antag = TK.Label( master=FRM_Fav_Antag,
                              text="Favorite MLP FIM Antagonists:",
                              font=("Comic Sans MS", 10, "bold"),
                              justify="center",
                              foreground="white",
                              background="gray",
                              width=40,
                              height=3  
                            );    

    Lab_Fav_Chars.place(x=25, y=5, height=20, width=200);
    Lab_Fav_Antag.place(x=23, y=5, height=20, width=200);

    Lbox_Fav_Char = TK.Listbox(master=FRM_Fav_Chars, listvariable=Character_Selection, exportselection=False);
    Array_Fav_Chars = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];   
    
    Array_Fav_Chars_Counter = 0;
    for x in Array_Fav_Chars:
        Lbox_Fav_Char.insert(Array_Fav_Chars_Counter,x);
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1; 

    Lbox_Fav_Char.place(x=45, y=40, height=130, width=150);

    #Note: necessary to add "exportselection=False" to constructor when more than one Listbox or events get mixed up between listboxes
    Lbox_Fav_Antag = TK.Listbox(master=FRM_Fav_Antag, listvariable=Antagonist_Selection,exportselection=False);
    Array_Fav_Antag = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];

    Array_Fav_Antag_Counter = 0;
    for y in Array_Fav_Antag:
        Lbox_Fav_Antag.insert(Array_Fav_Antag_Counter,y);
        Array_Fav_Antag_Counter = Array_Fav_Antag_Counter + 1;

    Lbox_Fav_Antag.place(x=45, y=40, height=130, width=150);

    #bind() catches listbox change event and sends it to event handler function
    Lbox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    Lbox_Fav_Antag.bind('<<ListboxSelect>>', Antagonist_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - In Frames - Multiple Selections and De-selecting
def Listboxes_7_Frames_DeSelecting():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 7 - DeSelecting");
    window.geometry("570x240");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar(); 
    Antagonist_Selection = TK.StringVar();

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Char.curselection();
        The_Selection = ",".join([Lbox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);
        Lbox_Fav_Char.selection_clear(0, 'end'); #clears selection

    def Antagonist_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Antag.curselection();
        The_Selection = ",".join([Lbox_Fav_Antag.get(h) for h in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);      
        Lbox_Fav_Antag.selection_clear(0, 'end'); #clears selection

    FRM_Fav_Chars = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=210  
                            );

    FRM_Fav_Antag = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=210  
                            );

    FRM_Fav_Chars.place(x=15, y=10, height=205, width=255); 
    FRM_Fav_Antag.place(x=280, y=10, height=205, width=255);

    Lab_Fav_Chars = TK.Label( master=FRM_Fav_Chars,
                              text="Favorite MLP FIM Characters:",
                              font=("Comic Sans MS", 10, "bold"),
                              justify="center",
                              foreground="white",
                              background="gray",
                              width=40,
                              height=3  
                            );

    Lab_Fav_Antag = TK.Label( master=FRM_Fav_Antag,
                              text="Favorite MLP FIM Antagonists:",
                              font=("Comic Sans MS", 10, "bold"),
                              justify="center",
                              foreground="white",
                              background="gray",
                              width=40,
                              height=3  
                            );    

    Lab_Fav_Chars.place(x=25, y=5, height=20, width=200);
    Lab_Fav_Antag.place(x=23, y=5, height=20, width=200);

    Lbox_Fav_Char = TK.Listbox(master=FRM_Fav_Chars, listvariable=Character_Selection, exportselection=False);
    Array_Fav_Chars = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];   
    
    Array_Fav_Chars_Counter = 0;
    for x in Array_Fav_Chars:
        Lbox_Fav_Char.insert(Array_Fav_Chars_Counter,x);
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1; 

    Lbox_Fav_Char.place(x=45, y=40, height=130, width=150);

    #Note: necessary to add "exportselection=False" to constructor when more than one Listbox or events get mixed up between listboxes
    Lbox_Fav_Antag = TK.Listbox(master=FRM_Fav_Antag, listvariable=Antagonist_Selection,exportselection=False);
    Array_Fav_Antag = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];

    Array_Fav_Antag_Counter = 0;
    for y in Array_Fav_Antag:
        Lbox_Fav_Antag.insert(Array_Fav_Antag_Counter,y);
        Array_Fav_Antag_Counter = Array_Fav_Antag_Counter + 1;

    Lbox_Fav_Antag.place(x=45, y=40, height=130, width=150);

    #bind() catches listbox change event and sends it to event handler function
    Lbox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    Lbox_Fav_Antag.bind('<<ListboxSelect>>', Antagonist_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - Multiple Selections
def Listboxes_8_Frames_Multiple_Selections():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 8 - Multiple_Selections");
    window.geometry("570x240");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar(); 
    Antagonist_Selection = TK.StringVar();

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Char.curselection();
        The_Selection = ",".join([Lbox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);

    def Antagonist_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Antag.curselection();
        The_Selection = ",".join([Lbox_Fav_Antag.get(h) for h in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);      

    FRM_Fav_Chars = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=210  
                            );

    FRM_Fav_Antag = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=210  
                            );

    FRM_Fav_Chars.place(x=15, y=10, height=205, width=255); 
    FRM_Fav_Antag.place(x=280, y=10, height=205, width=255);

    Lab_Fav_Chars = TK.Label( master=FRM_Fav_Chars,
                              text="Favorite MLP FIM Characters:",
                              font=("Comic Sans MS", 10, "bold"),
                              justify="center",
                              foreground="white",
                              background="gray",
                              width=40,
                              height=3  
                            );

    Lab_Fav_Antag = TK.Label( master=FRM_Fav_Antag,
                              text="Favorite MLP FIM Antagonists:",
                              font=("Comic Sans MS", 10, "bold"),
                              justify="center",
                              foreground="white",
                              background="gray",
                              width=40,
                              height=3  
                            );    

    Lab_Fav_Chars.place(x=25, y=5, height=20, width=200);
    Lab_Fav_Antag.place(x=23, y=5, height=20, width=200);

    #Note: Adding "exportselection=False" keeps tkinter from confusing events triggered when using multiple listboxes
    #Note: Adding "selectmode='multiple'" allows multiple selectin of listbox items

    Lbox_Fav_Char = TK.Listbox(master=FRM_Fav_Chars, listvariable=Character_Selection, exportselection=False, selectmode='multiple');
    Array_Fav_Chars = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];   
    
    Array_Fav_Chars_Counter = 0;
    for x in Array_Fav_Chars:
        Lbox_Fav_Char.insert(Array_Fav_Chars_Counter,x);
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1; 

    Lbox_Fav_Char.place(x=45, y=40, height=130, width=150);

    #Note: necessary to add "exportselection=False" to constructor when more than one Listbox or events get mixed up between listboxes
    Lbox_Fav_Antag = TK.Listbox(master=FRM_Fav_Antag, listvariable=Antagonist_Selection,exportselection=False, selectmode='multiple');
    Array_Fav_Antag = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];

    Array_Fav_Antag_Counter = 0;
    for y in Array_Fav_Antag:
        Lbox_Fav_Antag.insert(Array_Fav_Antag_Counter,y);
        Array_Fav_Antag_Counter = Array_Fav_Antag_Counter + 1;

    Lbox_Fav_Antag.place(x=45, y=40, height=130, width=150);

    #bind() catches listbox change event and sends it to event handler function
    Lbox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    Lbox_Fav_Antag.bind('<<ListboxSelect>>', Antagonist_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#9. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - In LabelFrames
def Listboxes_9_Multiple_Listboxes_In_LabelFrames():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 9 - Listboxes in LabelFrames");
    window.geometry("570x240");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar(); 
    Antagonist_Selection = TK.StringVar();

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Char.curselection();
        The_Selection = ",".join([Lbox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);

    def Antagonist_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Antag.curselection();
        The_Selection = ",".join([Lbox_Fav_Antag.get(h) for h in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);      

    FRM_Fav_Chars = TK.LabelFrame( master=window,
                                   text = "Favorite MLP FIM Characters",
                                   background = "gray",
                                   relief=TK.SUNKEN,
                                   borderwidth=5,
                                   width=250,
                                   height=200  
                                 );

    FRM_Fav_Antag = TK.LabelFrame( master=window,
                                   text = "Favorite MLP FIM Antagonists",
                                   background = "gray",
                                   relief=TK.SUNKEN,
                                   borderwidth=5,
                                   width=250,
                                   height=200  
                                 );

    FRM_Fav_Chars.place(x=15, y=10, height=205, width=255); 
    FRM_Fav_Antag.place(x=280, y=10, height=205, width=255);

    Lbox_Fav_Char = TK.Listbox(master=FRM_Fav_Chars, listvariable=Character_Selection, exportselection=False);
    Array_Fav_Chars = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];   
    
    Array_Fav_Chars_Counter = 0;
    for x in Array_Fav_Chars:
        Lbox_Fav_Char.insert(Array_Fav_Chars_Counter,x);
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1; 

    Lbox_Fav_Char.place(x=45, y=40, height=130, width=150);

    #Note: necessary to add "exportselection=False" to constructor when more than one Listbox or events get mixed up between listboxes
    Lbox_Fav_Antag = TK.Listbox(master=FRM_Fav_Antag, listvariable=Antagonist_Selection,exportselection=False);
    Array_Fav_Antag = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];

    Array_Fav_Antag_Counter = 0;
    for y in Array_Fav_Antag:
        Lbox_Fav_Antag.insert(Array_Fav_Antag_Counter,y);
        Array_Fav_Antag_Counter = Array_Fav_Antag_Counter + 1;

    Lbox_Fav_Antag.place(x=45, y=40, height=130, width=150);

    #bind() catches listbox change event and sends it to event handler function
    Lbox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    Lbox_Fav_Antag.bind('<<ListboxSelect>>', Antagonist_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  





#10. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listboxes - Pre-selecting Options
def Listboxes_10_Pre_Selecting_Item():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Listbox Example 10 - Pre-selecting Item");
    window.geometry("570x240");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar(); 
    Antagonist_Selection = TK.StringVar();

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Char.curselection();
        The_Selection = ",".join([Lbox_Fav_Char.get(i) for i in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);

    def Antagonist_Changed_Handler(event):
        Selected_Items = Lbox_Fav_Antag.curselection();
        The_Selection = ",".join([Lbox_Fav_Antag.get(h) for h in Selected_Items]);
        The_Message = "You selected: " + The_Selection;
        TK.messagebox.showinfo(title='Listbox Selected Items', message=The_Message);      

    FRM_Fav_Chars = TK.LabelFrame( master=window,
                                   text = "Favorite MLP FIM Characters",
                                   background = "gray",
                                   relief=TK.SUNKEN,
                                   borderwidth=5,
                                   width=250,
                                   height=200  
                                 );

    FRM_Fav_Antag = TK.LabelFrame( master=window,
                                   text = "Favorite MLP FIM Antagonists",
                                   background = "gray",
                                   relief=TK.SUNKEN,
                                   borderwidth=5,
                                   width=250,
                                   height=200  
                                 );

    FRM_Fav_Chars.place(x=15, y=10, height=205, width=255); 
    FRM_Fav_Antag.place(x=280, y=10, height=205, width=255);

    Lbox_Fav_Char = TK.Listbox(master=FRM_Fav_Chars, listvariable=Character_Selection, exportselection=False);
    Array_Fav_Chars = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];   
    
    Array_Fav_Chars_Counter = 0;
    for x in Array_Fav_Chars:
        Lbox_Fav_Char.insert(Array_Fav_Chars_Counter,x);
        Array_Fav_Chars_Counter = Array_Fav_Chars_Counter + 1; 

    Lbox_Fav_Char.place(x=45, y=40, height=130, width=150);

    #Note: necessary to add "exportselection=False" to constructor when more than one Listbox or events get mixed up between listboxes
    Lbox_Fav_Antag = TK.Listbox(master=FRM_Fav_Antag, listvariable=Antagonist_Selection,exportselection=False);
    Array_Fav_Antag = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];

    Array_Fav_Antag_Counter = 0;
    for y in Array_Fav_Antag:
        Lbox_Fav_Antag.insert(Array_Fav_Antag_Counter,y);
        Array_Fav_Antag_Counter = Array_Fav_Antag_Counter + 1;

    Lbox_Fav_Antag.place(x=45, y=40, height=130, width=150);

    #bind() catches listbox change event and sends it to event handler function
    Lbox_Fav_Char.bind('<<ListboxSelect>>', Character_Changed_Handler);
    Lbox_Fav_Antag.bind('<<ListboxSelect>>', Antagonist_Changed_Handler);
    
    #Example 1: Select 1st item in box 1
    Lbox_Fav_Char.select_set(0);

    #Example 2: Select item index that matches value = "Lord Tirek" in box 2
    Array_Fav_Antag_Counter = 0;
    for z in Array_Fav_Antag:
        if z == "Lord Tirek":
           Lbox_Fav_Antag.select_set(Array_Fav_Antag_Counter);
        Array_Fav_Antag_Counter = Array_Fav_Antag_Counter + 1;    

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#-----Invocations-----
#Listboxes_0_Basic();
#Listboxes_1_Calendar();
#Listboxes_2_Calendar();
#Listboxes_3_Adding_Choices_Using_Arrays();
#Listboxes_4_Adding_Choices_Alternate_Way();
#Listboxes_5_AutoNumbering();
#Listboxes_6_Multiple_Listboxes_In_Frames();
#Listboxes_7_Frames_DeSelecting();
Listboxes_8_Frames_Multiple_Selections();
#Listboxes_9_Multiple_Listboxes_In_LabelFrames();
#Listboxes_10_Pre_Selecting_Item();


