# Python tkinter Geometry GEOMETRY MANAGERS

# LINK = https://realpython.com/python-gui-tkinter/

# There are 3 Geometry Managers in Python
# 1 = .pack()
# 2 = .place()
# 3 = .grid()

#1. pack() = Computes a rectangular area called a "parcel" that’s just tall (or wide) enough to hold the widget and fills the remaining width (or height) in the window with blank space.
#   Centers the widget in the parcel unless a different location is specified.
#
# pack() accepts some keyword arguments for more precisely configuring widget placement. For example, you can set the fill keyword argument to specify in which direction the frames should fill.
# The options are tk.X to fill in the horizontal direction, tk.Y to fill vertically, and tk.BOTH to fill in both directions. 

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting attributes of an Frame
def Pack_1():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("800x550");
    window.configure(bg='white');

    Frame_1 = TK.Frame( master=window,
                        relief=TK.FLAT,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_2 = TK.Frame( master=window,
                        relief=TK.SUNKEN,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_3 = TK.Frame( master=window,
                        relief=TK.RAISED,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_4 = TK.Frame( master=window,
                        relief=TK.GROOVE,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_5 = TK.Frame( master=window,
                        relief=TK.RIDGE,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );                                     


    Label_0 = TK.Label( text="No Frame: Pony Python tkinter FRAME Objects",
                        font=("Comic Sans MS", 20, "bold"),
                        justify="center",
                        foreground="white",
                        background="black",
                        width=40,
                        height=3  
                     );

    Label_1 = TK.Label( master=Frame_1,
                       text="Label Inside Frame 1",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="black",
                       background="white",
                       width=40,
                       height=3  
                     );    

    Label_2 = TK.Label( master=Frame_2,
                       text="Label Inside Frame 2",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_3 = TK.Label( master=Frame_3,
                       text="Label Inside Frame 3",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_4 = TK.Label( master=Frame_4,
                       text="Label Inside Frame 4",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_5 = TK.Label( master=Frame_5,
                       text="Label Inside Frame 5",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_0.pack();
    Label_1.pack();
    Label_2.pack();
    Label_3.pack();
    Label_4.pack();
    Label_5.pack();

    Frame_1.pack();
    Frame_2.pack();
    Frame_3.pack();
    Frame_4.pack();
    Frame_5.pack();

    window.mainloop(); 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fill horizontally (TK.X)
def Pack_2():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("800x550");
    window.configure(bg='white');

    Frame_1 = TK.Frame( master=window,
                        relief=TK.FLAT,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_2 = TK.Frame( master=window,
                        relief=TK.SUNKEN,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_3 = TK.Frame( master=window,
                        relief=TK.RAISED,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_4 = TK.Frame( master=window,
                        relief=TK.GROOVE,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_5 = TK.Frame( master=window,
                        relief=TK.RIDGE,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );                                     


    Label_0 = TK.Label( text="No Frame: Pony Python tkinter FRAME Objects",
                        font=("Comic Sans MS", 20, "bold"),
                        justify="center",
                        foreground="white",
                        background="black",
                        width=40,
                        height=3  
                     );

    Label_1 = TK.Label( master=Frame_1,
                       text="Label Inside Frame 1",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="black",
                       background="white",
                       width=40,
                       height=3  
                     );    

    Label_2 = TK.Label( master=Frame_2,
                       text="Label Inside Frame 2",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_3 = TK.Label( master=Frame_3,
                       text="Label Inside Frame 3",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_4 = TK.Label( master=Frame_4,
                       text="Label Inside Frame 4",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_5 = TK.Label( master=Frame_5,
                       text="Label Inside Frame 5",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_0.pack();
    Label_1.pack();
    Label_2.pack();
    Label_3.pack();
    Label_4.pack();
    Label_5.pack();

    Frame_1.pack(fill=TK.X);
    Frame_2.pack(fill=TK.X);
    Frame_3.pack(fill=TK.X);
    Frame_4.pack(fill=TK.X);
    Frame_5.pack(fill=TK.X);

    window.mainloop(); 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fill vertically (TK.Y)
def Pack_3():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("800x550");
    window.configure(bg='white');

    Frame_1 = TK.Frame( master=window,
                        relief=TK.FLAT,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_2 = TK.Frame( master=window,
                        relief=TK.SUNKEN,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_3 = TK.Frame( master=window,
                        relief=TK.RAISED,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_4 = TK.Frame( master=window,
                        relief=TK.GROOVE,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_5 = TK.Frame( master=window,
                        relief=TK.RIDGE,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );                                     


    Label_0 = TK.Label( text="No Frame: Pony Python tkinter FRAME Objects",
                        font=("Comic Sans MS", 20, "bold"),
                        justify="center",
                        foreground="white",
                        background="black",
                        width=40,
                        height=3  
                     );

    Label_1 = TK.Label( master=Frame_1,
                       text="Label Inside Frame 1",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="black",
                       background="white",
                       width=40,
                       height=3  
                     );    

    Label_2 = TK.Label( master=Frame_2,
                       text="Label Inside Frame 2",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_3 = TK.Label( master=Frame_3,
                       text="Label Inside Frame 3",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_4 = TK.Label( master=Frame_4,
                       text="Label Inside Frame 4",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_5 = TK.Label( master=Frame_5,
                       text="Label Inside Frame 5",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_0.pack();
    Label_1.pack();
    Label_2.pack();
    Label_3.pack();
    Label_4.pack();
    Label_5.pack();

    Frame_1.pack(fill=TK.Y);
    Frame_2.pack(fill=TK.Y);
    Frame_3.pack(fill=TK.Y);
    Frame_4.pack(fill=TK.Y);
    Frame_5.pack(fill=TK.Y);

    window.mainloop(); 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fill vertically (TK.BOTH)
def Pack_4():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("800x550");
    window.configure(bg='white');

    Frame_1 = TK.Frame( master=window,
                        relief=TK.FLAT,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_2 = TK.Frame( master=window,
                        relief=TK.SUNKEN,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_3 = TK.Frame( master=window,
                        relief=TK.RAISED,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );

    Frame_4 = TK.Frame( master=window,
                        relief=TK.GROOVE,
                        borderwidth=5,
                        width=65,
                        height=50   
                      );

    Frame_5 = TK.Frame( master=window,
                        relief=TK.RIDGE,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );                                     


    Label_0 = TK.Label( text="No Frame: Pony Python tkinter FRAME Objects",
                        font=("Comic Sans MS", 20, "bold"),
                        justify="center",
                        foreground="white",
                        background="black",
                        width=40,
                        height=3  
                     );

    Label_1 = TK.Label( master=Frame_1,
                       text="Label Inside Frame 1",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="black",
                       background="white",
                       width=40,
                       height=3  
                     );    

    Label_2 = TK.Label( master=Frame_2,
                       text="Label Inside Frame 2",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_3 = TK.Label( master=Frame_3,
                       text="Label Inside Frame 3",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_4 = TK.Label( master=Frame_4,
                       text="Label Inside Frame 4",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_5 = TK.Label( master=Frame_5,
                       text="Label Inside Frame 5",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_0.pack();
    Label_1.pack();
    Label_2.pack();
    Label_3.pack();
    Label_4.pack();
    Label_5.pack();

    Frame_1.pack(fill=TK.BOTH);
    Frame_2.pack(fill=TK.BOTH);
    Frame_3.pack(fill=TK.BOTH);
    Frame_4.pack(fill=TK.BOTH);
    Frame_5.pack(fill=TK.BOTH);

    window.mainloop(); 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


# The SIDE argument specifies on which side of the window the widget should be placed. There are 4:
# side=TK.TOP
# side=TK.BOTTOM
# side=TK.LEFT
# side=TK.RIGHT

# expand=True  Sets widgets to auto-expand as a window is resized.

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fill vertically (TK.BOTH)
def Pack_5():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("1685x400");
    window.configure(bg='white');

    Frame_1 = TK.Frame( master=window,
                        relief=TK.FLAT,
                        borderwidth=5,
                        width=30,
                        height=20  
                      );

    Frame_2 = TK.Frame( master=window,
                        relief=TK.SUNKEN,
                        borderwidth=5,
                        width=30,
                        height=20   
                      );

    Frame_3 = TK.Frame( master=window,
                        relief=TK.RAISED,
                        borderwidth=5,
                        width=30,
                        height=20  
                      );

    Frame_4 = TK.Frame( master=window,
                        relief=TK.GROOVE,
                        borderwidth=5,
                        width=30,
                        height=20   
                      );

    Frame_5 = TK.Frame( master=window,
                        relief=TK.RIDGE,
                        borderwidth=5,
                        width=30,
                        height=20  
                      );                                     


    Label_0 = TK.Label( text="No Frame: Pony Python tkinter FRAME Objects",
                        font=("Comic Sans MS", 20, "bold"),
                        justify="center",
                        foreground="white",
                        background="black",
                        width=40,
                        height=3  
                     );

    Label_1 = TK.Label( master=Frame_1,
                       text="Label Inside Frame 1",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="black",
                       background="white",
                       width=40,
                       height=3  
                     );    

    Label_2 = TK.Label( master=Frame_2,
                       text="Label Inside Frame 2",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_3 = TK.Label( master=Frame_3,
                       text="Label Inside Frame 3",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_4 = TK.Label( master=Frame_4,
                       text="Label Inside Frame 4",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_5 = TK.Label( master=Frame_5,
                       text="Label Inside Frame 5",
                       font=("Comic Sans MS", 10, "bold"),
                       justify="center",
                       foreground="pink",
                       background="white",
                       width=40,
                       height=3  
                     ); 

    Label_0.pack();
    Label_1.pack();
    Label_2.pack();
    Label_3.pack();
    Label_4.pack();
    Label_5.pack();

    Frame_1.pack(fill=TK.BOTH,side=TK.LEFT,expand=True);
    Frame_2.pack(fill=TK.BOTH,side=TK.LEFT,expand=True);
    Frame_3.pack(fill=TK.BOTH,side=TK.LEFT,expand=True);
    Frame_4.pack(fill=TK.BOTH,side=TK.LEFT,expand=True);
    Frame_5.pack(fill=TK.BOTH,side=TK.LEFT,expand=True);

    window.mainloop(); 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#2. Place
#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Using place() geometry manager
def Place_1():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x350");
    window.configure(bg='white');

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



#3. Grid
#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Using grid() geometry manager
def Grid_1():
    import tkinter as tk;
    window = tk.Tk();
    window.title("Hello MOTO!");
    window.geometry("300x200");
    window.configure(bg='white');

    for i in range(3):
        for j in range(3):
            
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
        
            frame.grid(row=i, column=j);
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}");
            label.pack();

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Using grid() geometry manager - making windows auto-resize
# .columnconfigure() and .rowconfigure() adjust how rows and columns of grid grow as window is resized.
# Each method takes 3 arguments: index, weight and minimum size 
def Grid_2():
    import tkinter as TK;
    window = TK.Tk();

    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75);
        window.rowconfigure(i, weight=1, minsize=50);

        for j in range(0, 3):
            frame = TK.Frame( master=window,
                              relief=TK.RAISED,
                              borderwidth=1
                            );

            frame.grid(row=i, column=j, padx=5, pady=5);
            label = TK.Label(master=frame, text=f"Row {i}\nColumn {j}");
            label.pack(padx=5, pady=5);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# creates two Label widgets and places them in a grid with one column and two rows 
def Grid_3():
    import tkinter as TK;
    window = TK.Tk();
    window.columnconfigure(0, minsize=250);
    window.rowconfigure([0, 1], minsize=100);

    label1 = TK.Label(text="Row 1 = Twilight Sparkle");
    label1.grid(row=0, column=0);

    label2 = TK.Label(text="Row 2 = Rainbow Dash");
    label2.grid(row=1, column=0);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting "sticky parameter". Takes 4 cardinal directions as argument: n, s, e, w . Aligns objects towards that direction in each grid cell.
def Grid_4():
    import tkinter as TK;
    window = TK.Tk();
    window.columnconfigure(0, minsize=250);
    window.rowconfigure([0, 1], minsize=100);

    label1 = TK.Label(text="Row 1 = Twilight Sparkle");
    label1.grid(row=0, column=0,sticky="n");

    label2 = TK.Label(text="Row 2 = Rainbow Dash");
    label2.grid(row=1, column=0,sticky="n");

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# You can combine sticky cardinal parameters to position objects in corners 
def Grid_5():
    import tkinter as TK;
    window = TK.Tk();
    window.columnconfigure(0, minsize=250);
    window.rowconfigure([0, 1], minsize=100);

    label1 = TK.Label(text="Row 1 = Twilight Sparkle");
    label1.grid(row=0, column=0,sticky="ne");

    label2 = TK.Label(text="Row 2 = Rainbow Dash");
    label2.grid(row=1, column=0,sticky="sw");

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ew = force widget to fill cell in horizontal direction
# ns =  force widget to fill cell in vertical direction
# nsew = force widget to fill cell in both directions
def Grid_6():
    import tkinter as tk;
    window = tk.Tk();
    window.rowconfigure(0, minsize=50);
    window.columnconfigure([0, 1, 2, 3], minsize=50);

    label1 = tk.Label(text="1", bg="black", fg="white");
    label2 = tk.Label(text="2", bg="black", fg="white");
    label3 = tk.Label(text="3", bg="black", fg="white");
    label4 = tk.Label(text="4", bg="black", fg="white");

    label1.grid(row=0, column=0);
    label2.grid(row=0, column=1, sticky="ew");
    label3.grid(row=0, column=2, sticky="ns");
    label4.grid(row=0, column=3, sticky="nsew");

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------




#Invocations
#Pack_1();
#Pack_2();
#Pack_3();
#Pack_4();
#Pack_5();
#Place_1();
#Grid_1();
#Grid_2();
#Grid_3();
#Grid_4();
#Grid_5();
Grid_6();