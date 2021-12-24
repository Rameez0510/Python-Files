import random

def winner (c ,p):
    if c == p :
       return None
    elif c == 's' :
        if p == 'p' :
           return True
        elif p == 'x' :
            return False
    elif c == 'p' :
        if p == 's' :
            return False
        elif p == 'x' :
            return True
    elif c == "x" :
        if p == "s" :
           return True
        elif p == 'p' :
           return False

rounds = int(input('How much rounds you wanna play \n'))
cs = 0
ps = 0
p = ('Chose s for stone / p for paper / x for scizzor \n')
c = random.randint(1,3)
if c == 1 :
    c = "s"
elif c == 2 :
    c = 'p'
elif c == 3:
    c = 'x'

# a = winner(c,p)
# print('You choosed : ', p)
# print('Computer choosed :' , c)
# if a == None :
#     print('The match iz a tie :|')
# elif a == True :
#     print("You won the match :)")
# elif a == False :
#     print('You loosed the match :(')
#
for i in range(1 , rounds + 1) :

    print('ROUND : ' , i)
    p = input('Chose s for stone / p for paper / x for scizzor \n')
    c = random.randint(1, 3)
    if c == 1:
        c = "s"
    elif c == 2:
        c = 'p'
    elif c == 3:
        c = 'x'
    a = winner(c,p)
    print('You choosed : ', p)
    print('Computer choosed : ', c)
    if a == None:
        print('The round was a tie :|')
    elif a == True:
        print("You won this round :)")
        ps += 1
    elif a == False:
        print('You loosed this round :(')
        cs += 1
    print('*' * 105)
print('Your score iz : ' , str(ps))
print("Computer Score iz : " , str(cs))
if cs > ps :
    print('You losed the match')
elif cs < ps :
    print('You won the match')
elif cs == ps :
    print('The match was a tie')