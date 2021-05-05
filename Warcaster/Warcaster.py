from bin.lib.runtimevar import runtimevar;rtar=runtimevar();running=rtar["running"];dmgtypearray=rtar["dmgtypearray"];specialatkarray=rtar["specialatkarray"]
specialoptionsarray=rtar["specialoptionsarray"];savedattacks=rtar["savedattacks"]
#command flags
newcmd="NEW";helpcmd="HELP";debugcmd="DEBUG";exitcmd="EXIT";commandcmd="COMMAND";allcmd="ALL";atkcmd="ATK"
cmdarray=[newcmd,atkcmd,helpcmd,debugcmd,exitcmd,commandcmd]
#initialize
dashln=30;print("-"*dashln+"| Warcaster |"+"-"*dashln)
while running:
    uinput=input("| ");uinput=uinput.upper()
    #Debug Functions
    if uinput[:5] == debugcmd:
        from bin.lib.debugcmd import debugcmd;debugcmd(uinput,cmdarray,commandcmd)
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
            from bin.cmd.new_atk import new_atk;atkdata = {};atkdata=new_atk(atkdata,dmgtypearray,savedattacks)
