def debugcmd(uinput,cmdarray,commandcmd):
    print("> Debug:")
    if commandcmd in uinput:
        print(" - Checking for Command Conflictions - ")
        for x in cmdarray:
            for n in cmdarray:
                if x == n:continue
                else:
                    if x in n:
                        print(str(x) + " shares a value with " + str(n))
        print(" - This debug function is deprecated. Please refer to the documentation by using 'help debug command'");print(" - Complete -")
        
