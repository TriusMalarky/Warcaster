#runtime variables
running=True;dmgtypearray=["Acid","Bludgeoning","Cold","Fire","Force","Lightning","Necrotic","Piercing","Poison","Psychic","Radiant","Slashing","Thunder"]
specialatkarray=["Ammunition","Finesse","Heavy","Light","Loading","Ranged","Reach","Special","Thrown","Twohanded","Versatile","Improvised","Silvered","Other"]
specialoptionsarray=["Lance","Net"]
savedattackfile = open("Attacks\index.txt");exec("global savedattacks; savedattacks = "+savedattackfile.read());savedattackfile.close()
#command flags
newcmd="NEW";helpcmd="HELP";debugcmd="DEBUG";exitcmd="EXIT";commandcmd="COMMAND";allcmd="ALL";atkcmd="ATK"
cmdarray=[newcmd,atkcmd,helpcmd,debugcmd,exitcmd,commandcmd]
#initialize
dashln=30;print("-"*dashln+"| Warcaster |"+"-"*dashln)
while running:
    uinput=input("| ");uinput=uinput.upper()
    #Debug Functions
    if uinput[:5] == debugcmd:
        print("> Debug:")
        if uinput[6:] in commandcmd:
            print(" - Checking for Command Conflictions - ")
            for x in cmdarray:
                for n in cmdarray:
                    if x == n:continue
                    else:
                        if any(i in x for i in n):
                            print(str(x) + " shares a value with " + str(n))
            print(" - Complete -")
    #Help Functions
    elif uinput[:4] == helpcmd:
        print(">Help")
        if newcmd in uinput:
            print(" - Create a new entry. Entry types include:\n  -> Attack(use 'atk' in commands)\n  -> Enemy\n - Use 'help [entry type] for more information.")
        if atkcmd in uinput  or "ATTACK" in uinput:
            print(" - Attacks are abilities that deal damage, but are not magical. Most of them are attached to a weapon.")
        if debugcmd in uinput:
            print(" - Used to debug the program.")
    #new entry
    elif uinput[:1] in newcmd or uinput[:3] in newcmd:
        print(">New Entry")
        if atkcmd in uinput:
            print(">>New Attack");atkdata = {};atkdata["name"]=input(" { What would you like to call the attack?\n| ")
            new_atk=open("bin/cmdscr/new_atk.txt");exec(new_atk.read())
            if "Y" in input(" { Does this attack have any special effects? Y/N\n| ").upper():
                specialdata = input(" { Select the details you want to add to this attack by typing their names. Separate each option with a comma if there are multiple.\n" +
                                    " - Ammunition\n - Finesse\n - Heavy\n - Light\n - Loading\n - Ranged\n - Reach\n - Special\n - Thrown\n - Twohanded\n - Versatile\n"+
                                    " - Improvised\n - Silvered\n - Other (Use for custom abilities)\n| ").upper()
                atkdata['special']=False;atkdata['other']=False;atkdata['ammunition']=False
                for x in specialatkarray:
                    if x.upper() in specialdata:
                        exec("atkdata['"+x.lower()+"']=True")
                if atkdata["special"]:
                    if "Y" in input(" { Is the weapon a net?\n| "): atkdata["net"]=True
                    if "Y" in input(" { Is the weapon a lance?\n| "): atkdata["lance"]=True
                if atkdata["other"]:
                    atkdata["other_info"]=input(" { What special abilities does this attack have?\n| ")
                if atkdata["ammunition"]: atkdata["ammo_type"]=input(" { What item does this attack use as ammunition?\n| ")
            atk_save=open("bin/cmdscr/new_atk_save.txt");exec(atk_save.read())
