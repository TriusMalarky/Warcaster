def runtimevar():
    runtimevarray={}
    runtimevarray["running"]=True
    runtimevarray["dmgtypearray"]=["Acid","Bludgeoning","Cold","Fire","Force","Lightning","Necrotic","Piercing","Poison","Psychic","Radiant","Slashing","Thunder"]
    runtimevarray["specialatkarray"]=["Ammunition","Finesse","Heavy","Light","Loading","Ranged","Reach","Special","Thrown","Twohanded","Versatile","Improvised","Silvered","Other"]
    runtimevarray["specialoptionsarray"]=["Lance","Net"]
    savedattackfile = open("Attacks\index.txt");exec("global savedattacks; savedattacks = "+savedattackfile.read());savedattackfile.close()
    runtimevarray["savedattacks"]=savedattacks
    return runtimevarray
