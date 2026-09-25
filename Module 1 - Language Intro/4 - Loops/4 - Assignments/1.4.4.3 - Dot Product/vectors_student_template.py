import random
import numpy as np


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)

    # return the generated list
    return randoms


"""
Step 1: Generate two "vectors" of equal length but full of random values
"""
max_length = 10
maximum_value = 100
fixed_length = int(random.uniform(2, max_length))
vector_a = generate_random_int_list(fixed_length, maximum_value)
vector_b = generate_random_int_list(fixed_length, maximum_value)
print(vector_a) # Checking vector values
print(vector_b)

"""
Step 2: Iterate through the vector(s) and calculate the dot product
"""

def vector_dot(v1,v2): # Creating a function to get dot product

    product = np.dot(v1,v2) # Calculating the dot product between two vectors

    return product

solution = vector_dot(vector_a , vector_b) # Using the created function on the vectors

# store your result here. Do not change the name
dot_product = solution

### Your code here



"""
Step 3: Calculate the error of your dot_product compared with numpy's solution
"""
# check code with numpy...
a_np = np.asarray(vector_a)
b_np = np.asarray(vector_b)

# use dot product from numpy to check this result
correct = np.dot(a_np, b_np) 
error = correct - dot_product

# compare results
print("Your result: ", dot_product)
print("Correct result: ", correct)
print("Error: ", error)
