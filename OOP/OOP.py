# Object =  A "Bundle" of related attributes(variables) and methods(function)
#           Ex:- Phone, Cup, Book
#           If Phone is an object,
#           Attributes:- then with phone the attributes will be eg, what is the version_number = 13, manufacturer = google, or model_name = pixel
#           Methods:- What can you do with the phone?:- def AnswerCall(), def TurnOn(), def TurnOff()
#           You need a "class" to create many object

# class = (blueprint) used to design the structure and layout of an object

from car_class import Car
from Animal_class import Dog

# car1 is an INSTANCE (or instance object) of the Car class
# It's created from the Car blueprint with specific attributes
car1 = Car(
    "BMW i8",
    2014,
    "blue",
    True,
)
print(f"{car1.model} has {Car.wheeels} wheels")


# car1.Drive()
# car1.Park()
