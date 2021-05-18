import os
from bin.lib.runtimevar import runtimevar;rtar=runtimevar();running=rtar["running"];dmgtypearray=rtar["dmgtypearray"];specialatkarray=rtar["specialatkarray"]
specialoptionsarray=rtar["specialoptionsarray"];savedattacks=rtar["savedattacks"];savedcurrencies=rtar["savedcurrencies"]
#command flags
newcmd="NEW";helpcmd="HELP";debugcmd="DEBUG";exitcmd="EXIT";commandcmd="COMMAND";allcmd="ALL";atkcmd="ATK"
itemcmd="ITEM";curcmd="CURREN"
cmdarray=[newcmd,atkcmd,helpcmd,debugcmd,exitcmd,commandcmd,itemcmd,curcmd]
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
        elif itemcmd in uinput:
            from bin.cmd.new_item import new_item;itemdata={};itemdata=new_item(itemdata)
        elif curcmd in uinput:
            from bin.cmd.new_currency import new_currency;curdata={};curdata=new_currency(curdata,savedcurrencies)
