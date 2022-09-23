# Title: Python GUI Programming With TKinter - Widgets - LABELS
# Author: C. S. Germany 02/05/2022

# To Justify text in labels:
# justify=TK.CENTER
# justify=TK.LEFT
# justify=TK.RIGHT


# LINK = https://realpython.com/python-gui-tkinter/



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Adding a label. To do so, instantiate a TK.Label and associate it with a variable. Then call the pack() method to add it to the Window.
def Basic_Window():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("450x300");
    Hello = TK.Label(text="Hello, MOTO!");
    Hello.pack(); #adds to Window
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


# Note: Calling window.mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses. 
# It blocks any code that comes after it from running until you close the window where you called the method. 

# Widget Classes
# Label	= A widget used to display text OR images on the screen
# Button = A button that can contain text and can perform an action when clicked
# Entry = A text entry widget that allows only a single line of text
# Text = A text entry widget that allows multiline text entry
# Frame = A rectangular region used to group related widgets or provide padding between widgets
# Note: There are CLASSIC widgets and THEMED widgets


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting attributes of a label
def Label_1_Basic():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x500");    

    Label1 = TK.Label( text="When the last eagle flies.",
                       font=("Comic Sans MS", 20, "bold"),
                       foreground="white",
                       background="black",
                       width=40,
                       height=3  
                     );

    Label2 = TK.Label( text="Over the last crumbling mountain.",
                       font=("Comic Sans MS", 20, "bold"),    
                       fg="pink", #shorthand
                       bg="white", #shorthand
                       width=40,
                       height=3                        
                     );
                     
    Label3 = TK.Label( text="And the last lion roars.",
                       font=("Comic Sans MS", 20, "bold"),
                       foreground="#FFFFFF",
                       background="#34A2FE",
                       width=40,
                       height=3                         
                     );  

    Label4 = TK.Label( text="At the last dusty fountain.",
                       font=("Comic Sans MS", 20, "bold"),
                       foreground="#000000",
                       background="#FFFFFF",
                       width=40,
                       height=3                         
                     );                                                          

    Label1.pack();
    Label2.pack();
    Label3.pack();
    Label4.pack();
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Using PhotoImage class = only supports GIF and PGM/PPM formats.
def Label_2_Pictures():
    import tkinter as TK;

    window = TK.Tk();
    window.title("Label Images with tkinter PhotoImage - ONLY works with GIF");
    window.geometry("600x500");    

    The_IMAGE = TK.PhotoImage(file='Twilight_Sparkle_Animated_1.gif');

    Label_PICTURE = TK.Label( font=("Comic Sans MS", 20, "bold"),
                              foreground="white",
                              background="black",
                              width=40,
                              height=3  
                            );

    Label_PICTURE['image'] = The_IMAGE;
    Label_PICTURE['width'] = 300;
    Label_PICTURE['height'] = 300;                    

    Label_Title_1 = TK.Label( text="Displaying a GIF PICTURE with tkinter PhotoImage().",
                              font=("Comic Sans MS", 15),
                              foreground="white",
                              background="black",
                              width=100,
                              height=20  
                            ); 
                                            
    Label_PICTURE.pack();
    Label_Title_1.pack();
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------





#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ImageTk and Image classes from PIL(photo imaging Library) package = supports more generalized formats are JPEG/JPG and PNG
# Example:  from PIL import ImageTk,Image
def Label_3_Pictures():
    import tkinter as TK;
    from PIL import ImageTk,Image;

    window = TK.Tk();
    window.title("Label Images with PIL ImageTk and Image - works with JPG and PNG too");
    window.geometry("800x600");    

    The_IMAGE = Image.open("Twilight_Sparkle_Animated_1.gif");
    The_IMAGE = The_IMAGE.resize((250, 250), Image.ANTIALIAS);
    The_IMAGE = ImageTk.PhotoImage(The_IMAGE);

    Label_Title_1 = TK.Label( text="Displaying a GIF PICTURE with PIL ImageTk and Image.",
                              font=("Comic Sans MS", 15),
                              foreground="white",
                              background="black",
                              width=100,
                              height=20  
                            );    

    Label_PICTURE = TK.Label( font=("Comic Sans MS", 20, "bold"),
                              foreground="white",
                              background="black",
                              width=250,
                              height=250  
                            );

    Label_PICTURE['image'] = The_IMAGE;                                                            
    Label_PICTURE.pack();
    Label_Title_1.pack();
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ImageTk and Image classes from PIL can also display JPG and PNG, whereas tkinter PhotoImage can't.
def Label_4_Pictures():
    import tkinter as TK;
    from PIL import ImageTk,Image;

    window = TK.Tk();
    window.title("Label Images with PIL ImageTk and Image - works with JPG and PNG too");
    window.geometry("800x600");    

    The_IMAGE1 = Image.open("Twilight_Sparkle_Animated_1.gif");
    The_IMAGE1 = The_IMAGE1.resize((150, 150), Image.ANTIALIAS);
    The_IMAGE1 = ImageTk.PhotoImage(The_IMAGE1);

    Label_PICTURE1 = TK.Label( image=The_IMAGE1,
                               font=("Comic Sans MS", 20, "bold"),
                               foreground="white",
                               background="black",
                               width=200,
                               height=200  
                            );

    The_IMAGE2 = Image.open("Twilight_Sparkle_2.jpg");
    The_IMAGE2 = The_IMAGE2.resize((150, 150), Image.ANTIALIAS);
    The_IMAGE2 = ImageTk.PhotoImage(The_IMAGE2);

    Label_PICTURE2 = TK.Label( image=The_IMAGE2,
                               font=("Comic Sans MS", 20, "bold"),
                               foreground="white",
                               background="black",
                               width=200,
                               height=200  
                            );                            

    The_IMAGE3 = Image.open("RainbowDash_1.png");
    The_IMAGE3 = The_IMAGE3.resize((175, 175), Image.ANTIALIAS);
    The_IMAGE3 = ImageTk.PhotoImage(The_IMAGE3);

    Label_PICTURE3 = TK.Label( image=The_IMAGE3,
                               font=("Comic Sans MS", 20, "bold"),
                               foreground="white",
                               background="black",
                               width=250,
                               height=250  
                            );  

    Label_PICTURE1.pack();
    Label_PICTURE2.pack();
    Label_PICTURE3.pack();
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



def Test():
    import tkinter as TK;
    from PIL import ImageTk,Image;
    window = TK.Tk();  
    The_IMAGE2 = Image.open("Twilight_Sparkle_2.jpg");
    The_IMAGE2 = The_IMAGE2.resize((150, 150), Image.ANTIALIAS);
    The_IMAGE2 = ImageTk.PhotoImage(The_IMAGE2);

    Label_PICTURE2 = TK.Label( image=The_IMAGE2,
                               font=("Comic Sans MS", 20, "bold"),
                               foreground="white",
                               background="black",
                               width=200,
                               height=200  
                            );                      
    Label_PICTURE2.pack();
    window.mainloop();


#-----Invocations-----
#Basic_Window();
#Label_1_Basic();
#Label_2_Pictures();
#Label_3_Pictures();
#Label_4_Pictures();
Test();





"""

#Creating
label = ttk.Label(parent, text='Full name:')
Labels are created using the ttk::label command. Often, the text or image the label will display are specified via configuration options at the same time:

ttk::label .label -text {Full name:}
Labels are created using the Tk::Tile::Label class. Often, the text or image the label will display are specified via configuration options at the same time:

label = Tk::Tile::Label.new(parent) {text 'Full name:'}
Labels are created using the new_ttk__label method, a.k.a. Tkx::ttk__label(). Often, the text or image the label will display are specified via configuration options at the same time:

$label = $parent->new_ttk__label(-text => "Full name:");


#Displaying Text
resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')

.label configure -textvariable resultContents
set resultContents "New value to display"

$resultsVar = TkVariable.new
label['textvariable'] = $resultsVar
$resultsVar.value = 'New value to display'

$label->configure(-textvariable => \$resultContents);
$resultContents = "New value to display";


#Displaying Images

image = PhotoImage(file='myimage.gif')
label['image'] = image
image create photo imgobj -file "myimage.gif"
.label configure -image imgobj
image = TkPhotoImage.new(:file => "myimage.gif")
label['image'] = image
Tkx::image_create_photo( "imgobj", -file => "myimage.gif");
$label->configure(-image => "imgobj");


#Fonts, Colors, and More

TkDefaultFont:
Default for all GUI items not otherwise specified.
TkTextFont:
Used for entry widgets, listboxes, etc.
TkFixedFont:
A standard fixed-width font.
TkMenuFont:
The font used for menu items.
TkHeadingFont:
A font for column headings in lists and tables.
TkCaptionFont:
A font for window and dialog caption bars.
TkSmallCaptionFont:
Smaller captions for subwindows or tool dialogs.
TkIconFont:
A font for icon captions.
TkTooltipFont:
A font for tooltips.

label['font'] = "TkDefaultFont"
.label configure -font TkDefaultFont
label['font'] = "TkDefaultFont"
$label->configure(-font => "TkDefaultFont");

"""






#Basic Images
"""

from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="ball.ppm")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()   

"""