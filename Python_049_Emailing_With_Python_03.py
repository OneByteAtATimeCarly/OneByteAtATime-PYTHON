# Title: Emailing with Python 3 (Console) - Used to work with GMAIL until Google disabled this functionality
# Author: C. S. Germany 01/15/2022

# Used to work with GMAIL until Google disabled this functionality.
# Now you have to buy it. No longer free.


#---FUNCTION----------------------------------------------------------------------------------------------------------------------
# Send plain-text email using SMTP_SSL()
def Email_1():
    import smtplib;
    from email.mime.text import MIMEText;
    import socket;
    import base64;

    socket.setdefaulttimeout(None);
    HOST = "smtp.gmail.com";
    PORT = "587";
    sender = "Carly.Salali.Germany@gmail.com";
    receiver = "Carly.Salali.Germany@gmail.com";
    password = "IDK_Wh@t_D0_Y0u_Th1nk?";
    
    MESSAGE = "Hi Carly! Don't foget to remind yourself. Sincerely and reflexively, Carly.";
    MESS = MIMEText(MESSAGE);
    MESS['From'] = sender;
    MESS['To'] = receiver;
    MESS['Subject'] = 'Subject - Hello World';
    PAYLOAD = encode(message.as_bytes()).decode());

    #b64_bytes_data = base64.urlsafe_b64encode(MESS.as_bytes());
    #b64_string_data = b64_bytes_data.decode();
    #PAYLOAD = {'raw': b64_string_data};

    server = smtplib.SMTP();
    server.connect(HOST, PORT);
    server.starttls();
    server.login(sender,password);
    server.sendmail(sender,receiver,PAYLOAD);
    server.close();
#---------------------------------------------------------------------------------------------------------------------------------    






#---FUNCTION----------------------------------------------------------------------------------------------------------------------
# Send plain-text email using SMTP_SSL()
def Email_1():
    import smtplib, ssl;

    port = 465;  # For SSL
    smtp_server = "appmail.daytonastate.edu";
    sender_email = "Carly.Germany@daytonastate.edu";  
    receiver_email = "Carly.Germany@daytonastate.edu";
    password = input("Type password and press enter: ");

    message = """\
    Subject: Hi Carly!
    Re: Reminding myself
    This message is sent to you from yourself.
    This is a reminder to reming yourself.

    Reflexively and Sincerely,
    Carly Salali
    """

    context = ssl.create_default_context();

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
         server.login(sender_email, password);
         server.sendmail(sender_email, receiver_email, message);
#---------------------------------------------------------------------------------------------------------------------------------  