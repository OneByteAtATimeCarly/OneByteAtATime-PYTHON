# Title: Python GUI Programming With TKinter - Widgets - EVENT HANDLERS
# Author: C. S. Germany 02/05/2022

# LINK = https://realpython.com/python-gui-tkinter/

# window.mainloop() = starts the event loop. GUI runs in this loop. Continuously checks if an event has occurred. 
# If so and event is detected / triggered, event handler code will execute based on the event trigger.

#Bind = To call an event handler whenever an event occurs on a window, use .bind(). 
# The event handler is said to be bound to the event because it’s called every time the event occurs.

# Event Loop
# After we construct an application's initial user interface, it enters the Tk event loop. The event loop continually processes events, pulled from the system event queue dozens of times a second. 
# It watches for mouse or keyboard events, invoking command callbacks and event bindings as needed.


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Handling: Key Presses.  In this instance event handler is bound to WINDOW itself.
def Event_Handle_Key_Press():
    import tkinter as tk;

    window = tk.Tk()
 
    #Event handler behavior defined
    def handle_keypress(event):
        print("CHAR received was: ",event.char);

    # Event listener trigger set - bind() keypress event to handle_keypress()
    window.bind("<Key>", handle_keypress);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Handling  BUTTON clicks. In this case, the event handler is added to the widget itself using the "command" parameter.
# When you create each button, include the command parameter and point it to the event handler function you created. See code below:
def Event_Handle_Button_Click_1():
    import tkinter as tk;

    #Event Handlers for each button
    def increase():
        value = int(lbl_value["text"]);
        lbl_value["text"] = f"{value + 1}";

    def decrease():
        value = int(lbl_value["text"]);
        lbl_value["text"] = f"{value - 1}";

    #Make window nicely resizeable
    window = tk.Tk();
    window.rowconfigure(0, minsize=50, weight=1);
    window.columnconfigure([0, 1, 2], minsize=50, weight=1);

    #Create and grid Buttons and Labels
    btn_decrease = tk.Button(master=window, text="-", command=decrease);
    btn_decrease.grid(row=0, column=0, sticky="nsew");

    lbl_value = tk.Label(master=window, text="0");
    lbl_value.grid(row=0, column=1);

    btn_increase = tk.Button(master=window, text="+", command=increase);
    btn_increase.grid(row=0, column=2, sticky="nsew");

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------





#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#Using place() geometry manager
def Event_Handle_Button_Click_2():
    import tkinter as TK;
    window = TK.Tk();
    window.title("Hello MOTO!");
    window.geometry("600x350");
    window.configure(bg='white');

    #Event handlers
    def Discord_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Discord says:\nFriendhip is STUPID!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");

    def Fluttershy_Trigger():
        Text1.delete("1.0", TK.END);
        Text1.insert("1.0","Fluttershy says:\nLove one another!");
        Text1.tag_add("In_Da_Middle", "1.0", "end");        

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

    Button1 = TK.Button( command=Discord_Trigger,
                         text="Do NOT Click Me",
                         font=("Comic Sans MS", 10, "bold"),
                         justify="center",
                         foreground="white",
                         background="red",
                         width=30,
                         height=3  
                     );

    Button2 = TK.Button( command=Fluttershy_Trigger,
                         text="Click Me!",
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





# Blocking
# You run into problems when the event loop is prevented from processing events for a lengthy period. Your application won't redraw or respond to events and will appear to be frozen. 
# Imagine a user pressing a button. So the event loop calls the application code to handle the event. The code creates a progressbar, performs some time-consuming operations, and stops the progressbar. 
# Only then does the code return control back to the event loop. No events have been processed in the meantime, and no screen redrawing has occurred. So events have been piling up in the event queue.

# All screen updates are processed only in the event loop. So if you change the text of a label widget, that change doesn't appear onscreen immediately. 
# Instead, the widget notifies Tk that it needs to be redrawn. Later on, in between processing other events, Tk's event loop will ask the widget to redraw itself. 
# All drawing occurs only in the event loop. The change appears to happen immediately because the time between changing the widget and the actual redraw in the event loop is so short.
# But this only works as intended when there's no time-consuming code clogging up the event loop.

# Timer Events
# If you have long-running processes (ike network I/O), you must take alternative approaches to coding the event loop. 
# If possible, the very best thing you can do is break your operation into tiny steps, each of which can execute very quickly. 
# You let the event loop be responsible for when the next step occurs. That way, the event loop continues to run, processing regular events, updating the screen, and, 
# in between all that, calling your code to perform the next step of the operation. To make use of Timer Events:

# Our program asks the event loop to generate one of a series of Timer events at a later time. As part of its regular processing, when the event loop reaches that time, 
# it will call back into our code to handle the event. Our code would then perform the next step of the operation. It then schedules another timer event for the next step 
# of the operation and immediately returns control back to the event loop. And so on and so on.

# Tk's "after" command can be used to generate timer events. You provide the number of milliseconds to wait until the event should be fired. It may happen later than 
# that if Tk is busy processing other events, but it won't happen before. You can also ask that an idle event be generated; it will fire when no other events in the queue need to be processed.
# Tk's screen updates and redraws occur in the context of idle events.



#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# used a blocking form of "after" to simulate performing our operation
def Event_Handler_Blocked_01():
    import tkinter as tk;
    from tkinter import ttk;
    window = tk.Tk();

    #Globals
    global interrupt;

    def start():
        BTN_Start.configure(text='Stop', command=stop);
        LAB_Answer['text'] = "Working...";
        globals()['interrupt']  = False;
        window.after(1, step);
    
    def stop():
        globals()['interrupt'] = True;
    
    def step(count=0):
        PBAR_Progress['value'] = count;
        if globals()['interrupt']:
           result(None);
           return;
        window.after(100);  # next step in our operation; don't take too long!
        if count == 20:  # done!
           result(42);
           return;
        window.after(1, lambda: step(count+1));
    
    def result(answer):
        PBAR_Progress['value'] = 0;
        BTN_Start.configure(text='Start!', command=start);
        LAB_Answer['text'] = "Answer: " + str(answer) if answer else "No Answer";
    
    FRM_Main = ttk.Frame(window);
    FRM_Main.grid();
    BTN_Start = ttk.Button(FRM_Main, text="START", command=start); 
    BTN_Start.grid(column=1, row=0, padx=5, pady=5);
    LAB_Answer = ttk.Label(FRM_Main, text="No Answer"); 
    LAB_Answer.grid(column=0, row=0, padx=5, pady=5);
    PBAR_Progress = ttk.Progressbar(FRM_Main, orient="horizontal", mode="determinate", maximum=20); 
    PBAR_Progress.grid(column=0, row=1, padx=5, pady=5);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------------------------------------    



#Invocations
#Place_1();
#Event_Handle_Key_Press();
#Event_Handle_Button_Click_1();
#Event_Handle_Button_Click_2();
Event_Handler_Blocked_01();