# Title: Project - Google FooBar Challenge
# Author: C. S. Germany 08/08/2022

#

import sys

def solution(x):
    ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    REVERSEA = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
    DESCRAMBLED = []
    Alphabet_Counter = 0

    for y in x:
        #print("\n----------------------------------------------------------");
        #print("Processing char:",x);
        if(y.isalpha() and y.islower()):
           for z in ALPHABET:
               Alphabet_Counter = Alphabet_Counter + 1
               if(z == y):    
                  DESCRAMBLED.append(REVERSEA[Alphabet_Counter-1])
                  Alphabet_Counter = 0
                  break
        else: 
              DESCRAMBLED.append(y)          
    
    CONVERTED = ""
    RESULT = CONVERTED.join(DESCRAMBLED)
    return RESULT


#----------------------------------------------------------------------------------------------------------------------------

#Invocations
solution("vmxibkgrlm");
#print("Decrypted:",solution("vmxibkgrlm"));
#print("Decrypted:",solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"));
#print("Decrypted:",solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"));