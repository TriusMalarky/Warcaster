def reconcile_currency(saved):
    print(" - Reconciling Currencies - ")

    # Start Generate Reconciliation Dictionary
    currencies={} # <- Define Local Dictionary
    for i in saved: # <- Calls the main-list 'savedcurrencies'
        rfile=open("Currency/"+i+".txt","r+")
        exec("currencies['"+i+"']="+rfile.read())
    # End Generate Reconciliation Dictionary
    
    for i in currencies:
        entrypoplist = []
        for x in currencies[i]:
            if x==str(i+"posrate")or x==str(i+"negrate"):
                entrypoplist.append(x)
            if x[:-7] in currencies:
                # Compare pos-neg rates and confirm value if they are not congruent
                if 'negrate' in x and str(i+'posrate') in currencies[x[:-7]]:
                    if currencies[x[:-7]][str(i+'posrate')] == currencies[i][x]:
                        pass
                    else:
                        print(" { Values " +str(currencies[x[:-7]]['name'])+" ("+i+"posrate) and "+i+" ("+x+") do not match.")
                        newval=int(input(" { What value should they have?\n| "))
                        currencies[x[:-7]][str(i+'posrate')]=newval
                        currencies[i][x]=newval
                if 'posrate' in x and str(i+'negrate') in currencies[x[:-7]]:
                    if currencies[x[:-7]][str(i+'negrate')] == currencies[i][x]:
                        pass
                    else:
                        print(" { Values " +str(currencies[x[:-7]]['name'])+" ("+i+"negrate) and "+i+" ("+x+") do not match.")
                        newval=int(input(" { What value should they have?\n| "))
                        currencies[x[:-7]][str(i+'negrate')]=newval
                        currencies[i][x]=newval
        for k in currencies:
            if str(k+'negrate') not in currencies[i] and str(k+'posrate') not in currencies[i] and k not in i:
                inp = input(" { Are "+k+" worth more(type 'M') or less(type 'L') than "+i+"\n| )
                if inp.upper() == "M":
                    currencies[i][k+"posrate"]=int(input(" { How many "+i+" is a "+k+" worth?\n| "))
                elif inp.upper() == "L":
                    currencies[i][k+"negrate"]=int(input(" { How many "+k+" is a "+i+" worth?\n| "))
                    
        for n in entrypoplist:
            currencies[i].pop(n)
        newfile=open("Currency/"+str(i)+".txt","w");newfile.write(str(currencies[i]));newfile.close()
    print(" - Currencies Reconciled - ")
