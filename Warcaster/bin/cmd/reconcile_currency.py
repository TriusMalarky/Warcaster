def reconcile_currency(saved):
    print(" - Reconciling Currencies - ")
    currencies={}
    for i in saved: #Generate the dictionary needed for reconciliation
        rfile=open("Currency/"+i+".txt","r+")
        exec("currencies['"+i+"']="+rfile.read())
    for i in currencies:
        entrypoplist = []
        for x in currencies[i]:
            if x==str(i+"posrate")or x==str(i+"negrate"):
                entrypoplist.append(x)
            if x[:-7] in currencies:
                if 'negrate' in x and str(i+'posrate') in currencies[x[:-7]]:
                    if currencies[x[:-7]][str(i+'posrate')] == currencies[i][x]:
                        pass
                    else:
                        print(" { Values " +str(currencies[x[:-7]]['name'])+" ("+i+"posrate) and "+i+" ("+x+") do not match.")
                        newval=int(input(" { What value should they have?\n| "))
                        currencies[x[:-7]][str(i+'posrate')]=newval
                        currencies[i][x]=newval
                    
        for n in entrypoplist:
            currencies[i].pop(n)
                
    print(currencies)
