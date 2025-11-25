# ======================
# for loop with else
# ======================


#! Loop works from 0 to n-1

for i in range(5):
    print(i)

else:   # means loop ends not breaks
    print("Loop finished without break")








for i in range(6):
    print(i)

    if i == 4:
        break

else : 
    print("Loop Complete")














#? Find Missing Number in a Sequence
#? You have a list of numbers from 1 to n with one missing. Find the missing number-
#? using for-else.


numbers = [1, 2, 4, 5]
numbers.sort()  # ensure sorted
count = 1

for i in numbers:
    if i == count:
        count += 1

print("Missing number:", count)
