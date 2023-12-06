# Create a base class Vehicle with attributes like make, model, and year,
# and then create subclasses for specific types of vehicles like Car, Motorcycle, and Truck.
# Add methods to calculate mileage or towing capacity based on the vehicle type.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.make} {self.model} {self.year}"

    def mileage(self, total_miles, total_fuel_consumed):
        return (f"{self.make} {self.model} {self.year} has a mileage of {total_miles / total_fuel_consumed} miles per "
                f"gallon.")

    def towing_capacity(self):
        pass


class Car(Vehicle):
    def towing_capacity(self):
        return f"The car {self.display_info()} doesn't have a towing capacity"


class Motorcycle(Vehicle):
    def towing_capacity(self):
        return f"The motorcycle {self.display_info()}  doesn't have a towing capacity"


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def mileage(self, total_miles, total_fuel_consumed):
        return (f"{self.make} {self.model} {self.year} has a mileage of {total_miles / total_fuel_consumed} miles per "
                f"gallon.")

    def towing_capacity_function(self):
        return f"The truck {self.display_info()}  has a towing capacity of {self.towing_capacity} pounds"


def main():
    car = Car("Tesla", "Model 3", 2023)
    motorcycle = Motorcycle("Kawasaki", "Ninja 650", 2023)
    truck = Truck("Jeep", "Gladiator", 2023, 10000)

    print(car.display_info())
    print(car.mileage(300, 10))
    print(car.towing_capacity())

    print(motorcycle.display_info())
    print(motorcycle.mileage(150, 5))
    print(motorcycle.towing_capacity())

    print(truck.display_info())
    print(truck.mileage(350, 17))
    print(truck.towing_capacity_function())


if __name__ == "__main__":
    main()
