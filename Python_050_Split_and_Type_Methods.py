# Title: Python split() and type() Methods
# Author: C. S. Germany 01/06/2022

#Note:Remember python uses INDENTATION instead of braces to designate code blocks and functions


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Number_Chars_In_A_String():
    
    PlayerName = input("\nWhat's your name, player? ");
    Num_Chars = len(PlayerName);
    print("Number of chars in your name = ",Num_Chars,".");
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Variable_Swapping():

    a = input("\na: ");
    b = input("b: ");

    #SWAP values----------------------------------------
    TEMP = a;
    a = b;
    b = TEMP;
    #---------------------------------------------------

    print("\na: " + a);
    print("b: " + b);
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Python_Split_Method():

    #How Python's SPLIT method works
    txt = "welcome to the jungle";
    x = txt.split();
    print("\nUsing split by itself:");
    print("Entire array = ",x);
    print("Elelment 0 = ",x[0]);
    print("Elelment 1 = ",x[1]);
    print("Elelment 2 = ",x[2]);
    print("Elelment 3 = ",x[3]);

    #Using a delimiter/separator char
    txt = "When the last eagle flies,Over the last crumbling mountain,And the last lion roars,Over the last dusty fountain";
    x = txt.split(",");
    print("\nUsing split with a \",\" delimiter/separator:");
    print("Entire array = ",x);
    print("Elelment 0 = ",x[0]);
    print("Elelment 1 = ",x[1]);
    print("Elelment 2 = ",x[2]);
    print("Elelment 3 = ",x[3]);

    #Setting maxsplit parameter to 1 returns a list with 2 elements
    print("\nUsing split with maxsplit parameter:");
    txt2 = "Fluttershy#TwilightSparkle#RainbowDash#Rarity#AppleJack";
    z = txt2.split("#", 1);
    print(z);
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Add_Values():

    #Note: Don't even need SPLIT method above, as we know from C++ that every String is an array of type char
    Two_Digit_Number = input("\nType a two digit number: ");

    print("\n1st digit is: ",Two_Digit_Number[0],"  DataTYPE = ",type(Two_Digit_Number[0]));
    print("2nd digit is: ",Two_Digit_Number[1],"  DataTYPE = ",type(Two_Digit_Number[1]));
    print("\nConverting string datatype to integer and adding...");

    The_Sum = int(Two_Digit_Number[0]) + int(Two_Digit_Number[1]);

    print("\n",Two_Digit_Number[0]," + ",Two_Digit_Number[1]," = ",The_Sum);
    print("\nSum datatype = ",type(The_Sum),"\n");
#---------------------------------------------------------------------------------------------------------------------------------------------





#-----Function Invocations-----
Number_Chars_In_A_String();
Variable_Swapping();
Add_Values();
Python_Split_Method();


