import numpy as np
import matplotlib.pyplot as plt

# Define the range of alpha values
alpha_values = np.linspace(0.25, 1, 100)

# Initialize an array to store capacity values
capacity_values = []

# Simulate the channel for each alpha value
for alpha in alpha_values:
    # Define the binary symmetric channel transition probabilities
    p = alpha  # Probability of flipping a bit
    
    # Simulate the channel and calculate the capacity
    capacity = 1 - (-p * np.log2(p) - (1 - p) * np.log2(1 - p))
    capacity_values.append(capacity)

# Find the alpha value that maximizes the capacity
optimal_alpha = alpha_values[np.argmax(capacity_values)]
max_capacity = max(capacity_values)


# Print the optimal alpha and maximum capacity
print(f"The optimal alpha for maximum capacity is {optimal_alpha:.2f}")
print(f"The maximum capacity is {max_capacity:.4f}")

