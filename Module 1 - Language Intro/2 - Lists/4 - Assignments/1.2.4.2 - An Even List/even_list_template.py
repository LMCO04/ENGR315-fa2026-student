import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""

# length = len(even_list) 
# lw_mid = (len(even_list) // 2) - 1
# up_mid = lw_mid + 1

# print(up_mid)
# print(lw_mid)

# m1 = even_list[lw_mid]
# m2 = even_list[up_mid]
# print(m1 , m2)

# middle_avg = float((m1 + m2) // 2)


# this is the final result. Modify this line, and the empty lines above, to solve the assignment
# middle average means the average between the two values in the middle of the list
middle_average = sum(even_list[(len(even_list)//2)-1 : (len(even_list)//2)+1]) / 2

# the average of middle elements is
print("The average is: ", middle_average)
