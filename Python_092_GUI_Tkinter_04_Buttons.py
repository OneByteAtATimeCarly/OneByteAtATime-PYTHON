# Title: Python GUI Programming With TKinter - Widgets - BUTTONS
# Author: C. S. Germany 02/05/2022

# LINK = https://realpython.com/python-gui-tkinter/


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting attributes of a label
from tkinter import DISABLED
from tkinter.font import NORMAL


def GUI_Buttons():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x280");
    window.configure(bg='white');

    Label1 = TK.Label( text="Pony Python tkinter Buttons",
                       font=("Comic Sans MS", 20, "bold"),
                       foreground="white",
                       background="black",
                       width=40,
                       height=3  
                     );

    Label2 = TK.Label( text="Discord Says:",
                       font=("Comic Sans MS", 15, "bold"),
                       foreground="black",
                       background="white",
                       width=40,
                       height=3  
                     );    

    Label3 = TK.Label( text="Fluttershy Says:",
                       font=("Comic Sans MS", 15, "bold"),
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     );                                   

    Button1 = TK.Button( text="Do NOT Click Me",
                         font=("Comic Sans MS", 10, "bold"),
                         foreground="white",
                         background="red",
                         width=30,
                         height=3  
                     );

    Button2 = TK.Button( text="Click Me!",
                         font=("Comic Sans MS", 10, "bold"),
                         foreground="white",
                         background="green",
                         width=30,
                         height=3  
                     );

    Label1.pack();
    Label2.place(x=30, y=150, height=50, width=250);
    Label3.place(x=325, y=150, height=50, width=250);    
    Button1.place(x=30, y=200, height=50, width=250);
    Button2.place(x=325, y=200, height=50, width=250);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Adding Event Handler funtions to Buttons and listener  with command=
def Event_Handle_Button_Click():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x350");
    window.configure(bg='white');

    #Event handlers
    def Discord_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Discord says:\nFriendhip is STUPID!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");

    def Fluttershy_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Fluttershy says:\nLove one another!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");        

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

    Button1 = TK.Button( command=Discord_Trigger,
                         text="Do NOT Click Me",
                         font=("Comic Sans MS", 10, "bold"),
                         justify="center",
                         foreground="white",
                         background="red",
                         width=30,
                         height=3  
                     );

    Button2 = TK.Button( command=Fluttershy_Trigger,
                         text="Click Me!",
                         font=("Comic Sans MS", 10, "bold"),
                         justify="center",
                         foreground="white",
                         background="green",
                         width=30,
                         height=3  
                     );

    Label1.pack();
    Label2.place(x=30, y=150, height=50, width=250);
    Label3.place(x=325, y=150, height=50, width=250);    
    Button1.place(x=30, y=200, height=50, width=250);  
    Button2.place(x=325, y=200, height=50, width=250);

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
# Disabling and Enabling Button objects.  NORMAL state is enabled, disabled state is DISABLED
# Example: Button2["state"] = DISABLED;  Button2["state"] = NORMAL;     
def Event_Handle_Button_Click_Disable_Enable():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x350");
    window.configure(bg='white');

    #Event handlers
    def Discord_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Discord says:\nFriendhip is STUPID!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");
        Button2["state"] = NORMAL;

    def Fluttershy_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Fluttershy says:\nLove one another!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");        

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

    Button1 = TK.Button( command=Discord_Trigger,
                         text="Do NOT Click Me",
                         font=("Comic Sans MS", 10, "bold"),
                         justify="center",
                         foreground="white",
                         background="red",
                         width=30,
                         height=3  
                     );

    Button2 = TK.Button( command=Fluttershy_Trigger,
                         text="Click Me!",
                         font=("Comic Sans MS", 10, "bold"),
                         justify="center",
                         foreground="white",
                         background="green",
                         width=30,
                         height=3  
                     );

    Label1.pack();
    Label2.place(x=30, y=150, height=50, width=250);
    Label3.place(x=325, y=150, height=50, width=250);    
    Button1.place(x=30, y=200, height=50, width=250);  
    Button2.place(x=325, y=200, height=50, width=250);

    Button2["state"] = DISABLED;

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

#Invocations
#GUI_Buttons();
#Event_Handle_Button_Click();
Event_Handle_Button_Click_Disable_Enable();

