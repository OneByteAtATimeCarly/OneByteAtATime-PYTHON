# Title: Python GUI Programming With TKinter - Windows as Classes
# Author: C. S. Germany 02/05/2022

import tkinter as TK;

#Class--------------------------------------------------------------------------------------------------------------------------------------------------------
class Window_1(TK.Frame):
      def __init__(self, root):
          TK.Frame.__init__(self, root);
          Lab1 = TK.Label(self, text="Place 1 widget here...", anchor="c");
          Lab1.pack(side="top", fill="both", expand=True);
          Lab2 = TK.Label(self, text="Place another widget here...", anchor="c");
          Lab2.pack(side="top", fill="both", expand=True);         
#-------------------------------------------------------------------------------------------------------------------------------------------------------------         


#Class--------------------------------------------------------------------------------------------------------------------------------------------------------
class Window_2(TK.Frame):
      def __init__(self, root):
          TK.Frame.__init__(self, root);
          Lab1 = TK.Label(self, text="!!!HELLO WORLD!!!", anchor="c");
          Lab1.pack(side="top", fill="both", expand=True);
          Lab2 = TK.Label(self, text="Nice to meet you.", anchor="c");
          Lab2.pack(side="top", fill="both", expand=True);         
#-------------------------------------------------------------------------------------------------------------------------------------------------------------  

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def MAIN():
    ROOT1 = TK.Tk();
    VIEW1 = Window_1(ROOT1);
    VIEW1.pack(side="top", fill="both", expand=True);
    ROOT1.mainloop();

    ROOT2 = TK.Tk();
    VIEW2 = Window_2(ROOT2);
    VIEW2.pack(side="top", fill="both", expand=True);    
    ROOT2.mainloop();    
#------------------------------------------------------------------------------------------------------------------------------------------------------------



#Invocations
MAIN();