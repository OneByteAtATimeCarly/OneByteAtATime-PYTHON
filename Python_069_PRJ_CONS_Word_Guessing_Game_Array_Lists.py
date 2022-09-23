# Title: Project - Word Guessing Game
# Author: C. S. Germany 01/15/2022 

#More practice with Python array List objects and iterables

#Imports
from pydoc import doc
import random;
from os import system;

#NULL = input("Press \"ENTER\" to continue.");

#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def MAIN():

    #A 2D array List iterable. An array of arrays.
    WordBank = [ ["entitlement", "You think you deserve it."],
                 ["plagiarism", "Taking the credit for someone else's work."],
                 ["revenge", "Don't get mad, get even."],
                 ["generation", "By survival of the FITTEST, the present one will soon be extinct."],
                 ["pathetic", "It's always someone else's fault, it's not my responsibility."],
                 ["obsolete", "No longer relevant to the situation."],
                 ["entrapment", "Deceptively misleading situation..."],
                 ["scapegoat", "Blame it on me."],
                 ["cryptic", "l00k @ th1s, 1 m sew kewl n a11 l0ft3"],
                 ["disembowel", "Gut-wrenching..."],
                 ["adolescent", "You're not the boss of me..."],
                 ["agoraphobia", "Fear of open spaces..."],
                 ["claustrophobia", "Fear of closed spaces..."],
                 ["apocalyptic", "Of or pertaining to the end..."],
                 ["karma", "Getting what you deserve..."] ];

    NumberOfWords = len(WordBank);
    NumWordsToGuess = 5;

    RandomWords = [];
    for w in range(0,5):
        print("Creating element # ",w);
        RandomWords.append(0);

    RANDNUM = 0;
    Counter = 0;
    NumGuesses = 3;
    SCRAMBLE = "";
    GUESS = "";
    Score = 0;

    #system('cls');
    print("\nWord Guessing Game 1.0 - 2022 C.S.G.\n");  
    print("\nYou must guess " + str(NumWordsToGuess) + " scrambled words.");
    print("You will get " + str(NumGuesses) + " guesses per word.");

    #Generate array of random numbers without DUPLICATES
    while(Counter < len(RandomWords)):
          RANDNUM = random.randint(0,(NumberOfWords-1));
          Repeat = False;

          while(Repeat == False):
                for x in range(len(RandomWords)):
                    if(RANDNUM == RandomWords[x]):
                       print("Duplicate # found! Re-generating #.");
                       Repeat = True;
                       break;
                    elif(x == Counter):
                         RandomWords[Counter] = RANDNUM;
                         Counter += 1;
                         Repeat = True;
                         break;

    print("Random # List = ",RandomWords);                    

    for y in range(NumWordsToGuess):
        RandWord = RandomWords[y];
        WORD = WordBank[RandWord][0];
        CLUE = WordBank[RandWord][1];
        SCRAMBLE = list(WORD); #convert string to List of char (char array)

        #Scramble Randomly Chosen Word like a Bubble Sort
        for z in range(len(WORD)):
            RandNum = random.randint(0,(len(WORD)-1));
            TEMP1 = SCRAMBLE[RandNum];
            TEMP2 = SCRAMBLE[RandNum-1];
            SCRAMBLE[RandNum-1] = TEMP1;
            SCRAMBLE[RandNum] = TEMP2;

        Scrambled_Word = ''.join(SCRAMBLE);          
        print("\nGuessing for word # " + str((y+1)) + ".");
        print("Clue: " + CLUE);
        print("Scramble: " + Scrambled_Word);
        print("-------------------------");

        Guess_Counter = 0;

        while(Guess_Counter < NumGuesses):
            Guess_Counter += 1;
            GUESS = input("Attempt # " + str(Guess_Counter) + "? ");
            if(GUESS == WORD):
               print("\nYou did it! You guessed my word.");
               print("My word was: " + WORD);
               Guess_Counter = NumGuesses;
               Score += 1;
            else:
                  print("Sorry, you did not guess my word.\n");
                  if(Guess_Counter >= NumGuesses):
                     print("You are all out of guesses for this word.");
                     print("My word was: " + WORD);
                  else:
                     print("You have made " + str(Guess_Counter) + " guess(es) so far.");
                     print("Guess again!");

    print("\nGame Over.");
    print("\nFinal Score = " + str(Score));
    NULL = input("\nPress \"ENTER\" to continue.");           
               





#--------------------------------------------------------------------------------------------------------------------------------------------


#-----Invocations-----
MAIN();


