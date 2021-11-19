n = int(input('Enter a number : \n'))
print('* ' * n)
for i in range(1 , n -1) :
    print('* ' + ('  ' * (n -2)) + '*')
if n == 1 :
    pass
else :
    print('* ' * n)