name = input("Enter name \n")
eng = int(input("Enter English marks \n"))
hin = int(input("Enter Hindi marks \n"))
mat = int(input("Enter Maths marks \n"))

# ENGLISH
if (eng >= 33) :
	print( name , "got" , eng  , "marks in English and he is passed")
else :
	print(name , "got" , eng  , "marks in English and he is failed")

# HINDI	
if (hin >= 33) :
	print( name , "got" , hin  , "marks in Hindi and he is passed")
else :
	print(name , "got" , hin  , "marks in Hindi and he is failed")
	
# MATHS
if (mat >= 33) :
	print( name , "got" , mat  , "marks in Maths and he is passed")
else :
	print(name , "got" , mat  , "marks in Maths and he is failed")
	
	
overall = (eng + hin + mat)/3
if (overall >= 40) :
	print(" overall" , name  , "is passed and his percentage is" , overall)
else :
	print(" overall" , name  , "is failed and his percentage is" , overall)
