#Title: Coin Toss (Threaded version with sound)
#Author: Carly S. Germany
#Created: 02/15/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

#Note: PlaySound is a very simple module that can play WAV files and MP3s in Python. 
# The FIRST time you want to use Python's PlaySound module, you must install it into your IDE using:
# Example: pip install playsound
# Then RESTART Visual Studio Code or terminal.
# Then just import it with: from playsound import playsound

#Note: To keep game and GUI responsive when you call playsound, you must play each sound in a different thread from mainloop().
      # Also, the new version of playsound is broken and doesn't work right with multi-threading. Old version is better. To remedy this:
      # pip uninstall playsound
      # pip install playsound==1.2.2

#Function------------------------------------------------------------------------------------------------------------------------------------------------------------------
def GUI_Interface():
    import tkinter as tk;
    from PIL import ImageTk,Image;
    import random;
    from playsound import playsound;
    import threading; #Nescessary to spawn processes in Python THREADS

    #1. Build main interface Window and dynamically size it to display
    window = tk.Tk();
    window_Width = 528;
    window_Height = 541;
    window.title("GUI tkinter Coin Toss App 1.0 - 05/13/2-22 Carly Salali Germany");
    ScreenWidth = window.winfo_screenwidth();
    ScreenHeight = window.winfo_screenheight();
    Appear_in_the_Middle = '%dx%d+%d+%d' % (window_Width, window_Height, (ScreenWidth - window_Width) / 2, (ScreenHeight - window_Height) / 2);
    window.geometry(Appear_in_the_Middle);
    window.resizable(width=False, height=False);
    window.configure(bg='white');  

    #2. Setup Image objects for label to display
    Coin_TOSS_IMAGE = Image.open("Coin_TOSS.jpg");
    Coin_TOSS_IMAGE = Coin_TOSS_IMAGE.resize((320, 320), Image.ANTIALIAS);
    Coin_TOSS_IMAGE = ImageTk.PhotoImage(Coin_TOSS_IMAGE);

    Coin_HEAD_IMAGE = Image.open("Coin_HEADS.jpg");
    Coin_HEAD_IMAGE = Coin_HEAD_IMAGE.resize((300, 300), Image.ANTIALIAS);
    Coin_HEAD_IMAGE = ImageTk.PhotoImage(Coin_HEAD_IMAGE);

    Coin_TAIL_IMAGE = Image.open("Coin_TAILS.jpg");
    Coin_TAIL_IMAGE = Coin_TAIL_IMAGE.resize((300, 300), Image.ANTIALIAS);
    Coin_TAIL_IMAGE = ImageTk.PhotoImage(Coin_TAIL_IMAGE);
    
    #Globals
    Total_HEADS = 0;
    Total_TAILS = 0;

    #3. Event Handler for Toss Button
    def BTN_Toss_command():
        nonlocal Total_HEADS; #scopes into global vaiable outside this function
        nonlocal Total_TAILS; #scopes into global vaiable outside this function      
        LUCK = random.randint(0,1);
        if(LUCK == 0): 
           LAB_Coin['image'] = Coin_HEAD_IMAGE;
           Total_HEADS += 1;
           LAB_Num_Heads["text"] = "HEADS: " + str(Total_HEADS);
        else:
             LAB_Coin['image'] = Coin_TAIL_IMAGE;
             Total_TAILS += 1;
             LAB_Num_Tails["text"] = "TAILS: " + str(Total_TAILS);
        
        print("HEADS:",Total_HEADS,"     TAILS:",Total_TAILS);
        threading.Thread(target=playsound, args=('CoinToss.wav',), daemon=True).start(); 

    #4. Add tkinter Widgets to New Window
    LAB_Title = tk.Label(window);
    LAB_Title["borderwidth"] = "0px";
    LAB_Title["font"] = ("Arial Black", 20, "normal");
    LAB_Title["justify"] = "center";
    LAB_Title["background"] = "white";
    LAB_Title["foreground"] = "black"; 
    LAB_Title["text"] = "Coin Toss 1.0";
    LAB_Title.place(x=40,y=0,width=445,height=30);

    BTN_Toss = tk.Button(window);
    BTN_Toss["font"] = ("Comic Sans MS", 20, "bold");
    BTN_Toss["justify"] = "center";
    BTN_Toss["background"] = "red";
    BTN_Toss["foreground"] = "white"; 
    BTN_Toss["text"] = "TOSS";
    BTN_Toss["command"] = BTN_Toss_command;
    BTN_Toss.place(x=82,y=405,width=359,height=64);                     

    LAB_Coin = tk.Label(window);
    LAB_Coin['image'] = Coin_TOSS_IMAGE; 
    LAB_Coin["relief"] = "solid";
    LAB_Coin["borderwidth"] = "5px";
    LAB_Coin["font"] = ("Arial Black", 12, "normal");
    LAB_Coin["justify"] = "center";
    LAB_Coin["background"] = "white";
    LAB_Coin["foreground"] = "black"; 
    LAB_Coin["text"] = "Coin Image";
    LAB_Coin.place(x=70,y=45,width=385,height=345);                       

    LAB_Num_Heads = tk.Label(window);
    LAB_Num_Heads["borderwidth"] = "0px";
    LAB_Num_Heads["font"] = ("Arial Black", 10, "normal");
    LAB_Num_Heads["justify"] = "center";
    LAB_Num_Heads["background"] = "white";
    LAB_Num_Heads["foreground"] = "black"; 
    LAB_Num_Heads["text"] = "HEADS: 0";
    LAB_Num_Heads.place(x=1,y=490,width=150,height=30);

    LAB_Num_Tails = tk.Label(window);
    LAB_Num_Tails["borderwidth"] = "0px";
    LAB_Num_Tails["font"] = ("Arial Black", 10, "normal");
    LAB_Num_Tails["justify"] = "center";
    LAB_Num_Tails["background"] = "white";
    LAB_Num_Tails["foreground"] = "black"; 
    LAB_Num_Tails["text"] = "TAILS: 0";
    LAB_Num_Tails.place(x=380,y=490,width=150,height=30);                            

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----Invocations-----
GUI_Interface();


