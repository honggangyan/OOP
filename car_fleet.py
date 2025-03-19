from car import Car, ElectricCar

# make lists to hold the cars
gas_cars = []
electric_cars = []

# make 20 gas cars
for i in range(20):
    gas_car = Car("Toyota", 2020, "Red")
    gas_cars.append(gas_car)

# make 20 electric cars
for i in range(20):
    electric_car = ElectricCar("Tesla", 2022, "white")
    electric_cars.append(electric_car)

for car in gas_cars:
    gas_car.fill_tank()
    gas_car.drive()

for car in electric_cars:
    car.charge()
    car.drive()

# print the number of cars in the fleet
print(f"The fleet has {len(gas_cars)} gas cars and {len(electric_cars)} electric cars.")
