# Title: Python Console Colors
# Author: C. S. Germany 01/15/2022

#Note: Must change terminal type to do colors. Windows terminal doesn't handle ANSI coding for coloring text like other vt100 compatible terminals and Linux.
#Download Git Bash from: https://git-scm.com/download/win
#To change: Press CTRL+Shift+P  or  F1  and  then search for  "Terminal: Select Default Profile"
#POSH ISE = Powershell: Enable ISE Mode
#Linux (necessary for ANSI colors) = Git Bash


#1. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# OS Console default color. From cmd prompt type: color help.
# Modifies ALL text in console. Try function below. Then uncomment last to lines to change text back.
# Sets the default console foreground and background colors.

# Color attributes are specified by TWO hex digits -- the first
# corresponds to the background; the second the foreground.  Each digit
# can be any of the following values:

#    0 = Black       8 = Gray
#    1 = Blue        9 = Light Blue
#    2 = Green       A = Light Green
#    3 = Aqua        B = Light Aqua
#    4 = Red         C = Light Red
#    5 = Purple      D = Light Purple
#    6 = Yellow      E = Light Yellow
#    7 = White       F = Bright White

# If no argument is given, this command restores the color to what it was
# when CMD.EXE started.  This value either comes from the current console
# window, the /T command line switch or from the DefaultColor registry
# value.

def Colors_01_OS():
    import os;

    os.system('COLOR 09');
    print("Test this color.");
    #os.system('COLOR 0F');
    #print("Test this color.");
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



#2. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# Colorama - provides a few basic colors for Windows consoles which don't do ANSI colors.
# Methods: init() = start colorama, deinit() = deactivate colorama, reinit() - restart colorama.
# Options: Fore, Back and Style. See code below for usage.  
def Colors_02_COLORAMA():
    from colorama import Fore, Back, Style, init, reinit, deinit;

    init(); #activates colorama
    print("");
    print(Back.WHITE, Fore.MAGENTA + 'Twilight Sparkle says:')
    print(Back.BLACK, Fore.RED + 'Friendship is Magic!');
    print(Back.BLACK, Fore.RED + 'RED');
    print(Back.BLACK, Fore.GREEN + 'GREEN');
    print(Back.BLACK, Fore.BLUE + 'BLUE');
    print(Back.BLACK, Fore.MAGENTA + 'MAGENTA');
    print(Back.BLACK, Fore.YELLOW + 'YELLOW');
    print(Back.BLACK, Fore.WHITE + 'WHITE');
    print(Back.BLACK, Fore.CYAN + 'CYAN');
    print(Back.WHITE, Fore.BLACK + 'BLACK');
    print(Back.BLACK, Fore.WHITE, Style.DIM + 'Style = DIM');
    print(Back.BLACK, Fore.WHITE, Style.BRIGHT + 'Style = BRIGHT');
    print(Back.BLACK, Fore.WHITE, Style.NORMAL + 'Style = NORMAL');
    print(Style.RESET_ALL + ' Style = RESET');
    deinit(); #deactivates colorama
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Arguments passed to init() method:
# init(autoreset=True) = automatically resets console colors to defaults after every print statement. Without this arument, colors remain the same until EXPLICITLY changed.
# init(strip=None) = Pass True or False to override whether ANSI codes should be stripped from the output. Default behaviour is to strip if on Windows.
# init(convert=None) = Pass True or False to override whether to convert ANSI codes in the output into win32 calls. The default behaviour is to convert if on Windows.
# init(wrap=True) = In Windows colorama replaces sys.stdout and sys.stderr with proxy objects that override write() method. If this causes problems, wrapping can be disabled with False.


#3. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# init(autoreset=True) = automatically resets console colors to defaults after every print statement. Without this arument, colors remain the same until EXPLICITLY changed.
def Colors_03_COLORAMA():
    from colorama import Fore, Back, Style, init, reinit, deinit;

    init(autoreset=True); #activates colorama and automatically resets console colors 
    print("");
    print(Back.WHITE, Fore.MAGENTA + "Twilight Sparkle says:")
    print("Friendship is Magic!");
    deinit(); #deactivates colorama
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#4. Function-----------------------------------------------------------------------------------------------------------------------------------------------------
# ANSI - Using ANSI code with colorama. Colorama offers very basic and limited ANSI support on a Windows console. 
def Colors_04_COLORAMA():
    from colorama import Fore, Back, Style, init, reinit, deinit;

    init();
    print(""); 
    print('\033[31m' + "ANSI code for RED text");
    print('\033[39m' + "ANSI code for reset to default text"); 
    print('\033[0;35m' + "ANSI code for PURPLE"); 
    print('\033[1;35m' + "ANSI code for light PURPLE"); 
    print('\033[1;30m' + "ANSI code for DARK GRAY"); 
    deinit(); 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Note: You can install other modules with more advanced features to print colored text to console. But unlike colorama they are not built in.
# You will sacrificace some platform independence and you will need to download and install the modules:
# pip install blessings
# pip install termcolor


#Invocations
#Colors_01_OS();
Colors_02_COLORAMA();
#Colors_03_COLORAMA();
#Colors_04_COLORAMA();



