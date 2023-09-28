import numpy as np
from scipy.optimize import minimize_scalar

# Define the capacity function as a function of alpha
def capacity(alpha):
    if alpha < 0.25 or alpha > 1.0:
        return -np.inf  # Return negative infinity outside the valid range
    p = alpha  # Probability of error in the channel
    return 1 - (-p * np.log2(p) - (1 - p) * np.log2(1 - p))

# Use scipy's minimize_scalar to maximize the capacity
result = minimize_scalar(lambda alpha: -capacity(alpha), bounds=(0.25, 1.0), method='bounded')

# Get the value of alpha that maximizes the capacity
optimal_alpha = result.x
max_capacity = -result.fun  # Negate the result to get the maximum capacity

# Print the result
print(f"The value of alpha that maximizes the capacity is {optimal_alpha:.2f}")
print(f"The maximum capacity is {max_capacity:.4f} bits")

