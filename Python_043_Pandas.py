# Python Pandas
# Author: C. S. Germany 01/15/2022


#Example 0: Checking version
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Check_Version():
    import pandas as pd;
    print(pd.__version__);
#----------------------------------------------------------------------------------------------------------------------------   


#Example 1: Manipulating Data
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_1():
    import pandas;

    mydataset = {
                   'cars': ["BMW", "Volvo", "Ford"],
                   'passings': [3, 7, 2]
                };

    myvar = pandas.DataFrame(mydataset);
    print(myvar);
#----------------------------------------------------------------------------------------------------------------------------   



#Function-------------------------------------------------------------------------------------------------------------------------
def Panda_Table():
    import pandas;
    data = [[1, 'Rainbow Dash', 100, 10],
    [2, 'Fluttershy', 75, 20],
    [3, 'Twilight Sparkle', 70, 25],
    [4,'AppleJack', 60, 35]]; 
    headers=["Pos", "Team", "Win", "Lose"];  
    print(pandas.DataFrame(data,None,headers)); #HORIZONTAL table headers
    #print(pandas.DataFrame(data,headers,None)); #VERTICAL table headers
    #print(pandas.DataFrame(data,headers,headers)); #BOTH
#---------------------------------------------------------------------------------------------------------------------------------



#Example 2: Load a CSV file into a Pandas DataFrame
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_2():
    import pandas as pd;

    df = pd.read_csv('data.csv');
    print(df.to_string()); 
#----------------------------------------------------------------------------------------------------------------------------   



#Example 3: A Panda Series = a one-dimensional array holding data of any type, like a column in a table.
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_3_Series():
    import pandas as pd;

    a = [1, 7, 2];
    myvar = pd.Series(a);
    print(myvar);
#----------------------------------------------------------------------------------------------------------------------------



#Example 4: Labels = by default Pandas use array subecript value syntax
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_4_Series():
    import pandas as pd;

    a = [1, 7, 2];
    myvar = pd.Series(a);
    print(myvar);
    print(myvar[0]);
#----------------------------------------------------------------------------------------------------------------------------


#Example 5: index argument = create your own label names
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_5_Series():
    import pandas as pd;

    a = [1, 7, 2];
    myvar = pd.Series(a, index = ["x", "y", "z"]);

    print(myvar);
    print(myvar["y"]);
#----------------------------------------------------------------------------------------------------------------------------



#Example 6: Creating Panda Series from Dictionary
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_6_Series():
    import pandas as pd;

    calories = {"day1": 420, "day2": 380, "day3": 390};

    myvar = pd.Series(calories);
    print(myvar);
#----------------------------------------------------------------------------------------------------------------------------



#Example 7: Creating Panda Series from Partial Dictionary
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_7_Series():
    import pandas as pd;

    calories = {"day1": 420, "day2": 380, "day3": 390};

    myvar = pd.Series(calories, index = ["day1", "day2"]);
    print(myvar);
#----------------------------------------------------------------------------------------------------------------------------


#Example 8: DataFrames = multi-dimensional table data sets in Pandas. Where a Series is a single column, a DataFrame is an entire table.
#           A Pandas DataFrame is a 2 dimensional array. A table with rows and columns.
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_8_DataFrames():
    import pandas as pd;

    data = {
              "calories": [420, 380, 390],
              "duration": [50, 40, 45]
           };

    myvar = pd.DataFrame(data);

    print("\n1. Everything");
    print(myvar);
    print("\n2. Return Specified Row 0");
    print(myvar.loc[0]);
    print("\n3. Return Specified Row 0,1");
    print(myvar.loc[[0,1]]);
    print("\n4. Return Specified Row 0,1,2");
    print(myvar.loc[[0,1,2]]);
#----------------------------------------------------------------------------------------------------------------------------


#Example 9: DataFrames = customizing row names.
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_9_DataFrames():
    import pandas as pd;

    data = {
              "calories": [420, 380, 390],
              "duration": [50, 40, 45]
           };

    myvar = pd.DataFrame(data, index = ["day1", "day2", "day3"]);

    print("\n1. Everything with Customized Labels");
    print(myvar);
    print("\n2. Indexing Access by Customized Label");
    print(myvar.loc["day2"]);
#----------------------------------------------------------------------------------------------------------------------------


#Example 10: Loading CSV file into a Panda DataFrame. 
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_10():
    import pandas as pd;

    df = pd.read_csv('data.csv');
    print(df) ;
#----------------------------------------------------------------------------------------------------------------------------   

#Example 11: max_rows = your system's maximum rows. If DataFrame contains more than max_rows, it will return only the headers and first and last 5 rows.
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_11():
    import pandas as pd;

    print(pd.options.display.max_rows);

    #You can set the value higher to display more rows
    pd.options.display.max_rows = 9999;    
#----------------------------------------------------------------------------------------------------------------------------  


#Example 12: JSON files = plain text but have format of an object
#Funtion:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_12():
    import pandas as pd;

    df = pd.read_json('data.json');

    print(df.to_string());  
#----------------------------------------------------------------------------------------------------------------------------  


#Example 13: JSON files = have same format as Python Dictionaries. When this is the case, you can load JSON into DataFrame directly.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_13():
    import pandas as pd;

    data = {
      "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
      },
      "Pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":102
      },
      "Maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127
      },
      "Calories":{
        "0":409,
        "1":479,
        "2":340,
        "3":282,
        "4":406,
        "5":300
      }
    };

    df = pd.DataFrame(data);
    print(df); 
#---------------------------------------------------------------------------------------------------------------------------- 


#Example 14: head() = returns headers and a specified number of rows, starting from the top.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_14():
    import pandas as pd;
    df = pd.read_csv('data.csv');
    print(df.head(10));
    print(df.head());    
#----------------------------------------------------------------------------------------------------------------------------  


#Example 15: tail() = returns headers and a specified number of rows, starting from the bottom.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_15():
    import pandas as pd;
    df = pd.read_csv('data.csv');
    print(df.tail(10));
    print(df.tail());      
#----------------------------------------------------------------------------------------------------------------------------


#Example 16: info() = print information about the data.
#Function:--------------------------------------------------------------------------------------------------------------------
def Pandas_Example_16():
    import pandas as pd;
    df = pd.read_csv('data.csv');
    print(df.info());      
#----------------------------------------------------------------------------------------------------------------------------





#Invocations-------------------------
#Pandas_Check_Version();
#Pandas_Example_1();
#Pandas_Example_2();
#Pandas_Example_3_Series();
#Pandas_Example_8_DataFrames();
#Pandas_Example_9_DataFrames();
Pandas_Example_10();


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