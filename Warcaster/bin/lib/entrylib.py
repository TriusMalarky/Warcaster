def newentryinit(data,saved):
    print(" >> New " + data["entrytype"])
    # Get name
    data["name"]=input(" { What is this "+data["entrytype"]+" called?\n| ")
    if data["entrytype"] != "system":
        data["system"]=input(" { What system will this "+data["entrytype"]+" be legal in?\n| ")
    return data

def checkifused(data, saved):
    if data["name"] in saved:
        print("!Error: "+data["name"]+" already in use.")
        toEdit=input(" { Would you like to edit this entry? [Y/N]\n| ")

def removeentry(saved,entrytype,pathtoindex,pathtodir):
    print(" >> Delete " + entrytype)
    name = input(" { What " + entrytype + " do you want to delete?\n| ")
    if entrytype == "system":
        saved.pop(saved.index(name))
        savefile=open("bin\lib\systems.py","w")
        # Remove Duplicates
        savedexc=[]
        for i in saved:
            if i not in savedexc:
                savedexc.append(i)
        savedexcstr=str(savedexc)
        print(" { Deleting "+entrytype+ " " + name)
        savefile.write(str("saved="+savedexcstr));savefile.close()
    else:
        pass
    return saved
