#take a student full name and roll number generate email using first three letters of first name ,and last htree characters of roll nmbers
firstname=input("Enter:")
lastname=input("enter:")
rollno=input("enter:")
print(firstname[:3]+lastname[:3]+rollno[-3:])