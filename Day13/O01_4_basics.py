from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100) #which ensures reproducibility of random numbers
roll_a_die = np.random.randint(low=1, high=7,size=10)# simulates rolling a six-sided die
print("Roll a die: ", roll_a_die)
# The type of distribution for rolling a die is uniform discrete distribution

# roll 2 dice
dice_1 = np.random.randint(low=1, high=7, size=10)
dice_2 = np.random.randint(low=1, high=7, size=10)
print("Roll 2 dice: ", dice_1, dice_2)
totals = dice_1 + dice_2
print("Totals of 2 dice: ", totals)

# Sum       Number of ways

#  2              1
#  3              2
#  4              3
#  5              4
#  6              5
#  7              6
#  8              5
#  9              4
# 10              3
# 11              2
# 12              1

values = np.random.uniform(low=-10.0, high = 10.0, size=10)
print("Uniformly distributed values: ", values)

x = np.arange(-10.0, 10.0, 1)
y = np.random.normal(loc=0.0, scale=1.0, size=len(x))
print("y: ", y)