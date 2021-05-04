def new_atk(atkdata,dmgtypearray,savedattacks):
    print(">>New Attack");atkdata["name"]=input(" { What would you like to call the attack?\n| ")
    atkdata["dice"]=int(input(" { What dice should the attack use for damage? (Use just the number, i.e. a d6 would be '6'. Don't use non-number symbols or this will break.)\n| "))
    atkdata["numdice"]=int(input(" { How many dice should the attack use for damage? (Number symbols only)\n| "))
    atkdata["weapon"]=input(" { What weapon is this attack tied to? (Use 'body' if it is something like teeth or claws)\n| ")
    dmgtype=int(input(" { What damage type should this attack use?\n 1 - Acid\n 2 - Bludgeoning\n 3 - Cold\n 4 - Fire\n 5 - Force\n 6 - Lightning\n 7 - Necrotic\n 8 - Piercing\n 9 - Poison\n 10 - Psychic\n 11 - Radiant\n 12 - Slashing\n 13 - Thunder\n (Use numbers only)\n| "))
    atkdata["dmgtype"]=dmgtypearray[dmgtype-1];atkdata["range"]=int(input(" { What range does this attack have? (Use numbers divisible by 5. Use 5 for a melee attack, even if the weapon used has reach.\n| "))
    if "Y" in input(" { Does this attack have any special effects? Y/N\n| ").upper():
                    specialdata = input(" { Select the details you want to add to this attack by typing their names. Separate each option with a comma if there are multiple.\n" +
                                        " - Ammunition\n - Finesse\n - Heavy\n - Light\n - Loading\n - Ranged\n - Reach\n - Special\n - Thrown\n - Twohanded\n - Versatile\n"+
                                        " - Improvised\n - Silvered\n - Other (Use for custom abilities)\n| ").upper()
                    atkdata['special']=False;atkdata['other']=False;atkdata['ammunition']=False
                    for x in specialatkarray:
                        if x.upper() in specialdata:
                            exec("atkdata['"+x.lower()+"']=True")
                    if atkdata["special"]:
                        if "Y" in input(" { Is the weapon a net?\n| "): atkdata["net"]=True
                        if "Y" in input(" { Is the weapon a lance?\n| "): atkdata["lance"]=True
                    if atkdata["other"]:
                        atkdata["other_info"]=input(" { What special abilities does this attack have?\n| ")
                    if atkdata["ammunition"]: atkdata["ammo_type"]=input(" { What item does this attack use as ammunition?\n| ")
    savedattacks.add(atkdata["name"]);savedattackfile=open("Attacks\index.txt","w");savedattackfile.write(str(savedattacks))
    savedattackfile.close();newatkfile=open("Attacks/"+str(atkdata["name"])+".txt","w");newatkfile.write(str(atkdata));newatkfile.close();print(" - Complete -")
    return atkdata

