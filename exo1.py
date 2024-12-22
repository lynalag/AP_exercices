name = input("please enter your name: ")
if name== "VIP":
    print("enjoy your show for free")
else:
    tickets = int(input("how many tickets would you like to buy ? "))
    print("the total cost is ",tickets*15.50)