import numpy as np
import matplotlib.pyplot as plt

# Define the CDF function for X
def CDF_X(x):
    return -2 * np.exp(-x) + np.exp(-2 * x) + 1

# Define the range of x values
x = np.linspace(0, 10, 100)

# Calculate the CDF values for X
cdf_x = [CDF_X(val) for val in x]

# Plot the CDF
plt.figure(figsize=(10, 5))
plt.plot(x, cdf_x)
plt.xlabel("x")
plt.ylabel("F_X(x)")
plt.legend()
plt.title("Cumulative Distribution Function (CDF) of X")
plt.grid(True)
plt.savefig('/home/dhruv/EE23010/gate_49/figs/figure4')

