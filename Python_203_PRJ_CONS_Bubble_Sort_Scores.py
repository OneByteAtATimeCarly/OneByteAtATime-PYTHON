#Title: Bubble Sorting - HighScores
#Author: Carly S. Germany
#Created: 01/15/2022 
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# A basic BUBBLE SORT in Python
# range() function returns sequence of numbers starting from 0 (by default) and increments by 1 (by default) and stops before a specified number.
# Syntax: range(start, stop, step)
def High_Score1():
    import random;
    from os import system;
    system("cls"); 

    Total_Sum_of_Scores = 0;
    
    The_Scores = input("Enter SCORES separated by spaces: "); 

    Array_of_Scores = The_Scores.split(); #note: default = a whitespace

    Array_of_Scores_Int = [];

    for x in Array_of_Scores:
        Array_of_Scores_Int.append(int(x));

    Num_Scores = len(Array_of_Scores_Int); #get # elements in array   

    print("There are",Num_Scores,"scores to bubble sort.");    
  
    #Now that we have an array of scores in INT format, let's Bubble Sort them
    #Bubble sorts use 2 nested for loops

    #outer loop: iterates through number of elements in array -1
    for i in range(Num_Scores-1):

        #inner loop: for each element
        for j in range(0, Num_Scores - i - 1):

            #If value before is bigger than value after, swap them
            if(Array_of_Scores_Int[j] > Array_of_Scores_Int[j + 1]):
               TEMP = Array_of_Scores_Int[j];
               Array_of_Scores_Int[j] = Array_of_Scores_Int[j + 1];
               Array_of_Scores_Int[j + 1] = TEMP;

    print("\nScores from lowest to highest are:");

    Score_Counter = 0;
    for x in Array_of_Scores_Int:
        Score_Counter = Score_Counter + 1;  
        print(Score_Counter,". ",x,sep='');  

    print("\nThe highest score is:",Array_of_Scores_Int[Num_Scores-1]);                 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Using max() and min()
def High_Score2():
    import random;
    from os import system;
    system("cls"); 

    Total_Sum_of_Scores = 0;
    
    The_Scores = input("Enter SCORES separated by spaces: "); 

    Array_of_Scores = The_Scores.split();

    Array_of_Scores_Int = [];

    for x in Array_of_Scores:
        Array_of_Scores_Int.append(int(x));

    Num_Scores = len(Array_of_Scores_Int);    

    print("\nThere are",Num_Scores,"scores in this array.");
    print("Array values: ",Array_of_Scores_Int);    

    print("\nMAX score is:",max(Array_of_Scores_Int)); 
    print("MIN score is:",min(Array_of_Scores_Int));                  
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Alternate more EXPLICIT Bubble Sort
# range() function returns sequence of numbers starting from 0 (by default) and increments by 1 (by default) and stops before a specified number.
# Syntax: range(start, stop, step)
def High_Score3():
    import random;
    from os import system;
    system("cls"); 

    Total_Sum_of_Scores = 0;
    
    The_Scores = input("Enter SCORES separated by spaces: "); 

    Array_of_Scores = The_Scores.split();

    Array_of_Scores_Int = [];

    for x in Array_of_Scores:
        Array_of_Scores_Int.append(int(x));

    Num_Scores = len(Array_of_Scores_Int);    

    print("\nThere are",Num_Scores,"scores in this array.");
    print("\nBEFORE bubble sort array = ",Array_of_Scores_Int); 

    #Outer loop - iterate through each number in array
    for x in range(Num_Scores - 1):
        flag = 0;
        #Inner loop - compare current number, if greater than number to right swap places.
        for y in range(Num_Scores - 1):            
            if(Array_of_Scores_Int[y] > Array_of_Scores_Int[y + 1]): 
               TEMP = Array_of_Scores_Int[y];
               Array_of_Scores_Int[y] = Array_of_Scores_Int[y + 1];
               Array_of_Scores_Int[y + 1] = TEMP;
               flag = 1;

        if(flag == 0):
            break;

    print("AFTER bubble sort array = ",Array_of_Scores_Int);

    print("\nThe highest score is:",Array_of_Scores_Int[Num_Scores-1]);   
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Bubble_Sort_ASCENDING():

    #Array of unsorted randomly selected numbers
    Unsorted_Random_Nums = [20,5,17,100,30,50,14,7,444];

    print("\nBEFORE the bubble sort? The array is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);

    #Bubble sort this array!
    y = len(Unsorted_Random_Nums);

    #Bubble sort ASCENDING
    for i in range(y-1):
        for j in range(0, y-i-1):
            if(Unsorted_Random_Nums[j] > Unsorted_Random_Nums[j + 1]):
               Unsorted_Random_Nums[j], Unsorted_Random_Nums[j + 1] = Unsorted_Random_Nums[j + 1], Unsorted_Random_Nums[j];    

    print("\nAFTER the bubble sort? The array ASCENDING is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);
 
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Bubble_Sort_DESCENDING():

    #Array of unsorted randomly selected numbers
    Unsorted_Random_Nums = [20,5,17,100,30,50,14,7,444];

    print("\nBEFORE the bubble sort? The array is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);

    #Bubble sort this array!
    y = len(Unsorted_Random_Nums);

    #Bubble sort DESCENDING
    for i in range(y-1):
        for j in range(0, y-i-1):
            if(Unsorted_Random_Nums[j] < Unsorted_Random_Nums[j + 1]):
               Unsorted_Random_Nums[j], Unsorted_Random_Nums[j + 1] = Unsorted_Random_Nums[j + 1], Unsorted_Random_Nums[j];    

    print("\nAFTER the bubble sort? The array DESCENDING is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);
 
#---------------------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Bubble_Sort_ASCENDING_2():

    #Array of unsorted randomly selected numbers
    Unsorted_Random_Nums = [20,5,17,100,30,50,14,7,444];

    print("\nBEFORE the bubble sort? The array is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);

    #Bubble sort this array!
    y = len(Unsorted_Random_Nums);

    #Bubble sort ASCENDING
    for i in range(y-1):
        for j in range(0, y-i-1):
            if(Unsorted_Random_Nums[j] > Unsorted_Random_Nums[j + 1]):
               TEMP = Unsorted_Random_Nums[j];
               Unsorted_Random_Nums[j] = Unsorted_Random_Nums[j + 1];
               Unsorted_Random_Nums[j + 1] = TEMP;  

    print("\nAFTER the bubble sort? The array ASCENDING is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);
 
#---------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Bubble_Sort_DESCENDING_2():

    #Array of unsorted randomly selected numbers
    Unsorted_Random_Nums = [20,5,17,100,30,50,14,7,444];

    print("\nBEFORE the bubble sort? The array is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);

    #Bubble sort this array!
    y = len(Unsorted_Random_Nums);

    #Bubble sort DESCENDING
    for i in range(y-1):
        for j in range(0, y-i-1):
            if(Unsorted_Random_Nums[j] < Unsorted_Random_Nums[j + 1]):
               TEMP = Unsorted_Random_Nums[j];
               Unsorted_Random_Nums[j] = Unsorted_Random_Nums[j + 1];
               Unsorted_Random_Nums[j + 1] = TEMP;     

    print("\nAFTER the bubble sort? The array DESCENDING is:")
    for x in range(len(Unsorted_Random_Nums)):
        print("Element ",x," = ","% d" % Unsorted_Random_Nums[x]);
 
#---------------------------------------------------------------------------------------------------------------------------------------------

#-----Invocations-----
#High_Score1();
#High_Score2();
#High_Score3();
#Bubble_Sort_ASCENDING();
#Bubble_Sort_DESCENDING();
#Bubble_Sort_ASCENDING_2();
Bubble_Sort_DESCENDING_2();



