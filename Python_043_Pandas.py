# Python Pandas
# Author: C. S. Germany 01/15/2022

#PANDAS = a Python library used to analyze, compare, clean, manipulate and display data.
#History: Python PANDAs gets its name from "PANel DAta". Panel Data is a term for data sets that include observations over multiple
# time periods for the same individuals.

#To use PANDAs:
#1. Check for module: pip list
#2. Check version: pip show pandas 
#3. If needed, install the module: pip install pandas
#4. Import the module


#Example: Checking version
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Check_Version():
    import pandas as PD;
    print(PD.__version__);
#----------------------------------------------------------------------------------------------------------------------------   


#Example: Using a panda from the module itself without an instance
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_1():
    import pandas;

    BioMechanical_Hybrids = {
                              'Cylons': ["Cavil","Leoben","D'Anna","Simon","Aaron","Six","Sharon"],
                              'Threat Lvl': [666,100,80,50,20,5,9000]
                            };

    Threat_Analysis = pandas.DataFrame(BioMechanical_Hybrids);
    print(Threat_Analysis);
#----------------------------------------------------------------------------------------------------------------------------   


#Example: Using a panda via an instance created from the module
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_1B():
    import pandas as PD;

    HiddenLeaf_Ninjas = {
                              'Hdn Lf Ninjas': ["Naruto","Jiraiya","Kakashi","Hinata","Sakura","Sasuke","Kiba","Akamaru"],
                              'Chakra Lvls': [500,9000,800,200,300,500,250,100]
                        };

    Chakra_Analysis = PD.DataFrame(HiddenLeaf_Ninjas);
    print(Chakra_Analysis);
#----------------------------------------------------------------------------------------------------------------------------  


#Example: Panda table
#Function-------------------------------------------------------------------------------------------------------------------------
def Panda_Table():
    import pandas;

    Pony_Data = [  [1, 'Rainbow Dash',    100, 10],
                   [2, 'Fluttershy',       75, 20],
                   [3, 'Twilight Sparkle', 70, 25],
                   [4, 'AppleJack',        60, 35]
                ]; 
    
    Pony_Headers = ["Pos", "Team", "Win", "Lose"];  
    
    print("\n--------------------------------------------");
    print("A. HORIZONTAL panda table headers:\n");
    print(pandas.DataFrame(Pony_Data,None,Pony_Headers)); 

    print("\n--------------------------------------------");
    print("B. VERTICAL panda table headers:\n");
    print(pandas.DataFrame(Pony_Data,Pony_Headers,None)); 

    print("\n--------------------------------------------");
    print("C. HORIZONTAL and VERTICAL panda table headers:\n");
    print(pandas.DataFrame(Pony_Data,Pony_Headers,Pony_Headers)); 
#---------------------------------------------------------------------------------------------------------------------------------



#Example: A Panda Series = a 1-D array containing any type of data like a single column in a table.
#If no labels are specified, the values are labeled with an index number starting at 0.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Series_01():
    import pandas as PD;

    TNG_Cast = ["Picard","La Forge","Worf","Data","Riker","Crusher","Troi"];

    print("\nA. A panda SERIES is labled by INDEX values when no labels are specified.");
    TNG_No_Labels = PD.Series(TNG_Cast);
    print(TNG_No_Labels);

    print("\nB. A panda SERIES when labels are supplied for it.");
    TNG_Headers = ["Captain:","Engineer:","Tactical:","Science:","1st Mate:","Doctor:","Counselor:"];
    print(PD.DataFrame(TNG_Cast,TNG_Headers,None));

#----------------------------------------------------------------------------------------------------------------------------



#Example: Labels = by default Pandas use ARRAY subcript value syntax
#Fibonacci Sequence: Next number found by adding up the two numbers before it.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Series_02():
    import pandas as PD;

    Fibonacci_Sequence = [0,1,1,2,3,5,8,13,21,34];
    Golden_Ratio = PD.Series(Fibonacci_Sequence);

    print("\n-------------------------------------------------------------");
    print("A. Entire SERIES at once:\n");
    print(Golden_Ratio);

    print("\n-------------------------------------------------------------");
    print("B. Accessing SERIES element by element using subscript value\n");
    print("Element 0:",Golden_Ratio[0]);
    print("Element 1:",Golden_Ratio[1]);
    print("Element 2:",Golden_Ratio[2]);
    print("Element 3:",Golden_Ratio[3]);
    print("Element 4:",Golden_Ratio[4]);
    print("Element 5:",Golden_Ratio[5]);
    print("Element 6:",Golden_Ratio[6]);
    print("Element 7:",Golden_Ratio[7]);          

#----------------------------------------------------------------------------------------------------------------------------


#Example: Panda SERIES shorthand - use index argument to create label names
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Series_03():
    import pandas as PD;

    Transporter_Coordinates = [100.357, 90.82, 203.456];
    Beam_Target = PD.Series(Transporter_Coordinates, index = ["x pt:","y pt:","z pt:"]);

    print("\n-------------------------------------------------------------");
    print("A. Entire SERIES at once:\n");
    print(Beam_Target);

    print("\n-------------------------------------------------------------");
    print("B. SERIES element by element:\n");
    print("Element 1",Beam_Target["x pt:"]);
    print("Element 2",Beam_Target["y pt:"]);
    print("Element 3",Beam_Target["z pt:"]);


#----------------------------------------------------------------------------------------------------------------------------



#Example: Creating Panda SERIES from a Dictionary
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Series_04():
    import pandas as PD;

    Blood_Sugar = {  "Day 1:": 300, 
                     "Day 2:": 250, 
                     "Day 3:": 185, 
                     "Day 4:": 150
                  };

    Sugar_Levels = PD.Series(Blood_Sugar);

    print("\n-------------------------------------------------------------");
    print("A. Entire SERIES from Dictionary at once:\n");
    print(Sugar_Levels);

    print("\n-------------------------------------------------------------");
    print("B. Panda SERIES element by element:\n");
    print("Element 0: ",Sugar_Levels[0]);
    print("Element 1: ",Sugar_Levels[1]);
    print("Element 2: ",Sugar_Levels[2]);
    print("Element 3: ",Sugar_Levels[3]);

    print("\n-------------------------------------------------------------");
    print("\nC. Some Panda SERIES methods:\n");
    print("\nMethod DESCRIBE:\n",Sugar_Levels.describe(),sep='');
    print("\nAttribute ALL:\n",Sugar_Levels.all,sep='');
    print("\nAttribute ARRAY:\n",Sugar_Levels.array,sep='');
    print("\nAttribute index:\n",Sugar_Levels.index[0],sep='');

    print("\n-------------------------------------------------------------");
    print("\nD. Panda SERIES key-value pairs:\n");
    print("Element 0: KEY =",Sugar_Levels.index[0],"   VALUE =",Sugar_Levels[0]);
    print("Element 1: KEY =",Sugar_Levels.index[1],"   VALUE =",Sugar_Levels[1]);
    print("Element 2: KEY =",Sugar_Levels.index[2],"   VALUE =",Sugar_Levels[2]);
    print("Element 3: KEY =",Sugar_Levels.index[3],"   VALUE =",Sugar_Levels[3]);


#----------------------------------------------------------------------------------------------------------------------------



#Example: Creating Panda Series from Partial Dictionary
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Series_05():
    import pandas as PD;

    Betelgeuse_Luminosities = {"Year_2023": 14000, "Year_2024": 15000, "Year_2025": 16000};

    Countdown_to_Supernova = PD.Series(Betelgeuse_Luminosities, index = ["Year_2023", "Year_2024"]);

    print("A. Creating a Panda SERIES from the PARTIAL contens of a dictionary.");

    print(Countdown_to_Supernova);
#----------------------------------------------------------------------------------------------------------------------------




#Example: DataFrames = multi-dimensional table data sets in Pandas. Where a Series is a single column, a DataFrame is an entire table.
#           A Pandas DataFrame is a 2 dimensional array. A.K.A. a table with rows and columns.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_DataFrames_01():
    import pandas as PD;

    PinkiPie_Productivity = {  "DayOfWeek": [1,2,3,4,5,6,7],
                               "Cupcakes":  [444,333,777,42,851,0,500]
                            };

    PPP_Data = PD.DataFrame(PinkiPie_Productivity);

    print("\n*********************************************************************");
    print("A. Entire Panda DataFrame at once.");
    print(PPP_Data);

    print("\n*********************************************************************");
    print("B. Single Panda DataFrame row.\n");
    print(PPP_Data.loc[[0]]);

    print("\n*********************************************************************");
    print("C. All Panda DataFrames row by row via iterable FOR loop.\n");
    for X in range(len(PPP_Data)):
        print("___________________________________________________________");
        print("Row ",(X+1),"\n",PPP_Data.loc[X],sep='');

    print("\n*********************************************************************");
    print("D. Return Panda DataFrame rows specified as argument to loc() method.\n");   
    print(PPP_Data.loc[[0,1,2,3,4,5,6]]);

#----------------------------------------------------------------------------------------------------------------------------


#Example: DataFrames = customizing row names.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_DataFrames_02():
    import pandas as PD;

    PinkiPie_Productivity = {  "DayOfWeek": [1,2,3,4,5,6,7],
                               "Cupcakes":  [444,333,777,42,851,0,500]
                            };

    PPP_Data = PD.DataFrame(PinkiPie_Productivity, index=["Mon","Tues","Weds","Thurs","Fri","Sat","Sun"]);

    print("\n*********************************************************************");
    print("A. Entire Panda DataFrame at once with customized labels via the index parameter.");
    print(PPP_Data);

    print("\n*********************************************************************");
    print("B. Accessing single row by customized index parameter.");
    print(PPP_Data.loc["Fri"]);
#----------------------------------------------------------------------------------------------------------------------------



#Example 11: max_rows = your system's maximum rows. If DataFrame contains more than max_rows, it will return only the headers and first and last 5 rows.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_Max_Rows():
    import pandas as pd;

    print(pd.options.display.max_rows);

    #You can set the value higher to display more rows
    pd.options.display.max_rows = 9999;    
#----------------------------------------------------------------------------------------------------------------------------  




#CSV Example: Load and read from a CSV file into a Pandas DataFrame
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_CSV_01():
    import pandas as PD;

    Cast_of_One_Piece = PD.read_csv('Panda_CSV_Data.csv');

    print("\nA. EXAMPLE: Loading a CSV file into a Panda and reading data from it.\n");
    print(str(Cast_of_One_Piece)); 
#----------------------------------------------------------------------------------------------------------------------------   



#Example: 
# head() = returns headers and a specified number of rows, starting from the top.
# tail() = returns headers and a specified number of rows, starting from the bottom.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_CSV_02():
    import pandas as PD;

    Cast_of_One_Piece = PD.read_csv('Panda_CSV_Data.csv');

    print("\n*********************************************************************");
    print("A. HEAD() = Return headers and specified # of rows from TOP. If rows specified > last row ends at last.");
    print(Cast_of_One_Piece.head(4));  

    print("\n*********************************************************************");
    print("B. TAIL() = Return headers and specified # of rows from BOTTOM. ");
    print(Cast_of_One_Piece.tail(4));
#----------------------------------------------------------------------------------------------------------------------------  




#Example: info() = print information about panda's data.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_CSV_03():
    import pandas as PD;

    Cast_of_One_Piece = PD.read_csv('Panda_CSV_Data.csv');

    print("\nA. Using panda's info() method with data loaded from a CSV.\n");
    print(Cast_of_One_Piece.info());      
#----------------------------------------------------------------------------------------------------------------------------




#Example: JSON files = have same format as Python Dictionaries. When this is the case, you can load JSON into DataFrame directly.
#Notice formatting and syntax for JSON rows and columns when loaded into a Panda DataFrame.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_JSON_01():
    import pandas as PD;

    JSON_Data = {
      "Health":{
        "Fighter":200,
        "Paladin":180,
        "Mage":100,
        "Monk":250,
        "Thief":90,
        "Hybrid":125
      },
      "Atk":{
        "Fighter":10,
        "Paladin":8,
        "Mage":5,
        "Monk":12,
        "Thief":6,
        "Hybrid":7
      },
      "Def":{
        "Fighter":10,
        "Paladin":15,
        "Mage":5,
        "Monk":15,
        "Thief":10,
        "Hybrid":9
      },
      "Mag Pwr":{
        "Fighter":100,
        "Paladin":200,
        "Mage":1000,
        "Monk":500,
        "Thief":100,
        "Hybrid":300
      }      
    };

    Data_Frame = PD.DataFrame(JSON_Data);

    print("\nA. JSON files have same format as Python Dictionaries. When this is the case you can load JSON data into a DataFrame directly.");
    print(Data_Frame); 
#---------------------------------------------------------------------------------------------------------------------------- 



#Example: JSON files = plain text but have format of an object
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_JSON_02():
    import pandas as PD;

    Data_Frame = PD.read_json('Panda_JSON_Data.json');

    print(Data_Frame.to_string());  
#----------------------------------------------------------------------------------------------------------------------------  



#Cleaning BAD Data with Pandas
#Function:--------------------------------------------------------------------------------------------------------------------
# dropna() = removes rows with empty cells 
# By default dropna() returns a new DataFrame and will not change the original.
def Pandas_Cleaning_Bad_Data_01():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_01.csv');
    Modified_Data_Frame = Original_Data_Frame.dropna();

    print("\n*********************************************************************");
    print("A. The original DataFrame. Contains rows with empty cells.");
    print(Original_Data_Frame.to_string()); 

    print("\n*********************************************************************");
    print("B. New modfied DataFrame. All rows with empty cells have been removed.");
    print(Modified_Data_Frame.to_string());  
#----------------------------------------------------------------------------------------------------------------------------  



#Function:--------------------------------------------------------------------------------------------------------------------
# dropna() with argument "inplace=True" will modify original DataFrame and will not create a new DataFrame
def Pandas_Cleaning_Bad_Data_02():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_01.csv');
    
    print("\n*********************************************************************");
    print("A. Original DataFrame BEFORE calling dropna(inplace=True). Contains rows with empty cells.");
    print(Original_Data_Frame.to_string()); 

    Original_Data_Frame.dropna(inplace=True);    

    print("\n*********************************************************************");
    print("B. Original DataFrame AFTER calling dropna(inplace=True). All rows with empty cells have been removed.");
    print(Original_Data_Frame.to_string()); 
#----------------------------------------------------------------------------------------------------------------------------  



#Function:--------------------------------------------------------------------------------------------------------------------
# dropna() with argument "subset=['Atk'], inplace=True" to TARGET a specific column.
def Pandas_Cleaning_Bad_Data_03():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_01.csv');
    
    print("\n*********************************************************************");
    print("A. Original DataFrame BEFORE calling dropna(inplace=True). Contains rows with empty cells.");
    print(Original_Data_Frame.to_string()); 

    Original_Data_Frame.dropna(subset=['Atk'], inplace=True);    

    print("\n*********************************************************************");
    print("B. Original DataFrame AFTER calling dropna(subset=['Atk'],inplace=True). All rows with empty cells have been removed.");
    print("Specifically targets ONLY the Atk column for removal of empty cells.");
    print(Original_Data_Frame.to_string()); 
#----------------------------------------------------------------------------------------------------------------------------  


#Function:--------------------------------------------------------------------------------------------------------------------
# fillna() with argument "inplace=True" will REPLACE original DataFrame empty cells with specified data
def Pandas_Cleaning_Bad_Data_04():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_01.csv');
    
    print("\n*********************************************************************");
    print("A. Original DataFrame BEFORE calling fillna(444,inplace=True). Contains rows with empty cells.");
    print(Original_Data_Frame.to_string()); 

    Original_Data_Frame.fillna(444,inplace=True);    

    print("\n*********************************************************************");
    print("B. Original DataFrame AFTER calling fillna(444,inplace=True). All empty rows filles with 444.");
    print(Original_Data_Frame.to_string());  
#----------------------------------------------------------------------------------------------------------------------------


#Function:--------------------------------------------------------------------------------------------------------------------
# Casting data of the wrong type to the right type
# to_datetime() converts data to date format
def Pandas_Cleaning_Bad_Data_05():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_02.csv');
    
    print("\n*********************************************************************");
    print("A. Original DataFrame BEFORE casting bad data to correct type.");
    print(Original_Data_Frame.to_string()); 

    #Reflexive, column of data performs transformation on itself
    Original_Data_Frame['JoinedCrewDate'] = PD.to_datetime(Original_Data_Frame['JoinedCrewDate'],format='mixed');    

    print("\n*********************************************************************");
    print("B. Original DataFrame AFTER casting bad data to the correct type.");
    print(Original_Data_Frame.to_string());  
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Loc() = Targeting and REPLACING specific bad data
def Pandas_Cleaning_Bad_Data_06():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_01.csv');
    
    print("\n*********************************************************************");
    print("A. Original DataFrame BEFORE targeting and changing specific data.");
    print(Original_Data_Frame.to_string()); 

    Original_Data_Frame.loc[2,'Health'] = 42;   

    print("\n*********************************************************************");
    print("B. Original DataFrame AFTER targeting and changing specific data.");
    print(Original_Data_Frame.to_string());  
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Loc() and index = Targeting and REPLACING all bad data in an entire column with specified VALUE
def Pandas_Cleaning_Bad_Data_07():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_01.csv');
    
    print("\n*********************************************************************");
    print("A. Original DataFrame BEFORE targeting and CHANGING specific data.");
    print(Original_Data_Frame.to_string()); 

    for X in Original_Data_Frame.index:
        if(Original_Data_Frame.loc[X,'Health'] > 3000):
           Original_Data_Frame.loc[X,'Health'] = 444;
              
    print("\n*********************************************************************");
    print("B. Original DataFrame AFTER targeting and CHANGING specific data.");
    print(Original_Data_Frame.to_string());  
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Drop() = Targeting and DROPPING all bad data in an entire column
def Pandas_Cleaning_Bad_Data_08():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_01.csv');
    
    print("\n*********************************************************************");
    print("A. Original DataFrame BEFORE targeting and DROPPING specific data.");
    print(Original_Data_Frame.to_string()); 

    for X in Original_Data_Frame.index:
        if(Original_Data_Frame.loc[X,'Health'] > 3000):
           Original_Data_Frame.drop(X,inplace=True);
              
    print("\n*********************************************************************");
    print("B. Original DataFrame AFTER targeting and DROPPING specific data.");
    print(Original_Data_Frame.to_string());  
#----------------------------------------------------------------------------------------------------------------------------


#Function:--------------------------------------------------------------------------------------------------------------------
# Duplicated() and Drop_duplicates() = Return if rows are duplicates and remove duplicates (de-duplicating)
def Pandas_Cleaning_Bad_Data_09():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_BAD_DATA_02.csv');
    
    print("\n*********************************************************************");
    print("A. Are any rows in this DataFrame duplicated?");
    print(str(Original_Data_Frame.duplicated()));

    Original_Data_Frame.drop_duplicates(inplace=True);

    print("\n*********************************************************************");
    print("B. After calling drop_duplicates() are any rows in this DataFrame duplicated?");
    print(str(Original_Data_Frame.duplicated()));
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Correlations = calculates relationships between each column in data set.
# 1   = 1 to 1 relationship (each time value goes up in 1st column, other column goes up also)
# -1  = 1 to -1 relationship (each time value goes up in 1st column, other column goes down)
# 0.2 = NOT a good relationship
def Pandas_Pandas_Analyzing_Data_01():
    import pandas as PD;

    Original_Data_Frame = PD.read_csv('Panda_DATA_03.csv');

    print("\n*********************************************************************");
    print("A. Get correlations within DATA set.");    
    print(Original_Data_Frame.corr(numeric_only=True));
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Plotting Data
def Pandas_Pandas_Analyzing_Data_02():
    import pandas as PD;
    import matplotlib.pyplot as The_Plot;

    Original_Data_Frame = PD.read_csv('Panda_DATA_03.csv');

    print("\n*********************************************************************");
    print("A. BASIC PLOT: Plot diagram of the data set.");    

    Original_Data_Frame.plot();
    The_Plot.show();
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Plotting Data
def Pandas_Pandas_Analyzing_Data_03():
    import pandas as PD;
    import matplotlib.pyplot as The_Plot;

    Original_Data_Frame = PD.read_csv('Panda_DATA_03.csv');

    print("\n*********************************************************************");
    print("A. Specify Scatter PLOT: Scatter diagram of the data set.");    

    Original_Data_Frame.plot(kind='scatter',x='Health',y='Def');
    The_Plot.show();
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Plotting Data
def Pandas_Pandas_Analyzing_Data_04():
    import pandas as PD;
    import matplotlib.pyplot as The_Plot;

    Original_Data_Frame = PD.read_csv('Panda_DATA_03.csv');

    print("\n*********************************************************************");
    print("A. Specify Histogram PLOT: Histogram of the data set.");    

    Original_Data_Frame.plot(kind='hist');
    The_Plot.show();
#----------------------------------------------------------------------------------------------------------------------------



#Function:--------------------------------------------------------------------------------------------------------------------
# Plotting Data
def Pandas_Pandas_Analyzing_Data_05():
    import pandas as PD;
    import matplotlib.pyplot as The_Plot;

    Original_Data_Frame = PD.read_csv('Panda_DATA_03.csv');

    print("\n*********************************************************************");
    print("A. Specify Histogram PLOT based on only ONE columns (Health).");    

    Original_Data_Frame['Health'].plot(kind='hist');
    The_Plot.show();
#----------------------------------------------------------------------------------------------------------------------------


#Invocations-------------------------
#Pandas_Check_Version();
#Pandas_Example_1();
#Pandas_Example_1B();
#Panda_Table();
#Pandas_Series_01();
#Pandas_Series_02();
#Pandas_Series_03();
#Pandas_Series_04();
#Pandas_Series_05();
#Pandas_Example_DataFrames_01();
#Pandas_Example_DataFrames_02();
#Pandas_Example_Max_Rows();

#-----Pandas with CSV files
#Pandas_CSV_01();
#Pandas_CSV_02();
#Pandas_CSV_03();

#-----Pandas with JSON files
#Pandas_JSON_01();
#Pandas_JSON_02();

#-----Cleaning Bad Data with Pandas
#Pandas_Cleaning_Bad_Data_01();
#Pandas_Cleaning_Bad_Data_02();
#Pandas_Cleaning_Bad_Data_03();
#Pandas_Cleaning_Bad_Data_04();
#Pandas_Cleaning_Bad_Data_05();
#Pandas_Cleaning_Bad_Data_06();
#Pandas_Cleaning_Bad_Data_07();
#Pandas_Cleaning_Bad_Data_08();
#Pandas_Cleaning_Bad_Data_09();

#-----Analyzing Data with Pandas
#Pandas_Pandas_Analyzing_Data_01();
#Pandas_Pandas_Analyzing_Data_02();
#Pandas_Pandas_Analyzing_Data_03();
#Pandas_Pandas_Analyzing_Data_04();
Pandas_Pandas_Analyzing_Data_05();











"""
WHAT: Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?

Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

WHY: Pandas allows us to analyze big data and make conclusions based on statistical theories. Pandas can clean messy data sets, and make them readable and relevant.

HOW to Install: If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Install it using this command: pip install pandas
Once Pandas is installed, import it in your applications by adding the import keyword: import pandas

"""