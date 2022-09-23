# Title: Python GUI Programming With TKinter - Widgets - COMBOBOXES
# Author: C. S. Germany 02/05/2022

# For Comboboxes, you must use "from tkinter import ttk".

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comboboxes
def Comboboxes_1_Calendar():
    import tkinter as TK;
    from tkinter import ttk; #Necessary for comboboxes
    from tkinter import messagebox; #separate import necessary for messageboxes
    from calendar import month_name;
    window = TK.Tk();
    window.title("Combobox Example 1 - Using Calendar");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Month_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Month_Changed_Handler(event):
        TK.messagebox.showinfo(title='Result', message=f'You selected {Month_Selection.get()}!');    

    label = TK.Label(text="Please select a month:");
    label.pack(fill=TK.X, padx=5, pady=5);

    ComBox_Month = ttk.Combobox(window, textvariable=Month_Selection);

    #Get 1st 10 letters of every month
    ComBox_Month['values'] = [month_name[m][0:10] for m in range(1, 13)];

    #Prevent typing values
    ComBox_Month['state'] = 'readonly';
    ComBox_Month.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    ComBox_Month.bind('<<ComboboxSelected>>', Month_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comboboxes = Using the Set method
def Comboboxes_2_Calendar():
    import tkinter as TK;
    from tkinter import ttk; #Necessary for comboboxes
    from tkinter import messagebox; #separate import necessary for messageboxes
    from calendar import month_name;
    from datetime import datetime; #to get current date
    window = TK.Tk();
    window.title("Combobox Example 1 - Using Calendar");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Month_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Month_Changed_Handler(event):
        TK.messagebox.showinfo(title='Result', message=f'You selected {Month_Selection.get()}!');    

    label = TK.Label(text="Please select a month:");
    label.pack(fill=TK.X, padx=5, pady=5);

    ComBox_Month = ttk.Combobox(window, textvariable=Month_Selection);

    #Get 1st 10 letters of every month
    ComBox_Month['values'] = [month_name[m][0:10] for m in range(1, 13)];

    #Prevent typing values
    ComBox_Month['state'] = 'readonly';
    ComBox_Month.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    ComBox_Month.bind('<<ComboboxSelected>>', Month_Changed_Handler);

    Current_Month = datetime.now().strftime('%c');
    ComBox_Month.set(Current_Month);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comboboxes - Adding Choices
def Comboboxes_3_Adding_Choices():
    import tkinter as TK;
    from tkinter import ttk; #Necessary for comboboxes
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Combobox Example 3 - Adding CmbBox Choices");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Character_Changed_Handler(event):
        The_MESSAGE = "You selected: " + Character_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);    

    Lab_Fav_Char = TK.Label(text="Who is your favorite MLP character?");
    Lab_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    ComBox_Fav_Char = ttk.Combobox(window, textvariable=Character_Selection);
    ComBox_Fav_Char['values'] = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia']; #Set cmbbox choices as string array
    ComBox_Fav_Char['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    ComBox_Fav_Char.bind('<<ComboboxSelected>>', Character_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  




#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comboboxes - Auto-numbering options by appending to an array
def Comboboxes_4_AutoNumbering():
    import tkinter as TK;
    from tkinter import ttk; #Necessary for comboboxes
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Combobox Example 4 - Auto-numbering cmbbox options");
    window.geometry("375x250");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar();

    #Event Handler for Combobox
    def Character_Changed_Handler(event):
        The_MESSAGE = "You selected: " + Character_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);    

    Lab_Fav_Char = TK.Label(text="Who is your favorite MLP character?");
    Lab_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    #Auto-number array elements before passing it to combobox
    Fav_Char_Counter = 0;
    Array_Fav_Char_Choices = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];

    for x in range(len(Array_Fav_Char_Choices)):
        Fav_Char_Counter = Fav_Char_Counter + 1;
        Array_Fav_Char_Choices[x] = str(Fav_Char_Counter) + ". " + Array_Fav_Char_Choices[x];

    ComBox_Fav_Char = ttk.Combobox(window, textvariable=Character_Selection);
    ComBox_Fav_Char['values'] = Array_Fav_Char_Choices;
    ComBox_Fav_Char['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Char.pack(fill=TK.X, padx=5, pady=5);

    #bind() catches combobox change event and sends it to event handler function
    ComBox_Fav_Char.bind('<<ComboboxSelected>>', Character_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comboboxes - In Frames
def Comboboxes_5_Frames():
    import tkinter as TK;
    from tkinter import ttk; #Necessary for comboboxes
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Combobox Example 5 - Using Frames");
    window.geometry("550x240");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar();
    Antagonist_Selection = TK.StringVar();

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        The_MESSAGE = "Your favorite main CHARACTER is: " + Character_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);    

    def Antagonist_Changed_Handler(event):
        The_MESSAGE = "Your favorite ANTAGONIST is: " + Antagonist_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);         

    FRM_Fav_Chars = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=200  
                            );

    FRM_Fav_Antag = TK.Frame( master=window,
                              background = "gray",
                              relief=TK.SUNKEN,
                              borderwidth=5,
                              width=250,
                              height=200  
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

    ComBox_Fav_Char = ttk.Combobox(master=FRM_Fav_Chars, textvariable=Character_Selection);
    ComBox_Fav_Char['values'] = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];
    ComBox_Fav_Char['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Char.place(x=45, y=40, height=20, width=150);

    ComBox_Fav_Antag = ttk.Combobox(master=FRM_Fav_Antag, textvariable=Antagonist_Selection);
    ComBox_Fav_Antag['values'] = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];
    ComBox_Fav_Antag['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Antag.place(x=45, y=40, height=20, width=150);

    #bind() catches combobox change event and sends it to event handler function
    ComBox_Fav_Char.bind('<<ComboboxSelected>>', Character_Changed_Handler);
    ComBox_Fav_Antag.bind('<<ComboboxSelected>>', Antagonist_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  




#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comboboxes - In LabelFrames
def Comboboxes_6_LabelFrames():
    import tkinter as TK;
    from tkinter import ttk; #Necessary for comboboxes
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Combobox Example 6 - Using LabelFrames");
    window.geometry("550x240");
    window.configure(bg='white');
     
    #Variable for combobox state
    Character_Selection = TK.StringVar();
    Antagonist_Selection = TK.StringVar();

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        The_MESSAGE = "Your favorite main CHARACTER is: " + Character_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);    

    def Antagonist_Changed_Handler(event):
        The_MESSAGE = "Your favorite ANTAGONIST is: " + Antagonist_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);         

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

    ComBox_Fav_Char = ttk.Combobox(master=FRM_Fav_Chars, textvariable=Character_Selection);
    ComBox_Fav_Char['values'] = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];
    ComBox_Fav_Char['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Char.place(x=45, y=40, height=20, width=150);

    ComBox_Fav_Antag = ttk.Combobox(master=FRM_Fav_Antag, textvariable=Antagonist_Selection);
    ComBox_Fav_Antag['values'] = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];
    ComBox_Fav_Antag['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Antag.place(x=45, y=40, height=20, width=150);

    #bind() catches combobox change event and sends it to event handler function
    ComBox_Fav_Char.bind('<<ComboboxSelected>>', Character_Changed_Handler);
    ComBox_Fav_Antag.bind('<<ComboboxSelected>>', Antagonist_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comboboxes - Pre-selecting Options
def Comboboxes_7_Selected():
    import tkinter as TK;
    from tkinter import ttk; #Necessary for comboboxes
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Combobox Example 6 - Pre-selecting Options");
    window.geometry("550x240");
    window.configure(bg='white');
     
    #Variables for combobox state (pre-selected)
    Character_Selection = TK.StringVar();
    Character_Selection.set("Twilight Sparkle");
    Antagonist_Selection = TK.StringVar();
    Antagonist_Selection.set("Lord Tirek");

    #Event Handlers for Fav Comboboxes
    def Character_Changed_Handler(event):
        The_MESSAGE = "Your favorite main CHARACTER is: " + Character_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);    

    def Antagonist_Changed_Handler(event):
        The_MESSAGE = "Your favorite ANTAGONIST is: " + Antagonist_Selection.get() + ".";
        TK.messagebox.showinfo(title='Result', message=The_MESSAGE);         

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

    ComBox_Fav_Char = ttk.Combobox(master=FRM_Fav_Chars, textvariable=Character_Selection);
    ComBox_Fav_Char['values'] = ['Twilight Sparkle','Fluttershy','Rainbow Dash','Rarity','Apple Jack','Pinkie Pie','Princess Celestia'];
    ComBox_Fav_Char['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Char.place(x=45, y=40, height=20, width=150);

    ComBox_Fav_Antag = ttk.Combobox(master=FRM_Fav_Antag, textvariable=Antagonist_Selection);
    ComBox_Fav_Antag['values'] = ['Discord','Nightmare Moon','Lord Tirek','King Sombra','Queen Chrysalis','Storm King','Starlight Glimmer'];
    ComBox_Fav_Antag['state'] = 'readonly'; #Prevent typing values
    ComBox_Fav_Antag.place(x=45, y=40, height=20, width=150);

    #bind() catches combobox change event and sends it to event handler function
    ComBox_Fav_Char.bind('<<ComboboxSelected>>', Character_Changed_Handler);
    ComBox_Fav_Antag.bind('<<ComboboxSelected>>', Antagonist_Changed_Handler);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#-----Invocations-----
#Comboboxes_1_Calendar();
#Comboboxes_2_Calendar();
#Comboboxes_3_Adding_Choices();
#Comboboxes_4_AutoNumbering();
#Comboboxes_5_Frames();
#Comboboxes_6_LabelFrames();
Comboboxes_7_Selected();

