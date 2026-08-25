#write a pyhton program to take minutes as input and convert it into hours and remaining minuter
#eg=135minutes=2hours and 15 minutes
tm=int(input("Enter total minutes:"))
s=tm//60
m=tm%60
print(s,"hours and",m,"minutes")