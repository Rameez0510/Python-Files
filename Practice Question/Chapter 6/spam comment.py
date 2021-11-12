comment = input("Enter your comment : \n")

if ("make a lot of money" in comment) :
    print(comment , ": This is a spam comment")
elif ("subscribe now" in comment) :
    print(comment , ": This is a spam comment")
elif ("click this" in comment) :
    print(comment , ": This is a spam comment")
else :
    print(comment , ": This isn't a spam comment")