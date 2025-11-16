# =====================
# While Loop in Python
# =====================


# When to use while loop

# Use while loop when:
# ✔ You don’t know how many times the loop should run
# ✔ You want to repeat until a condition becomes False
# ✔ Taking continuous user input
# ✔ Waiting for something to happen

# No Do While Loop is in python




i = 1

while i <= 5:
    print(i)
    i = i + 1






# Ask user until they enter correct password
# password = ""

# while password != "abc@123":
#     password = input("Enter Password: ")

# print("Access Granted")







# Infinite Loop (runs forever)
# while True:
#     print("This never ends!")










# i = int(input("Enter the number: "))

# while (i<=10) :
#     i = int(input("Enter the number: "))
#     print(i)

# print("Done with the loop")






count = 5

while (count>=0) :
    print(count)
    count -= 1
else : 
    print("Out of Loop")








# Print numbers 1 to 5 (do-while style)
i = 1

while True:
    print(i)
    i += 1

    if i > 5:     # condition check at bottom
        break






# Do While Loop emulation
# i = int(input("Enter the number: "))
# print(i)    

# while (i<=10) :
#     i = int(input("Enter the number: "))
#     print(i)

# print("Done with the loop")








# =============================
# BREAK and CONTINUE in Python
# =============================


# Break = Stop the loop immediately
# When Python sees break, it jumps out of the loop (loop ends right there).


for i in range(1, 6):
    if i == 3:
        break
    print(i) # prints 1 2







# Example with While Loop
i = 1

while i <= 5:
    if i == 4:
        break
    print(i)   #prints 1 2 3
    i += 1
