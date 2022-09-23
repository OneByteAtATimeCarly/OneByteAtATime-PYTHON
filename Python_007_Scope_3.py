# Scope: Scope within nested functions and using "nonlocal"


#Variables declared outside a function are autmatically GLOBAL and available to all functions



#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
#   Default scope
def Scope_03():
    
    #Declared in parent function scope
    My_Name = "Carly Salali Germany";

    print("\nA. Default scope of nested functions when NOT using \"nonlocal\" - Change is LOCAL:\n");
    print("   Inside PARENT function: My_Name = ",My_Name);

    def Nested_Function_Inside_Function_1():
        My_Name = "Your FACE!";
        print("   Inside nested CHILD function: My_Name = ",My_Name);

    Nested_Function_Inside_Function_1();    
    print("   Back inside PARENT function: My_Name = ",My_Name);


    print("\nB. Default scope of nested functions when using \"nonlocal\" - Change is GLOBAL:\n");
    print("   Inside PARENT function: My_Name = ",My_Name);

    def Nested_Function_Inside_Function_2():
        nonlocal My_Name;
        My_Name = "Your FACE!";
        print("   Inside nested CHILD function: My_Name = ",My_Name);

    Nested_Function_Inside_Function_2();    
    print("   Back inside PARENT function: My_Name = ",My_Name);    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 



#-----Invocations-----
Scope_03();

