# Title: Python GUI Programming With TKinter - Widgets - SCALES
# Author: C. S. Germany 02/05/2022 

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Basic Scale
def Scales_01_Basic():
    import tkinter as TK;
    window = TK.Tk();
    window.title("tkinter Menu Objects");
    window.geometry("300x400");
    window.configure(bg='white');

    #Variable to get Scale Value
    Scale_Var = TK.DoubleVar();

    #Event Handler for Get Scale Value Button
    def Get_Scale_Value_Handler():
        Scale_Value = "Value = " + str(Scale_Var.get());
        LAB_Scale_Value_Output.config(text = Scale_Value);    

    #Create and place Scale Object
    The_Scale = TK.Scale(window, variable = Scale_Var);
    The_Scale.pack(anchor=TK.CENTER);

    BTN_Get_Scale_Value = TK.Button(window, text="Get Scale Value", command=Get_Scale_Value_Handler);
    BTN_Get_Scale_Value.pack(anchor=TK.CENTER);

    LAB_Scale_Value_Output = TK.Label(window);
    LAB_Scale_Value_Output.pack();    

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Basic Scale - Getting value
def Scales_02_Getting_Value():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Rainbow Dash's COOLNESS Scale");
    window.geometry("400x400");
    window.configure(bg='white');

    #Variable to get Scale Value
    Scale_Var = TK.DoubleVar();

    #Event Handler for Get Scale Value Button
    def Get_Scale_Value_Handler():
        Scale_Value = "Value = " + str(Scale_Var.get());
        LAB_Scale_Value_Output.config(text = Scale_Value);    

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Coolness Scale"); 
    LAB_Title.place(x=55,y=10,height=30,width=300);

    #Create and place Scale Object
    RD_Coolness_Scale = TK.Scale(window, variable = Scale_Var);
    RD_Coolness_Scale.place(x=175,y=60,height=150,width=40);

    BTN_Get_Scale_Value = TK.Button(window, command=Get_Scale_Value_Handler, font=("Comic Sans MS", 14, "bold"), text="Get Scale Value", background="purple", foreground="white");
    BTN_Get_Scale_Value.place(x=90,y=220,height=35,width=200); 

    LAB_Scale_Value_Output = TK.Label(window,font=("Comic Sans MS", 12, "bold"), text="20% more coolness goes HERE", background="black", foreground="white");
    LAB_Scale_Value_Output.place(x=40,y=270,height=100,width=300);   

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  


#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Basic Scale - Setting Scale object value
def Scales_03_Setting_Scale_Value():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Rainbow Dash's COOLNESS Scale");
    window.geometry("400x400");
    window.configure(bg='white');

    #Variable to get Scale Value
    Scale_Var = TK.DoubleVar();

    #Event Handler for Get Scale Value Button
    def Get_Scale_Value_Handler():
        Scale_Value = "Value = " + str(Scale_Var.get());
        LAB_Scale_Value_Output.config(text = Scale_Value);    

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Coolness Scale"); 
    LAB_Title.place(x=55,y=10,height=30,width=300);

    #Create and place Scale Object
    RD_Coolness_Scale = TK.Scale(window, variable = Scale_Var);
    RD_Coolness_Scale.place(x=175,y=60,height=150,width=40);

    BTN_Get_Scale_Value = TK.Button(window, command=Get_Scale_Value_Handler, font=("Comic Sans MS", 14, "bold"), text="Get Scale Value", background="purple", foreground="white");
    BTN_Get_Scale_Value.place(x=90,y=220,height=35,width=200); 

    LAB_Scale_Value_Output = TK.Label(window,font=("Comic Sans MS", 12, "bold"), text="20% more coolness goes HERE", background="black", foreground="white");
    LAB_Scale_Value_Output.place(x=40,y=270,height=100,width=300);   

    #Set Scale object with a default value. 20% cooler! :-)
    RD_Coolness_Scale.set(20);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Basic Scale - Setting Scale object range and granularity
def Scales_04_Setting_Scale_Range_and_Granularity():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Rainbow Dash's COOLNESS Scale");
    window.geometry("400x400");
    window.configure(bg='white');

    #Variable to get Scale Value
    Scale_Var = TK.DoubleVar();

    #Event Handler for Get Scale Value Button
    def Get_Scale_Value_Handler():
        Scale_Value = "Value = " + str(Scale_Var.get());
        LAB_Scale_Value_Output.config(text = Scale_Value);    

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Coolness Scale"); 
    LAB_Title.place(x=55,y=10,height=30,width=300);

    #Create and place Scale Object (use from_= and to= in constructor to specify begin and end values if don't want default 0-100)
    RD_Coolness_Scale = TK.Scale(window, variable = Scale_Var, from_=0, to=1000, orient=TK.VERTICAL);
    RD_Coolness_Scale.place(x=175,y=60,height=150,width=40);

    BTN_Get_Scale_Value = TK.Button(window, command=Get_Scale_Value_Handler, font=("Comic Sans MS", 14, "bold"), text="Get Scale Value", background="purple", foreground="white");
    BTN_Get_Scale_Value.place(x=90,y=220,height=35,width=200); 

    LAB_Scale_Value_Output = TK.Label(window,font=("Comic Sans MS", 12, "bold"), text="200% more coolness goes HERE", background="black", foreground="white");
    LAB_Scale_Value_Output.place(x=40,y=270,height=100,width=300);   

    #Set Scale object with a default value. 20% cooler! :-)
    RD_Coolness_Scale.set(200);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# HORIZONTAL Scale 
def Scales_05_HORIZONTAL_Scale():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Rainbow Dash's COOLNESS Scale");
    window.geometry("400x350");
    window.configure(bg='white');

    #Variable to get Scale Value
    Scale_Var = TK.DoubleVar();

    #Event Handler for Get Scale Value Button
    def Get_Scale_Value_Handler():
        Scale_Value = "Value = " + str(Scale_Var.get());
        LAB_Scale_Value_Output.config(text = Scale_Value);    

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Coolness Scale"); 
    LAB_Title.place(x=45,y=10,height=30,width=300);

    #Create and place Scale Object (use from_= and to= in constructor to specify begin and end values if don't want default 0-100)
    RD_Coolness_Scale = TK.Scale(window, variable = Scale_Var, from_=0, to=1000, orient=TK.HORIZONTAL);
    RD_Coolness_Scale.place(x=20,y=60,height=75,width=360);

    BTN_Get_Scale_Value = TK.Button(window, command=Get_Scale_Value_Handler, font=("Comic Sans MS", 14, "bold"), text="Get Scale Value", background="purple", foreground="white");
    BTN_Get_Scale_Value.place(x=90,y=150,height=35,width=200); 

    LAB_Scale_Value_Output = TK.Label(window,font=("Comic Sans MS", 12, "bold"), text="200% more coolness goes HERE", background="black", foreground="white");
    LAB_Scale_Value_Output.place(x=40,y=200,height=100,width=300);   

    #Set Scale object with a default value. 20% cooler! :-)
    RD_Coolness_Scale.set(200);

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#-----Invocations-----
#Scales_01_Basic();
#Scales_02_Getting_Value();
#Scales_03_Setting_Scale_Value();
#Scales_04_Setting_Scale_Range_and_Granularity();
Scales_05_HORIZONTAL_Scale();




