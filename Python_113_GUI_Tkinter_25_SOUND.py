# Title: Python GUI Programming With TKinter - Widgets - SOUND
# Author: C. S. Germany 02/05/2022

#Note: PlaySound is a very simple module that can play WAV files and MP3s in Python. 
# The FIRST time you want to use Python's PlaySound module, you must install it into your IDE using:
# Example: pip install playsound
# Then RESTART Visual Studio Code or terminal.
# Then just import it with: from playsound import playsound

#---Function---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Normal_PlaySound():
    from playsound import playsound;
    playsound("CoinToss.wav", block=True);  #optional argument block=False causes sound to play asynchronously    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     


#---Function---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Threaded_PlaySound():
    from playsound import playsound;
    import threading;
    import time;
    threading.Thread(target=playsound, args=('CoinToss.wav',), daemon=True).start(); 
    print("");
    for x in range(5):
        print((x+1),"... ",sep='',end='');
        time.sleep(1);  
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
#Normal_PlaySound();
Threaded_PlaySound();



