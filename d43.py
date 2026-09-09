#write a pyhton program to stimulate a digital lock system
#the lock should ask the user to enter a 4-digit pin if the entered PIN does not contain exactly 4 digits, the prograam should display an error mesage and ask again . if the entered pin is correct , the lock should open . otherwise , the program should ask the user to try again
correct_pin="2580"
while True:
    pin=input("enter 4 digit pin number:")
    if len(pin)!=4:
        print("PIN must be exactly 4 digits.")
        continue
    if pin ==correct_pin:
        print("Lock opened.")
        break
    else:
        print("Wrong pin . try again")
