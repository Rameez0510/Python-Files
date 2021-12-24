import random
print('computer turn......')
c = random.randint(1,3)
if c == 1 :
    c = 's'
elif c == 2 :
    c = 'w'
elif c == 3 :
    c = 'g'

p = input('Select s,w,g for snake , water , gun respectively \n')
def game (c , p) :
    if c == p :
        return None
    # snake
    elif c == 's' :
        if p == 'w' :
            return False
        elif p == 'g' :
            return True
    # water
    elif c == 'w':
        if p == 'g':
            return False
        elif p == 's':
            return True
    # gun
    elif c == 'g':
        if p == 's':
            return False
        elif p == 'w':
            return True
print("Computer chosed \n", c)
print('you chosed \n' , p)
a = game(c,p)
if a == False :
    print('You losed :(')
elif a :
    print('You won ;)')
elif a == None :
    print('The match is a tie')
