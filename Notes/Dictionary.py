# dictionary

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
print(a["city"]) # print the value of key "city"
print (a["list"]) # print the value of key "city" i.e. list

a["list"] = [3, 9,0,7] # change the list value
print(a["list"]) 
print (a["list"][3]) # print the value of key "list" 's at index 3

print(a["fruit"]) # print all the keys and values in fruit key
print (a["fruit"]["red"]) # print the value of the key red in the key fruit
