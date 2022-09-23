# Title: Python LAMDAS 
# Author: C. S. Germany 01/15/2022

# A small anonymous function that can take any number of arguments, but can only have one expression.

# Syntax: lambda arguments : expression
# Usage: When an anonymous function is required for a short period of time


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1 Argument: Creates anonymous function taking x as argument and assigns "Z" to access function. When called, "Z" is used to access function and a "3" is passed in. 
def Lamdas_0l():
    Z = lambda x : x + 777;
    The_result = Z(3);
    print(The_result);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# 2 Arguments: Take x and y as arguments and assigns "DaFunkt" to access function. When called, "DaFunkt" is used to access function and a "7" and "444" are passed in. 
def Lamdas_02():
    DaFunkt = lambda x,y : x * y;
    The_result = DaFunkt(7,444);
    print(The_result);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Nesting Lamdas inside other functions. Polymorphic. Not sure about the usefulness here, though. Clearer and more concise to simply write methods returning values. 
def Lamdas_03():

    def LAMBDA_MATH(X):
        return lambda y : y * X;

    DOUBLED = LAMBDA_MATH(2);
    TRIPLED = LAMBDA_MATH(3);

    print("DOUBLED:",DOUBLED(10));
    print("TRIPLED:",TRIPLED(10));

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#Lamdas_0l();
#Lamdas_02();
Lamdas_03();




