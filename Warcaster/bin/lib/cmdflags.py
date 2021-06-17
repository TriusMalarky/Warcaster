# Command Flag Lists. Please Organize in alphabetical order.
allflags=["a","all","al"]
attackflags=["atk","attack"]
currencyflags=["cur","curren","currency","curr"]
debugflags=["debug"]
deleteflags=["de","del","remove","rem","delete","remo","dele"]
editflags=["e","edit","ed","edi"]
exitflags=["x","exit","ex"]
helpflags=["h","help"]
itemflags=["i","item"]
listflags=["list","li","lis","l"]
newflags=["n","new"]
reconcileflags=["rec","recon","reconcile","reco"]
systemflags=["system","sys"]

# ALL flags.
flagslist=[allflags,attackflags,currencyflags,debugflags,deleteflags,editflags,exitflags,helpflags,itemflags,listflags,newflags,reconcileflags,systemflags]
flagnames=["all","attack","currency","debug","delete","edit","exit","help","item","list","new","reconcile","system"]

toplevelflags=[newflags,debugflags,exitflags,helpflags,reconcileflags,editflags,deleteflags] # All flags that trigger their own commands.
entrycommandflags=[newflags,reconcileflags,editflags,deleteflags] # All top level flags that deal with entries.
entrytypeflags=[currencyflags,systemflags,attackflags,itemflags] # All flags referring to entry types.


cmdflags={"list":flagslist,"names":flagnames}
