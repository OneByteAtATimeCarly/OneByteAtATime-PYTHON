# Title: Python Dates and Math
# Author: C. S. Germany 01/15/2022 

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   A datetime object returns: year, month, day, hour, minute, second, and microsecond.
def Dates_and_Time_0l():
    import datetime;
    Current_Time = datetime.datetime.now();
    print("\n     Current time =",Current_Time);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Scoping into different parts of dattime. Syntax = year, month, day, hour, minute, second, and microsecond.
def Dates_and_Time_02():
    import datetime;
    Current_Time = datetime.datetime.now();
    print("\n     Current year =",Current_Time.year);
    print("     Current month =",Current_Time.month);
    print("     Current Day of Month = =",Current_Time.day);
    print("     Current day of week =",Current_Time.weekday()); #0=Monday and 6=Sunday, so 3=Thursday
    print("     Current hour =",Current_Time.hour);
    print("     Current minute =",Current_Time.minute);
    print("     Current second =",Current_Time.second);
    print("     Current microsecond =",Current_Time.microsecond);

    #To get name of week day just pass int value returned from weekday() as index subecript to a list
    WeekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
    print("     Name of this day of the week = ",WeekDays[Current_Time.weekday()]);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Creating a custom datetime object
def Dates_and_Time_03():
    import datetime;
    Created_Time = datetime.datetime(2022,6,2);
    print("\n     Created datetime object =",Created_Time);

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   strftime() method = formats date objects into readable strings. Takes one parameter, format.
def Dates_and_Time_04():
    import datetime;
    Current_Time = datetime.datetime.now();
    print("     Current Year =",Current_Time.strftime("%Y"));
    print("     Current Month =",Current_Time.strftime("%B"));
    print("     Current Day of Month =",Current_Time.strftime("%d"));
    print("     Current Week Day =",Current_Time.strftime("%A"));
    print("     Current hour (12 hr) =",Current_Time.strftime("%I %p"));
    print("     Current hour (24 hr) =",Current_Time.strftime("%H"));
    print("     Current minute =",Current_Time.strftime("%M"));
    print("     Current second =",Current_Time.strftime("%S"));
    print("     Current microsecond =",Current_Time.strftime("%f"));
    print("     Current day of this year =",Current_Time.strftime("%j"));
    print("     Current week of this year =",Current_Time.strftime("%U"));
    print("     Current century =",Current_Time.strftime("%C"));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Getting the current time zone
def Dates_and_Time_05():
    import time;
    print("\n     Current Time Zone =",time.tzname[time.daylight]);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


# strftime() codes:
#   Code | Returns	                            |                           Example	
#   %a	   Weekday, short version	                                        Fri	
#   %A	   Weekday, full version	                                        Friday	
#   %w	   Weekday as a number 0-6, 0 is Sunday	                            4	
#   %d	   Day of month 01-31	                                            14	
#   %b	   Month name, short version	                                    Nov	
#   %B	   Month name, full version	                                        November	
#   %m	   Month as a number 01-12	                                        11	
#   %y	   Year, short version, without century	                            22	
#   %Y	   Year, full version	                                            2022	
#   %H	   Hour 00-23	                                                    19	
#   %I	   Hour 00-12	                                                    07	
#   %p	   AM/PM	                                                        AM	
#   %M	   Minute 00-59	                                                    42	
#   %S	   Second 00-59	                                                    08	
#   %f	   Microsecond 000000-999999	                                    444444	
#   %z	   UTC offset	                                                    +0100	
#   %Z	   Timezone	                                                        CST	
#   %j	   Day number of year 001-366	                                    365	
#   %U	   Week number of year, Sunday as the first day of week, 00-53	    52	
#   %W	   Week number of year, Monday as the first day of week, 00-53   	52	
#   %c	   Local version of date and time	                                Mon Dec 31 17:41:00 2018	
#   %C	   Century	                                                        20	
#   %x	   Local version of date	                                        12/31/18	
#   %X	   Local version of time	                                        17:41:00	
##  %%	   A % character	                                                %	
#   %G	   ISO 8601 year	                                                2017	
#   %u	   ISO 8601 weekday (1-7)	                                        1	
#   %V	   ISO 8601 weeknumber (01-53)	                                    01



#6. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Using min() and max() methods with iterables
def Math_Functions_01():
    
    Pony_Ages = [55,89,354,777,19,123,33,444,14,29,87,456,41];

    Pony_Youngest = min(Pony_Ages);
    Pony_Oldest = max(Pony_Ages);

    print("\n     Youngest pony =",Pony_Youngest);
    print("     Oldest pony =",Pony_Oldest);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   pow() method = Takes 2 arguemtns. 1st = a number. 2nd = what you wish to raise it to the power of. 
def Math_Functions_02():
    
    TwilightSparkle_Friendship_Power = pow(10,4); #10 to the power of 4

    print("\nTwilight's Friendship Power Level =",TwilightSparkle_Friendship_Power);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#7. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   abs() = Returns positive absolute value of a number whether negative or not
def Math_Functions_03():
    
    Lucky_Number = abs(-444); 

    print("\nLucky Number =",Lucky_Number);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#8. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Math Module Methods. sqrt(), ceil(), floor()
def Math_Functions_04():
    import math;

    print("");
    print("     sqrt()   The square root of 9 is:", math.sqrt(9));
    print("     ceil()   444.613 rounded UP is:", math.ceil(444.613));
    print("     floor()  444.613 rounded DOWN is:", math.floor(444.613));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
#Dates_and_Time_0l();
#Dates_and_Time_02();
#Dates_and_Time_03();
#Dates_and_Time_04();
#Dates_and_Time_05();

#Math_Functions_01();
#Math_Functions_02();
#Math_Functions_03();
Math_Functions_04();

