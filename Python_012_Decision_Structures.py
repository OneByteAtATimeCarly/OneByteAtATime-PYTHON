# Python Decision Structures
# Author: C. S. Germany 01/15/2022


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Basic if/else
def Decision_Structures_0l():
    
    The_Name = "Invader Zim";

    if(The_Name == "Invader Zim"):
       print("Good morning, sir!");
    else:
       print("Intruder alert!");   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Basic if/else
def Decision_Structures_02():
    
    The_Score = 42;

    if(The_Score == 42):
       print("The meaning of LIFE!");
    else:
       print("Void of any meaning or purpose.");   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Basic if/elif/else and using logical "and" and comparison operators <, >, <=, >=, ==
def Decision_Structures_03():
    
    Test_Scores = [65,85,97,45,100,63,88];

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

    if Score_1 > Score_2: print("Score_1 is greater than Score_2.");

    print("A") if Score_1 > Score_2 else print("B");


#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   OR vs. AND
def Decision_Structures_05():
    
    Score_1 = 42;
    Score_2 = 444;

    if(Score_1 > 10 and Score_1 < 42):
       print("Target condition A triggered!");

    if(Score_1 > 10 or Score_1 < 42):
       print("Target condition B triggered!");       


#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#Decision_Structures_0l();
#Decision_Structures_02();
#Decision_Structures_03();
#Decision_Structures_04();
Decision_Structures_05();



