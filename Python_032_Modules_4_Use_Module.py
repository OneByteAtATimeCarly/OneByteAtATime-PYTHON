#Title: Python Programming 029 - This Script Loads a Separately-coded Custom Python Module
#Author: Carly S. Germany
#Created: 04/25/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

# You can create your own modules and import them in Python.
# To do so, just save the code with a ".py" extension just as you would any other file.


#import Python_031_Modules_3_Class_Hierarchy;
#Princess_Celestia = Python_031_Modules_3_Class_Hierarchy.ALICORN;
#Princess_Celestia.Display_Entity();

import Python_031_Modules_3_Class_Hierarchy as HIERARCHY;

#1. Calling a FUNCTION from an EXTERNAL MODULE.
print("\n1. ",sep='',end='');
HIERARCHY.Test_Function();

#2. Retrieving the value of a VARIABLE from an EXTERNAL MODULE.
print("2. Value of test variable from external module is: \"",HIERARCHY.Test_Variable,"\".",sep='');

#3. Instantiating a CLASS from an EXTERNAL MODULE.
from Python_031_Modules_3_Class_Hierarchy import PONY;
from Python_031_Modules_3_Class_Hierarchy import UNICORN;
from Python_031_Modules_3_Class_Hierarchy import ALICORN;

#A. Build a PONY
print("\n-------------------------------------------------------------------------------");
print("A. Building a PONY.");
Apple_Jack = PONY("Apple Jack","Pony",9000,444,777,500);
Apple_Jack.Pony_Stuff();
Apple_Jack.Display_Entity();

#Build a UNICORN
print("\n-------------------------------------------------------------------------------");
print("B. Building a UNICORN.");
Rarity = UNICORN("Rarity","Unicorn",9000,333,999,25000);
Rarity.Display_Unicorn();
Rarity.Display_Entity();

#Build an ALICORN
print("\n-------------------------------------------------------------------------------");
print("C. Building a ALICORN.");
Twilight_Sparkle = ALICORN("Twilight Sparkle","Alicorn",30000,1000,1000,32000);
Twilight_Sparkle.Display_Alicorn();
Twilight_Sparkle.Display_Entity();







