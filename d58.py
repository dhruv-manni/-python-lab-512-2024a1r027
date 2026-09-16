#write a python program to print a right angled triangle
#inverted right angled triangle
print("inverted right angle")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")

    print()
