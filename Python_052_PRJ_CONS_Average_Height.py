# Title: Project - Average Height
# Author: C. S. Germany 01/06/2022


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
def Average_Height():
    import random;
    from os import system;
    system("cls"); 

    Total_Sum_of_Heights = 0;
    
    The_Heights = input("Enter heights in inches separated by spaces: "); 

    Array_of_Heights = The_Heights.split();

    Array_of_Heights_Int = [];

    for w in Array_of_Heights:
        Array_of_Heights_Int.append(int(w));

    Num_Heights = len(Array_of_Heights_Int);

    print("\nYou entered",Num_Heights,"heights. Adding heights and dividing by",Num_Heights,".");

    for x in Array_of_Heights_Int:
        Total_Sum_of_Heights = Total_Sum_of_Heights + x;

    print("\nTotal sum of all heights = ",Total_Sum_of_Heights);

    Avg_Height = Total_Sum_of_Heights / Num_Heights;
    print("Average HEIGHT = ",Avg_Height);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 


Average_Height();

