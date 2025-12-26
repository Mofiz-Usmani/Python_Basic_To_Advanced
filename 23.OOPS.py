# =================
# OOPS in Python
# =================







#* Attributes and Methods:

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand      # attribute
#         self.color = color      # attribute

#     def start(self):            # method
#         print(self.brand, "is starting...")

#     def drive(self):            # method
#         print(self.brand, "is driving...")


# my_car = Car("BMW", "Black")    # object created
# my_car.drive()
# my_car.start()
# print(my_car.color)
# print(my_car.brand)





#* Constructor

class Student:
    def __init__(self, name, age):   # constructor
        self.name = name              # attribute
        self.age = age                # attribute

# creating object
s1 = Student("Ali", 18)   # constructor runs automatically




class Student:
    name = "Alex"

stu1 = Student()
print(stu1.name)


