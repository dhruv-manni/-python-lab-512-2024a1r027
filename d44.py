# 3. Write a Python program to calculate the final bill amount after applying a
# discount.The program should take the total bill amount as input from the User
# Warning and apply the discount according to the following rules.After calculating
# the discount,the program should display the discount amount and the final bill
# amount payable by the customer.
# Bill Amount            Discount
# Above 5000             20 percent
# 3000 to 5000           10 percent
# Below 3000             No discount
bill=float(input("Enter total Bill amount:"))
if bill>5000:
    discount=bill*0.20
elif bill>=3000 and bill<=5000:
    discount=bill*0.10
else:
    discount=0
final_bill=bill-discount
print("Discount:",discount)
print("Final Bill:",final_bill)