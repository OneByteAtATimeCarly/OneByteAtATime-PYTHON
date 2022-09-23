# Title: Project - Love Calculator
# Author: C. S. Germany 01/06/2022 


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Love_Calculator():
    from os import system;
    system("cls");

    Person1_TRUE_Count = 0;
    Person1_LOVE_Count = 0;
    Person2_TRUE_Count = 0;
    Person2_LOVE_Count = 0;

    print("\nLove Calculator 1.0\n");

    #1. Get names
    Person1 = input("1st person's name: ");
    Person2 = input("2nd person's name: ");
    Person1NumLetters = len(Person1);
    Person2NumLetters = len(Person2);
    print("\nPerson 1:",Person1);
    print("Number of letters in 1st person's name:",Person1NumLetters);
    print("\nPerson 2:",Person2);
    print("Number of letters in 2nd person's name:",Person2NumLetters);

    #2. Check for TRUE letters
    print("\nChecking for TRUE letters in names:")
    for a in Person1.lower():
        if(a == "t" or a == "r" or a == "u" or a == "e"):
           Person1_TRUE_Count = Person1_TRUE_Count + 1;
    print("Number of TRUE letters that occur in 1st name:",Person1_TRUE_Count);
    for b in Person2.lower():
        if(b == "t" or b == "r" or b == "u" or b == "e"):
           Person2_TRUE_Count = Person2_TRUE_Count + 1;
    print("Number of TRUE letters that occur in 2nd name:",Person2_TRUE_Count);
    TRUE_Total = Person1_TRUE_Count + Person2_TRUE_Count;
    print("Total # of TRUE letters in both names:",TRUE_Total);

    #3. Check for LOVE letters
    print("\nChecking for LOVE letters in names:")
    for c in Person1.lower():
        if(c == "l" or c == "o" or c == "v" or c == "e"):
           Person1_LOVE_Count = Person1_LOVE_Count + 1;
    print("Number of LOVE letters that occur in 1st name:",Person1_LOVE_Count);
    for d in Person2.lower():
        if(d == "l" or d == "o" or d == "v" or d == "e"):
           Person2_LOVE_Count = Person2_LOVE_Count + 1;
    print("Number of LOVE letters that occur in 2nd name:",Person2_LOVE_Count);
    LOVE_Total = Person1_LOVE_Count + Person2_LOVE_Count;
    print("Total # of LOVE letters in both names:",LOVE_Total);

    #4. Convert, Concatenate, Combine and Total
    TRUE_LOVE_TOTAL_String = str(TRUE_Total) + str(LOVE_Total);
    print("\nTRUE + LOVE total Combined as a String = ",TRUE_LOVE_TOTAL_String);

    print("\nConverting concatenated string back to integer for comparison.");
    TRUE_LOVE_TOTAL_INT = int(TRUE_LOVE_TOTAL_String);
    print("Value of integer is:",TRUE_LOVE_TOTAL_INT);

    #5. Compare and Display Final Score
    print("\nFinal Score:");
    if(TRUE_LOVE_TOTAL_INT < 10 or TRUE_LOVE_TOTAL_INT > 90):
       print("Your score is",TRUE_LOVE_TOTAL_INT,". You go together like coke and mentos.");
    elif(TRUE_LOVE_TOTAL_INT >= 40 and TRUE_LOVE_TOTAL_INT <= 50):
       print("Your score is",TRUE_LOVE_TOTAL_INT,". You are alright together.");   
    else:
       print("Your score is",TRUE_LOVE_TOTAL_INT,". Who knows?");
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


Love_Calculator();

