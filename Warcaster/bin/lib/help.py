def help(cmdarray,uinput,newcmd,helpcmd,debugcmd,eitcmd,commandcmd,allcmd,atkcmd):
    print(">Help")
    if newcmd in uinput:
        print(" - Create a new entry or edit a previously created entry. Entry types include:\n  -> Attack(use 'atk' in commands)\n  -> Enemy\n - Use 'help [entry type]' or 'help new [entry type]' for more information.")
    elif atkcmd in uinput  or "ATTACK" in uinput:
        print(" - Attacks are abilities that deal damage, but are not magical. Most of them are attached to a weapon.")
    elif debugcmd in uinput:
        if commandcmd in uinput: print(" - Deprecated debug command. Compares different command flag lists. May be reinstated if complex command flags are reinstituted.")
        else:print(" - Used to debug the program.")
    elif allcmd in uinput:
        print(" - new <entrytype>")
    else:
        print(" - No option specified. Use 'help all' for a list of commands.")
