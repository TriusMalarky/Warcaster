import os # <- Import Operating System. I forgot what this was for, it might not be relevant anymore. Leave it in.
from bin.lib.entrylib import * # Import Entry Library Functions

# Import variables from the init
from bin.lib.init import init;save=init();flags=save["flags"]

def findflag(flag): # <- Lambda for finding the right set of flags to check against
    return flags["list"][flags["names"].index(flag)]


dashln=30*"-";print(dashln+"| Warcaster |"+dashln) # Prints the title banner at the beginning of the script.


while save["running"]: # <- Runs the program until exit command is given

    
    uinput=input("| ");uinput=uinput.lower();uinput=uinput.split() # <- Takes the user's input and formats it for parsing.
    if uinput == []: uinput = ["null"] # <- Check to prevent script from crashing when no input is present

    if uinput[0] in findflag("exit"): print(" - Closing Warcaster - "); save["running"]=False # <- Exit Warcaster

    elif uinput[0] in findflag("new"):
        if len(uinput) > 1:
            if uinput[1] in findflag("system"): from bin.cmd.new_system import new_system;save["systems"]=new_system(save["systems"])
        else: print(" >> Please specify entry type")

    elif uinput[0] in findflag("delete"):
        if len(uinput) > 1:
            if uinput[1] in findflag("system"): from bin.cmd.delete_system import delete_system;save["systems"]=delete_system(save["systems"])
        else: print(" >> Please specify entry type")

    elif uinput[0] in findflag("list"):
        if len(uinput) > 1:
            def printall(flag,title):
                string=" { Saved " + title + ": \n"
                for i in save[flag]:
                    string = string + " - " + i + "\n"
                print(string)
            if uinput[1] in findflag("system"):
                printall("systems","Systems")
        else: print(" >> Please specify entry type")

    else: pass # <- Tells the script to ignore what happened if input doesn't fall under any of the above options. May not be relevant.
