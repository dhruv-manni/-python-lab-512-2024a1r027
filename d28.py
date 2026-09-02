# #write a python program to check email address ends with miet jmmu or not
# n=input("enter the email address:")
# print(n[10:])

n=input("enter the email address:")
index=n.find("@")
domain=n[index+1]
print("Domain:",domain)