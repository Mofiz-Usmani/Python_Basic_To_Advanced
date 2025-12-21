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

i = int(input("Enter the number : "))

print(i)

while (i <= 10) :
    i = int(input("Enter the number : "))
    print(i)

print("Done with the loop")










# ===============
#? Questions
# ===============




#? Reverse a number

n = int(input("Enter a number: "))

rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reversed number:", rev)







#? Check if a number is palindrome

n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")





#? Find the factorial without using for loop

n = int(input("Enter the number = "))

fact = 1
count = 1

while(count <= n):
    fact = fact * count
    count += 1
    
print(fact)

# OR

n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial =", fact)






#? Print Fibonacci series up to n terms

#? Find the largest digit in a number

#? Check Armstrong number (e.g., 153 = 1³+5³+3³)

#? Sum of digits until single digit
#? Keep adding the digits of a number until only one digit remains.
#? Example:

#? Input: 9875  
#? 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2  
#? Output: 2

#? Count number of digits without using len()

#? Print reverse of a number without converting to string

#? Find the product of even digits only

#? Example:

#? Input: 2457  
#? Even digits = 2, 4 → Product = 8  
#? Output: 8


#? Check if a number is a strong number

#? A strong number is a number whose sum of the factorials of its digits equals the number itself.
#? Example:

#? 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145  
#? Output: Strong number



#? Ask the user for a string and check whether it is a palindrome or not.
#? A is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.



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







for i in range(1, 13) : 
    if i == 11:
        break
    print("5 X",i, "=", 5 * i)
    







n = 5
num = int(input("Guess the number btwn (1-10): "))

while True : 
    if n == num :
        print("Right Guess")
        break
    else:
        num = int(input("Wrong!!! Guess Again: "))

print("Game Finished")



# Continue = Skip that iteration & jump to next round of loop
# It does not stop the loop.
# It only skips the current step.




for i in range(1, 6):
    if i == 3:
        continue
    print(i)    #prints 1 2 4 5  Number 3 is skipped.







i = 0

while i < 5:
    i += 1
    
    if i == 2:
        continue
    print(i)    #prints 1 3 4 5







#? Q1: 
#? Design a program to continuously input a number from user & print if it is-
#? positive or negative until the user enters “Quit”.


#? Q2:
#? Using while, check whether a number is a palindrome.


#? Q3:
#? Write a program using while loop to count how many times a digit appears in a number.
#? Example: n = 122333, digit = 3 → output: 3


#? Q4:
#? Using while, check whether a number is an Armstrong number.


#? Q5:
#? Write a program using while loop to remove all zeroes from a number.
#? Example: 102030 → 123