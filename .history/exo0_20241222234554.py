peopleNbr = int(input("How many people need a ride? "))
peopleInTaxi = int(input("How many people fit in one taxi? "))

taxis = peopleNbr / peopleInTaxi
if peopleNbr % peopleInTaxi != 0:
    taxis = taxis + 1

print("Number of taxis needed is:", taxis)
