# sets

s = {1, 7,8,1,7}
print(s) # won't print repetitive values

a = {}
print(type(a)) # type will be dictionary not set

b = set()
print (type(b)) # type will be set

b.add(2) # will add value to set
b.add(4)

b.add((2, 4,6)) # tuples can be added in sets
print(b) 
