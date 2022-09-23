# Title: Python GUI Programming With TKinter - Widgets - PRE-BUILT DIALOGS
# Author: C. S. Germany 02/05/2022

# Link = https://realpython.com/python-gui-tkinter/

#Function-------------------------------------------------------------------------------------------------------------------------
def GUI_App_Example_1_Temp_Converter():
    import tkinter as TK;

    def fahrenheit_to_celsius():
        fahrenheit = ent_temperature.get();
        celsius = (5 / 9) * (float(fahrenheit) - 32);
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}";

    # Set up the window
    window = TK.Tk();
    window.title("Temperature Converter");
    window.resizable(width=False, height=False);

    # Create Fahrenheit entry frame with Entry and label widget
    frm_entry = TK.Frame(master=window);
    ent_temperature = TK.Entry(master=frm_entry, width=10);
    lbl_temp = TK.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}");

    # Place Entry and Label into frame using the .grid() geometry manager
    ent_temperature.grid(row=0, column=0, sticky="e");
    lbl_temp.grid(row=0, column=1, sticky="w");

    # Create the conversion Button and result display Label
    btn_convert = TK.Button( master=window,
                             text="\N{RIGHTWARDS BLACK ARROW}",
                             command=fahrenheit_to_celsius
                           );

    lbl_result = TK.Label(master=window, text="\N{DEGREE CELSIUS}");

    # Set up the layout using the .grid() geometry manager
    frm_entry.grid(row=0, column=0, padx=10);
    btn_convert.grid(row=0, column=1, pady=10);
    lbl_result.grid(row=0, column=2, padx=10);

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------




#Function-------------------------------------------------------------------------------------------------------------------------
# In this example we import pre-built dialogs to open and save files form tkinter
# askopenfilename = pre-built open file dialog
# asksaveasfilename = pre-built save file dialog
def GUI_App_Example_2_Text_Editor():
    import tkinter as TK;
    from tkinter.filedialog import askopenfilename, asksaveasfilename;
    window = TK.Tk();
    window.title("Twilight Sparkle's Text Editor");
    window.rowconfigure(0, minsize=600, weight=1);
    window.columnconfigure(1, minsize=800, weight=1);

    def open_file():
        filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]);
        
        if not filepath:
           return;
        txt_edit.delete("1.0", TK.END);

        with open(filepath, mode="r", encoding="utf-8") as input_file:
             text = input_file.read();
             txt_edit.insert(TK.END, text);

        window.title(f"Twilight Sparkle's Text Editor - {filepath}");

    def save_file():
        filepath = asksaveasfilename( defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]);
        if not filepath:
           return;

        with open(filepath, mode="w", encoding="utf-8") as output_file:
             text = txt_edit.get("1.0", TK.END);
             output_file.write(text);

        window.title(f"Simple Text Editor - {filepath}");

    txt_edit = TK.Text(window);
    frm_buttons = TK.Frame(window, relief=TK.RAISED, bd=2);
    btn_open = TK.Button(frm_buttons, text="Open", command=open_file);
    btn_save = TK.Button(frm_buttons, text="Save As...", command=save_file);

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5);
    btn_save.grid(row=1, column=0, sticky="ew", padx=5);

    frm_buttons.grid(row=0, column=0, sticky="ns");
    txt_edit.grid(row=0, column=1, sticky="nsew");

    window.mainloop();
#-------------------------------------------------------------------------------------------------------------------------------




#Invocations
#GUI_App_Example_1_Temp_Converter();
GUI_App_Example_2_Text_Editor();

