# Title: Python LAMDAS 
# Author: C. S. Germany 01/15/2022

# Definition: A Python lambda function is small anonymous function that can take any number of arguments, but can only have one expression.
# History: Lambda functions emulate lambda calculus, a language based on pure abstraction, formalized by Alonzo Church in the 1930s.

# Turing-Complete: A term used in computability theory that describes abstract machines. These are called "automata". An automaton is
# considered to be "Turing-Complete" if it can be used to emulate a "Turing Machine". It is also called "computationally universal".
# Most modern programming languages are Turing-Complete. An example of one that is not is HTML. HTML is not Turing-Complete because
# it cannot actively change the state of the system. Only when combined with another language like JavaScript can HTML in combination
# with that other language be considered a Turing-Complete system. Another example is REGEX. REGEX expressions are not Turing-Complete.
# This is because tey include back-references, and a finite automaton cannot handle back references.

# Regular expression: REGEX are sets of characters using syntactic rules in a programming language. 

# Turing machine: A mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according
# to a table of rules. This model is capable of implementing any computer algorithm.

# Functional Languages: Haskell, Lisp, Erlang. Programming emphasizes abstraction, transformation, composition and purity (no state or side-effects).

# Imperative Languages: Fortran, C, Python. Programmed with statements that manipulate program flow step-by-step with detailed instructions.
# This promotes mutation and requires managing state.

# In January 1994, map(), filter(), reduce(), and the LAMBDA operator were added to Python. So even though it is an IMPERATIVE and not a 
# FUNCTIONAL programming language, Python can emulate functional abstractions.

# Syntax: lambda arguments : expression
# Usage: When an anonymous function is required for a short period of time
# Comparison: Provides polymorphic functions like C++'s function pointers.

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




