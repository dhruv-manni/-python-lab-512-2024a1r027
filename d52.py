#Write a program to input a number and reverse it using arithmetic operations only
n=int(input("enter a number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("Reverse number is:",reverse)