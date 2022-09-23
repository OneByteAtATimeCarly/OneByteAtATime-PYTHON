# Title: Project - QUIZ - Parallel vs. 2D Array List objects
# Author: C. S. Germany 01/15/2022 

# Python QUIZ Project - To illustrate the difference between Parallel vs. 2D Array List objects

#Imports
from os import system;

#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def MAIN():
    system('cls');
    print("\n   QUIZ: Multi-dimensional 2D vs. Parallel Arrays\n");
    CHOICE = "*";

    while(CHOICE != "1" and CHOICE != "2" and CHOICE != "3"):
          print("\n\n            Select an Option:");
          print("------------------------------------------");
          print("|                                        |");
          print("|   (M)ulti-dimensional 2D Array Quiz.   |");
          print("|   (P)arallel Array Quiz                |");
          print("|   (Q)uit                               |");
          print("|                                        |");
          print("------------------------------------------");
          CHOICE = input("           Your CHOICE? ");

          if(CHOICE == "p"): QUIZ_PARALLEL_ARRAY();
          elif(CHOICE == "m"): QUIZ_MULTI_DIMENSIONAL_ARRAY();
          elif(CHOICE == "q"): break;
          else: print("\n Invalid option. Please choose again."); 
#--------------------------------------------------------------------------------------------------------------------------------------------


#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def QUIZ_PARALLEL_ARRAY():
    #Example of using PARALLEL Arrays. 4 separate List array objects that maintain a parallel relationship.
    MaxWrongGuesses = 3;
    TotalWrongGuesses = 0;
    WrongPerQuestionCount = 0;
    RightCount = 0;
    Score = 0;  

    Questions = ["Most lethal, maneuverable dog fighter America ever made?", 
                "Who was the harbinger of death that actually saved humans and Cylons?", 
                "In the end it doesn't even matter?", 
                "Sci-Fi novel by Isaac Asimov that introduced \"3 Laws Safe\"?", 
                "Quantum theory that allows instantaneous FTL communication over any distance?"];

    Answers = ["f-14 tomcat", 
               "starbuck", 
               "lincoln park", 
               "i robot", 
               "entanglement"];

    Clues= ["When jet fighters MEOW ...", 
            "Apollo's BFF", 
            "One thing, I don't know why, doesn't even matter how hard you try.", 
            "Cannot by action or omission of action harm a human.", 
            "Even if on opposite sides of the universe, 1 spin relates to the other."];

    UsersInput =[ "", "", "", "", ""];            

    system('cls');
    print("QUIZ using PARALLEL Arrays: 4 separate Python List objects that maintain a parallel relationship.");
    NULL = input("Press \"ENTER\" to continue.");

    for x in range(len(Questions)):
        print("\nQuestion ",str(x+1),": ",Questions[x],sep='');
        UsersInput[x] = input("Answer? ");
        print("You said: \"",UsersInput[x],"\"",sep='');

        if(UsersInput[x] != Answers[x]):
           TotalWrongGuesses += 1;
           WrongPerQuestionCount += 1;

           if(WrongPerQuestionCount < MaxWrongGuesses):
              print("\nSorry. That was wrong.");
              print("Here's a hint: " + Clues[x] + "");
              x -= 1;
           else: 
              print("\nUnfortunately, you have exceeded the maximim number of guesses for this question.");
              print("The maximum number of guesses is set to:",MaxWrongGuesses);
              print("Moving on to next question now.");
        else:
              print("\nThat's it! You got it right!");
              Score += 1; 
              RightCount += 1;
              WrongPerQuestionCount = 0;               

        print("\n**********Current Status**********");
        print("TOTAL Wrong Guesses:",TotalWrongGuesses);
        print("Wrong Guesses for Current Question:",WrongPerQuestionCount);
        print("TOTAL Questions Answered Correctly:",RightCount);
        
        #Reset wrong counter for next question if exceeded max num guesses or player is correct
        if(WrongPerQuestionCount > (MaxWrongGuesses-1)):
           print("\nResetting wrong question counter.");
           WrongPerQuestionCount = 0;

        NULL = input("Press \"ENTER\" to continue.");    

    print("\nQUIZ complete.");
    FinalScore = Score * 20;
    
    if(FinalScore == 0): print("Score:",FinalScore,"\nComment: NOTHING? Not even 1? Try GUESSING next time!\nGrade: F");
    if(FinalScore == 20): print("Score:",FinalScore,"\nComment: Got at least 1 right.\nGrade: F");
    if(FinalScore == 40): print("Score:",FinalScore,"\nComment: Got at least 2 right\nGrade: D");
    if(FinalScore == 60): print("Score:",FinalScore,"\nComment: Got at least 3 right\nGrade: C");
    if(FinalScore == 80): print("Score:",FinalScore,"\nComment: Got at least 4 right\nGrade: B");
    if(FinalScore == 100): print("Score:",FinalScore,"\nComment: Got ALL of them right! Well done!\nGrade: A++");

    print("\nExiting QUIZ_PARALLEL_ARRAY function.");
    NULL = input("Press \"ENTER\" to continue.");
#--------------------------------------------------------------------------------------------------------------------------------------------      



#---FUNCTION---------------------------------------------------------------------------------------------------------------------------------
def QUIZ_MULTI_DIMENSIONAL_ARRAY():
    #Example of using MULTI-DIMENSIONAL Arrays. In this instance, a single 2D List array object acting as an array of arrays replaces 4 parallel arrays.
    MaxWrongGuesses = 3;
    TotalWrongGuesses = 0;
    WrongPerQuestionCount = 0;
    RightCount = 0;
    Score = 0;
    GuessWasCorrect = False;

    QandClueandA = [ ["El dia de los muertos? ","october 30","Same month as Halloween.","****"],
                     ["Favorite game? ","descent 3","Maze-like first person shooter game.","****"],
                     ["Best sci-fi series ever made? ","bsg","Frack off cylon!","****"],
                     ["Favorite hobby? ","music","The hills are alive...","****"],
                     ["Popular vacation destination? ","bahamas","Ja man, on da beaches.","****"] 
                   ]; 

    system('cls');
    print("QUIZ using MULTI-DIMENSIONAL Arrays: A single 2D List array object acting as an array of arrays replaces 4 parallel arrays.");
    NULL = input("\nPress \"ENTER\" to continue.");   

    x = 0;

    while(x < len(QandClueandA)): 
        system('cls');
        print("\nQuestion " + str((x+1)) + ": " + QandClueandA[x][0]); 
        QandClueandA[x][3] = (input("\nANSWER? ")).lower(); 
        print("You said: " + QandClueandA[x][3]);

        if(QandClueandA[x][1] != QandClueandA[x][3]):
           TotalWrongGuesses +=1;
           WrongPerQuestionCount +=1;

           if(WrongPerQuestionCount < MaxWrongGuesses):
              print("\nSorry. That was wrong.");
              print("Here's a hint: " + QandClueandA[x][2] + "");
              x -= 1;    
           else:
                 print("\nUnfortunately, you have exceeded the maximim number of guesses" +
                       "\nfor this question, which is: " + str(MaxWrongGuesses) + ".");
                 print( "Moving on to next question now.");
        else:
              print("\nThat's it! You got it right!");
              Score += 1; 
              RightCount += 1;
              GuessWasCorrect = True;

        print("\n**********Current Status**********");
        print("TOTAL Wrong Guesses:",TotalWrongGuesses);
        print("Wrong Guesses for Current Question:",WrongPerQuestionCount);
        print("TOTAL Questions Answered Correctly:",RightCount);

        #Reset wrong counter for next question if exceeded max num guesses or player is correct
        if(WrongPerQuestionCount > (MaxWrongGuesses-1) or GuessWasCorrect == True):
           print("\nResetting wrong question counter.");
           WrongPerQuestionCount = 0;
           GuessWasCorrect = False; 

        x += 1;
        NULL = input("\nPress \"ENTER\" to continue.");    

    print("\nQUIZ complete.");
    FinalScore = Score * 20; 

    if(FinalScore == 0): print("Score:",FinalScore,"\nComment: NOTHING? Not even 1? Try GUESSING next time!\nGrade: F");
    if(FinalScore == 20): print("Score:",FinalScore,"\nComment: Got at least 1 right.\nGrade: F");
    if(FinalScore == 40): print("Score:",FinalScore,"\nComment: Got at least 2 right\nGrade: D");
    if(FinalScore == 60): print("Score:",FinalScore,"\nComment: Got at least 3 right\nGrade: C");
    if(FinalScore == 80): print("Score:",FinalScore,"\nComment: Got at least 4 right\nGrade: B");
    if(FinalScore == 100): print("Score:",FinalScore,"\nComment: Got ALL of them right! Well done!\nGrade: A++");

    print("\nExiting QUIZ_MULTI_DIMENSIONAL_ARRAY function.");
    NULL = input("Press \"ENTER\" to continue.");           

#--------------------------------------------------------------------------------------------------------------------------------------------      



#---Invocations-----
MAIN();

