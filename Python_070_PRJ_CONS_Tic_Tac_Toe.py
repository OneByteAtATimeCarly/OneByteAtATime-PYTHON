# Title: Project - Tic Tac Toe Game
# Author: C. S. Germany 08/08/2022


#Imports
from os import system;
from re import I;
from typing_extensions import IntVar;

#Globals
EASY = False;

#---FUNCTION---------------------------------------------------------------------------------------------------------------------
def MAIN():
    GameBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];
    SQUARES = 9;
    PlayerPiece = "";
    ComputerPiece = "";
    CurrentPlayer = "";

    PlayerPiece = Introduction();

    #Whatever player chooses, 'X' or 'O'? The computer gets the other.    
    if(PlayerPiece == "X"):
       ComputerPiece = "O";
    else: 
       ComputerPiece = "X";
        
    CurrentPlayer = "X";

    Display(GameBoard);

    while((CheckForAWinner(GameBoard,SQUARES)) == 'N'):
           print("CurrentPlayer = " + CurrentPlayer);

           if(CurrentPlayer == PlayerPiece):
              print("Player's move.");
              CHOICE = PlayerPlays(GameBoard,SQUARES,PlayerPiece);
              N = int(CHOICE); #Note: Have to shave off xtra from Read-Host
              GameBoard[N] = PlayerPiece;
              #GameBoard[CHOICE[1]] = PlayerPiece;
           else: 
                 print("Computer's move.");
                 CHOICE = ComputerPlays(GameBoard,SQUARES,PlayerPiece,ComputerPiece);
                 N = int(CHOICE); #Note: Have to shave off xtra from Read-Host
                 GameBoard[N] = ComputerPiece; 
                 #GameBoard[CHOICE[1]] = ComputerPiece; 

           Display(GameBoard);          

           if(CurrentPlayer == PlayerPiece):
              CurrentPlayer = ComputerPiece;
           else:
                 CurrentPlayer = PlayerPiece;         

    DisplayWinner((CheckForAWinner(GameBoard, SQUARES)),ComputerPiece,PlayerPiece); 

    print("Game Over!");
    print("Exiting Tic Tac Toe");
    
#--------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------
def Introduction():
    FirstOrSecond = "";
    Intelligence = "";
    PlayerPiece = "z";

    system('cls');

    print("\n                   Welcome to Tic Tac Toe 1.0.\n");
    print("This game uses basic logic to emulate the AI of an NPC opponent");
    print("using several decision structures and fuinction calls.");
    print("\nTo play, enter a number, 0 - 8.  The number you enter will");
    print("indicate which of 9 positions you desire below:\n\n");
    print("                 0 | 1 | 2");
    print("               -------------");
    print("                 3 | 4 | 5");
    print("               -------------");
    print("                 6 | 7 | 8\n\n");
    print("The computer will play as your NPC oponent in this game.\n");     

    while(Intelligence != "i" and Intelligence != "s"):
          print("\nDo you want your NPC opponent to be more (i)ntelligent or more (s)imple?\n" +
                "Choosing this option for your opponent sets the difficulty of the game.\n");

          Intelligence = (input("Your choice? ")).lower();
    
          if(Intelligence == "i"):
             print("\nOk, your NPC opponent will be more dificult to beat.\n");
             EASY = False;

          elif(Intelligence == "s"):
               print("\nOk, your NPC opponent will be easier to beat.\n");
               globals()['EASY'] = True;

          else: print("\nThat is an invalid response.\n");              
                 
    while(FirstOrSecond != "y" and FirstOrSecond != "n"):
          print("\nDo you want to make the first move (y/n)?");

          FirstOrSecond = (input("Your choice? ")).lower();
    
          if(FirstOrSecond == "y"):
             print("\nOk, you take the first move.");
             print("You are \"X\". Computer is \"O\".\n");
             PlayerPiece = "X";

          elif(FirstOrSecond == "n"):
               print("\nOk, your NPC opponent takes the first move.\n");
               print("You are \"O\". Computer is \"X\".\n");
               PlayerPiece = "O";

          else: print("\nThat is an invalid response.\n\n"); 

    NULL = input("\nPress \"ENTER\" to continue.");

    return PlayerPiece;
#--------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------
def Display(BOARD):
    print("\n");
    print("\t" + BOARD[0] + " | " + BOARD[1] + " | " + BOARD[2]);
    print("\t---------");
    print("\t" + BOARD[3] + " | " + BOARD[4] + " | " + BOARD[5]);
    print("\t---------");
    print("\t" + BOARD[6] + " | " + BOARD[7] + " | " + BOARD[8]);
    print("\n\n");   
#--------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------
def CheckForAWinner(BOARD,SQUARES):

    #Use Python array List to encode all possible winning patterns
    WINNING_ROWS = [ [0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6] ]; 

    TOTAL_ROWS = 8; 
    
    #If an row has three values that are the same? We have a winner.
    #We will either return 'X' or 'O' as the winner. Or a TIE and 
    #end the game. Or else we will return 'N' and keep playing the game.
    for ROW in range(0,TOTAL_ROWS):
        if(BOARD[WINNING_ROWS[ROW][0]] != ' ' and
           BOARD[WINNING_ROWS[ROW][0]] == BOARD[WINNING_ROWS[ROW][1]] and
           BOARD[WINNING_ROWS[ROW][1]] == BOARD[WINNING_ROWS[ROW][2]]):
           return BOARD[WINNING_ROWS[ROW][0]];

    #If we don't have a winner? Check for a possible TIE.
    NoEmptySpaces = True;

    #Check to see if empty spaces left on BOARD. If not? Game over.
    for x in range(0,SQUARES):
        if(BOARD[x] == ' '):
           NoEmptySpaces = False;

    if(NoEmptySpaces == True):
       return 'T';

    #If nobdy wins, not a tie and empty spaces remain on BOAD return 'N' and keep playing
    return 'N';
#--------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------
#Return whether or not BOARD position is empty or already has a piece on it.
def LegalMove(MOVE,BOARD):
    return (BOARD[MOVE] == ' ');
#--------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------
def PlayerPlays(BOARD,SQUARES,PlayerP):
    print("\nHuman choosing location: ");

    PlayersMove = -1;
    
    while(PlayersMove > SQUARES or PlayersMove < 0 or
          (LegalMove(PlayersMove,BOARD) == False)):
           print("\nChoose a location (0-8): ");  
           PlayersMove = int(input("Your move? "));

           if(PlayersMove > SQUARES or PlayersMove < 0):
              print("\nThat number is outside of the valid range of 1-8.");
           elif(LegalMove(PlayersMove,BOARD) == False):
                print("\nYou cannot choose that location. It already has a(n) " +
                       BOARD[PlayersMove] + " in it.\n");

    return PlayersMove;
#--------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------
def ComputerPlays(BOARD,SQUARES,PlayerP,ComputerP):
    print("\nComputer choosing location: ");

    #1. If computer can win on next choice, then make that choice.
    for x in range(0,SQUARES):
        if(LegalMove(x,BOARD)):
           BOARD[x] = ComputerP;
           if((CheckForAWinner(BOARD, SQUARES)) == ComputerP):
               print(str(x) + "\n",end='');
               return x;
           #Done checking this choice, so undo it.    
           BOARD[x] = ' ';    

    #Note: Computer will not try to block player's winning move if EASY = true
    print("Value of global EASY = ",globals()['EASY']);
    if(globals()['EASY'] == False):
       #2. If human can win on next choice, block that choice.
       for y in range(0,SQUARES):
           if(LegalMove(y,BOARD)):
              BOARD[y] = PlayerP;
              if((CheckForAWinner(BOARD, SQUARES)) == PlayerP):
                  print(str(y) + "\n",end='');
                  return y;
              #Done checking this choice, so undo it.    
              BOARD[y] = ' ';

    #3. If no one can win on next choice? Pick best open square.
    PreferredChoices = [4, 0, 2, 6, 8, 1, 3, 5, 7];       

    for z in range(0,SQUARES): 
        CHOICE = PreferredChoices[z];
        if(LegalMove(CHOICE,BOARD)):
           print(str(CHOICE) + "\n",end='');
           return CHOICE;  

#--------------------------------------------------------------------------------------------------------------------------------



#---FUNCTION---------------------------------------------------------------------------------------------------------------------
def DisplayWinner(TheWinner,ComputerP,PlayerP):
    if(TheWinner == ComputerP):
       print("" + TheWinner + " wins the game.");
       print("The NPC opponent wins this match.");
       print("Sorry, the PLAYER looses.\n");
    elif(TheWinner == PlayerP):
         print("" + TheWinner + " wins the game.");
         print("The PLAYER wins this match.");
         print("The NPC looses.\n");
    else:
         print("The game ends in a tie.");
         print("Nether PLAYER nor the NPC wins.\n");

#--------------------------------------------------------------------------------------------------------------------------------



#-----Invocations-----
MAIN();


