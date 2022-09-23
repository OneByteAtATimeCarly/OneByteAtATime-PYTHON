# Title: Project - Calculating Days, Weeks, Months, Leap Years
# Author: C. S. Germany 01/06/2022 


#IMPORTS--------------------------------------------------------------------------------------------------------------------------
from datetime import date
#---------------------------------------------------------------------------------------------------------------------------------


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Calculate_Between_Two_Days():
    Start_Date = date(2019,7,2);
    End_Date = date(2022,7,2);

    RESULT = End_Date - Start_Date;

    DAYS = RESULT.days;
    WEEKS = RESULT.days / 7;
    YEARS = RESULT.days / 365;
    MONTHS = YEARS  * 12;
    print("\nFLOAT result is:");
    print("Days:",DAYS);
    print("Weeks:",WEEKS);
    print("Years:",YEARS);
    print("Months:",MONTHS);

    print("\nINT result is:");
    print("Days:",int(DAYS));
    print("Weeks:",int(WEEKS));
    print("Years:",int(YEARS));
    print("Months:",int(MONTHS));  
#---------------------------------------------------------------------------------------------------------------------------------------------- 


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Calculate_Age_From_BirthDay():
    Birthdate = date(1969,11,10);
    Today = date.today();
    Age = Today.year - Birthdate.year - ( (Today.month, Today.day) < (Birthdate.month, Birthdate.day) );

    print("\nYou are ",Age," years old.");
#---------------------------------------------------------------------------------------------------------------------------------------------- 


#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Calculate_LifeSpan():
    Birthdate = date(1969,11,10);
    EstimatedLifeSpan = 75;
    print("\nBirthdate:",Birthdate);
    print("Estimated Lifespan:",EstimatedLifeSpan,"years");

    Future = EstimatedLifeSpan + Birthdate.year;
    FutureDate = date(Future,Birthdate.month,Birthdate.day);
    print("\nAt an estimated lifespan of",EstimatedLifeSpan,", you will reach the end at:",FutureDate);

    #Total Time
    Total_DAYS = EstimatedLifeSpan * 365;
    Total_WEEKS = EstimatedLifeSpan * 52;
    Total_YEARS = EstimatedLifeSpan;
    Total_MONTHS = EstimatedLifeSpan  * 12;
    print("\nYour total lifespan will contain:");
    print("Total DAYS:",Total_DAYS);
    print("Total YEARS:",Total_YEARS);
    print("Total WEEKS:",Total_WEEKS);
    print("Total MONTHS:",Total_MONTHS);

    #Expired Time
    Today = date.today();
    Expired = Today - Birthdate;
    Expired_DAYS = Expired.days;
    Expired_YEARS = Expired_DAYS / 365;
    Expired_WEEKS = Expired_YEARS * 52;
    Expired_MONTHS = Expired_YEARS  * 12;
    print("\nYou have already used up:");
    print("Expired DAYS:",Expired_DAYS);
    print("Expired YEARS:",Expired_YEARS);
    print("Expired WEEKS:",Expired_WEEKS);
    print("Expired MONTHS:",Expired_MONTHS);  

    #Time Remaining
    Remaining_DAYS = Total_DAYS - Expired_DAYS;
    Remaining_YEARS = Total_YEARS - Expired_YEARS;
    Remaining_WEEKS = Total_WEEKS - Expired_WEEKS;
    Remaining_MONTHS = Total_MONTHS - Expired_MONTHS;
    print("\nYou're remaning time is:");
    print("Remaining DAYS:",Remaining_DAYS);
    print("Remaining YEARS:",Remaining_YEARS);
    print("Remaining WEEKS:",Remaining_WEEKS);
    print("Remaining MONTHS:",Remaining_MONTHS,"\n");  

#----------------------------------------------------------------------------------------------------------------------------------------------



#FUNCTION--------------------------------------------------------------------------------------------------------------------------------------
def Calculate_LeapYear():
    
    #Formula: Every year that is evenly divisible by 4 
    #         EXCEPT every year that is evenly divisible by 100
    #         UNLESS the year is also evenly divisible by 400

    The_YEAR = 2022;
    #YEAR = int(input("Enter year: "));
    
    print("\nLeapYear Calculator 1.0");

    #1.If evenly divisible by 100? It's Century year. So check - is it evenly divisible by 400?
    if (The_YEAR % 400 == 0) and (The_YEAR % 100 == 0):
       print("\n",The_YEAR,"is a leap year.","\n");
    
    #2.If NOT evenly divisible by 100? NOT a Century year. So check - is it evenly divisible by 4?
    elif (The_YEAR % 4 == 0) and (The_YEAR % 100 != 0):
          print("\n",The_YEAR,"is a leap year.","\n");

    #3.If year matches neither condition above and NOT evenly divisible by 400 or 4? NOT a leap year.
    else:
          print("\n",The_YEAR,"is NOT a leap year.","\n");
#----------------------------------------------------------------------------------------------------------------------------------------------



#-----Function Invocations-----
Calculate_Between_Two_Days();
Calculate_Age_From_BirthDay();
Calculate_LifeSpan();
Calculate_LeapYear();




#------------------------------------------------------------------------------------------------------------------------------------------------

#2000 ÷ 4 = 500 (Leap)
#2000 ÷ 100 = 20 (Not Leap)
#2000 ÷ 400 = 5 (Leap!)

#So the year 2000 is a leap year.

#But the year 2100 is not a leap year because:
#2100 ÷ 4 = 525 (Leap)
#2100 ÷ 100 = 21 (Not Leap)
#2100 ÷ 400 = 5.25 (Not Leap)
#------------------------------------------------------------------------------------------------------------------------------------------------