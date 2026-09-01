#write a python program to fill the given letter template with name and date

letter='''
Dear <Name>
You are selected!
<Date>
'''

name=input("Enter name:")
date=input("enter Date:")

letter=letter.replace("<Name>",name)
letter=letter.replace("<Date>",date)
print(letter)