#Title: A Google FooBar Challenge Solution
#Author: Carly S. Germany
#Created: 04/05/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

import sys

def solution(x):
    ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
    REVERSEA = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"];
    DESCRAMBLED = [];
    Alphabet_Counter = 0;

    for y in x:
        #print("\n----------------------------------------------------------");
        #print("Processing char:",x);
        if(y.isalpha() and y.islower()):
           for z in ALPHABET:
               Alphabet_Counter = Alphabet_Counter + 1;
               if(z == y):    
                  DESCRAMBLED.append(REVERSEA[Alphabet_Counter-1]);
                  Alphabet_Counter = 0;
                  break;
        else: 
              DESCRAMBLED.append(y);      
    
    CONVERTED = "";
    RESULT = CONVERTED.join(DESCRAMBLED);
    return RESULT;


#----------------------------------------------------------------------------------------------------------------------------

#Invocations
#solution("vmxibkgrlm");
print("\n");
print("Decrypted:",solution("vmxibkgrlm"));
print("Decrypted:",solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"));
print("Decrypted:",solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"));









"""

Criteria for Google Challenege and Constraints you must agree to abide by in Python version:

Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.
Standard libraries are supported EXCEPT for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.
Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

foobar:~/i-love-lance-janice Carly.Salali.Germany$ cat readme.txt
I Love Lance & Janice
=====================

You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, you're pretty sure it's not job-related --
they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that these minions are
wasting time passing non-job-related notes, it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code:

1. Every lowercase letter [a..z] is replaced with the corresponding one in [z..a]
2. Every other character (including uppercase letters and punctuation) is left untouched.  

So in their love-letter code 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.
For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string.
Then you can show the commander proof that these minions are talking
about ""Lance & Janice"" instead of doing their jobs.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?

Input:
solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer.
If your solution passes the test cases, it will be removed from your home folder.
foobar:~/i-love-lance-janice Carly.Salali.Germany$
cat constraints.txt

"""

