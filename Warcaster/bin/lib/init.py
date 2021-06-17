import os
def init():
    save={} # <- Local Dictionary to be passed to main
    save["running"]=True # <- This is used as a toggle, the exit command will set it false which will end the script.

    # Damage Types. This will change soon as we want users to be able to define their own damage types.
    save["dmgtypearray"]=["Acid","Bludgeoning","Cold","Fire","Force","Lightning","Necrotic","Piercing","Poison","Psychic","Radiant","Slashing","Thunder"]

    # Special aspects of attacks. This will also change soon so that users can define their own.
    save["specialatkarray"]=["Ammunition","Finesse","Heavy","Light","Loading","Ranged","Reach","Special","Thrown","Twohanded","Versatile","Improvised","Silvered","Other"]

    # Special Options.
    save["specialoptionsarray"]=["Lance","Net"]
    
    from Attacks.index import savedattacks;save["attacks"]=savedattacks
    
    from Currency.index import savedcurrencies;save["currencies"]=savedcurrencies
    
    from Systems import savedsystems;save["systems"]=savedsystems

    from bin.lib.cmdflags import cmdflags;save["flags"]=cmdflags
    
    return save # <- Returns the above variables to main
