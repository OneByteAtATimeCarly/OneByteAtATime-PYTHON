# Title: Python GUI Programming With TKinter - Widgets - SPINBOXES
# Author: C. S. Germany 02/05/2022

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Spinbox
def SpinBox_0l():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    window = TK.Tk();
    window.title("tkinter Progressbar Objects");
    window.geometry("450x150");
    window.configure(bg='white');         

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Coolness Spinner"); 
    LAB_Title.place(x=60,y=10,height=30,width=320);

    #Create and place Spinbox
    SpnBox_Main = TK.Spinbox(window, from_=0, to=100, font=("Comic Sans MS", 20, "bold"));
    SpnBox_Main.place(x=30,y=60,height=40,width=390);   

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Spinbox
def SpinBox_02_Set_Value():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    window = TK.Tk();
    window.title("tkinter Progressbar Objects");
    window.geometry("450x150");
    window.configure(bg='white');         

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Coolness Spinner"); 
    LAB_Title.place(x=60,y=10,height=30,width=320);

    #Variable used to set Spinnerbox value
    SpinnerVar = TK.IntVar();

    #Create and place Spinbox
    SpnBox_Main = TK.Spinbox(window, from_=0, to=100, font=("Comic Sans MS", 20, "bold"),textvariable=SpinnerVar);
    SpnBox_Main.place(x=30,y=60,height=40,width=390);  

    SpinnerVar.set(20);     

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Spinbox
def SpinBox_03_Change_Increment_and_Get_Value():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    window = TK.Tk();
    window.title("tkinter Progressbar Objects");
    window.geometry("450x320");
    window.configure(bg='white');         

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Coolness Spinner"); 
    LAB_Title.place(x=60,y=10,height=30,width=320);

    #Event Handler for Get Spinner Value Button
    def Get_BTN_Spinner_Handler():
        Spinner_Value = "Value = " + str(SpinnerVar.get());
        LAB_Spinner_Value_Output.config(text = Spinner_Value);

    #Variable used to set Spinnerbox value
    SpinnerVar = TK.IntVar();

    #Create and place Spinbox (increment changed to 5 with increment=5)
    SpnBox_Main = TK.Spinbox(window, from_=0, to=1000, increment=5, font=("Comic Sans MS", 20, "bold"),textvariable=SpinnerVar,);
    SpnBox_Main.place(x=30,y=60,height=40,width=390);  

    SpinnerVar.set(20);  

    BTN_Get_Spinner_Value = TK.Button(window, command=Get_BTN_Spinner_Handler, font=("Comic Sans MS", 14, "bold"), text="Get Spinner Value", background="purple", foreground="white");
    BTN_Get_Spinner_Value.place(x=130,y=130,height=35,width=200); 

    LAB_Spinner_Value_Output = TK.Label(window,font=("Comic Sans MS", 12, "bold"), text="200% more coolness goes HERE", background="black", foreground="white");
    LAB_Spinner_Value_Output.place(x=75,y=180,height=100,width=300);         

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#-----Invocations-----
#SpinBox_0l();
#SpinBox_02_Set_Value();
SpinBox_03_Change_Increment_and_Get_Value();








