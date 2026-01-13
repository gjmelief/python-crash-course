# Exercise 9-9 From 'Python Crash Course'
# 09-01-2026 G. Melief

# Exercise editing example electric_car.py from the book


class Car:
    """A simple attempt to represent a car."""


    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""


    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade battery size to 65 if it isn't already"""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Upgraded the battery to 65 kWh")
        else:
            print("The battery is already 65 kWh")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""


    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

# Make instance of ElectricCar. Upgrade battery size
ev1 = ElectricCar('Tesla', 'Model 3', 2021)
ev1.battery.get_range()
print("\nUpgrade the battery when size is smaller then 65 kWh")
ev1.battery.upgrade_battery()
ev1.battery.get_range()