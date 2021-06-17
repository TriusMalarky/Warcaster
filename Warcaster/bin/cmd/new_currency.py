# Variable 'data' is an empty dictionary passed from main and returned.
# Variable 'saved' is 'savedcurrencies' list from main.

def new_currency(data,saved):

    # Function Banner
    print(">> New Currency")

    # Get Currency Name
    data["name"]=input(" { What would you like to call the currency?\n| ")

    
    for i in saved:
        inp = input(" { Is this worth more(type 'M') or less(type 'L') than "+i+"\n| ")
        if inp.upper() == "M":
            data[i+"posrate"]=int(input(" { How many "+i+" is a "+data["name"]+" worth?\n| "))
        elif inp.upper() == "L":
            data[i+"negrate"]=int(input(" { How many "+data["name"]+" is a "+i+" worth?\n| "))
        else:
            print(" { You typed an invalid option. You may try one more time.")
            inp = input(" { Is this worth more(type 'M') or less(type 'L') than "+i)
            if inp.upper() == "M":
                data[i+"posrate"]=int(input(" { How many "+i+" is a "+data["name"]+" worth?\n| "))
            elif inp.upper() == "L":
                data[i+"negrate"]=int(input(" { How many "+data["name"]+" is a "+i+" worth?\n| "))
            else:
                print(" { You typed an invalid option. You will need to edit this entry to add a value for this option.")

                
    saved.append(data["name"])
    savedfile=open("Currency\index.py","w")
    savedn=[]
    for i in saved:
        if i not in savedn:
            savedn.append(i)
    savednstr=str(savedn)
    savedfile.write(str("savedcurrencies="+savednstr))
    savedfile.close();newfile=open("Currency/"+str(data["name"])+".txt","w");newfile.write(str(data));newfile.close();print(" - Complete -")
    from bin.cmd.reconcile_currency import reconcile_currency;reconcile_currency(saved)
