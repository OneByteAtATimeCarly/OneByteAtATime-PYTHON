# Title: Python GUI Programming With TKinter - Widgets - NOTEBOOKS
# Author: C. S. Germany 02/05/2022

# Notebook Objects. They have tabs, each tab is a Frame object in tkinter.
# add() = add a tab to the notebook
# hide() = temporarily remove a tab from the notebook.
# forget() = remove a tab permanently

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Notebook - Instantiating
def Notebook_0l():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    window = TK.Tk();
    window.title("tkinter Notebook Objects");
    window.geometry("450x450");
    window.configure(bg='white');         

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Twilight Sparkle's Magic Notebook"); 
    LAB_Title.place(x=45,y=10,height=30,width=360);

    #Create and place Notebook
    NB_The_Notebook = ttk.Notebook(window);
    NB_The_Notebook.place(x=15,y=50,height=320,width=420);

    #Create and size Frame objects that will serve as Notebook's tabs and add them to Notebook
    FRM_Page1 = ttk.Frame(NB_The_Notebook, width=400, height=300);   # 1st page
    FRM_Page2 = ttk.Frame(NB_The_Notebook, width=400, height=300);   # 2nd page
    FRM_Page3 = ttk.Frame(NB_The_Notebook, width=400, height=300);   # 3rd page

    NB_The_Notebook.add(FRM_Page1, text='Page 1');
    NB_The_Notebook.add(FRM_Page2, text='Page 2');
    NB_The_Notebook.add(FRM_Page3, text='Page 3');

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Notebook - Adding tkinter objects to pages
def Notebook_02():
    import tkinter as TK;
    from tkinter import ttk; #necessary, progressbar not in TK
    window = TK.Tk();
    window.title("tkinter Notebook Objects");
    window.geometry("450x450");
    window.configure(bg='white');         

    LAB_Title = TK.Label(window,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Twilight Sparkle's Magic Notebook"); 
    LAB_Title.place(x=45,y=10,height=30,width=360);

    #Create and place Notebook
    NB_The_Notebook = ttk.Notebook(window);
    NB_The_Notebook.place(x=15,y=50,height=320,width=420);

    #Create and size Frame objects that will serve as Notebook's tabs and add them to Notebook
    FRM_Page1 = TK.Frame(NB_The_Notebook, width=400, height=300, background="white", relief=TK.SUNKEN);   # 1st page
    FRM_Page2 = TK.Frame(NB_The_Notebook, width=400, height=300, background="white", relief=TK.SUNKEN);   # 2nd page
    FRM_Page3 = TK.Frame(NB_The_Notebook, width=400, height=300, background="white", relief=TK.SUNKEN);   # 3rd page

    NB_The_Notebook.add(FRM_Page1, text='Page 1');
    NB_The_Notebook.add(FRM_Page2, text='Page 2');
    NB_The_Notebook.add(FRM_Page3, text='Page 3');

    #Page 1 Title and Contents
    LAB_Page1_Title = TK.Label(FRM_Page1,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Friendship Magic", justify=TK.CENTER); 
    LAB_Page1_Title.place(x=25,y=10,height=40,width=350);
    LAB_Page1_Message = "1. Hug your friends.\n2. Help your friends.\n3. Love your friends.\n4. Be faithful to your friends." + \
                        "\n5. Listen to your friends.\n6. Play with your friends.\n7. Laugh with your friends.\n8. Cry with your friends" + \
                        "\n9. Forgive your friends.";
    LAB_Page1_Contents = TK.Label(FRM_Page1,font=("Comic Sans MS", 11), background="white", foreground="black",text=LAB_Page1_Message, justify=TK.LEFT); 
    LAB_Page1_Contents.place(x=50,y=60,height=210,width=350);    

    #Page 2 Title and Contents
    LAB_Page2_Title = TK.Label(FRM_Page2,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Healing Magic"); 
    LAB_Page2_Title.place(x=25,y=10,height=40,width=350);
    LAB_Page2_Message = "1. Close your eyes and be still.\n2. Listen to the Universe.\n3. Accept the flow of reality.\n4. Be at one with nature." + \
                        "\n5. Bend with the wind.\n6. Drink plenty of water.\n7. Eat healthy natural food.\n8. Get enough rest." + \
                        "\n9. Sleep well and DREAM.";
    LAB_Page2_Contents = TK.Label(FRM_Page2,font=("Comic Sans MS", 11), background="white", foreground="black",text=LAB_Page2_Message, justify=TK.LEFT); 
    LAB_Page2_Contents.place(x=35,y=60,height=210,width=350);     

    #Page 3 Title and Contents
    LAB_Page3_Title = TK.Label(FRM_Page3,font=("Comic Sans MS", 15, "bold"), background="white", foreground="black",text="Teleportation Magic"); 
    LAB_Page3_Title.place(x=25,y=10,height=40,width=350);    
    LAB_Page3_Message = "1. Visualize WHERE and WHEN you want to be.\n2. Focus on that single point of spacetime.\n3. Shift your quantum state towards that singularity." + \
                        "\n4. Redirect your existence towards that coordinate.\n5. Anchor yourself in the new 4-D reality.";

    LAB_Page3_Contents = TK.Label(FRM_Page3,font=("Comic Sans MS", 11), background="white", foreground="black",text=LAB_Page3_Message, justify=TK.LEFT); 
    LAB_Page3_Contents.place(x=25,y=50,height=130,width=375);              

    window.mainloop();
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#Notebook_0l();
Notebook_02();








