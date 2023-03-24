#Title: Calculator (using Python and tkinter GUI)
#Author: Carly S. Germany
#Created: 03/05/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

#Globals  (make accessible to nested child and parent functions)
Num_1 = 0.0;
Num_2 = 0.0;
Operation = "";
Is_Next_Expression = "False";
Need_To_Clear = "False";
Clicked_Equals = "False";
Final_Output = "False";
Add_Space = "False";

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Initalize():
    globals()['Num_1'] = 0.0;
    globals()['Num_2'] = 0.0;
    globals()['Operation'] = "";
    globals()['Is_Next_Expression'] = "False";
    globals()['Need_To_Clear'] = "False";
    globals()['Clicked_Equals'] = "False";
    globals()['Final_Output'] = "False";
    globals()['Add_Space'] = "False";     
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Calculator_GUI_Interface():
    import tkinter as tk;
    from tkinter import ttk;
    import tkinter.font as tkFont
    from tkinter.ttk import Style;
    import math;

    Short_Term_Memory = "";

    #1. Build main interface Window and dynamically size it to display
    window = tk.Tk();
    window_Width = 528;
    window_Height = 570;
    window.title("Python tkinter - Calculator 1.0 - 2022 - Carly Salali Germany");
    ScreenWidth = window.winfo_screenwidth();
    ScreenHeight = window.winfo_screenheight();
    Appear_in_the_Middle = '%dx%d+%d+%d' % (window_Width, window_Height, (ScreenWidth - window_Width) / 2, (ScreenHeight - window_Height) / 2);
    window.geometry(Appear_in_the_Middle);
    window.resizable(width=False, height=False);
    window.configure(bg='white');  

    VAR_Output = tk.StringVar();

    #2. Event Handlers for Buttons

    def Key_Number(The_Number):
        if(globals()['Need_To_Clear'] == "True"):
           VAR_Output.set("");  
           globals()['Need_To_Clear'] = "False";

        Current_Value = VAR_Output.get();
        VAR_Output.set(Current_Value + The_Number);

        if(globals()['Add_Space'] == "True"):
           LAB_Expression["text"] = LAB_Expression.cget("text") + " " + The_Number;
           globals()['Add_Space'] = "False";  
        elif(globals()['Add_Space'] == "False"):
             LAB_Expression["text"] = LAB_Expression.cget("text") + The_Number; 


    def BTN_7_command():
        Key_Number("7");      

    def BTN_8_command():
        Key_Number("8");

    def BTN_9_command():
        Key_Number("9");

    def BTN_4_command():
        Key_Number("4");    

    def BTN_5_command():
        Key_Number("5");

    def BTN_6_command():
        Key_Number("6");

    def BTN_1_command():
        Key_Number("1");

    def BTN_2_command():
        Key_Number("2");

    def BTN_3_command():
        Key_Number("3");

    def BTN_0_command():
        Key_Number("0");

    def BTN_Decimal_command():
        Key_Number(".");

    def BTN_CE_command():
        VAR_Output.set("");
        LAB_Expression["text"] = "";
        Initalize();         

    def BTN_ADD_command():
        Calculate("+");

    def BTN_SUBTRACT_command():
        Calculate("-");

    def BTN_MULTIPLY_command():
        Calculate("*");

    def BTN_DIVIDE_command():
        Calculate("/");

    def BTN_Sq_Rt_command():
        The_Number = VAR_Output.get();
        Digi_Num = float(The_Number);
        Sqr_Root_Value = math.sqrt(Digi_Num);
        LAB_Expression["text"] = "The Square Root of " + The_Number + " = " + str(Sqr_Root_Value); 
        VAR_Output.set(str(Sqr_Root_Value));

    def BTN_Cube_command():
        The_Number = VAR_Output.get();
        Digi_Num = float(The_Number);
        Cube_Value = Digi_Num * Digi_Num * Digi_Num;
        LAB_Expression["text"] = "The Cube of " + The_Number + " = " + str(Cube_Value); 
        VAR_Output.set(str(Cube_Value));

    def BTN_EQUALS_command():
        Math_EQUALS();

    def BTN_Farenheit_command():
        The_Number = VAR_Output.get();
        Digi_Num = float(The_Number);
        Farenheit = (Digi_Num * 9 / 5) + 32;
        LAB_Expression["text"] = The_Number + " degrees Celcius = " + str(Farenheit) + " degrees Farenheit"; 
        VAR_Output.set(str(Farenheit));

    def BTN_Celcius_command():
        The_Number = VAR_Output.get();
        Digi_Num = float(The_Number);
        Celcius = ((Digi_Num - 32) * 5) / 9;
        LAB_Expression["text"] = The_Number + " degrees Farenheit = " + str(Celcius) + " degrees Celcius"; 
        VAR_Output.set(str(Celcius));

    def BTN_Mem_Add_command():
        global Short_Term_Memory;
        Short_Term_Memory = VAR_Output.get();

    def BTN_Mem_Recall_command():
        global Short_Term_Memory;
        VAR_Output.set(Short_Term_Memory); 

    def BTN_Mem_Clear_command():
        global Short_Term_Memory;
        Short_Term_Memory = ""; 
                   

    #3. Add tkinter Widgets to New Window
    LAB_Expression = tk.Label(window);
    LAB_Expression["borderwidth"] = "2px";
    LAB_Expression["relief"] = "solid";
    LAB_Expression["font"] = ("Arial", 10, "normal");
    LAB_Expression["justify"] = "left";
    LAB_Expression["background"] = "white";
    LAB_Expression["foreground"] = "black";
    LAB_Expression["text"] = "Expressions Go Here";          
    LAB_Expression.place(x=10,y=0,width=507,height=30);

    ENT_Output = tk.Entry(window);
    ENT_Output["textvariable"] = VAR_Output;
    ENT_Output["borderwidth"] = "3px";
    ENT_Output["font"] = ("Lucida Console", 25, "normal");
    ENT_Output["justify"] = "right";
    #ENT_Output["background"] = "grey";
    ENT_Output["foreground"] = "black";         
    ENT_Output.place(x=10,y=50,width=507,height=67);
    #ENT_Output.focus();
    VAR_Output.set("");

    BTN_7 = tk.Button(window);
    BTN_7["font"] = ("Arial Black", 38, "normal");
    BTN_7["justify"] = "center";
    BTN_7["background"] = "blue";
    BTN_7["foreground"] = "white";    
    BTN_7["text"] = "7";
    BTN_7.place(x=50,y=130,width=75,height=75);
    BTN_7["command"] = BTN_7_command;

    BTN_8 = tk.Button(window);
    BTN_8["font"] = ("Arial Black", 38, "normal");
    BTN_8["justify"] = "center";
    BTN_8["background"] = "blue";
    BTN_8["foreground"] = "white";  
    BTN_8["text"] = "8";
    BTN_8.place(x=130,y=130,width=75,height=75);
    BTN_8["command"] = BTN_8_command;

    BTN_9 = tk.Button(window);
    BTN_9["font"] = ("Arial Black", 38, "normal");
    BTN_9["justify"] = "center";
    BTN_9["background"] = "blue";
    BTN_9["foreground"] = "white";  
    BTN_9["text"] = "9";
    BTN_9.place(x=210,y=130,width=75,height=75);
    BTN_9["command"] = BTN_9_command;

    BTN_4 = tk.Button(window);
    BTN_4["font"] = ("Arial Black", 38, "normal");
    BTN_4["justify"] = "center";
    BTN_4["background"] = "blue";
    BTN_4["foreground"] = "white"; 
    BTN_4["text"] = "4";
    BTN_4.place(x=50,y=210,width=75,height=75);
    BTN_4["command"] = BTN_4_command;   

    BTN_5 = tk.Button(window);
    BTN_5["font"] = ("Arial Black", 38, "normal");
    BTN_5["justify"] = "center";
    BTN_5["background"] = "blue";
    BTN_5["foreground"] = "white"; 
    BTN_5["text"] = "5";
    BTN_5.place(x=130,y=210,width=75,height=75);
    BTN_5["command"] = BTN_5_command;

    BTN_6 = tk.Button(window);
    BTN_6["font"] = ("Arial Black", 38, "normal");
    BTN_6["justify"] = "center";
    BTN_6["background"] = "blue";
    BTN_6["foreground"] = "white"; 
    BTN_6["text"] = "6";
    BTN_6.place(x=210,y=210,width=75,height=75);
    BTN_6["command"] = BTN_6_command;

    BTN_1 = tk.Button(window);
    BTN_1["font"] = ("Arial Black", 38, "normal");
    BTN_1["justify"] = "center";
    BTN_1["background"] = "blue";
    BTN_1["foreground"] = "white"; 
    BTN_1["text"] = "1";
    BTN_1.place(x=50,y=290,width=75,height=75);
    BTN_1["command"] = BTN_1_command;

    BTN_2 = tk.Button(window);
    BTN_2["font"] = ("Arial Black", 38, "normal");
    BTN_2["justify"] = "center";
    BTN_2["background"] = "blue";
    BTN_2["foreground"] = "white"; 
    BTN_2["text"] = "2";
    BTN_2.place(x=130,y=290,width=75,height=75);
    BTN_2["command"] = BTN_2_command;

    BTN_3 = tk.Button(window);
    BTN_3["font"] = ("Arial Black", 38, "normal");
    BTN_3["justify"] = "center";
    BTN_3["background"] = "blue";
    BTN_3["foreground"] = "white"; 
    BTN_3["text"] = "3";
    BTN_3.place(x=210,y=290,width=75,height=75);
    BTN_3["command"] = BTN_3_command;

    BTN_0 = tk.Button(window);
    BTN_0["font"] = ("Arial Black", 38, "normal");
    BTN_0["justify"] = "center";
    BTN_0["background"] = "blue";
    BTN_0["foreground"] = "white"; 
    BTN_0["text"] = "0";
    BTN_0.place(x=50,y=370,width=75,height=75);
    BTN_0["command"] = BTN_0_command;

    BTN_Decimal = tk.Button(window);
    BTN_Decimal["font"] = ("Arial Black", 38, "normal");
    BTN_Decimal["justify"] = "center";
    BTN_Decimal["background"] = "blue";
    BTN_Decimal["foreground"] = "white"; 
    BTN_Decimal["text"] = ".";
    BTN_Decimal.place(x=130,y=370,width=75,height=75);
    BTN_Decimal["command"] = BTN_Decimal_command;

    BTN_CE = tk.Button(window);
    BTN_CE["font"] = ("Arial Black", 32, "normal");
    BTN_CE["justify"] = "center";
    BTN_CE["background"] = "blue";
    BTN_CE["foreground"] = "white"; 
    BTN_CE["text"] = "CE";
    BTN_CE.place(x=210,y=370,width=75,height=75);
    BTN_CE["command"] = BTN_CE_command;

    LAB_Mem = tk.Label(window);
    LAB_Mem["borderwidth"] = "0px";
    LAB_Mem["font"] = ("Comic Sans MS", 15, "normal");
    LAB_Mem["justify"] = "center";
    LAB_Mem["background"] = "white";
    LAB_Mem["foreground"] = "red";
    LAB_Mem["text"] = "Memory Functions";      
    LAB_Mem.place(x=65,y=460,width=200,height=30);

    BTN_Mem_Add = tk.Button(window);
    BTN_Mem_Add["font"] = ("Arial Black", 30, "normal");
    BTN_Mem_Add["justify"] = "center";
    BTN_Mem_Add["background"] = "blue";
    BTN_Mem_Add["foreground"] = "white"; 
    BTN_Mem_Add["text"] = "M+";
    BTN_Mem_Add.place(x=50,y=490,width=75,height=75);
    BTN_Mem_Add["command"] = BTN_Mem_Add_command;

    BTN_Mem_Recall  = tk.Button(window);
    BTN_Mem_Recall["font"] = ("Arial Black", 30, "normal");
    BTN_Mem_Recall["justify"] = "center";
    BTN_Mem_Recall["background"] = "blue";
    BTN_Mem_Recall["foreground"] = "white"; 
    BTN_Mem_Recall["text"] = "MR";
    BTN_Mem_Recall.place(x=130,y=490,width=75,height=75);
    BTN_Mem_Recall["command"] = BTN_Mem_Recall_command;

    BTN_Mem_Clear = tk.Button(window);
    BTN_Mem_Clear["font"] = ("Arial Black", 30, "normal");
    BTN_Mem_Clear["justify"] = "center";
    BTN_Mem_Clear["background"] = "blue";
    BTN_Mem_Clear["foreground"] = "white"; 
    BTN_Mem_Clear["text"] = "M-";
    BTN_Mem_Clear.place(x=210,y=490,width=75,height=75);
    BTN_Mem_Clear["command"] = BTN_Mem_Clear_command;     

    BTN_ADD = tk.Button(window);
    BTN_ADD["font"] = ("Arial Black", 38, "normal");
    BTN_ADD["justify"] = "center";
    BTN_ADD["background"] = "blue";
    BTN_ADD["foreground"] = "white"; 
    BTN_ADD["text"] = "+";
    BTN_ADD.place(x=320,y=130,width=75,height=75);
    BTN_ADD["command"] = BTN_ADD_command;

    BTN_SUBTRACT = tk.Button(window);
    BTN_SUBTRACT["font"] = ("Arial Black", 38, "normal");
    BTN_SUBTRACT["justify"] = "center";
    BTN_SUBTRACT["background"] = "blue";
    BTN_SUBTRACT["foreground"] = "white"; 
    BTN_SUBTRACT["text"] = "-";
    BTN_SUBTRACT.place(x=320,y=210,width=75,height=75);
    BTN_SUBTRACT["command"] = BTN_SUBTRACT_command;

    BTN_MULTIPLY = tk.Button(window);
    BTN_MULTIPLY["font"] = ("Arial Black", 38, "normal");
    BTN_MULTIPLY["justify"] = "center";
    BTN_MULTIPLY["background"] = "blue";
    BTN_MULTIPLY["foreground"] = "white"; 
    BTN_MULTIPLY["text"] = "*";
    BTN_MULTIPLY.place(x=320,y=290,width=75,height=75);
    BTN_MULTIPLY["command"] = BTN_MULTIPLY_command;

    BTN_DIVIDE = tk.Button(window);
    BTN_DIVIDE["font"] = ("Arial Black", 38, "normal");
    BTN_DIVIDE["justify"] = "center";
    BTN_DIVIDE["background"] = "blue";
    BTN_DIVIDE["foreground"] = "white"; 
    BTN_DIVIDE["text"] = "/";
    BTN_DIVIDE.place(x=320,y=370,width=75,height=75);
    BTN_DIVIDE["command"] = BTN_DIVIDE_command;

    BTN_Sq_Rt = tk.Button(window);
    BTN_Sq_Rt["font"] = ("Arial Black", 32, "normal");
    BTN_Sq_Rt["justify"] = "center";
    BTN_Sq_Rt["background"] = "blue";
    BTN_Sq_Rt["foreground"] = "white"; 
    BTN_Sq_Rt["text"] = "Sq";
    BTN_Sq_Rt.place(x=400,y=130,width=75,height=75);
    BTN_Sq_Rt["command"] = BTN_Sq_Rt_command;

    BTN_Cube = tk.Button(window);
    BTN_Cube["font"] = ("Arial Black", 32, "normal");
    BTN_Cube["justify"] = "center";
    BTN_Cube["background"] = "blue";
    BTN_Cube["foreground"] = "white"; 
    BTN_Cube["text"] = "Cu";
    BTN_Cube.place(x=400,y=210,width=75,height=75);
    BTN_Cube["command"] = BTN_Cube_command;

    BTN_EQUALS = tk.Button(window);
    BTN_EQUALS["font"] = ("Arial Black", 38, "normal");
    BTN_EQUALS["justify"] = "center";
    BTN_EQUALS["background"] = "blue";
    BTN_EQUALS["foreground"] = "white"; 
    BTN_EQUALS["text"] = "=";
    BTN_EQUALS.place(x=400,y=290,width=75,height=155);
    BTN_EQUALS["command"] = BTN_EQUALS_command;

    BTN_Celcius = tk.Button(window);
    BTN_Celcius["font"] = ("Arial Black", 20, "normal");
    BTN_Celcius["justify"] = "center";
    BTN_Celcius["background"] = "blue";
    BTN_Celcius["foreground"] = "white"; 
    BTN_Celcius["text"] = "Celcius";
    BTN_Celcius.place(x=320,y=450,width=155,height=55);
    BTN_Celcius["command"] = BTN_Celcius_command;

    BTN_Farenheit = tk.Button(window);
    BTN_Farenheit["font"] = ("Arial Black", 20, "normal");
    BTN_Farenheit["justify"] = "center";
    BTN_Farenheit["background"] = "blue";
    BTN_Farenheit["foreground"] = "white"; 
    BTN_Farenheit["text"] = "Farenheit";
    BTN_Farenheit.place(x=320,y=510,width=155,height=55);
    BTN_Farenheit["command"] = BTN_Farenheit_command;        

    def Calculate(op): 
        globals()['Operation'] = op;
        globals()['Add_Space'] = "True";       
        The_NUMBER = VAR_Output.get();

        if(globals()['Is_Next_Expression'] == "True"):

           if(globals()['Clicked_Equals'] == "False"):
              globals()['Num_2'] = float(The_NUMBER);
              if(op == "+"): globals()['Num_1'] = globals()['Num_1'] + globals()['Num_2'];
              elif(op == "-"): globals()['Num_1'] = globals()['Num_1'] - globals()['Num_2'];
              elif(op == "*"): globals()['Num_1'] = globals()['Num_1'] * globals()['Num_2'];  
              elif(op == "/"): 
                               if(globals()['Num_2'] == 0): 
                                  globals()['Num_1'] = 0; #catch divide by zero error here
                               globals()['Num_1'] = globals()['Num_1'] / globals()['Num_2']; 

              VAR_Output.set(globals()['Num_1']);
              globals()['Need_To_Clear'] = "True";

              if(globals()['Final_Output'] == "False"):
                 LAB_Expression["text"] = The_NUMBER + " " + op;
              elif(globals()['Final_Output'] == "True"):
                   LAB_Expression["text"] = LAB_Expression.cget("text") + " = " +  str(globals()['Num_1']);
                   globals()['Final_Output'] = "False";   

           elif(globals()['Clicked_Equals'] == "True"):
                globals()['Clicked_Equals'] = "False";

        else:
            globals()['Num_1'] = float(The_NUMBER);
            globals()['Need_To_Clear'] = "True";
            globals()['Is_Next_Expression'] = "True";          
            LAB_Expression["text"] = The_NUMBER + " " + op;



    def Math_EQUALS():
        globals()['Final_Output'] = "True";
        Calculate(globals()['Operation']);
        globals()['Need_To_Clear'] = "True";
        globals()['Clicked_Equals'] = "True";


    Initalize();
    LAB_Expression["text"] = "";
    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
#-----Invocations-----
Calculator_GUI_Interface();


