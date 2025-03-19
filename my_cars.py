from car import Car, ElectricCar

my_VW = Car("VW", 2020, "blue")
my_Tesla = ElectricCar("Tesla", 2022, "red")

my_VW.fill_tank()
my_VW.drive()


my_Tesla.charge()
my_Tesla.drive()
