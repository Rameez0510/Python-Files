n = int(input('Enter a number : \n'))
a = ' '
s = '*'
m = n
x = 1
for i in range(1 , n +1) :
    m -= 1
    b = a * m
    c = s * x
    print(str(b) + str(c))
    x += 2
