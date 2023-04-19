#Title: Python Programming 002 - Comment tags, console output using print() and console input using input()
#Author: Carly S. Germany
#Created: 01/15/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

# Two ways to comment out code in Python
# 1. Single line using #
# 2. Mutli-line using a string literal """


# Method 1
# This is an example of using method 1.
# Any comments must be preceded by a "#".

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Topic_0l():

    #1. We can use the input method to retrieve string data from the end-user of our console application.
    Player_Name = input("What's your name, Player One? ");
    print("\nHello,",Player_Name,"!");

    #2. The print() function uses ESCAPE SEQUENCES. Example: \n = new line
    print("\nExample 1: DEFAULT print. Adding an extra line with escape sequence.");
    print("           Line1:  Hello",Player_Name,"!");
    print("           Line2:  Python is fun.");   

    #3. The print() function uses ESCAPE SEQUENCES. Example: \" = literal quote
    print("\nExample 2: DEFAULT print. Adding quotes with escape sequence.");
    print("           Line1:  Hello\"",Player_Name,"\"!");
    print("           Line2:  Python is fun.");    

    #4. The print() function automatically adds a line and a space.
    print("\nExample 3: DEFAULT print. Notice it automatically adds line and a spaces:");
    print("           Line1:  Hello",Player_Name,"!");
    print("           Line2:  Python is fun.");

    #5. When spaces are not desired, you can alter this with sep=''
    print("\nExample 4: NO SPACE print. No more automatic spacing:");
    print("           Line1:  Hello ",Player_Name,"!",sep='');
    print("           Line2:  Python is fun.");

    #6. When lines are not desired, you can alter this with end='' 
    print("\nExample 5: NO LINE print. No more automatic lines, would have to add with escape sequence here:");
    print("           Line1:  Hello",Player_Name,"!",end='');
    print("           Line2:  Python is fun.");    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#-----Invocations-----
Topic_0l();


# Method 2
# The code below wraps multiple lines up in a single comment by turning it into a string literal
# using 3 quote marks to open and close the multi-line comment.

"""
This is a multi-line comment in Python.
It's a string literal. So everything 
between the opening and closing TRIPLE quotes
is part of the comment.
"""
