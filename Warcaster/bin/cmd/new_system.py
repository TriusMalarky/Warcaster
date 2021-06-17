from bin.lib.entrylib import * # Import Entry Library Functions

def new_system(saved):
    # Variable 'saved' is 'savedsystems' from main

    # Initialize Function Variables
    data={} # Initiate new dictionary
    data["entrytype"]="system" # Local variable for use in libfuncs
    data=entryinit(data,saved)
