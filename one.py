#OBJECT - A "bundle" of related attributes (variables) and methods (functions)
#         Example. A phone, cup , book are objects
#Object can represent real world entities or items.
# Attributes are what our objects have while methods are what our objects can do.

# A method is a function which belongs within an object.
# A phone has attributes for example , phone_number, phone price
#A phone can also have methods(function) for example, def make_call():
#                                                   , def receive_call:
#                                                   , def turn_on():
#                                                    , def turn_off():

#         You need a "class" to create many object
# class = (blueprint) used to design the structure and layout of an object.

#

#HOW TO CREATE AN OBJECT
#1 Create a class of our object (In this case a car object)
class Car:
    def __init__(self, model, year, color, for_sale):
        #To assign the above attributes
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("BMW", 2025, "black", False)
car2 = Car("Land rover", 2026, "black", True)
car3 = Car("NOAH", 2026, "white", False)
print(car1.model)
print(car1.year)
print(car2.model)
print(car2.year)
print(car3.model)
print(car3.year)
print(car1.color)
print(car2.color)
print(car3.color)
print(car1.for_sale)
print(car1)
print(car2)
print(car3)


#
# To construct a car object we need a special type of method called a constructor
# which works similarly to a function
#


#METHODS = Are actions that our objects can perform.




