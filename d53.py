#wap to input a decimal number and convert it into binary without using the built in bin dunction
n=int(input("enter a number:"))
binary=""
while n>0:
    rem=n%2
    binary=str(rem)+binary
    n=n//2
print("Binary number is:",binary)