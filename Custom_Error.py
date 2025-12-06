# ================================
# Raising Custom Errors in Python 
# ================================

# In Python, sometimes you want to give your own error message instead of Python’s default message.
# For that, you define a custom exception class and then raise it.



age = int(input("Enter your age: "))

if age < 18:
    raise AgeError("You must be 18 or above!")
else:
    print("Access granted")