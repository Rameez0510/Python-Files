num = int(input('Enter a number: \n'))
prime = False
for i in range(2 , num) :
    if i%num == 0 :
        prime = True
        break
if prime :
        print(num , " is a prime number")
else:
        print(num , " is not a prime number")