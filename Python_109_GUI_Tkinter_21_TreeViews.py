# Title: Python GUI Programming With TKinter - Widgets - TREEVIEWS
# Author: C. S. Germany 02/05/2022

# Treeview Objects. They hold a list of items. Each item has one or more columns.


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Treeview - Instantiating
def TreeView_0l():
    import tkinter as TK;
    from tkinter import ttk;
    from tkinter import messagebox; #separate import necessary for messageboxes
    window = TK.Tk();
    window.title("tkinter Treeview Objects");
    window.geometry("630x350");
    window.configure(bg='white');         

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Rainbow Dash's Terrific Treeview"); 
    LAB_Title.place(x=45,y=10,height=30,width=360);

    #1. Create Tuple to define columns
    TUP_TV_Columns = ('Pony_First_Name', 'Pony_Last_Name', 'Pony_Email');

    #2. Create Treeview Object
    TV_TreeView1 = ttk.Treeview(window, columns=TUP_TV_Columns, show='headings');    

    #3. Define headings of columns Tuple
    TV_TreeView1.heading('Pony_First_Name', text='First Name');
    TV_TreeView1.heading('Pony_Last_Name', text='Last Name');
    TV_TreeView1.heading('Pony_Email', text='Pony Mail');

    #4. Generate sample data using an array
    Pony_Contacts = [];
    for PONY in range(1, 100):
        Pony_Contacts.append((f'First Name {PONY}', f'Last Name {PONY}', f'PonyMail{PONY}@equestria.edu'));

    #5.  Add data to the Treeview
    for PONY in Pony_Contacts:
        TV_TreeView1.insert('', TK.END, values=PONY);

    #6. Define Event Handler for Treeview Item Selected
    def item_selected(event):
        for selected_item in TV_TreeView1.selection():
            item = TV_TreeView1.item(selected_item);
            record = item['values'];
            TK.messagebox.showinfo(title='Information', message=', '.join(record));

    #7. Bind Event Handler method to Treeview
    TV_TreeView1.bind('<<TreeviewSelect>>', item_selected);

    #8.  Grid Treeview onto window 
    TV_TreeView1.grid(row=0, column=0, sticky='nsew');

    #9. Add Scrollbar to Treeview
    SB_TV_ScrlBar = ttk.Scrollbar(window, orient=TK.VERTICAL, command=TV_TreeView1.yview);
    TV_TreeView1.configure(yscroll=SB_TV_ScrlBar.set);
    SB_TV_ScrlBar.grid(row=0, column=1, sticky='ns'); 

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
TreeView_0l();









