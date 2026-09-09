#4 #Write a python program to create a simple password validation system.
# the programmer should repeadedly ask the user to enter a password until a valid password is entered a password will be considered valid only if it ha sat leat 8 characters and contains the @symbol
while True:
    password = input("Enter password: ")

    if len(password) >= 8 and "@" in password:
        print("Valid password")
        break
    else:
        print("Invalid password. Try again.")