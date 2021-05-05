def help(cmdarray,uinput,newcmd,helpcmd,debugcmd,eitcmd,commandcmd,allcmd,atkcmd):
    print(">Help")
    if newcmd in uinput:
        print(" - Create a new entry. Entry types include:\n  -> Attack(use 'atk' in commands)\n  -> Enemy\n - Use 'help [entry type] for more information.")
    if atkcmd in uinput  or "ATTACK" in uinput:
        print(" - Attacks are abilities that deal damage, but are not magical. Most of them are attached to a weapon.")
    if debugcmd in uinput:
        print(" - Used to debug the program.")
