#Nested and Parallel Repetition Structures
import os;
import random;

#---------------------------------------------------------------------------------------------------------------------------------------------------------
def Nesting_00():
    #A. Single Loop (vertical line)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("A. Single loop, line 10 char wide\n");
    for X in range(10):
        print("*",end='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_01():
    #B. Nested Loop (Vertical Rectangle 10 char wide by 10 char tall)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("B. Nested Loop (Vertical Rectangle 10 char wide by 10 char tall)\n");
    for X in range(10):
        print("");
        
        for Y in range(10):
            print("*",sep='',end='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_02():
    #C. Nested Loop (Vertical Square 10 char wide by 5 char tall)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("C. Nested Loop (Vertical Square 10 char wide by 5 char tall)\n");
    for X in range(5):
        print("");
        
        for Y in range(10):
            print("*",sep='',end='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_03():
    #D. Nested Loop (Horizontal Rectangle)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("D. Nested Loop (Horizontal Rectangle 20 char wide by 5 char tall)\n");
    for X in range(5):
        print("");
        
        for Y in range(20):
            print("*",sep='',end='');
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_04():
    #E. Nested Loop (Right Triangle )
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("E. Nested Loop (Right Triangle)\n");

    for X in range(10):
        
        for Y in range(X):
            print("*",sep='',end='');

        print("");
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Nesting_05():
    #F. Nested Loop (Short Right Triangle)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("F. Nested Loop (Short Right Triangle 1 char to 10 char increment by 2)\n");

     #3rd agrgument to the range() method increment by 2 instead of the default 1
    for X in range(1,10,2):
        
        for Y in range(0,X):
            print("*",sep='',end='');

        print("");
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Parallel_06():
    #G. Parallel Loops 1 (Diamond)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("G. Parallel Loop (Diamond)\n");

    Z = 5;

    for i in range(0,Z):
        print(" "*(Z-i), "*"*(i*2+1));

    for i in range(Z-2, -1, -1):
        print(" "*(Z-i), "*"*(i*2+1));
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Parallel_07():
    #H. Parallel Loops 2 (Diamond)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("H. Parallel Loop (Diamond)\n");

    A=5;
    for i in range(1,A+1):
        print ((A-i)*(" ")+(i*" *"));

    for i in range(A-1,0,-1):
        print((A-i)*(" ")+(i*" *"));
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Single_08():
    #I. Single Loop 1 (Diamond)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("I. Single Loop 1 (Diamond)\n");

    num = 9

    for i in range(1, num+1):
        i = i - (num//2 +1)
        if(i < 0):
           i = -i;
        print(" " * i + "*" * (num - i*2) + " "*i);
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Single_09():
    #J. Single Loop 1 (Diamond)
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("J. Single Loop 2 (Diamond)\n");

    side = 10;
    for x in list(range(side)) + list(reversed(range(side-1))):
        print('{: <{w1}}{:*<{w2}}'.format('', '', w1=side-x-1, w2=x*2+1));
#---------------------------------------------------------------------------------------------------------------------------------------------------------


def Tree_10():
    #K. A Tree
    os.system("cls");
    print("\n\n----------------------------------------------------------------------");
    print("K. Single Loop (Tree)\n"); 

    Height = 5;
    for i in range(Height):
        print(("+" * (i * 2 + 1)).center(Height * 2 - 1));
#------------------------------------------------------------------------------------------





#Invocations
#Nesting_00();
#Nesting_01();
#Nesting_02();
#Nesting_03();
#Nesting_04();
#Nesting_05();
#Parallel_06();
#Parallel_07();
#Single_08();
#Single_09();
Tree_10();


