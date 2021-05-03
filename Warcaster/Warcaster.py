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
            new_atk=open("bin/cmdscr/new_atk.txt");exec(new_atk.read())
