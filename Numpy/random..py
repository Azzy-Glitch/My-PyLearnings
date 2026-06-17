import numpy as np

rng = np.random.default_rng()  # create a random number generator
print(rng)  # Generator(PCG64) at 0x7F8B8C8B9A90

# generate random numbers
print(rng.random())  # a random float in the range [0.0, 1.0)
print(rng.random(5))  # an array of 5 random floats in the range [0.0, 1.0)
print(rng.random((2, 3)))  # a 2x3 array of random floats in the range [0.0, 1.0)
print(rng.random.uniform(1, 10))  # a random float in the range [1.0, 10.0)

# generate random integers
print(rng.integers(10))  # a random integer in the range [0, 10)
print(rng.integers(1, 10))  # a random integer in the range [1, 10)
print(rng.integers(1, 10, size=5))  # an array of 5 random integers in the range [1, 10)
print(rng.integers(1, 10, size=(2, 3)))  # a 2x3 array of random integers in the range [1, 10)

rng = np.random.default_rng(42)  # create a random number generator with a seed
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(rng.choice(fruits))  # randomly select a fruit from the list
print(rng.choice(fruits, size=3))  # randomly select 3 fruits from the list