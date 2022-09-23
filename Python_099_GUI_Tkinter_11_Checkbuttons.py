# Title: Python GUI Programming With TKinter - Widgets - CHECKBUTTONS (checkboxes)
# Author: C. S. Germany 02/05/2022


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Checkbutton Objects
def CheckButton_1():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x420");
    window.configure(bg='white');

    #Variables used to get/set state of check buttons
    CheckButtonState1 = TK.IntVar(); #int value
    CheckButtonState2 = TK.IntVar(); #int value

    #Event handlers
    def Get_Checkbutton_State():
        if(CheckButtonState1.get() == 0 and CheckButtonState2.get()  == 0 ):
           Label_CkBtnState["text"] = "Neither Discord nor Fluttershy checked.";
        elif(CheckButtonState1.get()  == 1 and CheckButtonState2.get()  == 0 ):
           Label_CkBtnState["text"] = "Only Discord checked.";
        elif(CheckButtonState1.get()  == 0 and CheckButtonState2.get()  == 1 ):
           Label_CkBtnState["text"] = "Only Fluttershy checked."; 
        elif(CheckButtonState1.get()  == 1 and CheckButtonState2.get() == 1 ):
           Label_CkBtnState["text"] = "Both Discord and Fluttershy checked.";
        else: Label_CkBtnState["text"] = "This should never happen.";        

    def Discord_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Discord says:\nFriendhip is STUPID!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");
        Get_Checkbutton_State();

    def Fluttershy_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Fluttershy says:\nLove one another!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");     
        Get_Checkbutton_State();

    Label1 = TK.Label( text="Pony Python tkinter Text Objects",
                       font=("Comic Sans MS", 20, "bold"),
                       justify="center",
                       foreground="white",
                       background="black",
                       width=40,
                       height=3  
                     );

    Label2 = TK.Label( text="Discord Says:",
                       font=("Comic Sans MS", 15, "bold"),
                       justify="center",
                       foreground="black",
                       background="white",
                       width=40,
                       height=3  
                     );    
 
    Label3 = TK.Label( text="Fluttershy Says:",
                       font=("Comic Sans MS", 15, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     );

    Label_CkBtnState = TK.Label( text="Check Button State",
                                 font=("Comic Sans MS", 12),
                                 justify="center",
                                 foreground="white",
                                 background="green",
                                 width=40,
                                 height=3  
                               );                                                      

    Chk_Button1 = TK.Checkbutton( window,
                                  command = Discord_Trigger,
                                  variable = CheckButtonState1,
                                  onvalue = 1, 
                                  offvalue = 0,
                                  text="Do NOT Click Me",
                                  font=("Comic Sans MS", 10, "bold"),
                                  justify="center",
                                  foreground="black",
                                  background="red",
                                  width=30,
                                  height=3  
                                );

    Chk_Button2 = TK.Checkbutton( window,
                                  command = Fluttershy_Trigger, 
                                  text = "Music", 
                                  variable = CheckButtonState2,
                                  onvalue = 1, 
                                  offvalue = 0, 
                                  font=("Comic Sans MS", 10, "bold"),
                                  foreground="black",
                                  background="red",                                  
                                  justify="center",
                                  width=30,
                                  height=3 
                                );

    Label1.pack();
    Label2.place(x=30, y=150, height=50, width=250);
    Label3.place(x=325, y=150, height=50, width=250);    
    Chk_Button1.place(x=30, y=200, height=50, width=250);  
    Chk_Button2.place(x=325, y=200, height=50, width=250);
    Label_CkBtnState.place(x=130, y=350, height=50, width=350);

    Text1 = TK.Text( font=("Comic Sans MS", 15, "bold"),
                     foreground="white",
                     background="black",
                     width=60,
                   );    

    Text1.place(x=130, y=270, height=65, width=350);
    Text1.insert("1.0","Princess Celestia Says:\nFriendship is Magic!");
    Text1.tag_configure("In_Da_Middle", justify='center');
    Text1.tag_add("In_Da_Middle", "1.0", "end");

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Checkbutton Objects
def CheckButton_2():
    import tkinter as TK;

    top = TK.Tk()
    CheckVar1 = TK.IntVar();
    CheckVar2 = TK.IntVar();

    C1 = TK.Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20);
    C2 = TK.Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20);

    C1.pack();
    C2.pack();

    top.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Checkbutton Objects in Frames
def Checkbuttons_In_Frames():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Checkbuttons in FRAME objects.");
    window.geometry("550x310");
    window.configure(bg='white');

    #For use with checkbuttons to get state
    ChkBut_1_State = TK.IntVar();
    ChkBut_2_State = TK.IntVar();
    ChkBut_3_State = TK.IntVar();
    ChkBut_4_State = TK.IntVar();
    ChkBut_5_State = TK.IntVar();
    ChkBut_6_State = TK.IntVar();
    ChkBut_7_State = TK.IntVar();
    ChkBut_8_State = TK.IntVar();
    ChkBut_9_State = TK.IntVar();
    ChkBut_10_State = TK.IntVar();
    ChkBut_11_State = TK.IntVar();
    ChkBut_12_State = TK.IntVar();
    ChkBut_13_State = TK.IntVar();
    ChkBut_14_State = TK.IntVar();

    #Event handler
    def Get_Checkbutton_State():
        if(ChkBut_1_State.get() == 1):
           Label_CHOICE ["text"] = "You selected Twilight Sparkle.";
        elif(ChkBut_2_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Rainbow Dash.";
        elif(ChkBut_3_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Fluttershy."; 
        elif(ChkBut_4_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Rarity."; 
        elif(ChkBut_5_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Apple Jack."; 
        elif(ChkBut_6_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Pinkie Pie."; 
        elif(ChkBut_7_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Princess Celestia.";
        elif(ChkBut_8_State.get() == 1):
             Label_CHOICE ["text"] = "You selected Discord.";
        elif(ChkBut_9_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Nightmare Moon.";
        elif(ChkBut_10_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Lord Tirek."; 
        elif(ChkBut_11_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected King Sombra."; 
        elif(ChkBut_12_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Queen Chrysalis."; 
        elif(ChkBut_13_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Storm King."; 
        elif(ChkBut_14_State.get()  == 1):
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

    ChkBut_1 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "1. Twilight Sparkle", 
                               variable = ChkBut_1_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    ChkBut_2 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "2. Rainbow Dash", 
                               variable = ChkBut_2_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    ChkBut_3 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,    
                               text = "3. Fluttershy", 
                               variable = ChkBut_3_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );  

    ChkBut_4 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "4. Rarity", 
                               variable = ChkBut_4_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    ChkBut_5 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "5. Apple Jack", 
                               variable = ChkBut_5_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    ChkBut_6 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "6. Pinkie Pie", 
                               variable = ChkBut_6_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );    

    ChkBut_7 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "7. Princess Celestia", 
                               variable = ChkBut_7_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      

    ChkBut_8 = TK.Checkbutton( master=FRM_Fav_Antag,
                               command=Get_Checkbutton_State,
                               text = "1. Discord", 
                               variable = ChkBut_8_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             ); 

    ChkBut_9 = TK.Checkbutton( master=FRM_Fav_Antag,
                               command=Get_Checkbutton_State,
                               text = "2. Nightmare Moon", 
                               variable = ChkBut_9_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      

    ChkBut_10 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "3. Lord Tirek", 
                                variable = ChkBut_10_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    ChkBut_11 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "4. King Sombra", 
                                variable = ChkBut_11_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    ChkBut_12 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "5. Queen Chrysalis", 
                                variable = ChkBut_12_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );    

    ChkBut_13 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "6. Storm King", 
                                variable = ChkBut_13_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    ChkBut_14 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "7. Starlight Glimmer", 
                                variable = ChkBut_14_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );                                                                                                       

    ChkBut_1.place(x=40, y=40, height=20, width=200);
    ChkBut_2.place(x=40, y=60, height=20, width=200);
    ChkBut_3.place(x=40, y=80, height=20, width=200);
    ChkBut_4.place(x=40, y=100, height=20, width=200);
    ChkBut_5.place(x=40, y=120, height=20, width=200);
    ChkBut_6.place(x=40, y=140, height=20, width=200);
    ChkBut_7.place(x=40, y=160, height=20, width=200);
    ChkBut_8.place(x=40, y=40, height=20, width=200);
    ChkBut_9.place(x=40, y=60, height=20, width=200);
    ChkBut_10.place(x=40, y=80, height=20, width=200);
    ChkBut_11.place(x=40, y=100, height=20, width=200);
    ChkBut_12.place(x=40, y=120, height=20, width=200);
    ChkBut_13.place(x=40, y=140, height=20, width=200);
    ChkBut_14.place(x=40, y=160, height=20, width=200);    

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
def Checkbuttons_In_LabelFrames():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Checkbuttons in FRAME objects.");
    window.geometry("550x310");
    window.configure(bg='white');

    #For use with checkbuttons to get state
    ChkBut_1_State = TK.IntVar();
    ChkBut_2_State = TK.IntVar();
    ChkBut_3_State = TK.IntVar();
    ChkBut_4_State = TK.IntVar();
    ChkBut_5_State = TK.IntVar();
    ChkBut_6_State = TK.IntVar();
    ChkBut_7_State = TK.IntVar();
    ChkBut_8_State = TK.IntVar();
    ChkBut_9_State = TK.IntVar();
    ChkBut_10_State = TK.IntVar();
    ChkBut_11_State = TK.IntVar();
    ChkBut_12_State = TK.IntVar();
    ChkBut_13_State = TK.IntVar();
    ChkBut_14_State = TK.IntVar();

    #Event handler
    def Get_Checkbutton_State():
        if(ChkBut_1_State.get() == 1):
           Label_CHOICE ["text"] = "You selected Twilight Sparkle.";
        elif(ChkBut_2_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Rainbow Dash.";
        elif(ChkBut_3_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Fluttershy."; 
        elif(ChkBut_4_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Rarity."; 
        elif(ChkBut_5_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Apple Jack."; 
        elif(ChkBut_6_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Pinkie Pie."; 
        elif(ChkBut_7_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Princess Celestia.";
        elif(ChkBut_8_State.get() == 1):
             Label_CHOICE ["text"] = "You selected Discord.";
        elif(ChkBut_9_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Nightmare Moon.";
        elif(ChkBut_10_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Lord Tirek."; 
        elif(ChkBut_11_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected King Sombra."; 
        elif(ChkBut_12_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Queen Chrysalis."; 
        elif(ChkBut_13_State.get()  == 1):
             Label_CHOICE ["text"] = "You selected Storm King."; 
        elif(ChkBut_14_State.get()  == 1):
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

    ChkBut_1 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "1. Twilight Sparkle", 
                               variable = ChkBut_1_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    ChkBut_2 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "2. Rainbow Dash", 
                               variable = ChkBut_2_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    ChkBut_3 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,    
                               text = "3. Fluttershy", 
                               variable = ChkBut_3_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );  

    ChkBut_4 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "4. Rarity", 
                               variable = ChkBut_4_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );

    ChkBut_5 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "5. Apple Jack", 
                               variable = ChkBut_5_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                   
                               width=199,
                               height=19 
                             );    

    ChkBut_6 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "6. Pinkie Pie", 
                               variable = ChkBut_6_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );    

    ChkBut_7 = TK.Checkbutton( master=FRM_Fav_Chars,
                               command=Get_Checkbutton_State,
                               text = "7. Princess Celestia", 
                               variable = ChkBut_7_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      

    ChkBut_8 = TK.Checkbutton( master=FRM_Fav_Antag,
                               command=Get_Checkbutton_State,
                               text = "1. Discord", 
                               variable = ChkBut_8_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             ); 

    ChkBut_9 = TK.Checkbutton( master=FRM_Fav_Antag,
                               command=Get_Checkbutton_State,
                               text = "2. Nightmare Moon", 
                               variable = ChkBut_9_State,
                               onvalue = 1, 
                               offvalue = 0, 
                               font=("Comic Sans MS", 10, "bold"),
                               anchor="w",
                               foreground="black",
                               background="gray",                                  
                               width=199,
                               height=19 
                             );      

    ChkBut_10 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "3. Lord Tirek", 
                                variable = ChkBut_10_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    ChkBut_11 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "4. King Sombra", 
                                variable = ChkBut_11_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    ChkBut_12 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "5. Queen Chrysalis", 
                                variable = ChkBut_12_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );    

    ChkBut_13 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "6. Storm King", 
                                variable = ChkBut_13_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );

    ChkBut_14 = TK.Checkbutton( master=FRM_Fav_Antag,
                                command=Get_Checkbutton_State,
                                text = "7. Starlight Glimmer", 
                                variable = ChkBut_14_State,
                                onvalue = 1, 
                                offvalue = 0, 
                                font=("Comic Sans MS", 10, "bold"),
                                anchor="w",
                                foreground="black",
                                background="gray",                                  
                                width=199,
                                height=19 
                             );                                                                                                       

    ChkBut_1.place(x=40, y=10, height=20, width=200);
    ChkBut_2.place(x=40, y=30, height=20, width=200);
    ChkBut_3.place(x=40, y=50, height=20, width=200);
    ChkBut_4.place(x=40, y=70, height=20, width=200);
    ChkBut_5.place(x=40, y=90, height=20, width=200);
    ChkBut_6.place(x=40, y=110, height=20, width=200);
    ChkBut_7.place(x=40, y=130, height=20, width=200);
    ChkBut_8.place(x=40, y=10, height=20, width=200);
    ChkBut_9.place(x=40, y=30, height=20, width=200);
    ChkBut_10.place(x=40, y=50, height=20, width=200);
    ChkBut_11.place(x=40, y=70, height=20, width=200);
    ChkBut_12.place(x=40, y=90, height=20, width=200);
    ChkBut_13.place(x=40, y=110, height=20, width=200);
    ChkBut_14.place(x=40, y=130, height=20, width=200);    

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
# Checkbutton Objects using Image objects 
def Checkbuttons_Using_Image_Objects():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Checkbuttons in FRAME objects.");
    window.geometry("550x310");
    window.configure(bg='white');

    def switchState():
        if cb1.get() == 1:
           disp_Lb.config(text='ON');
        
        elif cb1.get() == 0:
             disp_Lb.config(text='OFF');
        else:
             disp_Lb.config(text='error!');

    switch_on = TK.PhotoImage(width=50, height=50);
    switch_off = TK.PhotoImage(width=50, height=50);
    switch_on.put(("green",), to=(0, 0, 23,23));
    switch_off.put(("red",), to=(24, 0, 47, 23));

    cb1 = TK.IntVar();

    TK.Checkbutton(window, 
                   image=switch_off, 
                   selectimage=switch_on, 
                   onvalue=1, offvalue=0, 
                   variable=cb1, indicatoron=False, 
                   command=switchState).pack(padx=20, pady=10);

    disp_Lb = TK.Label(window);
    disp_Lb.pack();

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
    def Checkbox1_Checked_Handler():
        if Checkbox_Var.get() == 1:
           BTN_Asleep_Or_Awake['state'] = TK.NORMAL;
           BTN_Asleep_Or_Awake.configure(text='Awake!');
        elif Checkbox_Var.get() == 0:
             BTN_Asleep_Or_Awake['state'] = TK.DISABLED;
             BTN_Asleep_Or_Awake.configure(text='Asleep!');
        else:
              TK.messagebox.showerror('!ERROR!', 'This is NOT supposed to happen.');

    TK.Checkbutton(window, text="accept T&C", variable=Checkbox_Var, onvalue=1, offvalue=0, command=Checkbox1_Checked_Handler).pack();

    BTN_Asleep_Or_Awake = TK.Button(window, text='Sleeping!', state=TK.DISABLED, padx=20, pady=5);
    BTN_Asleep_Or_Awake.pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Checkbutton Objects - deselect, select 
def Checkbuttons_DeSelecting():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Checkbuttons - Deselecting and Selecting.");
    window.geometry("300x250");
    window.configure(bg='white');

    #Event Handler
    def clear_selection():
        cb1.deselect();
        cb2.deselect();
        cb3.deselect();
        cb4.deselect();
        cb5.deselect();
        cb6.deselect();
    
    var = TK.BooleanVar();
    var.set(True);
 
    cb1 = TK.Checkbutton(window, text='Click me!', variable=var);
    cb1.pack();
    cb2 = TK.Checkbutton(window, text='Click me!', variable=var);
    cb2.pack();
    cb3 = TK.Checkbutton(window, text='Click me!', variable=var);
    cb3.pack();
    cb4 = TK.Checkbutton(window, text='Click me!', variable=var);
    cb4.pack();
    cb5 = TK.Checkbutton(window, text='Click me!', variable=var);
    cb5.pack();
    cb6 = TK.Checkbutton(window, text='Click me!', variable=var);
    cb6.pack();

    TK.Button(window, text='Deselect All Checkbuttons', command=clear_selection).pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------    



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


#-----Invocations-----
#CheckButton_1();
#CheckButton_2();
#Checkbuttons_In_Frames();
#Checkbuttons_In_LabelFrames();
#Checkbuttons_Using_Image_Objects();
#Checkbuttons_Selecting();
#Checkbuttons_DeSelecting();
Radiobuttons_and_Checkbuttons_Combining_Into_Dialog_Window();














"""
w = Checkbutton ( master, option, ... )
Parameters
master − This represents the parent window.

options − Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

Sr.No.	Option & Description
1	
activebackground

Background color when the checkbutton is under the cursor.

2	
activeforeground

Foreground color when the checkbutton is under the cursor.

3	
bg

The normal background color displayed behind the label and indicator.

4	
bitmap

To display a monochrome image on a button.

5	
bd

The size of the border around the indicator. Default is 2 pixels.

6	
command

A procedure to be called every time the user changes the state of this checkbutton.

7	
cursor

If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.

8	
disabledforeground

The foreground color used to render the text of a disabled checkbutton. The default is a stippled version of the default foreground color.

9	
font

The font used for the text.

10	
fg

The color used to render the text.

11	
height

The number of lines of text on the checkbutton. Default is 1.

12	
highlightcolor

The color of the focus highlight when the checkbutton has the focus.

13	
image

To display a graphic image on the button.

14	
justify

If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT.

15	
offvalue

Normally, a checkbutton's associated control variable will be set to 0 when it is cleared (off). You can supply an alternate value for the off state by setting offvalue to that value.

16	
onvalue

Normally, a checkbutton's associated control variable will be set to 1 when it is set (on). You can supply an alternate value for the on state by setting onvalue to that value.

17	
padx

How much space to leave to the left and right of the checkbutton and text. Default is 1 pixel.

18	
pady

How much space to leave above and below the checkbutton and text. Default is 1 pixel.

19	
relief

With the default value, relief=FLAT, the checkbutton does not stand out from its background. You may set this option to any of the other styles

20	
selectcolor

The color of the checkbutton when it is set. Default is selectcolor="red".

21	
selectimage

If you set this option to an image, that image will appear in the checkbutton when it is set.

22	
state

The default is state=NORMAL, but you can use state=DISABLED to gray out the control and make it unresponsive. If the cursor is currently over the checkbutton, the state is ACTIVE.

23	
text

The label displayed next to the checkbutton. Use newlines ("\n") to display multiple lines of text.

24	
underline

With the default value of -1, none of the characters of the text label are underlined. Set this option to the index of a character in the text (counting from zero) to underline that character.

25	
variable

The control variable that tracks the current state of the checkbutton. Normally this variable is an IntVar, and 0 means cleared and 1 means set, but see the offvalue and onvalue options above.

26	
width

The default width of a checkbutton is determined by the size of the displayed image or text. You can set this option to a number of characters and the checkbutton will always have room for that many characters.

27	
wraplength

Normally, lines are not wrapped. You can set this option to a number of characters and all lines will be broken into pieces no longer than that number.

Methods
Following are commonly used methods for this widget −

Sr.No.	Method & Description
1	
deselect()

Clears (turns off) the checkbutton.

2	
flash()

Flashes the checkbutton a few times between its active and normal colors, but leaves it the way it started.

3	
invoke()

You can call this method to get the same actions that would occur if the user clicked on the checkbutton to change its state.

4	
select()

Sets (turns on) the checkbutton.

5	
toggle()

Clears the checkbutton if set, sets it if cleared.
"""