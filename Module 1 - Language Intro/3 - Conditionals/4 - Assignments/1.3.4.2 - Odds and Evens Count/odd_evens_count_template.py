# bring in randomness cause we need it in our lives
import random

### Begin Dr. Forsyth Code. Do Not Modify ###

# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# set the maximum length of the list
max_length = 100

# set the maximum upper bound for the list
upper_bound = 1000

# generate a random lists of integers
nums = generate_random_int_list(max_length, upper_bound)

# create two variables to hold the final answers
num_evens = 0
num_odds = 0

### YOUR CODE BEGINS HERE ###
print(nums)

def find_evenodd(list_name):
    evens = 0
    odds = 0

    element = list_name[0]

    for element in list_name:
        if element % 2 == 0:

            evens += 1

        else:
            odds += 1

    return evens, odds
    
num_evens, num_odds = find_evenodd(nums)

print(num_evens, num_odds)
    

