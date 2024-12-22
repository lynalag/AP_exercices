amount = int(input("Enter the total amount : "))
items = int(input("Enter the number of items : "))
day = input("Enter the day : ")
discount = 0
if items>5 : discount = 5

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    discount = discount + 10
elif day in ["saturday", "sunday"]:
     discount = discount + 20
else:
    print("Invalid day of the week entered.")
    total = amount - amount*(discount/100)
print("total price after discount : ",total)