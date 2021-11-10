# set operations
s = {5,6,8,11}

print(len(s)) #set length

s.pop() # removes any value randomly
print (s)

s.add(8) # add 8 to set
print (s)

s.remove(6) # removes 6 from set
print (s)

s.union({8, 11,55}) # print the unique number in both set
print (s)

s.intersection({8, 11,55})
print (s)
