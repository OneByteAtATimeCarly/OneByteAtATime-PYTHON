# Title: Python Functions 5 - Command line part 2
# Author: C. S. Germany 01/15/2022

# Python provides a getopt module that helps you parse command-line options and arguments.
# Basic command line script in GLOBAL namespace

# Syntax: getopt.getopt(args, options, [long_options])
# 
# args         = This is the argument list to be parsed.
# options      = This is the string of option letters that the script wants to recognize, with options that require an argument should be followed by a colon (:).
# long_options = This is optional parameter and if specified, must be a list of strings with the names of the long options, which should be supported. 
#                Long options, which require an argument should be followed by an equal sign ('='). To accept only long options, options should be an empty string.
 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 
import sys, getopt;

def main(argv):
    inputfile = '';
    outputfile = '';
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["InputFile=","OutputFile="]);
    except getopt.GetoptError:
           print("Incorrect Syntax or argumentation! Correct usage from cmd prompt is:");
           print("python \"Python_017_Functions_05.py\" -i <InputFile> -o <OutputFile>");
           sys.exit(2);

    for opt, arg in opts:
        if opt == '-h':
           print("\nHELPING! Correct usage from cmd prompt is");
           print("python \"Python_017_Functions_05.py\" -i <InputFile> -o <OutputFile>");
           sys.exit();
        elif opt in ("-i", "--InputFile"):
             Input_File = arg;
        elif opt in ("-o", "--OutputFile"):
             Output_File = arg;
    print("The INPUT file is: \"",Input_File,"\"",sep='');
    print("The OUTPUT file is: \"",Output_File,"\"",sep='');


if __name__ == "__main__":
   main(sys.argv[1:]);
#---------------------------------------------------------------------------------------------------------------------------------------------------------------- 




#-----Invocations-----

# To run, do not hit "debug" or F5. Rather, from a CMD PROMPT go the the sctipt directory and run from cmd line: 
# cd to "cd\Bills\Carlys_Python_Scripts_2022\Programming_CONSOLE", change to D:
# python "Python_017_Functions_05.py" -h
# python "Python_017_Functions_05.py" -i "UnicornMagic.txt" -o "PegasusPower.txt"
# python "Python_017_Functions_05.py" --InputFile "UnicornMagic.txt" --OutputFile "PegasusPower.txt"




