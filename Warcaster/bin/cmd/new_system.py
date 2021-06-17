from bin.lib.entrylib import * # Import Entry Library Functions

def new_system(saved):
    # Variable 'saved' is 'savedsystems' from main

    # Initialize Function Variables
    data={} # Initiate new dictionary
    data["entrytype"]="system" # Local variable for use in libfuncs
    data=newentryinit(data,saved)

    
    # Using a separate clause from checkifused function because systems only have the name as data.
    if data["name"] in saved:
        print("!Error: "+data["name"]+" already exists.")
    else:
        saved.append(data["name"])
        savefile=open("bin\lib\systems.py","w")
        # Remove Duplicates
        savedexc=[]
        for i in saved:
            if i not in savedexc:
                savedexc.append(i)
        savedexcstr=str(savedexc)
        #Write File
        print(" { Saving "+data["entrytype"]+" " + data["name"])
        savefile.write(str("saved="+savedexcstr));savefile.close()
    print(" - Complete - ")
    return saved # <- Return the new saved list for runtime updating

    
