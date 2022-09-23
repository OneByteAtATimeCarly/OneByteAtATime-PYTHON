# Title: Emailing with Python 2 (Console) - Another Way
# Author: C. S. Germany 01/15/2022

import smtplib
#SERVER = "localhost"

FROM = 'M365Relay@tenant.domainname.com'

TO = ["Carly.Salali.Germany@gmail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."


# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

password = "SuperC@l@Fr@j@l@st1c";
server = smtplib.SMTP('smtp.office365.com');
server.starttls();
server.login(FROM,password);
server.sendmail(FROM, TO, message);
server.quit();


