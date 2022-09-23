# Title: Python GUI Programming With TKinter - Opening a New Window from the Current Window 2
# Author: C. S. Germany 02/05/2022

from tkinter import *;
import tkinter as tk;
root = tk.Tk();

#---Name_Window-------------------------------------------------------------------------------------------------------------- 
class Name_Window(object):
 
    def newWindow(self): # new window definition
        Nam_Win = Toplevel(root);
        Nam_Win.configure(bg='black'); 
        Nam_Win.title("Please enter your name.");
        Name_Window_Width = 300;
        Name_Window_Height = 150;
        ScreenWidth = Nam_Win.winfo_screenwidth();
        ScreenHeight = Nam_Win.winfo_screenheight();
        Appear_in_the_Middle = '%dx%d+%d+%d' % (Name_Window_Width, Name_Window_Height, (ScreenWidth - Name_Window_Width) / 2, (ScreenHeight - Name_Window_Height) / 2);
        Nam_Win.geometry(Appear_in_the_Middle);
        Nam_Win.resizable(width=False, height=False);
        
        Name_Data = tk.StringVar();

        def SUBMIT_Button_Handler():
            The_Name = Name_Data.get();
            print("Name =",The_Name);
            Nam_Win.destroy();        

        Label_NAM = Label(Nam_Win, text="Please enter your name below, player.", font=('Helvetica 12'), bg='black', fg='white').pack(pady=10);
        Entry_NAM = Entry(Nam_Win, width=25, font=('Helvetica 12'),textvariable=Name_Data).pack(pady=10);
        Button_NAM = Button(Nam_Win, width=15, height=10, font=('Helvetica 11'), text="SUBMIT", bg='red', command=SUBMIT_Button_Handler).pack(pady=10);
    
    def mainFrame(self,root):
        root.title('Open New Window!!!');
        root.geometry("200x200"); 
        root.resizable(0,0);
        button1 =Button(root, text ="open new window", command =self.newWindow);
        button1.place(x = 50, y = 25, width=100, height=25);
#---------------------------------------------------------------------------------------------------------------------------- 

app = Name_Window();
app.mainFrame(root);
root.mainloop();

