# Title: Python - Formatting text into columns and rows
# Author: C. S. Germany 01/15/2022 

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Formatting text into columns by concatenating strings and using format() method and {:<} (LEFT), {>:} (RIGHT) and {^:} (CENTER)
def Formatting_Text_0l():
    MLP_FIM_Main_Chars = ("Twilight Sparkle",42,True,"Rarity",444,False);

    print("\nA. Tuples can hold multiple different data types, like strings, integers and booleans all at once.:\n\n  ",MLP_FIM_Main_Chars);
    
    print("\nB. Tuple one item at a time:\n");
    
    Char_Counter = 0;
    for x in MLP_FIM_Main_Chars:
        Char_Counter = Char_Counter + 1;
        MESSAGE1 = "   " + str(Char_Counter) + ". Value: " + str(x);
        MESSAGE2 = "Data Type:" + str(type(x));
        print('{:<35}{:>0}'.format(MESSAGE1,MESSAGE2));

    print("\nC. Accessing one particular element in a Tuple via its index:\n");    
    print("  ","The MLP FIM main character at position 0 is:",MLP_FIM_Main_Chars[0]);
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Formatting left, right and center
def Formatting_Text_02():
    print("\nBasic format() method padding and spacing directions:\n");
    print("LEFT:     ","|LEFT| {:<40} |RIGHT|".format('*'));
    print("CENTER:   ","|LEFT| {:^40} |RIGHT|".format('*'));
    print("RIGHT:    ","|LEFT| {:>40} |RIGHT|".format('*'));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Specifying fill chars
def Formatting_Text_03():
    print("\nSpecifying fill characters:\n");
    print("LEFT:     ","|LEFT| {:*<40} |RIGHT|".format('X'));
    print("CENTER:   ","|LEFT| {:_^40} |RIGHT|".format('X'));
    print("RIGHT:    ","|LEFT| {:->40} |RIGHT|".format('X'));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Formatting an entire 2-D array
def Formatting_Text_04():
    print("\nFormatting an entire array element by element:\n");

    MLP_DATA = [  ['NAME', 'AGE', 'ABILITY', 'M-POWER'],
                  ['Twilight Sparkle', 409, 'All Unicorn Magic', 9000],
                  ['Fluttershy', 390, 'Animal Friendship', 2000],
                  ['Rainbow Dash', 401, 'Sonic Rain Boom', 6500],
                  ['Rarity', 350, 'Telekinesis', 1850],
                  ['Apple Jack', 405, 'Cowgal Combat', 1555],
                  ['Pinkie Pie', 210, 'Party Poppers', 1459],
               ];

    SEPARATOR = '-' * 80;

    for i in range(len(MLP_DATA)):
        if i == 0:
           print("\n");
           print(SEPARATOR);
           print('{:<20}{:<7}{:<22}{:<7}'.format(MLP_DATA[i][0],MLP_DATA[i][1],MLP_DATA[i][2],MLP_DATA[i][3]));
           print(SEPARATOR);
        else:
           print('{:<20}{:<7}{:<22}{:<7}'.format(MLP_DATA[i][0],MLP_DATA[i][1],MLP_DATA[i][2],MLP_DATA[i][3]));           
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#5. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Formatting an entire 2-D array as a single object. If you know C++, you will see we are DEREFERENCING the array with * .
# Must dereference the array to access inner arrays and their elements. 
def Formatting_Text_05():
    print("\nFormatting an ENTIRE array all at ONCE\n");

    MLP_DATA = [  ['NAME', 'AGE', 'ABILITY', 'M-POWER'],
                  ['Twilight Sparkle', 409, 'All Unicorn Magic', 9000],
                  ['Fluttershy', 390, 'Animal Friendship', 2000],
                  ['Rainbow Dash', 401, 'Sonic Rain Boom', 6500],
                  ['Rarity', 350, 'Telekinesis', 1850],
                  ['Apple Jack', 405, 'Cowgal Combat', 1555],
                  ['Pinkie Pie', 210, 'Party Poppers', 1459],
               ];

    SEPARATOR = '-' * 80;

    print(SEPARATOR);
    print('{:<20}{:<7}{:<22}{:<7}'.format(*MLP_DATA[0]));
    print(SEPARATOR);

    for ROW in MLP_DATA:
        print('{:<20}{:<7}{:<22}{:<7}'.format(*ROW));           
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#06. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# DYNAMICALLY formatting text into columns
def Formatting_Text_Dynamically10():
    
    print("\nThis code will dynamically space columns based on lengths of tuple strings in array.\n");

    Rows_in_the_Array = [('Twilight Sparkle', '444', 'Friendship Magic'), 
                         ('Rainbow Dash', '42', 'Sonic Rain Boom')];

    lens = [];

    for COLUMN in zip(*Rows_in_the_Array):
        lens.append(max([len(v) for v in COLUMN]));
    
    format = "  ".join(["{:<" + str(l) + "}" for l in lens]);
    
    for ROW in Rows_in_the_Array:
        print(format.format(*ROW));
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#07. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Unpacking (de-referencing)
def Unpacking_DeReferencing_01():
    
    print("\nUnpacking (de-referencing).\n");

    primes = [2, 3, 5, 7, 11, 13];

    def product(*nums):
        from functools import reduce;
        p = reduce(lambda x, y: x * y, nums);
        return p; 

    print("-------------------------------------------------------------");
    print("A. WITHOUT unpacking List (de-refrencing)");
    print(product(primes));

    print("-------------------------------------------------------------");
    print("B. WITH unpacking List (de-refrencing)");
    print(product(*primes));
#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#08. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Unpacking (de-referencing)
def Unpacking_DeReferencing_02():
    
    print("\nUnpacking (de-referencing).\n");

    headers = {  'Accept': 'text/plain',
                 'Content-Length': 444, 
                 'Host': 'https://twilightsparkle.com' 
              }

    def PRE_PROCESS(**headers):
        content_length = headers['Content-Length']; 
        print('Content Length: ', content_length);
        host = headers['Host'];
        if 'https' not in host: 
           print("Secure Status:   BAD! You must use SSL for https communication.");
        else:
           print("Secure Status:   GOOD! You are using SSL."); 

    print("-------------------------------------------------------------");
    print("A. WITH unpacking Dictionary (double de-refrencing)");
    print(PRE_PROCESS(headers));

    #print("-------------------------------------------------------------");
    #print("B. WITHOUT unpacking Dictionary (double de-refrencing), Generates ERROR.");
    #print(PRE_PROCESS(headers));

#------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
#Formatting_Text_0l();
#Formatting_Text_02();
#Formatting_Text_03();
#Formatting_Text_04();
#Formatting_Text_05();
#Formatting_Text_Dynamically10();
#Unpacking_DeReferencing_01();
Unpacking_DeReferencing_02();

