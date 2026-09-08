#take a password and check length,presence of @,whwther first and last characters are different
n=input("password:")

print("length at least 8:",len(n)>=8)
print("Contains @:","@" in n)
print("First  and last different:",n[0]!=n[-1])