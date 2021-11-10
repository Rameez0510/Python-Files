h = {
    "ladka"   : "boy" , 
    "gaadi"   : "vehicle" , 
    "janwar"  : "animal", 
    "chappal" : "slipper" , 
    "sadak"   : "road"
}

print("Available words are: " , h.keys())
a = input("Enter hindi word \n")
print("The translation of this word iz : " , h.get(a))
