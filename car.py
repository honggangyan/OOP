class Car:
    """this is a class for car"""

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        # fual capacity in liters
        self.fuel_capacity = 50
        # fuel level in liters
        self.fuel_level = 0

    def get_description(self):
        """return a string description of the car"""
        print(f"The {self.model} is a {self.year} {self.color} car.")

    def fill_tank(self):
        """fill the tank to the max"""
        self.fuel_level = self.fuel_capacity
        print(f"The {self.model} is now filled to the top.")

    def drive(self):
        """drive the car"""
        print(f"The {self.model} is now driving.")

    def update_fuel_level(self, new_fuel_level):
        """update the fuel level"""
        if new_fuel_level > self.fuel_capacity:
            print(f"The {self.model} cannot hold that much fuel.")
        else:
            self.fuel_level = new_fuel_level
            print(f"The {self.model} now has {self.fuel_level} liters of fuel.")

    def add_fuel(self, amount):
        """add fuel to the tank"""
        if self.fuel_level + amount > self.fuel_capacity:
            print(f"The {self.model} cannot hold that much fuel.")
        else:
            self.fuel_level += amount
            print(f"The {self.model} now has {self.fuel_level} liters of fuel.")


# my_car = car("Toyota", 2020, "Red")

# print(my_car.get_description())
# print(my_car.fill_tank())
# print(my_car.drive())

# my_new_car = car("Ford", 2021, "Blue")
# my_new_car.fuel_level = 20
# print(my_new_car.update_fuel_level(my_new_car.fuel_level))
# print(my_new_car.add_fuel(10))


# Instances as attributes, for example a electric car has a battery, the battery can be a class.
class Battery:
    """this is a class for batteries"""

    def __init__(self, size=70):
        """initialize the battery size and charge level of 0%"""
        self.size = size
        self.charge_level = 0

    def get_range(self):
        """return the range of the battery"""
        if self.size == 70:
            return 240
        elif self.size == 90:
            return 300


# Electric Car inherit from object car
class ElectricCar(Car):
    """this is a class for electric cars"""

    def __init__(self, model, year, color):
        """initialize the electric car"""
        # call the parent class constructor, and inherit the attributes
        super().__init__(model, year, color)

        # add the electric car specific attributes
        # battery capacity in kWh
        # add the battery as an attribute
        self.battery = Battery()

    def charge(self):
        """charge the battery to the max"""
        self.battery_level = 100
        print(f"The {self.model} is now charged to {self.battery_level}%.")

    def fill_tank(self):
        """fill the tank"""
        print(f"The {self.model} does not have a tank.")


# my_ecar = ElectricCar("Tesla", 2022, "model 3")
# print(my_ecar.get_description())
# print(my_ecar.fill_tank())
# print(my_ecar.drive())
# print(my_ecar.charge())


# my_ecar = ElectricCar("Tesla", 2022, "model Y")
# print(my_ecar.get_description())
# print(my_ecar.battery.get_range())
