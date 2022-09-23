# Title: Python ITERATORS
# Author: C. S. Germany 01/15/2022 

#An object containing a countable number of values. Lists, Tuples, Dictionaries, and Sets are iterable objects you can get an iterator from. 
# Methods: __iter__(),   __next__(),  iter(),  next()

#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# inter() to return iterator from a Tuple. Use next() method to return each Tuple item in sequence. 
def Iterators_0l():
    Tuple_MLP_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");

    The_Iterator = iter(Tuple_MLP_Main_Chars);

    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# A string in and of itself is an iterable objects since it's really an array of type char.
def Iterators_02():
    The_Message = "MLP Friendship is Magic";

    The_Iterator = iter(The_Message);

    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));
    print(next(The_Iterator));            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING 1: Iterators work behind the scenes with iterable objects like Lists, Tuples, Dictionaries and Sets to allow us to use them in repetition structures.
def Iterators_03():
    Tuple_MLP_Main_Chars = ("Twilight Sparkle","Fluttershy","Rainbow Dash","Rarity","Apple Jack","Pinkie Pie");

    for X in Tuple_MLP_Main_Chars:
        print(X);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# LOOPING 2: Iterators work behind the scenes with iterable objects like Lists, Tuples, Dictionaries and Sets to allow us to use them in repetition structures.
def Iterators_04():
    The_Message = "MLP Friendship is Magic!";

    for X in The_Message:
        print(X);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#-----Invocations-----
#Iterators_0l();
#Iterators_02();
#Iterators_03();
Iterators_04();
