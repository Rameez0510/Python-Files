def fun(rk): # def is used to define a function
    print("hello" , rk)
fun("rameez") #this will print hello rameez

def mysum (n1 , n2) : #we can put more than 1 value also
    return n1 + n2
s = mysum(3,55)
print(s)

def hello (name = "Stranger") :
    print('hello ' + name)
hello('rameez') # if name given then return with name
hello() # return the given value above if value not given here