# Q. 2

letter = '''Dear <NAME> 
We are very happy to say that in international level coding competition 
You are selected! 
Date : <DATE> '''

NAME = input ("Enter your name : ")
DATE = input("Enter today's date : ")
letter = letter.replace ("<NAME>" , NAME)
letter = letter.replace ("<DATE>" , DATE)
print(letter)
