# When to use class method and when to use static method?

class Car:
    # Class attribute
    car_count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.car_count += 1

    # Instance method
    def display_info(self):
        return f"This car is a {self.make} {self.model}."

    # Static method
    # Does not use self or cls. It is like a function outside.
    # Used for utility-like operations, independent of the class or instance.
    @staticmethod
    def is_valid_speed(speed):
        # Static method doesn't use self or cls
        return speed > 0

    # Class method
    # Uses cls to access the class attribute.
    # Useful for class-level operations like keeping track of total cars created.
    @classmethod
    def total_cars(cls):
        # Class method uses cls to access class-level data
        return f"Total cars created: {cls.car_count}"


# Creating car objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Instance method
print(car1.display_info())  # This car is a Toyota Corolla.
print(car2.display_info())  # This car is a Honda Civic.

# Static method
print(Car.is_valid_speed(60))  # True
print(Car.is_valid_speed(-5))  # False

# Class method
print(Car.total_cars())  # Total cars created: 2
