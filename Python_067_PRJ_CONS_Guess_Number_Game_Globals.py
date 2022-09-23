# Title: Project - Guess Number Game 2
# Author: C. S. Germany 08/11/2021  

#----------------------------------------------------------------------------------------------------
import random;
import math;
from os import system,name;
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#Globals
Number_Low = 0;
Number_High = 0;
#------------------------------------------------------------------------------------------------------------------------

#Note: Defining functions: Statements must have the same indentation level

#------------------------------------------------------------------------------------------------------------------------
def Clear():
    #Windows
    if name == 'nt':
       _ = system('cls')
  
    #Mac,Linux,Posix
    else:
        _ = system('clear')
#------------------------------------------------------------------------------------------------------------------------
def Play_Game():
    global Number_Low;
    global Number_High;

    Clear();
    print("\n  Guess My Number 1.0");

    PlayerName = input("What's your name, player? ");
    Number_Low = int(input("\n  Lowest number in range? "));
    Number_High = int(input("  Highest number in range? "));
    
    x = random.randint(Number_Low, Number_High);

    print("\n  You have ",round(math.log(Number_High - Number_Low + 1, 2))," chances left to guess my number.\n");
 
    GuessCount = 0;  #Initialize number of guesses
 
    #Minimum number of guesses depends on range
    while GuessCount < math.log(Number_High - Number_Low + 1, 2):
          GuessCount += 1;
 
          MESSAGE = "  Guess my number between " + str(Number_Low) + " and " + str(Number_High) + ": ";
          PlayersGuess = int(input(MESSAGE));
 
          if x == PlayersGuess:
                  print("  Woohoo! You guessed it with ",GuessCount," guess(es)");
                  break;
    
          elif x > PlayersGuess:
                   print("  Guess too small.");

          elif x < PlayersGuess:
                   print("  Guess too high.");
 
          #If Guess more than required guesses show number
          if GuessCount >= math.log(Number_High - Number_Low + 1, 2):
                      print("\n  My number was %d" % x);
                      print("\t  Nice game!");

#------------------------------------------------------------------------------------------------------------------------

Play_Game();



 

