def entryinit(data,saved):
    # Get name
    data["name"]=input(" { What is this "+data["entrytype"]+" called?\n| ")

def checkifused(data, saved):
    if data["name"] in saved:
        print("!Error: "+data["name"]+" already in use.")
        toEdit=input(" { Would you like to edit this entry? [Y/N]\n| ")
