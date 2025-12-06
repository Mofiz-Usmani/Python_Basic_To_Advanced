# ================================
# Raising Custom Errors in Python 
# ================================

# In Python, sometimes you want to give your own error message instead of Python’s default message.
# For that, you define a custom exception class and then raise it.

# Why Use Custom Errors?

# ✔ Better understanding of what went wrong
# ✔ Makes big programs easier to debug
# ✔ Helps to enforce rules (e.g., age, number ranges)



age = int(input("Enter your age: "))

if age < 18:
    raise AgeError("You must be 18 or above!")
else:
    print("Access granted")









# Handling (Catching) Custom Errors with try-except

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Not eligible to vote!")
except AgeError as e:
    print("Custom Error:", e)










# Example with Two Custom Errors

class NegativeNumberError(Exception):
    pass

number = int(input("Enter a number: "))

if number < 0:
    raise NegativeNumberError("Negative numbers are not allowed")
elif number == 0:
    raise ValueError("Zero is not allowed (built-in error)")
else:
    print("Valid number:", number)
