# Title: Project - Grading Program
# Author: C. S. Germany 01/06/2022 


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#DICTIONARIES - contains KEY and VALUE pairs. They are collections which are ordered, changeable and do not allow duplicates. Values in dictionary items can be of any data type.
#Dictionary update() method = modifies items in a Dictionary if they exist, or adds them if they don't.
#ljust() = pad to left
#rjust() = pad to right
#center() = pad to center
def Grading_Program():
    import random;
    from os import system;
    system("cls");
    
    GRADE = "";

    Dictionary_of_Scores = {"Fluttershy" : 75, 
                            "Twilight Sparkle" : 100,
                            "Rainbow Dash" : 85,
                            "AppleJack" : 69,   
                            "Pinkie Pie" : 60,
                            "Rarity" : 90,  
                          };

    print("\n1. Create Dictionary of SCORES.\n");
    print("Dictionary of SCORES:",Dictionary_of_Scores,"\n");
    print("-----------------KEY + VALUE Pairs-----------------");
    for x in Dictionary_of_Scores:
        print("KEY (Name)",x.ljust(17),"   VALUE (Score):",Dictionary_of_Scores[x]);

    print("\n2. Create Dictionary of GRADES from Dictionary of SCORES.\n");
    
    Dictionary_of_Grades = { };

    for x in Dictionary_of_Scores:
        
        if(Dictionary_of_Scores[x] >= 91 and Dictionary_of_Scores[x] <= 100):
           GRADE = "A = Outstanding";
        elif(Dictionary_of_Scores[x] >= 81 and Dictionary_of_Scores[x] <= 90):   
             GRADE = "B = Exceeds Expectations";
        elif(Dictionary_of_Scores[x] >= 71 and Dictionary_of_Scores[x] <= 80):   
             GRADE = "C = Acceptable";
        elif(Dictionary_of_Scores[x] >= 65 and Dictionary_of_Scores[x] <= 70):   
             GRADE = "D = Barely made it";     
        elif(Dictionary_of_Scores[x] < 64):   
             GRADE = "F = Total Fail"; 
        else:
              print("INVALID GRADE. OUtside acceptable range.");       

        Dictionary_of_Grades.update({x : GRADE});

    print("3. Display newly populated Dictionary of Grades:\n");
    print("Dictionary of GRADES:",Dictionary_of_Grades,"\n");
    print("-----------------KEY + VALUE Pairs-----------------");
    for y in Dictionary_of_Grades:
        print("KEY (Name)",y.ljust(17),"   VALUE (Grade):",Dictionary_of_Grades[y]);        

#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



# -------Invocations-------    
Grading_Program();

