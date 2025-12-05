# =====================
# Functions in Python
# =====================


# A function is a block of code that:
# ✔ has a name
# ✔ runs only when you call it
# ✔ helps avoid repeating code



# Simple function
def greet():
    print("Hello!")

greet()





# Function with Parameters
# Parameters = input values.

def add(a, b):
    print(a + b)


add(5, 3)




# a and b are required arguments
def average(a, b):   
    print("The average is : ", (a+b)/2)

average(4,9)


# Default Arguments
def average(a=3, b=8):   
    print("The average is : ", (a+b)/2)

average()   # if give values while calling it overrites the defult values





# Keyword Arguments in Python
# When you call a function, you normally pass values in order:

def greet(name, age):
    print(name, age)

greet("Eddie", 20)   # normal way



# But keyword arguments let you specify the parameter by name, not by order:
greet(age=20, name="Eddie")

# Why keyword arguments are useful?

# Order doesn’t matter
# You can pass values in any order.

# More readable
# You can clearly see what each value is for.

# Example:
def user_info(name, city, age):
    print("Name:", name)
    print("City:", city)
    print("Age:", age)

user_info(age=21, name="Aman", city="Delhi")







# Variable Length Arguments in Python

# Sometimes you don’t know how many values a user will pass to a function.

# Python allows this using:

# 1️⃣ *args → for unlimited positional arguments 
# 2️⃣ **kwargs → for unlimited keyword arguments


# 1. *args (many values → tuple)  (📌 * → gives you a tuple)
# Use when you want to pass any number of values.

def add_numbers(*args):
    print(args)

add_numbers(10, 20, 30, 40)   #Output: (10, 20, 30, 40)




# You can loop:
def total(*args):
    sum = 0
    for i in args:
        sum += i
    print("Total: ", sum)

total(5,10, 20, 40, 30, 50)






# 2. **kwargs (many keyword arguments → dictionary) (📌 ** → gives you a dictionary)
# Use when you want many key=value pairs.

def user(**kwargs):
    print(kwargs)

user(name="Aman", age=21, city="Mumbai")




# Function with Return Value
# return sends back a result.

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)
# or
# print(multiply(4,5))









# Default Parameters
# If user doesn’t give value, default is used.

def greet(name="User"):
    print("Hello", name)

greet()         # uses default "User"
greet("Eddie")  # uses provided value












# Function with Multiple Returns
def calc(a, b):
    return a+b, a-b, a*b

x, y, z = calc(10, 5)

print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)







def is_palindrome():
    s = input("Enter a string: ")
    temp = ""
    for i in range(len(s)-1, -1, -1):
        temp += s[i]
    if temp == s:
        print("Palindrome")
    else:
        print("Not Palindrome")

is_palindrome()





# ===============================
# BUILT-IN FUNCTIONS IN PYTHON
# ===============================

# These are functions that Python already provides.
# You don’t need to create them — just use them directly.

# Examples:
# print(), len(), type(), range(), input(), etc.












# ===============
# Questions
# ===============



#? Fibonacci Using Recursion
#? Write a recursive function fibonacci(n) that returns the nth Fibonacci number.

#? Armstrong Number in Range
#? Write a function find_armstrong_numbers(start, end) that finds all Armstrong
#? numbers between two given numbers.


#? Longest Word in a Sentence
#? Write a function longest_word(sentence) that returns the longest word in a given string.