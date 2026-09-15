#write a python program that asks the user to enter a username and password
# #  the user should get only 3 attempts if the correct credentia;s are entered display "login successfully" and stop 
# the loop if all attempts are used display "account locked"
correct_username=input("Enter Correct_Username:")
correct_password=input("Enter Correct_Password:")
attempts=3
while attempts>0:
    username=input("Enter Username:")
    password=input("Enter Password:")

    if username==correct_username and password==correct_password:
        print("Login Successful")
        break
    else:
        attempts=attempts-1
        print("Worng details.Attempts left:",attempts)

    if attempts==0:
        print("Account Locked")
#write a python program to input a number and check whether it is prime or not A number is prime f it ha no divisor other than 1 and itself
#3
#write a python program to input two numbers and find their gratest common divisor using a loop
#4
#Write a python program to check whether to check whether a number is perfect number a number is pergect if the sum of its proper divisor equal to no ist