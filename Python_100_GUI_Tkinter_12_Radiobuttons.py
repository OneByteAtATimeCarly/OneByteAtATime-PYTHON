# Title: Python GUI Programming With TKinter - Widgets - RADIO BUTTONS
# Author: C. S. Germany 02/05/2022

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Radiobuttons and Checkbutton Objects - combining features for a dialog
def Radiobuttons_and_Checkbuttons_Combining_Into_Dialog_Window():
    import tkinter as TK;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("Radiobuttons everypony!");
    window.geometry("400x300");
    window.configure(bg='white');

    #String variables with default values for Entry Objects
    Player_Name = TK.StringVar(value='Anonymous');
    Player_Email = TK.StringVar();
    Player_Password = TK.StringVar();

    #State Variables for Radiobuttons and Checkboxes
    RadioButton1_Var = TK.IntVar();
    CheckBox1_Var =  TK.IntVar();    

    #Event Handler for Radiobutton1 Group
    def RadioButton1_Selection_Handler():
        Player_Gender_Choice = RadioButton1_Var.get();
        if(Player_Gender_Choice == 1):
           TITLE = 'Ms.';
        elif(Player_Gender_Choice == 2):
           TITLE = 'Mr.';
        elif(Player_Gender_Choice == 3):
           TITLE = 'Sparkle';
        return TITLE;

    #Event Handler for Submit Button
    def Button_Submit_Handler():
        try:
            P_title = RadioButton1_Selection_Handler();
            P_name = Player_Name.get();
            P_email = Player_Email.get();
            P_password = Player_Password.get();
            MESSAGE = "Title: " + P_title + "\nName: " + P_name + "\nEmail: " + P_email + "\nPassword:" + P_password;
            TK.messagebox.showinfo('MLP Successful Submission',MESSAGE);
        except Exception as ep:
               return TK.messagebox.showwarning('MLP FIM', 'Invalid input. Try again.');

    #Event Handler for Checkbox1
    def Checkbox1_Checked_Handler():
        if CheckBox1_Var.get() == 1:
           Button_Submit['state'] = TK.NORMAL;
        else:
              Button_Submit['state'] = TK.DISABLED;
              TK.messagebox.showerror('MLP FIM Offer You Can\'t Refuse', 'You MUST accept all terms and conditions first!');

    #Main label that other components are nested inside of
    Label_Main = TK.Label(window,bg='#dddddd');
    Label_Main.pack(); 

    #Fields and lables nested inside of Label_Main
    LAB_Player_Name = TK.Label(Label_Main, text='Full Name').grid(row=0, column=0, padx=5, pady=5, sticky = 'w');
    LAB_Player_Email = TK.Label(Label_Main, text='Email').grid(row=1, column=0, padx=5, pady=5, sticky = 'w');
    LAB_Player_Password = TK.Label(Label_Main, text='Password').grid(row=2, column=0, padx=5, pady=5, sticky = 'w');
    ENT_Player_Name = (TK.Entry(Label_Main,textvariable=Player_Name,width=50)).grid(row=0, column=2);
    ENT_Player_Email = (TK.Entry(Label_Main,textvariable=Player_Email,width=50)).grid(row=1, column=2);
    ENT_Player_Password = (TK.Entry(Label_Main,textvariable=Player_Password,width=50,show="*")).grid(row=2, column=2); 

    #Gender Radiobuttons and Frame
    Frm_Gender = TK.LabelFrame(Label_Main, text='Gender', padx=30, pady=10);
    TK.Radiobutton(Frm_Gender, text='Female', variable=RadioButton1_Var, value=1,command=RadioButton1_Selection_Handler).pack(anchor=TK.W);
    TK.Radiobutton(Frm_Gender, text='Male', variable=RadioButton1_Var, value=2,command=RadioButton1_Selection_Handler).pack(anchor=TK.W);
    TK.Radiobutton(Frm_Gender, text='Unicorn', variable=RadioButton1_Var, value=3,command=RadioButton1_Selection_Handler).pack(anchor=TK.W);
    Frm_Gender.grid(row=3, columnspan=3,padx=30);
    
    #Accept Checkbutton
    TK.Checkbutton(Label_Main, text='Accept terms and conditions', variable=CheckBox1_Var, onvalue=1, offvalue=0,command=Checkbox1_Checked_Handler).grid(row=4, columnspan=4, pady=5);

    #Submit Button
    Button_Submit = TK.Button(Label_Main, text="Submit", command=Button_Submit_Handler, padx=50, pady=5, state=TK.DISABLED);
    Button_Submit.grid(row=5, columnspan=4, pady=2);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  




#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Radiobutton Objects in Frames
def Radiobuttons_In_Frames():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Radiobuttons in FRAME objects.");
    window.geometry("550x310");
    window.configure(bg='white');

    #For use with checkbuttons to get state
    RadioButton_Fave_Character_Grp_State = TK.IntVar();
    RadioButton_Fave_Antagonist_Grp_State = TK.IntVar();

    #Event handler Character Radio Buttons
    def Get_Radiobutton_State_Characters():
        if(RadioButton_Fave_Character_Grp_State.get() == 1):
           Label_CHOICE ["text"] = "You selected Twilight Sparkle.";
        elif(RadioButton_Fave_Character_Grp_State.get()  == 2):
             Label_CHOICE ["text"] = "You selected Rainbow Dash.";
        elif(RadioButton_Fave_Character_Grp_State.get()  == 3):
             Label_CHOICE ["text"] = "You selected Fluttershy."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 4):
             Label_CHOICE ["text"] = "You selected Rarity."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 5):
             Label_CHOICE ["text"] = "You selected Apple Jack."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 6):
             Label_CHOICE ["text"] = "You selected Pinkie Pie."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 7):
             Label_CHOICE ["text"] = "You selected Princess Celestia.";

    #Event handler Character Radio Buttons 
    def Get_Radiobutton_State_Antagonists():                    
        if(RadioButton_Fave_Antagonist_Grp_State.get() == 1):
             Label_CHOICE ["text"] = "You selected Discord.";
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 2):
             Label_CHOICE ["text"] = "You selected Nightmare Moon.";
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 3):
             Label_CHOICE ["text"] = "You selected Lord Tirek."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 4):
             Label_CHOICE ["text"] = "You selected King Sombra."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 5):
             Label_CHOICE ["text"] = "You selected Queen Chrysalis."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 6):
             Label_CHOICE ["text"] = "You selected Storm King."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 7):
             Label_CHOICE ["text"] = "You selected Starlight Glimmer.";    

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

    RadBut_1 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "1. Twilight Sparkle", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 1, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    RadBut_2 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "2. Rainbow Dash", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 2, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    RadBut_3 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,    
                               text = "3. Fluttershy", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 3, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );  

    RadBut_4 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "4. Rarity", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 4, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    RadBut_5 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "5. Apple Jack", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 5, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    RadBut_6 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "6. Pinkie Pie", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 6, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );    

    RadBut_7 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "7. Princess Celestia", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 7, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      


    RadBut_8 = TK.Radiobutton( master=FRM_Fav_Antag,
                               command=Get_Radiobutton_State_Antagonists,
                               text = "1. Discord", 
                               variable = RadioButton_Fave_Antagonist_Grp_State,
                               value = 1, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             ); 

    RadBut_9 = TK.Radiobutton( master=FRM_Fav_Antag,
                               command=Get_Radiobutton_State_Antagonists,
                               text = "2. Nightmare Moon", 
                               variable = RadioButton_Fave_Antagonist_Grp_State,
                               value = 2, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      

    RadBut_10 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "3. Lord Tirek", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 3, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    RadBut_11 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "4. King Sombra", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 4, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    RadBut_12 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "5. Queen Chrysalis", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 5, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );    

    RadBut_13 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "6. Storm King", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 6, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    RadBut_14 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "7. Starlight Glimmer", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 7, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );                                                                                                       

    RadBut_1.place(x=40, y=40, height=20, width=200);
    RadBut_2.place(x=40, y=60, height=20, width=200);
    RadBut_3.place(x=40, y=80, height=20, width=200);
    RadBut_4.place(x=40, y=100, height=20, width=200);
    RadBut_5.place(x=40, y=120, height=20, width=200);
    RadBut_6.place(x=40, y=140, height=20, width=200);
    RadBut_7.place(x=40, y=160, height=20, width=200);
    RadBut_8.place(x=40, y=40, height=20, width=200);
    RadBut_9.place(x=40, y=60, height=20, width=200);
    RadBut_10.place(x=40, y=80, height=20, width=200);
    RadBut_11.place(x=40, y=100, height=20, width=200);
    RadBut_12.place(x=40, y=120, height=20, width=200);
    RadBut_13.place(x=40, y=140, height=20, width=200);
    RadBut_14.place(x=40, y=160, height=20, width=200);    

    Label_CHOICE = TK.Label( text="Who will you choose?",
                             font=("Comic Sans MS", 18, "bold"),
                             justify="center",
                             foreground="pink",
                             background="black",
                             width=500,
                             height=15  
                           );

    Label_CHOICE.place(x=20, y=240, height=40, width=505);                        

    window.mainloop();                             
#-------------------------------------------------------------------------------------------------------------------------------------------------------------





#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Checkbutton Objects in LabelFrames. LabelFrames have a text component that the Frame wisdget does not have.
def Radiobuttons_In_LabelFrames():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Checkbuttons in FRAME objects.");
    window.geometry("550x310");
    window.configure(bg='white');

    #For use with checkbuttons to get state
    RadioButton_Fave_Character_Grp_State = TK.IntVar();
    RadioButton_Fave_Antagonist_Grp_State = TK.IntVar();

    #Event handler Character Radio Buttons
    def Get_Radiobutton_State_Characters():
        if(RadioButton_Fave_Character_Grp_State.get() == 1):
           Label_CHOICE ["text"] = "You selected Twilight Sparkle.";
        elif(RadioButton_Fave_Character_Grp_State.get()  == 2):
             Label_CHOICE ["text"] = "You selected Rainbow Dash.";
        elif(RadioButton_Fave_Character_Grp_State.get()  == 3):
             Label_CHOICE ["text"] = "You selected Fluttershy."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 4):
             Label_CHOICE ["text"] = "You selected Rarity."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 5):
             Label_CHOICE ["text"] = "You selected Apple Jack."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 6):
             Label_CHOICE ["text"] = "You selected Pinkie Pie."; 
        elif(RadioButton_Fave_Character_Grp_State.get()  == 7):
             Label_CHOICE ["text"] = "You selected Princess Celestia.";

    #Event handler Character Radio Buttons 
    def Get_Radiobutton_State_Antagonists():                    
        if(RadioButton_Fave_Antagonist_Grp_State.get() == 1):
             Label_CHOICE ["text"] = "You selected Discord.";
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 2):
             Label_CHOICE ["text"] = "You selected Nightmare Moon.";
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 3):
             Label_CHOICE ["text"] = "You selected Lord Tirek."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 4):
             Label_CHOICE ["text"] = "You selected King Sombra."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 5):
             Label_CHOICE ["text"] = "You selected Queen Chrysalis."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 6):
             Label_CHOICE ["text"] = "You selected Storm King."; 
        elif(RadioButton_Fave_Antagonist_Grp_State.get()  == 7):
             Label_CHOICE ["text"] = "You selected Starlight Glimmer.";    

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

    RadBut_1 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "1. Twilight Sparkle", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 1, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    RadBut_2 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "2. Rainbow Dash", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 2, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    RadBut_3 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,    
                               text = "3. Fluttershy", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 3, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );  

    RadBut_4 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "4. Rarity", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 4, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    RadBut_5 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "5. Apple Jack", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 5, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    RadBut_6 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "6. Pinkie Pie", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 6, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );    

    RadBut_7 = TK.Radiobutton( master=FRM_Fav_Chars,
                               command=Get_Radiobutton_State_Characters,
                               text = "7. Princess Celestia", 
                               variable = RadioButton_Fave_Character_Grp_State,
                               value = 7, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      


    RadBut_8 = TK.Radiobutton( master=FRM_Fav_Antag,
                               command=Get_Radiobutton_State_Antagonists,
                               text = "1. Discord", 
                               variable = RadioButton_Fave_Antagonist_Grp_State,
                               value = 1, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             ); 

    RadBut_9 = TK.Radiobutton( master=FRM_Fav_Antag,
                               command=Get_Radiobutton_State_Antagonists,
                               text = "2. Nightmare Moon", 
                               variable = RadioButton_Fave_Antagonist_Grp_State,
                               value = 2, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      

    RadBut_10 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "3. Lord Tirek", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 3, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    RadBut_11 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "4. King Sombra", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 4, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    RadBut_12 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "5. Queen Chrysalis", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 5, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );    

    RadBut_13 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "6. Storm King", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 6, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    RadBut_14 = TK.Radiobutton( master=FRM_Fav_Antag,
                                command=Get_Radiobutton_State_Antagonists,
                                text = "7. Starlight Glimmer", 
                                variable = RadioButton_Fave_Antagonist_Grp_State,
                                value = 7, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );                                                                                                       

    RadBut_1.place(x=40, y=20, height=20, width=200);
    RadBut_2.place(x=40, y=40, height=20, width=200);
    RadBut_3.place(x=40, y=60, height=20, width=200);
    RadBut_4.place(x=40, y=80, height=20, width=200);
    RadBut_5.place(x=40, y=100, height=20, width=200);
    RadBut_6.place(x=40, y=120, height=20, width=200);
    RadBut_7.place(x=40, y=140, height=20, width=200);
    RadBut_8.place(x=40, y=20, height=20, width=200);
    RadBut_9.place(x=40, y=40, height=20, width=200);
    RadBut_10.place(x=40, y=60, height=20, width=200);
    RadBut_11.place(x=40, y=80, height=20, width=200);
    RadBut_12.place(x=40, y=100, height=20, width=200);
    RadBut_13.place(x=40, y=120, height=20, width=200);
    RadBut_14.place(x=40, y=140, height=20, width=200);    

    Label_CHOICE = TK.Label( text="Who will you choose?",
                             font=("Comic Sans MS", 18, "bold"),
                             justify="center",
                             foreground="pink",
                             background="black",
                             width=500,
                             height=15  
                           );

    Label_CHOICE.place(x=20, y=240, height=40, width=505);                                  

    window.mainloop();                             
#-------------------------------------------------------------------------------------------------------------------------------------------------------------




#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Checkbutton Objects - enable, disable, select 
def Checkbuttons_Selecting():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Checkbuttons - Selecting.");
    window.geometry("200x100");
    window.configure(bg='white');

    #Checbox state variable
    Checkbox_Var = TK.IntVar();
    Checkbox_Var.set(1);

    #Event Handler for Checkbox
    def Radiobutton1_Selected_Handler():
        if Checkbox_Var.get() == 1:
           BTN_Asleep_Or_Awake['state'] = TK.NORMAL;
           BTN_Asleep_Or_Awake.configure(text='Awake!');
        elif Checkbox_Var.get() == 0:
             BTN_Asleep_Or_Awake['state'] = TK.DISABLED;
             BTN_Asleep_Or_Awake.configure(text='Asleep!');
        else:
              TK.messagebox.showerror('!ERROR!', 'This is NOT supposed to happen.');

    TK.Radiobutton(window, text="accept T&C", variable=Checkbox_Var, value=1, command=Radiobutton1_Selected_Handler).pack();

    BTN_Asleep_Or_Awake = TK.Button(window, text='Sleeping!', state=TK.DISABLED, padx=20, pady=5);
    BTN_Asleep_Or_Awake.pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Checkbutton Objects - deselect, select 
def Radiobuttons_DeSelecting():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Checkbuttons - Deselecting and Selecting.");
    window.geometry("300x250");
    window.configure(bg='white');

    var = TK.IntVar();
    var.set(1);    

    #Event Handler
    def clear_selection():
        RB1.deselect();
        RB2.deselect();
        RB3.deselect();
        RB4.deselect();
        RB5.deselect();
        RB6.deselect();
 
    RB1 = TK.Radiobutton(window, text='Click me!', variable=var, value=1);
    RB1.pack();
    RB2 = TK.Radiobutton(window, text='Click me!', variable=var, value=1);
    RB2.pack();
    RB3 = TK.Radiobutton(window, text='Click me!', variable=var, value=1);
    RB3.pack();
    RB4 = TK.Radiobutton(window, text='Click me!', variable=var, value=1);
    RB4.pack();
    RB5 = TK.Radiobutton(window, text='Click me!', variable=var, value=1);
    RB5.pack();
    RB6 = TK.Radiobutton(window, text='Click me!', variable=var, value=1);
    RB6.pack();

    TK.Button(window, text='Deselect All Checkbuttons', command=clear_selection).pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------    

 


#-----Invocations-----
#Radiobuttons_and_Checkbuttons_Combining_Into_Dialog_Window();
#Radiobuttons_In_Frames();
#Radiobuttons_In_LabelFrames();
#Checkbuttons_Selecting();
Radiobuttons_DeSelecting();





