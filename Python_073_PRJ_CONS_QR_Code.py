# Title: Project - Generating QR codes
# Author: C. S. Germany 08/08/2022

#Dependecy: pip install qrcode

import qrcode;

MESSAGE = "Python - I love you truly madly deeply!";
Super_Secret_QR_Image = qrcode.make(data=MESSAGE);
Super_Secret_QR_Image.save("To_My_Forbidden_Love.png");

