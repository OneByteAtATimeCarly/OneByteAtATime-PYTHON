#Title: Purple Python Port Pinger 1.0 (GUI Network Scanner)
#Author: Carly S. Germany
#Created: 05/12/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

# Note that you MUST use multi-threading when calling functions that loop with a tkinter GUI. 
# If you do not and run everything in the same thread, the GUI will lock up and not respond until the loop in the external fuinction finishes.

import tkinter as tk;
import tkinter.messagebox as MB;
import datetime;
import platform;
import os;
import socket;
import threading;
import subprocess;

#Globals
window = tk.Tk();
window.title("Python tkinter - Purple Python Port Pinger 1.0 - 2022 - Carly Salali Germany");
window_Width = 1100;
window_Height = 520;
ScreenWidth = window.winfo_screenwidth();
ScreenHeight = window.winfo_screenheight();
Appear_in_the_Middle = '%dx%d+%d+%d' % (window_Width, window_Height, (ScreenWidth - window_Width) / 2, (ScreenHeight - window_Height) / 2);
window.geometry(Appear_in_the_Middle);
window.resizable(width=False, height=False);
window.configure(bg='black'); 
GUI = None; #pointer that will be used to reference GUI class for functions (instantiated later)

#---Class--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PPPPP_GUI:

#------Inline Functions------
      def Get_Current_Network(self): 
          #Note: Code below works only for Windows and WLAN. Specify alt interface for other. For Linux call "ifconfig" or "iwconfig" respectively.
          Client_Hostname = socket.gethostname(); 
          IP_Settings = subprocess.run('ipconfig /all',stdout=subprocess.PIPE,text=True).stdout.lower();
          scan=False;
          IP_Address = "";
          Default_Gateway = "";
          Subnet_Mask = "";
          DNS_Servers = "";
          scan = "";

          #Comment/uncomment line below to toggle WLAN and wired ethernet connection (till I find room on the GUi for a button)
          for i in IP_Settings.split('\n'):
              #if 'wireless' in i: scan=True;
              if((i != None) and ("ethernet adapter ethernet:" in i)): scan=True;
              #if((i != None) and ("ethernet adapter vmware network adapter vmnet8:" in i)): scan=True;

              #Only get value 1st iternation. If value != null don't retrieve
              if scan:
                 if 'ipv4 address' in i and IP_Address == "": 
                    IP_Address = i.split(':')[1].strip();
                    IP_Address = IP_Address.replace("(preferred)","");
                 if 'default gateway' in i and Default_Gateway == "": 
                    Default_Gateway = i.split(':')[1].strip();   
                 if 'subnet mask' in i and Subnet_Mask == "": 
                    Subnet_Mask = i.split(':')[1].strip(); 
                 if 'dns servers' in i and DNS_Servers == "": 
                    DNS_Servers = i.split(':')[1].strip();         

          MESSAGE = "IP v4 ad: " +  IP_Address;
          MESSAGE += "      Subnet: " + Subnet_Mask;
          MESSAGE += "\nHostname: " + Client_Hostname;
          MESSAGE += "           DNS: " + DNS_Servers;
          MESSAGE += "\nGateway:  " + Default_Gateway;
          self.TXT_Current_Network.insert("0.0", MESSAGE);
          print("\n" + MESSAGE);          

#----------------------------------------------------------------------------------------------------------------------           

      def refresh(self):
          window.update();
          window.after(1000,self.refresh);

#----------------------------------------------------------------------------------------------------------------------       

      def Ping_Sweep_1(self):
          self.TXT_Main_Output.delete("0.0", "end");
          Net_IP = self.ENT_Network.get();
          Start_Host = self.ENT_Start_Host.get();
          End_Host = self.ENT_End_Host.get();

          MESSAGE = "\n Initiating PING Sweep.\n";
          MESSAGE += " Received from GUI:\n";
          MESSAGE += "\n Network Address: " + Net_IP; 
          MESSAGE +=  "\n Starting Host: " + Start_Host;
          MESSAGE +=  "\n Ending Host: " + End_Host + "\n";

          self.TXT_Main_Output.insert("0.0", MESSAGE);
          print(MESSAGE);

          The_Ping = "";

          IP_PARTS = Net_IP.split('.');
          NETWORK_IP = IP_PARTS[0] + '.' + IP_PARTS[1] + '.' + IP_PARTS[2] + '.';

          Starting_Host = int(Start_Host);
          Ending_Host = int(End_Host);
          Ending_Host += 1;

          OS = platform.system();

          if(OS == "Windows"):
             print("Windows OS detected.");
             Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
             self.TXT_Main_Output.delete(1.0,"end");
             self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + " Windows OS detected.");
             The_Ping = "ping -n 1 ";
          else:
             print("Hopefully Linux OS detected.");
             Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
             self.TXT_Main_Output.delete(1.0,"end");
             self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + " Hopefully Linux OS detected.");
             The_Ping = "ping -c 1 ";   

          #Get starting time of scan
          Time_Start = datetime.datetime.now();
          MESSAGE = " Start time: " + str(Time_Start);  
          MESSAGE += "\n Scanning ...\n";  
          print(MESSAGE);
          Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
          self.TXT_Main_Output.delete(1.0,"end");
          self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE); 

          for IP in range(Starting_Host,Ending_Host):
              ADDRESS = NETWORK_IP + str(IP);
              MESSAGE = " Pinging " + ADDRESS; 
              Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
              self.TXT_Main_Output.delete(1.0,"end");
              self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE);
              self.TXT_Main_Output.see("end"); #autoscrolls TEXT object to bottom
              print(MESSAGE);
              The_Command = The_Ping + ADDRESS;
              The_Response = os.popen(The_Command);
              LIST = The_Response.readlines();

              for LINE in LIST:
                  if(LINE.count("TTL")):
                     MESSAGE = "        " + ADDRESS + "---> Live!"; 
                     print(MESSAGE); 
                     Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
                     self.TXT_Main_Output.delete(1.0,"end");
                     self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE);
                     break;  

          Time_End = datetime.datetime.now();
          Total_Time = Time_End - Time_Start;
          MESSAGE = "\nScan completed in: " + str(Total_Time);
          print(MESSAGE);
          Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
          self.TXT_Main_Output.delete(1.0,"end");
          self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE); 

#----------------------------------------------------------------------------------------------------------------------           

      def Threaded_Ping_Sweep_1(self):
          self.refresh();
          threading.Thread(target=self.Ping_Sweep_1).start();

#---------------------------------------------------------------------------------------------------------------------- 
              
      def Port_Scan_1(self):
          self.TXT_Main_Output.delete("0.0", "end");
          The_Host = self.ENT_Host.get();
          Start_Port = self.ENT_Start_Port.get();
          End_Port = self.ENT_End_Port.get();

          MESSAGE = "\n Initiating PORT Scan.\n";
          MESSAGE += " Received from GUI:\n";
          MESSAGE += "\n Host to scan: " + The_Host; 
          MESSAGE +=  "\n Starting Port: " + Start_Port;
          MESSAGE +=  "\n Ending Port: " + End_Port + "\n";

          self.TXT_Main_Output.insert("0.0", MESSAGE);
          print(MESSAGE);

          # Check time when scan started
          Time_Start = datetime.datetime.now();
          
          Remote_Server = The_Host;
          Remote_Server_IP = socket.gethostbyname(Remote_Server);
          Port_Start = int(Start_Port);
          Port_End = int(End_Port);

          MESSAGE =  "\n Scanning remote host: " + Remote_Server_IP + "\n";
          Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
          self.TXT_Main_Output.delete(1.0,"end");
          self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE); 
          print(MESSAGE);

          try:
              for port in range(Port_Start,Port_End): 
                  MESSAGE = " Scanning port: " + str(port);
                  Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
                  self.TXT_Main_Output.delete(1.0,"end");
                  self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE); 
                  self.TXT_Main_Output.see("end"); #autoscrolls TEXT object to bottom
                  print(MESSAGE);  
                  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                  socket.setdefaulttimeout(.1);
                  result = sock.connect_ex((Remote_Server_IP, port));
                  if result == 0:
                     MESSAGE = "\n ********** Port " + str(port) + ":-->Open!";
                     Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
                     self.TXT_Main_Output.delete(1.0,"end");
                     self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE); 
                     print(MESSAGE);
                  sock.close();

          except KeyboardInterrupt:
                 MESSAGE = "\n You pressed Ctrl + C to terminate process.";
                 Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
                 self.TXT_Main_Output.delete(1.0,"end");
                 self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE); 
                 print(MESSAGE);
                 self.sys.exit();

          except socket.gaierror:
                 print("");
                 MESSAGE = "\n Hostname could not be resolved. Exiting ...";
                 Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
                 self.TXT_Main_Output.delete(1.0,"end");
                 self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE);
                 print(MESSAGE);                 
                 self.sys.exit();

          except socket.error:
                 MESSAGE = "\n Couldn't connect to server. Exiting ...";
                 Txt_Box_Contents = self.TXT_Main_Output.get("0.0",tk.END);
                 self.TXT_Main_Output.delete(1.0,"end");
                 self.TXT_Main_Output.insert("0.0", Txt_Box_Contents + MESSAGE);
                 print(MESSAGE);                 
                 self.sys.exit();

          # Checking the time again
          Time_Finish = datetime.datetime.now();

          # Calculates the difference of time, to see how long it took to run the script
          Time_Total =  Time_Finish - Time_Start;

          # Printing the information to screen     
          MESSAGE = "Scanning Completed in: " + str(Time_Total);
          self.TXT_Main_Output.insert("1.0", MESSAGE);
          print(MESSAGE);                     
#---------------------------------------------------------------------------------------------------------------------- 

      def Threaded_Port_Scan_1(self):
          self.refresh();
          threading.Thread(target=self.Port_Scan_1).start();

#---------------------------------------------------------------------------------------------------------------------- 

    #---Constructor----------------------------------------------------------------------------     
      def __init__(self, master=None):

          self.RB_Ping_Or_Port_Var = tk.IntVar();

          #Event handlers for File menu items
          def File_Menu_NEW_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From FILE menu clicked NEW");
          def File_Menu_CLOSE_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From FILE menu clicked CLOSE"); 

          #Event handlers for View menu items
          def View_Menu_ZOOMIN_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM IN");
          def View_Menu_ZOOMOUT_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM OUT"); 

          #Event handlers for Help menu items
          def Help_Menu_Get_Network_Data_Handler():  BTN_Get_Current_Network_Settings();
          def Help_Menu_HELP_Handler(): 
              MESSAGE = "Welcome to the Purple Python Port Pinger. This project is";
              MESSAGE += "\na simple network scanning tool for initiating ping sweeps";
              MESSAGE += "\nand port scans. It is an endeavor to learn some of the basics";
              MESSAGE += "\nof socket and multiprocess programming and multi-threading";
              MESSAGE += "\nin Python.\n";
              MESSAGE += "\nMulti-threading is necessary for this project because the ";
              MESSAGE += "\ntkinter GUI will lock and not refresh or respond when";
              MESSAGE += "\nexternal functions that initiate long, time-consuming loops";
              MESSAGE += "\nare called - that is UNLESS you place each external function";
              MESSAGE += "\ncall in its own separate thread outside the GUI's mainloop";
              MESSAGE += "\nthread used to display widgets and listen for event triggers.\n";
              MESSAGE += "\nTo initiate a ping sweep, enter the parameters and click the";
              MESSAGE += "\n\"INITIATE\" button for the selected Ping Sweep label frame.";
              MESSAGE += "\nTo initiate a port scan, enter the parameters and click the";
              MESSAGE += "\n\"INITIATE\" button for the selected Port Scan label frame.";
              MESSAGE += "\nTo get the network environment for the current host, click the";
              MESSAGE += "\n\"Get Host Network Data\" button.";
              MB.showinfo(title='PPPP Help Menu', message=MESSAGE); 
          
          def Help_Menu_ABOUT_Handler(): 
              MESSAGE = "Purple Python Port Pinger 1.0\nCarly Salali Germany - 2022";
              MB.showinfo(title='PPPP About Menu', message=MESSAGE);   

          #Event Handlers for Buttons
          def RB_Ping_Selection_Handler():
              self.BTN_Init_Port['state'] = tk.DISABLED;
              self.BTN_Init_Ping['state'] = tk.NORMAL;
              self.ENT_Host['state'] = tk.DISABLED;
              self.ENT_Start_Port['state'] = tk.DISABLED;
              self.ENT_End_Port['state'] = tk.DISABLED;              
              self.ENT_Network['state'] = tk.NORMAL;
              self.ENT_Start_Host['state'] = tk.NORMAL;
              self.ENT_End_Host['state'] = tk.NORMAL;                                      

          def RB_Port_Selection_Handler():   
              self.BTN_Init_Ping['state'] = tk.DISABLED;
              self.BTN_Init_Port['state'] = tk.NORMAL; 
              self.ENT_Network['state'] = tk.DISABLED;
              self.ENT_Start_Host['state'] = tk.DISABLED;
              self.ENT_End_Host['state'] = tk.DISABLED;
              self.ENT_Host['state'] = tk.NORMAL;
              self.ENT_Start_Port['state'] = tk.NORMAL;
              self.ENT_End_Port['state'] = tk.NORMAL;

          def BTN_Init_Ping_Handler():
              self.Threaded_Ping_Sweep_1(); 

          def BTN_Init_Port_Handler():
              self.Threaded_Port_Scan_1();   

          def BTN_Get_Current_Network_Settings():
              #Note: Code below works only for Windows. For Linux call "ifconfig" or "iwconfig" respectively.
              IP_Settings = subprocess.run('ipconfig /all',stdout=subprocess.PIPE,text=True).stdout.lower();
              self.TXT_Main_Output.delete("0.0", "end");
              self.TXT_Main_Output.insert("0.0", "\n IP Settings for Current Host:\n\n" + IP_Settings);                 

#---A. Frame: Main Window -------------------------------------------------------------
          self.FRM_Main_Window = tk.Frame(master);
          self.FRM_Main_Window.configure(height=520, width=1100, borderwidth=3, relief="flat", background="#8080ff");
          self.FRM_Main_Window.place(anchor="nw", height=520, width=1100, x=0, y=0);

          self.LAB_Title = tk.Label(self.FRM_Main_Window);
          self.LAB_Title.configure(background="#8080ff",foreground="#FFFFFF", font="{Barlow Condensed} 13 {}", text="Purple Python Port Pinger");
          self.LAB_Title.place(anchor="nw", height=25, width=240, x=870, y=2);  

          self.BTN_Get_Host_Net_Data = tk.Button(self.FRM_Main_Window, command=BTN_Get_Current_Network_Settings);
          self.BTN_Get_Host_Net_Data.configure(background="#ff0000",font="{Lucida Console} 10 {}",foreground="#ffffff",text="Get Host Network Data");
          self.BTN_Get_Host_Net_Data.place(anchor="nw", height=25, width=363, x=395, y=3);          

#---B. Create main Menu Bar------------------------------------------------------------   
          self.master = master;
          self.Main_Menu_Bar = tk.Menu(self.master);
          self.master.config(menu = self.Main_Menu_Bar);

          #File Menu
          self.File_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.File_Menu.add_command(label="New", command=File_Menu_NEW_Handler);
          self.File_Menu.add_command(label="Close", command=File_Menu_CLOSE_Handler);      
          self.File_Menu.add_separator(); # Add separator line to menu
          self.File_Menu.add_command(label="Exit", command=window.quit); #built-in method closes window
          self.Main_Menu_Bar.add_cascade(label="File", menu=self.File_Menu); #adds menu File_Menu to Main_Menu_Bar             
     
          #View Menu
          self.View_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.View_Menu.add_command(label="Zoom In +", command=View_Menu_ZOOMIN_Handler);
          self.View_Menu.add_command(label="Zoom Out -", command=View_Menu_ZOOMOUT_Handler);
          self.Main_Menu_Bar.add_cascade(label="View", menu=self.View_Menu); #adds menu File_Menu to Main_Menu_Bar    

          #Help Menu
          self.Help_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.Help_Menu.add_command(label="Get Network Data", command=Help_Menu_Get_Network_Data_Handler);
          self.Help_Menu.add_command(label="Help", command=Help_Menu_HELP_Handler);
          self.Help_Menu.add_command(label="About", command=Help_Menu_ABOUT_Handler);
          self.Main_Menu_Bar.add_cascade(label="Help", menu=self.Help_Menu); #adds menu File_Menu to Main_Menu_Bar                   

#---C. Frame: Ping Sweeper -------------------------------------------------------------          
          self.LFRM_Ping_Sweeper = tk.LabelFrame(self.FRM_Main_Window);
          self.LFRM_Ping_Sweeper.configure(height=200, width=377, borderwidth=3, relief="sunken", background="#8080ff", text="Ping Sweeper");
          self.LFRM_Ping_Sweeper.place(anchor="nw", height=200, width=377, x=5, y=3); 

          self.RB_Activate_Ping_Sweeper = tk.Radiobutton(self.LFRM_Ping_Sweeper, variable=self.RB_Ping_Or_Port_Var, value=1, command=RB_Ping_Selection_Handler);
          self.RB_Activate_Ping_Sweeper.configure(height=25, width=190, background="#8080ff", font="{Arial} 12 {}", text="Activate Ping Sweeper");
          self.RB_Activate_Ping_Sweeper.place(anchor="nw", height=25, width=190, x=18, y=10);            

          self.LAB_Network = tk.Label(self.LFRM_Ping_Sweeper);
          self.LAB_Network.configure(background="#8080ff", borderwidth=0, relief="flat", font="{Arial} 12 {}", anchor="nw", text="Network:");
          self.LAB_Network.place(anchor="w", x=22, y=57);

          self.LAB_Start_Host = tk.Label(self.LFRM_Ping_Sweeper);
          self.LAB_Start_Host.configure(background="#8080ff", borderwidth=0, relief="flat", font="{Arial} 12 {}", anchor="nw", text="Start Host:");
          self.LAB_Start_Host.place(anchor="w", x=22, y=92);

          self.LAB_End_Host = tk.Label(self.LFRM_Ping_Sweeper);
          self.LAB_End_Host.configure(background="#8080ff", borderwidth=0, relief="flat", font="{Arial} 12 {}", anchor="nw", text="End Host:");
          self.LAB_End_Host.place(anchor="w", x=22, y=127);

          self.ENT_Network = tk.Entry(self.LFRM_Ping_Sweeper);
          self.ENT_Network.configure(width=232, background="#000000", foreground="#ffffff", borderwidth=3, justify="center", relief="sunken", font="{Courier} 12 {}");
          self.ENT_Network.insert("0", "192.168.0.0");
          self.ENT_Network.place(anchor="nw", height=25, width=232, x=105, y=45);

          self.ENT_Start_Host = tk.Entry(self.LFRM_Ping_Sweeper);
          self.ENT_Start_Host.configure(width=232, background="#000000", foreground="#ffffff", borderwidth=3, justify="center", relief="sunken", font="{Courier} 12 {}");
          self.ENT_Start_Host.insert("0", "1");
          self.ENT_Start_Host.place(anchor="nw", height=25, width=232, x=105, y=80);

          self.ENT_End_Host = tk.Entry(self.LFRM_Ping_Sweeper);
          self.ENT_End_Host.configure(width=232, background="#000000", foreground="#ffffff", borderwidth=3, justify="center", relief="sunken", font="{Courier} 12 {}");
          self.ENT_End_Host.insert("0", "254");
          self.ENT_End_Host.place(anchor="nw", height=25, width=232, x=105, y=115);

          self.BTN_Init_Ping = tk.Button(self.LFRM_Ping_Sweeper, command=BTN_Init_Ping_Handler);
          self.BTN_Init_Ping.configure(background="#ff0000",font="{Lucida Console} 12 {}",foreground="#ffffff",text="INITIATE");
          self.BTN_Init_Ping.place(anchor="nw", height=30, width=320, x=22, y=147);
          

#---D. Frame: Port Scanner -------------------------------------------------------------            
          self.LFRM_Port_Scanner = tk.LabelFrame(self.FRM_Main_Window);
          self.LFRM_Port_Scanner.configure(height=200, width=377, borderwidth=3, relief="sunken", background="#8080ff", text="Port Scanner");
          self.LFRM_Port_Scanner.place(anchor="nw", height=200, width=377, x=5, y=310);       

          self.RB_Activate_Port_Scanner = tk.Radiobutton(self.LFRM_Port_Scanner, variable=self.RB_Ping_Or_Port_Var, value=2, command=RB_Port_Selection_Handler);
          self.RB_Activate_Port_Scanner.configure(height=25, width=190, background="#8080ff", font="{Arial} 12 {}", text="Activate Port Scanner");
          self.RB_Activate_Port_Scanner.place(anchor="nw", height=25, width=190, x=18, y=10);

          self.LAB_Host = tk.Label(self.LFRM_Port_Scanner);
          self.LAB_Host.configure(background="#8080ff", borderwidth=0, relief="flat", font="{Arial} 12 {}", anchor="nw", text="Host:");
          self.LAB_Host.place(anchor="nw", x=20, y=45);

          self.LAB_Start_Port = tk.Label(self.LFRM_Port_Scanner);
          self.LAB_Start_Port.configure(background="#8080ff", borderwidth=0, relief="flat", font="{Arial} 12 {}", anchor="nw", text="Start Port:");
          self.LAB_Start_Port.place(anchor="nw", x=20, y=80);

          self.LAB_End_Port = tk.Label(self.LFRM_Port_Scanner);
          self.LAB_End_Port.configure(background="#8080ff", borderwidth=0, relief="flat", font="{Arial} 12 {}", anchor="nw", text="End Port:" );
          self.LAB_End_Port.place(anchor="nw", x=20, y=115);

          self.ENT_Host = tk.Entry(self.LFRM_Port_Scanner);
          self.ENT_Host.configure(width=232, background="#000000", foreground="#ffffff", borderwidth=3, justify="center", relief="sunken", font="{Courier} 12 {}");
          self.ENT_Host.insert("0", "192.168.0.0");
          self.ENT_Host.place(anchor="nw", height=25, width=232, x=105, y=45);

          self.ENT_Start_Port = tk.Entry(self.LFRM_Port_Scanner);
          self.ENT_Start_Port.configure(width=232, background="#000000", foreground="#ffffff", borderwidth=3, justify="center", relief="sunken", font="{Courier} 12 {}");
          self.ENT_Start_Port.insert("0", "1");
          self.ENT_Start_Port.place(anchor="nw", height=25, width=232, x=105, y=80)

          self.ENT_End_Port = tk.Entry(self.LFRM_Port_Scanner);
          self.ENT_End_Port.configure(width=232, background="#000000", foreground="#ffffff", borderwidth=3, justify="center", relief="sunken", font="{Courier} 12 {}");
          self.ENT_End_Port.insert("0", "65534");
          self.ENT_End_Port.place(anchor="nw", height=25, width=232, x=105, y=115)

          self.BTN_Init_Port = tk.Button(self.LFRM_Port_Scanner, command=BTN_Init_Port_Handler);
          self.BTN_Init_Port.configure(background="#ff0000",font="{Lucida Console} 12 {}",foreground="#ffffff",text="INITIATE");
          self.BTN_Init_Port.place(anchor="nw", height=30, width=320, x=22, y=147);


#---E. Frame: Main Output -------------------------------------------------------------
          self.LFRM_Main_Output = tk.LabelFrame(self.FRM_Main_Window);
          self.LFRM_Main_Output.configure(height=480, width=700, borderwidth=3, relief="sunken", background="#8080ff", text="Main Output");
          self.LFRM_Main_Output.place(anchor="nw", height=480, width=700, x=390, y=30);

          self.SB_Vert_TXT_Main_Output = tk.Scrollbar(self.LFRM_Main_Output, orient = tk.VERTICAL);
          self.SB_Vert_TXT_Main_Output.pack(side=tk.RIGHT, fill=tk.Y);

          self.TXT_Main_Output = tk.Text(self.LFRM_Main_Output, yscrollcommand=self.SB_Vert_TXT_Main_Output.set);
          self.TXT_Main_Output.configure(height=457, width=678, background="#000000", foreground="#ffffff", borderwidth=3, relief="sunken", font="{Courier} 10 {}");
          self.TXT_Main_Output.insert("0.0", "\n This is the MAIN OUTPUT panel.\n Ping sweep and port scan results will display here.");
          self.TXT_Main_Output.place(anchor="nw", height=457, width=678, x=1, y=1);

          self.SB_Vert_TXT_Main_Output.config(command=self.TXT_Main_Output.yview); #set scrollbar behavior

          #Populate text object on starup with example text
          self.TXT_Main_Output.insert(tk.END,"\n\n");
          for Entry_Line_Item in range(255):
              self.TXT_Main_Output.insert(tk.END, "Ping " + str(Entry_Line_Item) + "\n");   

#---F. Frame: Current Network  -------------------------------------------------------------
          self.LFRM_Current_Network = tk.LabelFrame(self.FRM_Main_Window);
          self.LFRM_Current_Network.configure(height=95, width=377, borderwidth=3, relief="sunken", background="#8080ff", text="Current Network");
          self.LFRM_Current_Network.place(anchor="nw", height=95, width=377, x=5, y=210);  

          self.TXT_Current_Network = tk.Text(self.LFRM_Current_Network);
          self.TXT_Current_Network.configure(height=76, width=370, background="#000000", foreground="#ffffff", borderwidth=3, relief="sunken", font="{Courier} 9 {}");
          self.TXT_Current_Network.place(anchor="nw", height=76, width=370, x=1, y=1);                                       

#---G. Default Load Settings -------------------------------------------------------------
          self.RB_Ping_Or_Port_Var.set(1); #set default radio button selection
          RB_Ping_Selection_Handler();
          self.Get_Current_Network();

#---End Class----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----Invocations-----
GUI = PPPPP_GUI(window); #instantiate GUI class

#---Launch Main Window---
window.mainloop();

