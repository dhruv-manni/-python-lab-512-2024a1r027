#WAPP to input marks of 10 students .store only valid marks between o and 100 in a list skip invalid marks
# 2.Write a Python program to input marks of 10 students.Store only valid marks between 0 
# and 100 in a list.skip invalid marks. 
marks = []

for i in range(10):
    m = int(input("Enter marks: "))

    if m >= 0 and m <= 100:
        marks.append(m)

print("Valid marks:", marks)