from car_02 import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


print("-----")
import car_02

my_beetle = car_02.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car_02.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())