class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it")

    def update_odometer(self, mileage):
        # self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print(f"You can alter the odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def decrement_odometer(self, miles):
        self.odometer_reading -= miles


my_new_car = Car('Audi', 'A94', 2023)
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(32)
my_new_car.read_odometer()


myUsed_car = Car('Benz', 'Maybach', 2015)
print(myUsed_car.get_descriptive_name())

myUsed_car.update_odometer(23500)
myUsed_car.read_odometer()
myUsed_car.increment_odometer(100)
myUsed_car.read_odometer()
myUsed_car.decrement_odometer(3650)
myUsed_car.read_odometer()
