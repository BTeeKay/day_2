# For the following list of numbers:

from unittest import skip


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even = []
for num in numbers:
    if (num % 2) == 0:
        even.append(num)

print(even)
# 2. Print the difference between the largest and smallest value:
high = 0
low = 9999
for n in numbers:
    if high < n:
        high = n
    if low > n:
        low = n
print(high - low)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
pointer = 0

for number in numbers:
    if number == pointer and number == 2:
        print("True")
    pointer = number

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
#    numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
total = 0
check = False
for n in numbers:
    if n == 6:
        check = True
    if check == False:
        total += n
    if n == 7:
        check = False

print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
#    numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
#    total = 1 + 6 + 2 + 2 + 7 + 1 + 6 + 7 = 32
pointer = 0
total = 0

for number in numbers:
    if number == 13 or pointer == 13:
        skip
    else:
        total += number
    pointer = number

print(total)







