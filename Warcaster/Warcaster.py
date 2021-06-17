import os # <- Import Operating System. I forgot what this was for, it might not be relevant anymore. Leave it in.
from bin.lib.entrylib import * # Import Entry Library Functions

# Import variables from the init
from bin.lib.init import init;save=init();flags=save["flags"]

def findflag(flag):
    return flags["list"][flags["names"].index(flag)]


dashln=30*"-";print(dashln+"| Warcaster |"+dashln) # Prints the title banner at the beginning of the script.


while save["running"]: # <- The while running section makes sure the script runs until the user turns it off. I haven't actually implemented the exit command yet.

    
    uinput=input("| ");uinput=uinput.lower();uinput=uinput.split() # <- Takes the user's input and formats it for parsing.

    if uinput[0] in findflag("exit"): print(" - Closing Warcaster - "); save["running"]=False # <- Exit Warcaster
