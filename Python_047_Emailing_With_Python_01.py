# Title: Emailing with Python 1 (Console)
# Author: C. S. Germany 01/15/2022

#Note: This methods WORKS and is TESTED with authenticated accounts like M365/O365.


#---FUNCTION----------------------------------------------------------------------------------------------------------------------
# Send plain-text email using SMTP_SSL()
def Email_1():
    import smtplib;
    from email.mime.multipart import MIMEMultipart;
    from email.mime.text import MIMEText;

    Mail_Message = """Hello Carly,
                      Don't forget to remind yoruself to remind yourself not to forget.
                      Sincerely and reflexively,
                      Carly Salali"""

    The_Sender = "M365Relay@tenant.domainname.com";
    The_Receiver = "Carly.Salali.Germany@gmail.com";
    The_Password = "1nTh3End1tD03sntR3@llyM@tt3r";
    
    #Setup MIME
    message = MIMEMultipart();
    message['From'] = The_Sender;
    message['To'] = The_Receiver;
    message['Subject'] = 'Test email from Carly';

    #The body and the attachments for the mail
    message.attach(MIMEText(Mail_Message, 'plain'));

    #Create SMTP session for sending the email
    session = smtplib.SMTP('smtp.office365.com',587); #specify server with port
    session.starttls(); #enable security
    session.login(The_Sender, The_Password);
    Message_Text = message.as_string();
    session.sendmail(The_Sender, The_Receiver, Message_Text);
    session.quit();
    print('Mail Sent');
#---------------------------------------------------------------------------------------------------------------------------------    



#-----Invocations----------
Email_1();

