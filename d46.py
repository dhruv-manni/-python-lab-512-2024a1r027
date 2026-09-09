for i in range(1,6):
    marks=int(input("enter marks:"))
    if marks<0 or marks>100:
        print("Invalid marks skipped:")
        continue
    print("valid marks:",marks)