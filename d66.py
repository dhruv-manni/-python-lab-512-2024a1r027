#
number=[]
unique_numbers=[]
n=int(input("enter total numbers:"))
for i in range(n):
    num=int(input("enter number:"))
    number.append(num)

for num in number:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("original list:",number)
print("unique list:",unique_numbers)