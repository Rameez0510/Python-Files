# dictionary methods

a = {
    "city"    : "Bhopal" , 
    "country" : "India" , 
    "states"  : "29" , 
    "list"    : [2, 7,8,9] , 
    "fruit"   : {
        "yellow" : "banana" , 
        "red"    : "Apple"
    }
}

print(a.items()) # print everything in dic a in tuple form
print(a.keys()) # return list of keys

a.update({ "food" : "daal chawal"})
print(a) # adds the key with value

print(a.get("list")) # print the value of key
print (a.get("bam")) # if value not available returns none instead of error
