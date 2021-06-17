def entryinit(data,saved):
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
