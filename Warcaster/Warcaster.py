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
        from bin.lib.help import help;help(cmdarray,uinput,newcmd,helpcmd,debugcmd,exitcmd,commandcmd,allcmd,atkcmd)
    #new entry
    elif uinput[:1] in newcmd or uinput[:3] in newcmd:
        print(">New Entry")
        if atkcmd in uinput:
            from bin.cmd.new_atk import new_atk;atkdata = {};atkdata=new_atk(atkdata,dmgtypearray,savedattacks)
