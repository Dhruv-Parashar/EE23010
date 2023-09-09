import numpy as np

# Define the random variable and corresponding probabilities
X = np.array([0, 500, 2000, 3000])
P_X = np.array([9995/10000, 3/10000, 1/10000, 1/10000])

# Calculate the expectation using vector multiplication
E_X = np.sum(X * P_X)

print(f"The expectation (E(X)) is approximately Rs. {E_X:.2f}")

