cities = {}

while True:
    city = input("Enter a city: ")
    if city == "stop": break
    population = len(city)*1000000
    cities[city] = population

sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)
for city, population in sorted_cities:
    print("city :", city, "population:", population