marks = int(input("Enter the student's marks \n"))
if 90 < marks <= 100 :
    print("Your grade is EX")
elif 80 < marks <= 90 :
    print("Your grade is A")
elif 70 < marks <= 80 :
    print("Your grade is B")
elif 60 < marks <= 70 :
    print("Your grade is C")
elif 50 < marks <= 60 :
    print("Your grade is D")
elif marks <= 50 :
    print("Your grade is F")
else :
    print("Marks must be under 100")
