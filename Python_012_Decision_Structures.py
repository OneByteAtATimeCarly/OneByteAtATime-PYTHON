# Python Decision Structures
# Author: C. S. Germany 01/15/2022


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Basic if/else
def Decision_Structures_0l():
    
    The_Name = "Carly";

    if(The_Name == "Invader Zim"):
       print("\nGood morning, sir!\n");
    else:
       print("\nIntruder alert!\n");   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Basic if/else
def Decision_Structures_02():
    
    The_Score = 42;

    if(The_Score == 42):
       print("\nThe meaning of LIFE!\n");
    else:
       print("\nVoid of any meaning or purpose.\n");   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Basic if/elif/else and using logical "and" and comparison operators <, >, <=, >=, ==
def Decision_Structures_03():
    
#Logical Comparison Operators: AND and OR
# AND = BOTH sides have to be true
# OR Only ONE side has to be true

    Test_Scores = [65,85,97,45,100,63,88,444];

    for z in Test_Scores:
        
        if(z >= 0 and z < 60):
           print("   ","Score = ",z,"  Grade = F");
        elif(z >= 61 and z < 70):
           print("   ","Score = ",z,"  Grade = D");
        elif(z >= 70 and z < 80):
           print("   ","Score = ",z,"  Grade = C");
        elif(z >= 80 and z < 90):
           print("   ","Score = ",z,"  Grade = B");
        elif(z >= 90 and z <= 100):
           print("   ","Score = ",z,"  Grade = A"); 
        else:
           print("\nThis score is invalid.");                        

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Shorthand if/else
def Decision_Structures_04():
    
    Score_1 = 42;
    Score_2 = 444;

    if Score_1 > Score_2: print("\nScore_1 is greater than Score_2.\n");
    else: print("\nScore 1 is NOT greater than Score 2.\n");

    print("A") if Score_1 > Score_2 else print("B");


#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   OR vs. AND
def Decision_Structures_05():
    
    Score_1 = 42;
    Score_2 = 444;

    if(Score_1 > 10 and Score_1 <= 42):
       print("\nTarget condition A triggered!");

    if(Score_1 > 10 or Score_1 < 42):
       print("Target condition B triggered!\n");       


#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Unlike C++, Java or PowerShell, there is no switch statement in Python
# You can approximate a switch statement however using a series of simple one-line if statements.
def Decision_Structures_06():
    User_Input = "";

    while(User_Input != "q"):
          User_Input = input("\nWhat was your score? (q to quit) ");

          if(User_Input != "q"):
             
             if(User_Input.isdigit()):
                print("Numerical value entered. Let's proceed.");
                print("Converting the STRING data to INT type.");
                The_Score = int(User_Input); 
    
                print("\nYour grade is: ",end='');

                if(The_Score < 65): print("F"); 
                elif(The_Score >= 65 and The_Score < 70): print("D");
                elif(The_Score >= 70 and The_Score < 80): print("C");
                elif(The_Score >= 80 and The_Score < 90): print("B");
                elif(The_Score >= 90 and The_Score <= 99): print("A");
                elif(The_Score == 100): print("Perfect A+! 100%!");
                elif(The_Score > 100): print("A++! Awesome!");

                print("\n");
             
             else: print("That was NOT a number!");
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#Decision_Structures_0l();
#Decision_Structures_02();
#Decision_Structures_03();
#Decision_Structures_04();
#Decision_Structures_05();
Decision_Structures_06();




