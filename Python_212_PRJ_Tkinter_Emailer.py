#Title: Emailer (using Python and tkinter GUI)
#Author: Carly S. Germany
#Created: 04/17/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

import tkinter as tk;
import tkinter.ttk as ttk;
import smtplib;
from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;

#O365 smtp server = smtp.office365.com
#GMAIL smtp server = smtp.gmail.com

#Globals
window = tk.Tk();
window.title("Python tkinter - TKMailer - 2022 - Carly Salali Germany");
window_Width = 600;
window_Height = 460;
ScreenWidth = window.winfo_screenwidth();
ScreenHeight = window.winfo_screenheight();
Appear_in_the_Middle = '%dx%d+%d+%d' % (window_Width, window_Height, (ScreenWidth - window_Width) / 2, (ScreenHeight - window_Height) / 2);
window.geometry(Appear_in_the_Middle);
window.resizable(width=False, height=False);
window.configure(bg='#E6E6FA'); 
GUI = None; #pointer that will be used to reference GUI class for functions (instantiated later)

#---Class-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Emailer_GUI:

      #Class Data Members
      The_Sender = "";
      The_Recipient = "";
      The_Port = "";
      The_Server = "";
      The_Password = "";
      The_Subject = "";
      The_Message = "";

    #--------------------------------------------------------------------------------------------------------------
      def Email_Them(self):
          #Display Email Parameters
          print("\n-----------------------------------------------------------------");
          print("Server:",self.The_Server);
          print("Port:",self.The_Port);
          print("Password:",self.The_Password);
          print("Sender:",self.The_Sender);
          print("Recipient:",self.The_Recipient);
          print("Subject:",self.The_Subject);
          print("Message:",self.The_Message);
          print("\n-----------------------------------------------------------------");

          #Setup MIME
          message = MIMEMultipart();
          message['From'] = self.The_Sender;
          message['To'] = self.The_Recipient;
          message['Subject'] = self.The_Subject;

          #The body and the attachments for the mail
          message.attach(MIMEText(self.The_Message, 'plain'));

          #Create SMTP session for sending the email
          session = smtplib.SMTP(self.The_Server,self.The_Port);
          session.starttls(); #enable security
          session.login(self.The_Sender, self.The_Password);
          Message_Text = message.as_string();
          session.sendmail(self.The_Sender, self.The_Recipient, Message_Text);
          session.quit();
          print('Mail Sent');
    #--------------------------------------------------------------------------------------------------------------      

      #Constructor
      def __init__(self, master=None):

          #ENT Text Variables
          Sender_Data = tk.StringVar();
          Recipient_Data = tk.StringVar();
          Server_Data = tk.StringVar();
          Password_Data = tk.StringVar();
          Subject_Data = tk.StringVar();
          Port_Data = tk.StringVar();

          #Event Handlers
          def Handle_Button_SEND():
              self.The_Sender = Sender_Data.get();
              self.The_Recipient = Recipient_Data.get();
              self.The_Port = Port_Data.get();
              self.The_Server = Server_Data.get();
              self.The_Password = Password_Data.get();
              self.The_Subject = Subject_Data.get();
              self.The_Message = self.TXT_Message_Body.get("1.0",tk.END);
              self.Email_Them();

          #GUI Widgets and Components
          self.FRM_Main_Window = tk.Frame(master);
          self.FRM_Main_Window.configure(height=460, width=600, borderwidth=3, relief="flat", background="#E6E6FA");
          self.FRM_Main_Window.place(anchor="nw", height=460, width=600, x=0, y=0);

          self.LAB_Title = tk.Label(self.FRM_Main_Window, background="#E6E6FA", foreground="#000000");
          self.LAB_Title.configure(justify=tk.LEFT, anchor="w", font=('Helvetica 10'), text="tkinter EMailer - 2022 - Carly Salali Germany");
          self.LAB_Title.place(anchor="nw", width=300, x=10, y=5);

          self.LAB_Sender = tk.Label(self.FRM_Main_Window, background="#E6E6FA", foreground="#000000");
          self.LAB_Sender.configure(justify=tk.LEFT, anchor="w", font=('Helvetica 9'), text="Sender:");
          self.LAB_Sender.place(anchor="nw", width=90, x=10, y=40);

          self.ENT_Sender = tk.Entry(self.FRM_Main_Window, textvariable=Sender_Data);
          self.ENT_Sender.configure(width=222, justify="center", font=('Helvetica 9'), borderwidth=2, relief="sunken", state="normal");
          self.ENT_Sender.place(anchor="nw", height=20, width=222, x=73, y=40);

          self.LAB_Recipient = tk.Label(self.FRM_Main_Window, background="#E6E6FA", foreground="#000000");
          self.LAB_Recipient.configure(justify=tk.LEFT, anchor="w", font=('Helvetica 10'), text="Recipient:");
          self.LAB_Recipient.place(anchor="nw", width=90, x=10, y=65);

          self.ENT_Recipient = tk.Entry(self.FRM_Main_Window, textvariable=Recipient_Data);
          self.ENT_Recipient.configure(width=222, justify="center", font=('Helvetica 9'), borderwidth=2, relief="sunken", state="normal");
          self.ENT_Recipient.place(anchor="nw", height=20, width=222, x=73, y=65);

          self.LAB_Port = tk.Label(self.FRM_Main_Window, background="#E6E6FA", foreground="#000000");
          self.LAB_Port.configure(justify=tk.LEFT, anchor="w", font=('Helvetica 9'), text="Port:");
          self.LAB_Port.place(anchor="nw", width=90, x=304, y=10);

          self.ENT_Port  = tk.Entry(self.FRM_Main_Window, textvariable=Port_Data);
          self.ENT_Port.configure(width=218, justify="center", font=('Helvetica 9'), borderwidth=2, relief="sunken", state="normal");
          self.ENT_Port.place(anchor="nw", height=20, width=218, x=368, y=10);

          self.LAB_Server = tk.Label(self.FRM_Main_Window, background="#E6E6FA", foreground="#000000");
          self.LAB_Server.configure(justify=tk.LEFT, anchor="w", font=('Helvetica 9'), text="Server:");
          self.LAB_Server.place(anchor="nw", width=90, x=304, y=40);

          self.ENT_Server = tk.Entry(self.FRM_Main_Window, textvariable=Server_Data);
          self.ENT_Server.configure(width=218, justify="center", font=('Helvetica 9'), borderwidth=2, relief="sunken", state="normal");
          self.ENT_Server.place(anchor="nw", height=20, width=218, x=368, y=40);

          self.LAB_Password = tk.Label(self.FRM_Main_Window, background="#E6E6FA", foreground="#000000");
          self.LAB_Password.configure(justify=tk.LEFT, anchor="w", font=('Helvetica 9'), text="Password:");
          self.LAB_Password.place(anchor="nw", width=90, x=304, y=65);
        
          #Uses show="*" to implement masking for password entry
          self.ENT_Password = tk.Entry(self.FRM_Main_Window, textvariable=Password_Data);
          self.ENT_Password.configure(width=218, justify="center", font=('Helvetica 9'), borderwidth=2, relief="sunken", state="normal",show="*");
          self.ENT_Password.place(anchor="nw", height=20, width=218, x=368, y=65);

          self.LAB_Subject = tk.Label(self.FRM_Main_Window, background="#E6E6FA", foreground="#000000");
          self.LAB_Subject.configure(justify=tk.LEFT, anchor="w", font=('Helvetica 9'), text="Subject:");
          self.LAB_Subject.place(anchor="nw", width=90, x=10, y=100);

          self.ENT_Subject = tk.Entry(self.FRM_Main_Window, textvariable=Subject_Data);
          self.ENT_Subject.configure(width=512, justify="center", font=('Helvetica 9'), borderwidth=2, relief="sunken", state="normal");
          self.ENT_Subject.place(anchor="nw", height=20, width=512, x=73, y=100);

          #Message Components - LabelFrame, TEXT widget and vertical scroll bar
          self.LabFrm_Message = tk.LabelFrame(self.FRM_Main_Window);
          self.LabFrm_Message.configure(height=280, width=576, background="#E6E6FA", foreground="#000000", borderwidth=2, relief="sunken", text="Message Body");
          self.LabFrm_Message.place(anchor="nw", height=280, width=576, x=10, y=130);

          self.SB_Vert_TXT_Message_Body = tk.Scrollbar(self.LabFrm_Message, orient = tk.VERTICAL);
          self.SB_Vert_TXT_Message_Body.pack(side=tk.RIGHT, fill=tk.Y);

          self.TXT_Message_Body = tk.Text(self.LabFrm_Message);
          self.TXT_Message_Body.configure(height=250, width=548, background="#FFFFFF", foreground="#000000", borderwidth=2, relief="sunken", takefocus=True);
          self.TXT_Message_Body.place(anchor="nw", height=250, width=548, x=5, y=5);

          self.SB_Vert_TXT_Message_Body.config(command=self.TXT_Message_Body.yview); #set scrollbar behavior   

          self.BTN_Send = tk.Button(self.FRM_Main_Window,command=Handle_Button_SEND);
          self.BTN_Send.configure(height=30, width=576, justify="center", background="#FF0000", foreground="#FFFFFF", text="SEND");
          self.BTN_Send.place(anchor="nw", height=30, width=576, x=10, y=420);

          #Initial Values When Window Launches
          self.TXT_Message_Body.insert("1.0","Hi!");
          Sender_Data.set("Carly.Salali.Germany@gmail.com");
          Recipient_Data.set("Twilight.Sparkle@equestria.com");
          Port_Data.set("587");
          Server_Data.set("smtp.gmail.com");
          Password_Data.set("123456789");
          Subject_Data.set("Greetings! You have been invited to the Grand Gala!");          

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----Invocations-----
GUI = Emailer_GUI(window); #instantiate GUI class
window.mainloop();

