# =================
# OOPS in Python
# =================





# class Student:
#     subject = "Python"
#     college = "ABC"
#     year = "4th year"

# stu1 = Student()
# stu2 = Student()

# print(stu1.subject, stu1.college, stu1.year)
# print(stu2.subject, stu2.college, stu2.year)









class Car:
    def __init__(self, brand, color):
        self.brand = brand      # attribute
        self.color = color      # attribute

    def start(self):            # method
        print(self.brand, "is starting...")

    def drive(self):            # method
        print(self.brand, "is driving...")

my_car = Car("BMW", "Black")    # object created
my_car.drive()
my_car.start()
print(my_car.color)
print(my_car.brand)

