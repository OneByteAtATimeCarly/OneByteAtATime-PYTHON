# Title: Python GUI Programming With TKinter - Widgets - ENTRYS
# Author: C. S. Germany 02/05/2022

# LINK = https://realpython.com/python-gui-tkinter/

# Entry objects get a SINGLE LINE of input. (They don't get multiple line input. For that use Text class objects.)

# Use following methods
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
# To create an ENTRY with masking for PASSWORDS, use add [ show="*" ] into it's .configure().

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting attributes of an Entry
def GUI_Entry1():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x320");
    window.configure(bg='white');

    Label1 = TK.Label( text="Pony Python tkinter Entry Objects",
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

    Button1 = TK.Button( text="Do NOT Click Me",
                         font=("Comic Sans MS", 10, "bold"),
                         justify="center",
                         foreground="white",
                         background="red",
                         width=30,
                         height=3  
                     );

    Button2 = TK.Button( text="Click Me!",
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
    Entry1 = TK.Entry( text="ENTRY Object",
                       font=("Comic Sans MS", 15),
                       justify="center",
                       foreground="white",
                       background="black",
                       width=30,
                     );
    
    Entry1.place(x=130, y=270, height=35, width=350);
    Entry1.insert(0,"Friendship is Magic!");

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Invocations
GUI_Entry1();

