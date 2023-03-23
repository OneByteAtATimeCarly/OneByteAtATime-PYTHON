#Title: Guess a Number
#Author: Carly S. Germany
#Created: 08/11/2021 
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

#IMPORTS--------------------------------------------------------------------------------------------------------------------------

import random;
from os import system,name;
#---------------------------------------------------------------------------------------------------------------------------------

#Note: Defining functions: Statements must have the same indentation level
#Syntax for log methods = math.log(x, base)


#FUNCTION-------------------------------------------------------------------------------------------------------------------------
def Clear():
    #Windows OS
    if name == 'nt':
       _ = system('cls');
  
    #Mac,Linux,Posix OS
    else:
        _ = system('clear');

#FUNCTION------------------------------------------------------------------------------------------------------------------------
def Play_Game():
    Number_Low = 0;
    Number_High = 0;
    NumGuesses = 0;

    Clear();
    print("\n  Guess My Number 1.0");

    PlayerName = input("  What's your name, player? ");
    print("  Welcome to a new number guessing game, ",PlayerName,".",sep='');

    Number_Low = int(input("\n  Lowest number in range (1-99)? "));
    Number_High = int(input("  Highest number in range (1-100)? "));

    if((Number_Low > 0 and Number_Low < 100) and (Number_High > 1 and Number_High <= 100)):
        print("\n  High and low numbers allowed. They are within the required range.\n");
    else: 
        print("\n  High or low number OUTSIDE of required range!");
        print("  Since you can't follow the rules, WE'LL set them for you.\n");
        Number_Low = 1;
        Number_High = 10;
    
    print("  Low = ",Number_Low);
    print("  High = ",Number_High);
    The_Range = Number_High - Number_Low;
    print("  Range = ",The_Range);

    if(The_Range >= 0 and The_Range < 10): NumGuesses = 3;
    elif(The_Range >= 10 and The_Range < 20): NumGuesses = 4;
    elif(The_Range >= 20 and The_Range < 30): NumGuesses = 5;
    elif(The_Range >= 30 and The_Range < 40): NumGuesses = 6;
    elif(The_Range >= 40 and The_Range < 50): NumGuesses = 7;
    elif(The_Range >= 50 and The_Range < 101): NumGuesses = 7;

    print("\n  Based on the difficulty of the range between the low and high numbers you provided,");
    print("  You get",NumGuesses,"guesses against my secret number for this game.");
    print("\n  Generating my secret number using your range now ...\n");
        
    The_Secret_Num = random.randint(Number_Low, Number_High);

    GuessCount = 0;  #Initialize number of guesses

    #Minimum number of guesses depends on range
    while(GuessCount < NumGuesses):
          GuessCount += 1;
 
          MESSAGE = "  Guess the secret number between " + str(Number_Low) + " and " + str(Number_High) + ": ";
          PlayersGuess = int(input(MESSAGE));
 
          if The_Secret_Num == PlayersGuess:
                  print("\n  Yay!!! You win, ",PlayerName,"!",sep='');
                  print("  You guessed my secret number with ",GuessCount," guess(es), ",PlayerName,".",sep='');
                  break;
    
          elif The_Secret_Num > PlayersGuess:
                   print("  Guess too small, ",PlayerName,".",sep='');

          elif The_Secret_Num < PlayersGuess:
                   print("  Guess too high, ",PlayerName,".",sep='');
 
    print("\n  Game Over. My secret number was: ",The_Secret_Num,".",sep='');
#---------------------------------------------------------------------------------------------------------------------------------

#Invocations
Play_Game();



 

