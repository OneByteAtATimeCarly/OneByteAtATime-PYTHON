# Title: Project - BMI Calculator
# Author: C. S. Germany 01/06/2022 


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def BMI_Metric():
    
    print("\nBMI Calculator (METRIC)");
    User_Weight = input("\nEnter your weight in kilograms: ");
    User_Height = input("Enter your height in meters: ");

    BMI_Float = float(User_Weight) / (float(User_Height) * float(User_Height));

    print("\nFLOAT values: ",User_Weight," / ","( ",User_Height," x ",User_Height," )"," = ",BMI_Float,"\n");

    BMT_Int = int(BMI_Float);

    print("\nConverting FLOATs to INTs and rounding to whole number values:\n");
    print("\nINT values: ",User_Weight," / ","( ",User_Height," x ",User_Height," )"," = ",BMT_Int,"\n");
#---------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def BMI_English():
    
    print("\nBMI Calculator (ENGLISH)");
    User_Weight = input("\nEnter your weight in pounds: ");
    User_Height = input("Enter your height in inches: ");

    BMI_Float = 703 * ( float(User_Weight) / (float(User_Height) * float(User_Height)) );

    print("\nFLOAT values: ",User_Weight," / ","( ",User_Height," x ",User_Height," )"," = ",BMI_Float,"\n");

    BMT_Int = int(BMI_Float);

    print("\nConverting FLOATs to INTs and rounding to whole number values:\n");
    print("\nINT values: ",User_Weight," / ","( ",User_Height," x ",User_Height," )"," = ",BMT_Int,"\n");
#---------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def BMI_English_2():
    
    print("\nBMI Calculator (ENGLISH)");
    User_Weight = input("\nEnter your weight in pounds: ");
    User_Height = input("Enter your height in inches: ");

    BMI_Float = 703 * ( float(User_Weight) / (float(User_Height) * float(User_Height)) );

    print("\nFLOAT values: ",User_Weight," / ","( ",User_Height," x ",User_Height," )"," = ",BMI_Float,"\n");

    BMT_Int = int(BMI_Float);

    print("\nConverting FLOATs to INTs and rounding to whole number values:\n");
    print("\nINT values: ",User_Weight," / ","( ",User_Height," x ",User_Height," )"," = ",BMT_Int,"\n");

    print("Assessing your BMI ...");

    if BMI_Float < 18.5:
                   print("You are underweight. Eat a cheeseburger!");

    elif BMI_Float > 18.5 and BMI_Float < 25:
                     print("You have have a normal weight and are one of the BEAUTIFUL people.");

    elif BMI_Float > 25 and BMI_Float < 30:
                     print("You are slightly overweight, chubz.");   

    elif BMI_Float > 30 and BMI_Float < 35:
                     print("You are obese. Put that doughnut down, Pyle!");  

    elif BMI_Float > 35:
                     print("You are MORBIDLY obese. Nothing but prunes and cabbage for you.");                                                 
                     


#---------------------------------------------------------------------------------------------------------------------------------------------


#-----Invocations-----
#BMI_Metric();
#BMI_English();
BMI_English_2();

