import os # <- Import Operating System. I forgot what this was for, it might not be relevant anymore. Leave it in.
from bin.lib.entrylib import * # Import Entry Library Functions

# Import variables from the init
from bin.lib.init import init;save=init()

# Command Flags.
# These used to be lists in order to implement aliases for each command, but I had trouble implementing it so I put that to the side to work
# on more important functions. I'll revisit that functionality at a later date.
newcmd="NEW";helpcmd="HELP";debugcmd="DEBUG";exitcmd="EXIT";commandcmd="COMMAND";allcmd="ALL";atkcmd="ATK"
itemcmd="ITEM";curcmd="CURREN";reconcmd="RECON"
# An array containing all of the command flags. Was used in a debug function that I had implemented to run through all the command flag lists
# and detect conflicting flags. That function is still in the code, but isn't useful.
cmdarray=[newcmd,atkcmd,helpcmd,debugcmd,exitcmd,commandcmd,itemcmd,curcmd,reconcmd]


dashln=30*"-";print(dashln+"| Warcaster |"+dashln) # Prints the title banner at the beginning of the script.


while running: # <- The while running section makes sure the script runs until the user turns it off. I haven't actually implemented the exit command yet.

    
    uinput=input("| ");uinput=uinput.upper() # <- Takes the user's input when a function isn't running.
    
    # Debug Functions
    # These will largely be used by the devs to check if certain things are running correctly.
    # They will be included in the help command in case users need them.
    # See bin/lib/debugcmd.py
    if uinput[:5] == debugcmd:
        from bin.lib.debugcmd import debugcmd;debugcmd(uinput,cmdarray,commandcmd)
        
    # Help Functions
    # These should be written well so that users can understand them.
    # See bin/lib/help.py
    elif uinput[:4] == helpcmd:
        from bin.lib.help import help;help(cmdarray,uinput,newcmd,helpcmd,debugcmd,exitcmd,commandcmd,allcmd,atkcmd)
        
    # Create New Entry
    # Entries are any complex variable, such as attack, monster, or item, that will be called by the encounter runner.
    elif uinput[:1] in newcmd or uinput[:3] in newcmd:
        print(">New Entry")
        if atkcmd in uinput: # <- New Attack
            from bin.cmd.new_atk import new_atk;atkdata = {};atkdata=new_atk(atkdata,dmgtypearray,savedattacks)
        elif itemcmd in uinput: # <- New Item
            from bin.cmd.new_item import new_item;itemdata={};itemdata=new_item(itemdata)
        elif curcmd in uinput: # <- New Currency
            from bin.cmd.new_currency import new_currency;curdata={};curdata=new_currency(curdata,savedcurrencies)

    # Reconcile Entries
    # The 'New Entry' scripts will run the reconciliation commands automatically, but we'll give the user the ability
    # to manually reconcile in case they do something we don't expect.
    elif uinput[:5] in reconcmd:
        print(">Reconciling")
        if curcmd in uinput: # <- Reconcile Currencies
            from bin.cmd.reconcile_currency import reconcile_currency;reconcile_currency(savedcurrencies)
