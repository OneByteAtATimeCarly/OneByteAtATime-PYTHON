# Title: Python GUI Programming With TKinter - Widgets - CANVAS Objects
# Author: C. S. Germany 02/05/2022

# Canvas Objects. Manages a 2D collection of graphical objects — lines, circles, text, images, other widgets, and more.
# You can embed other widgets inside of Canvas objects.

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ARC
def Canvas_01_ARC():
    import tkinter as TK;

    window = TK.Tk();
    window.title("Canvas Widget - ARC - example 01");
    window.geometry("400x400");    

    CNV_Canvas1 = TK.Canvas(window, bg="blue", height=250, width=300);

    TUP_Coordinates = (10, 50, 240, 210);
    ARC = CNV_Canvas1.create_arc(TUP_Coordinates, start=0, extent=150, fill="red");

    CNV_Canvas1.pack() 
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LINE
def Canvas_02_LINE():
    import tkinter as TK;

    window = TK.Tk();
    window.title("Canvas Widget - ARC - example 01");
    window.geometry("430x300");    

    CNV_Canvas1 = TK.Canvas(window, bg="blue", height=270, width=400);
    CNV_Canvas1.place(x=10, y=10);

    # Creates a lines of 300 (straight vertical dashed line)
    LINE1 = CNV_Canvas1.create_line(300, 35, 300, 200, dash = (5, 2), fill='red');
         
    # Creates a triangle
    LINE2 = CNV_Canvas1.create_line(55, 85, 155, 85, 105, 180, 55, 85, fill='white');
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# RECTANGLE
def Canvas_03_RECTANGLE():
    import tkinter as TK;

    window = TK.Tk();
    window.title("Canvas Widget - ARC - example 01");
    window.geometry("430x300");    

    CNV_Canvas1 = TK.Canvas(window, bg="blue", height=270, width=400);
    CNV_Canvas1.place(x=10, y=10);

    # Creates RECTANGLEs
    RECTANGLE1 = CNV_Canvas1.create_rectangle(50,100,200,50,fill="blue");
    RECTANGLE1 = CNV_Canvas1.create_rectangle(200,250,350,200,fill="yellow");
        
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# POLYGON
def Canvas_04_POLYGON():
    import tkinter as TK;

    window = TK.Tk();
    window.title("Canvas Widget - ARC - example 01");
    window.geometry("430x300");    

    CNV_Canvas1 = TK.Canvas(window, bg="blue", height=270, width=400);
    CNV_Canvas1.place(x=10, y=10);

    #Define coordinartes in an array
    PolyPoints = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200];

    # Create Polygon
    POLYGON1 = CNV_Canvas1.create_polygon(PolyPoints, outline='red',fill='white', width=5);
        
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



# Images directly on Window Background with TK.Canvas

#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ImageTk and Image classes from PIL(photo imaging Library) package = supports more generalized formats are JPEG/JPG and PNG
# Example:  from PIL import ImageTk,Image
def Window_Display_Image_On_Background_GIF():
    import tkinter as TK;
    from PIL import ImageTk,Image;

    window = TK.Tk();
    window.title("Drawing Image on Window background with PIL ImageTk and Image - works with JPG and PNG too");
    window.geometry("800x650");    

    The_IMAGE = Image.open("Twilight_Sparkle_Animated_1.gif");
    The_IMAGE = The_IMAGE.resize((300,300), Image.ANTIALIAS);
    The_IMAGE = ImageTk.PhotoImage(The_IMAGE);

    WindowBG = TK.Canvas(window,width=500,height=500);
    WindowBG.create_image(300,300,image=The_IMAGE);
    WindowBG.pack();

    Label_Title_1 = TK.Label( text="Drawing GIF Image with PIL ImageTk and Image directly on window background.",
                              font=("Comic Sans MS", 15),
                              foreground="white",
                              background="black",
                              width=100,
                              height=20  
                            );    
               
    Label_Title_1.pack();
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ImageTk and Image classes from PIL(photo imaging Library) package = supports more generalized formats are JPEG/JPG and PNG
# Example:  from PIL import ImageTk,Image
def Window_Display_Image_On_Background_JPG():
    import tkinter as TK;
    from PIL import ImageTk,Image;

    window = TK.Tk();
    window.title("Drawing Image on Window background with PIL ImageTk and Image - works with JPG and PNG too");
    window.geometry("800x650");    

    The_IMAGE = Image.open("Twilight_Sparkle_2.jpg");
    The_IMAGE = The_IMAGE.resize((300,300), Image.ANTIALIAS);
    The_IMAGE = ImageTk.PhotoImage(The_IMAGE);

    WindowBG = TK.Canvas(window,width=500,height=500);
    WindowBG.create_image(300,300,image=The_IMAGE);
    WindowBG.pack();

    Label_Title_1 = TK.Label( text="Drawing JPG Image with PIL ImageTk and Image directly on window background.",
                              font=("Comic Sans MS", 15),
                              foreground="white",
                              background="black",
                              width=100,
                              height=20  
                            );    
               
    Label_Title_1.pack();
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ImageTk and Image classes from PIL(photo imaging Library) package = supports more generalized formats are JPEG/JPG and PNG
# Example:  from PIL import ImageTk,Image
def Window_Display_Image_On_Background_PNG():
    import tkinter as TK;
    from PIL import ImageTk,Image;

    window = TK.Tk();
    window.title("Drawing Image on Window background with PIL ImageTk and Image - works with JPG and PNG too");
    window.geometry("800x650");    

    The_IMAGE = Image.open("RainbowDash_1.png");
    The_IMAGE = The_IMAGE.resize((300,300), Image.ANTIALIAS);
    The_IMAGE = ImageTk.PhotoImage(The_IMAGE);

    WindowBG = TK.Canvas(window,width=500,height=500);
    WindowBG.create_image(300,300,image=The_IMAGE);
    WindowBG.pack();

    Label_Title_1 = TK.Label( text="Drawing PNG Image with PIL ImageTk and Image directly on window background.",
                              font=("Comic Sans MS", 15),
                              foreground="white",
                              background="black",
                              width=100,
                              height=20  
                            );    
               
    Label_Title_1.pack();
    
    window.mainloop();
# ------------------------------------------------------------------------------------------------------------------------------------



#-----Invocations-----
#Canvas_01_ARC();
#Canvas_02_LINE();
#Canvas_03_RECTANGLE();
Canvas_04_POLYGON();

#Loading GIF, JOG and PNG Images on a Canvas
#Window_Display_Image_On_Background_GIF();
#Window_Display_Image_On_Background_JPG();
#Window_Display_Image_On_Background_PNG();


