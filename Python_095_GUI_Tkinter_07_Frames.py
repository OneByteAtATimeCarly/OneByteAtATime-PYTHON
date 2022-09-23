# Title: Python GUI Programming With TKinter - Widgets - FRAMES
# Author: C. S. Germany 02/05/2022

# LINK = https://realpython.com/python-gui-tkinter/

# Frame widgets are important for organizing the layout of your widgets in an application. Frame widgets are great for organizing other widgets in a logical manner. 
# Related widgets can be assigned to the same frame so that, if the frame is ever moved in the window, then the related widgets stay together.

# You add objects to a frame by specifying "master=Frame_Name" as a parameter in the object's constructor. See code below.

# Frame widgets have a RELIEF attribute that creates a border around the frame. You can set relief to the following values:

# tk.FLAT: Has no border effect (the default value)
# tk.SUNKEN: Creates a sunken effect
# tk.RAISED: Creates a raised effect
# tk.GROOVE: Creates a grooved border effect
# tk.RIDGE: Creates a ridged effect

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting attributes of an Entry
def Frames_1_Basic():
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
def Frames_Other_Attributes():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Frame Stuff");
    window.geometry("800x550");
    window.configure(bg='white');

    Frame_1 = TK.Frame( master=window,
                        relief=TK.GROOVE,
                        borderwidth=5,
                        width=65,
                        height=50  
                      );
    
    Frame_1.pack();
    window.mainloop(); 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Invocations
#Frames_1_Basic();
Frames_Other_Attributes();







"""

#Padding
f['padding'] = 5           # 5 pixels on all sides
f['padding'] = (5,10)      # 5 on left and right, 10 on top and bottom
f['padding'] = (5,7,10,12) # left: 5, top: 7, right: 10, bottom: 12
.f configure -padding 5           ;# 5 pixels on all sides
.f configure -padding "5 10"      ;# 5 on left and right, 10 on top and bottom
.f configure -padding "5 7 10 12" ;# left: 5, top: 7, right: 10, bottom: 12
f['padding'] = '5'          ;# 5 pixels on all sides
f['padding'] = '5 10'       ;# 5 on left and right, 10 on top and bottom
f['padding'] = '5 7 10 12'  ;# left: 5, top: 7, right: 10, bottom: 12
$f->configure(-padding => "5");         # 5 pixels on all sides
$f->configure(-padding => "5 10");      # 5 on left and right, 10 on top and bottom
$f->configure(-padding => "5 7 10 12"); # left: 5, top: 7, right: 10, bottom: 12

#Borders
frame['borderwidth'] = 2
frame['relief'] = 'sunken'
.frame configure -borderwidth 2 -relief sunken
frame['borderwidth'] = 2
frame['relief'] = 'sunken'
$frame->configure(-borderwidth => 2, -relief => "sunken");

#Styles
s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()
ttk::style configure Danger.TFrame -background red -borderwidth 5 -relief raised
grid [ttk::frame .f -width 200 -height 200 -style Danger.TFrame]
Tk::Tile::Style.configure('Danger.TFrame', "background" => "red", "borderwidth" => 5, "relief" => "raised")
f = Tk::Tile::Frame.new(root) {width 200; height 200; style "Danger.TFrame"}.grid()
Tkx::ttk__style_configure("Danger.TFrame", -background => "red", -borderwidth => 5, -relief => "raised");
my $f = $mw->new_ttk__frame(-width => 200, -height => 200, -style => "Danger.TFrame")->g_grid();
#

"""