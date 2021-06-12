import os
def runtimevar():
    runtimevarray={} # <- Local Dictionary to be passed to main
    runtimevarray["running"]=True # <- This is used as a toggle, the exit command will set it false which will end the script.

    # Damage Types. This will change soon as we want users to be able to define their own damage types.
    runtimevarray["dmgtypearray"]=["Acid","Bludgeoning","Cold","Fire","Force","Lightning","Necrotic","Piercing","Poison","Psychic","Radiant","Slashing","Thunder"]

    # Special aspects of attacks. This will also change soon so that users can define their own.
    runtimevarray["specialatkarray"]=["Ammunition","Finesse","Heavy","Light","Loading","Ranged","Reach","Special","Thrown","Twohanded","Versatile","Improvised","Silvered","Other"]

    # Special Options.
    runtimevarray["specialoptionsarray"]=["Lance","Net"]
    
    # Attacks.
    # The variables above will look more like this* once we rework them.
    savedattackfile = open("Attacks\\index.txt");exec("global savedattacks; savedattacks = "+savedattackfile.read());savedattackfile.close()
    runtimevarray["savedattacks"]=savedattacks;

    # Currencies.
    # *This looks different from the attacks because I couldn't get it to work for this for some reason. This is smoother though, so I'll be
    # switching the attacks over to this.
    from Currency.index import savedcurrencies
    runtimevarray["savedcurrencies"]=savedcurrencies

    
    return runtimevarray # <- Returns the above variables to main
