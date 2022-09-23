# Casting Variables: Converting variables from one data type to another 

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Converting variables to strings with str()
def Casting_0l():
    x = "444";    # x will be STRING "444"
    y = 444;      # y will be INTEGER 444
    z = 444.13;   # z will be FLOAT 444.0

    print("\nA. Default data types chosen by Python automatically:\n");
    print("    x = ",x,"      TYPE:",type(x));
    print("    y = ",y,"      TYPE:",type(y));
    print("    z = ",z,"   TYPE:",type(z));

    #Cast each data type to a string (redefines each variable)
    x = str(x);
    y = str(y);
    z = str(z);

    print("\nB. Data types after explicitly casting them to a string:\n");
    print("    x = ",x,"      TYPE:",type(x));
    print("    y = ",y,"      TYPE:",type(y));
    print("    z = ",z,"   TYPE:",type(z));    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Truncating variables when casting to Integers
def Casting_02():
    x = 42.7735;  
    y = 444.1325;     

    print("\nC. Casting from data type FLOAT to data type INT truncates. As FLOATS x and y are:\n");
    print("    x = ",x,"      TYPE:",type(x));
    print("    y = ",y,"     TYPE:",type(y));

    #Casting FLOAT to INT
    x = int(x);
    y = int(y);

    print("\nD. After casting, we can see the value to the right of the decimal has been truncated (NOT rounded):\n");
    print("    x = ",x,"      TYPE:",type(x));
    print("    y = ",y,"     TYPE:",type(y));  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Converting string data to FLOATS and INTEGERS
def Casting_03():
    x = "42";  
    y = "444";     

    print("\nE. As STRING data, x and y are:\n");
    print("    x = ",x,"      TYPE:",type(x));
    print("    y = ",y,"     TYPE:",type(y));

    #Casting STRING to FLOAT and INT
    x = int(x);
    y = float(y);

    print("\nF. After casting, we can see the strings were converted to an integer and a float:\n");
    print("    x = ",x,"       TYPE:",type(x));
    print("    y = ",y,"    TYPE:",type(y));  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
Casting_0l();
Casting_02();
Casting_03();

