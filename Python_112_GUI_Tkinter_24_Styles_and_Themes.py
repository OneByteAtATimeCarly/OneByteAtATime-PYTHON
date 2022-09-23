# Title: Python GUI Programming With TKinter - Widgets - STYLES and THEMES
# Author: C. S. Germany 02/05/2022

# Styles = Each widget in tkinter can have a specific style. Many styles can be active at once.
# Themes = Are collections of styles, collectively applies to widgets. Only 1 theme can be active at at time.

# Built-in Themes Are: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Listing available themes
def Theme_01_Get_Available_Themes():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Styles and Themes");
    window.geometry("700x150");
    window.configure(bg='white'); 

    #Get available theme styles
    thm = ttk.Style();
    THEMES = thm.theme_names();
    MESSAGE1 = "Available themes are:\n\n" + str(THEMES);
    print(MESSAGE1);

    #Get current theme
    CurrentTheme = thm.theme_use();
    MESSAGE2 = "\n\nCurrent THEME = " + CurrentTheme;
    print(MESSAGE2);

    Final_Message = MESSAGE1 + MESSAGE2;

    LAB_Output = TK.Label(window,font=("Comic Sans MS", 12), background="white", foreground="black",text=Final_Message); 
    LAB_Output.place(x=10,y=10,width=690,height=140);
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting a theme
def Theme_02_Setting_A_Theme():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Styles and Themes");
    window.geometry("570x250");
    window.configure(bg='white'); 

    #Set new them
    thm = ttk.Style();
    Old_Theme_Default = CurrentTheme = thm.theme_use();
    thm.theme_use('clam');
    New_Theme = thm.theme_use();
    MESSAGE1 = "Old default theme: " + Old_Theme_Default + "\nNew modified theme: " + New_Theme;

    LAB_Output = TK.Label(window,font=("Comic Sans MS", 30), background="white", foreground="black",text="Setting a Theme!", borderwidth=3, relief="solid", justify= TK.CENTER); 
    LAB_Output.place(x=10,y=10,width=550,height=100);

    LAB_Theme = TK.Label(window,font=("Comic Sans MS", 12), background="white", foreground="black",text=MESSAGE1, justify= TK.LEFT); 
    LAB_Theme.place(x=20,y=155,width=250,height=45);    

    BTN_Start = TK.Button(window,font=("Comic Sans MS", 20), background="red", foreground="white",text="BUTTON"); 
    BTN_Start.place(x=340,y=130,width=200,height=100);  
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Downloading and importing a custom theme
def Theme_03_Downloading_And_Setting_A_Custom_Theme():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Styles and Themes");
    window.geometry("570x250");
    window.configure(bg='white'); 
    
    #FIRST, find your custom theme package and download it. Extract it. Then:
    #Load and set custom downloaded theme
    window.tk.call('lappend', 'auto_path', "D:/Bills/Carlys_Python_Scripts_2022/GUI_Python_Programming/Themes/awthemes-10.4.0");
    window.tk.call('package', 'require', 'awdark');

    #Set new them
    thm = ttk.Style();
    Old_Theme_Default = CurrentTheme = thm.theme_use();
    thm.theme_use('awdark');
    New_Theme = thm.theme_use();
    MESSAGE1 = "Old default theme: " + Old_Theme_Default + "\nNew modified theme: " + New_Theme;

    LAB_Output = TK.Label(window,font=("Comic Sans MS", 30), background="white", foreground="black",text="Setting a Theme!", borderwidth=3, relief="solid", justify= TK.CENTER); 
    LAB_Output.place(x=10,y=10,width=550,height=100);

    LAB_Theme = TK.Label(window,font=("Comic Sans MS", 12), background="white", foreground="black",text=MESSAGE1, justify= TK.LEFT); 
    LAB_Theme.place(x=20,y=155,width=250,height=45);    

    BTN_Start = TK.Button(window,font=("Comic Sans MS", 20), background="red", foreground="white",text="BUTTON"); 
    BTN_Start.place(x=340,y=130,width=200,height=100);  
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Getting and Setting a style
def Theme_04_Getting_Current_Style():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Styles and Themes");
    window.geometry("570x260");
    window.configure(bg='white'); 

    LAB_Output = TK.Label(window,font=("Comic Sans MS", 30), background="white", foreground="black",text="Setting a Theme!", borderwidth=3, relief="solid", justify= TK.CENTER); 
    LAB_Output.place(x=10,y=10,width=550,height=110);

    LAB_Style = TK.Label(window,font=("Comic Sans MS", 10), background="white", foreground="black",text="nada", justify= TK.LEFT); 
    LAB_Style.place(x=00,y=135,width=300,height=120);    

    BTN_Start = TK.Button(window,font=("Comic Sans MS", 20), background="red", foreground="white",text="BUTTON"); 
    BTN_Start.place(x=340,y=130,width=200,height=100);  

    #Get current style and set to new one
    Current_BTN_Style = BTN_Start.winfo_class();
    Current_LAB_Output_Style = LAB_Output.winfo_class();
    Current_LAB_Style_Style = LAB_Style.winfo_class();

    MESSAGE1 = "Button Old: " + Current_BTN_Style + "\n" + \
               "Label Output: " + Current_LAB_Output_Style + "\n" + \
               "Label Style: " + Current_LAB_Style_Style + "\n";

    LAB_Style['text'] = MESSAGE1; 
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting a style
def Theme_05_Getting_ttk_Style():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Styles and Themes");
    window.geometry("570x260");
    window.configure(bg='white'); 

    #Note: To get TButton and TLabel we must create labels and buttons from ttk. and NOT TK.
    LAB_Output = ttk.Label(window,font=("Comic Sans MS", 30), background="white", foreground="black",text="Setting a Theme!", borderwidth=3, relief="solid", justify= TK.CENTER); 
    LAB_Output.place(x=10,y=10,width=550,height=110);

    LAB_Style = ttk.Label(window,font=("Comic Sans MS", 12), background="white", foreground="black",text="nada", justify=TK.LEFT); 
    LAB_Style.place(x=50,y=125,width=300,height=120);    

    BTN_Start = ttk.Button(window, text="BUTTON"); 
    BTN_Start.place(x=340,y=130,width=200,height=100);  

    #Get current style and set to new one
    Current_BTN_Style = BTN_Start.winfo_class();
    Current_LAB_Output_Style = LAB_Output.winfo_class();
    Current_LAB_Style_Style = LAB_Style.winfo_class();

    MESSAGE1 = "Button Old: " + Current_BTN_Style + "\n" + \
               "Label Output: " + Current_LAB_Output_Style + "\n" + \
               "Label Style: " + Current_LAB_Style_Style + "\n";

    LAB_Style['text'] = MESSAGE1; 
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Setting a style
def Theme_06_Setting_ttk_Style():
    import tkinter as TK;
    from tkinter import ttk;
    window = TK.Tk();
    window.title("tkinter Styles and Themes");
    window.geometry("570x260");
    window.configure(bg='white'); 

    #Note: To get TButton and TLabel we must create labels and buttons from ttk. and NOT TK.
    LAB_Output = ttk.Label(window,font=("Comic Sans MS", 30), background="white", foreground="black",text="Setting a Theme!", borderwidth=3, relief="solid", justify= TK.CENTER); 
    LAB_Output.place(x=10,y=10,width=550,height=110);

    LAB_Style = ttk.Label(window,font=("Comic Sans MS", 12), background="white", foreground="black",text="nada", justify=TK.LEFT); 
    LAB_Style.place(x=50,y=125,width=300,height=120);    

    BTN_Start = ttk.Button(window, text="BUTTON", style='Emergency.TButton'); 
    BTN_Start.place(x=340,y=130,width=200,height=100);  

    #Get current style and set to new one
    Current_BTN_Style = BTN_Start.winfo_class();
    Current_LAB_Output_Style = LAB_Output.winfo_class();
    Current_LAB_Style_Style = LAB_Style.winfo_class();

    MESSAGE1 = "Button Old: " + Current_BTN_Style + "\n" + \
               "Label Output: " + Current_LAB_Output_Style + "\n" + \
               "Label Style: " + Current_LAB_Style_Style + "\n";

    LAB_Style['text'] = MESSAGE1; 
    
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Invocations
#Theme_01_Get_Available_Themes();
#Theme_02_Setting_A_Theme();
#Theme_03_Downloading_And_Setting_A_Custom_Theme();
#Theme_04_Getting_Current_Style();
#Theme_05_Getting_ttk_Style();
Theme_06_Setting_ttk_Style();




