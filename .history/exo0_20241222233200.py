peopleNbr = int(input("how many people need a ride? "))
peopleInTaxi = int(input("how many people fit in one taxi? "))
taxis= peopleNbr // peopleInTaxi
if peopleNbr % peopleInTaxi != 0: taxis = taxis + 1
print("number of taxis needed is :" ,taxis )