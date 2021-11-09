# STRING FUNCTIONS

# 1. len()function

aot = "attack on titan"
print ("length of aot iz " , len(aot))

# 2. string.endswith()

print ('''Does aot ends with "tan" :  ''' ,   aot.endswith("tan"))

# 3. string.count()

print ("Number of 'T' in Attack on Titan iz  " , aot.count("t"))

# 4. string.capitalize()

print("When the first word of attack on titan iz capital -> ", aot.capitalize())

# 5. string.find()

print(''' Location of "titan" -> ''' , aot.find("titan"))

# 6. string.replace("oldword" , "newword")

print (aot.replace("titan" , "Eren Yeager"))
