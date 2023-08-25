import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Sample size
simlen = 10000

# Possible outcomes
k_values = np.arange(0, 5)
print(k_values)

# Generate X1 and X2 without explicit loops
y = np.random.randint(0, 2, size=(4, simlen))

# Calculate X without loops
X = np.sum(y, axis=0)

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)

# Simulated probability
psim = counts / simlen

X_axis = [4,1.5,-1,-3.5,-6]

#Theoretical Probability
Prob = [0.0625,0.25,0.375,0.25,0.0625]


# Plotting
plt.stem(X_axis, psim, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.stem(X_axis, Prob, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Analysis')
plt.xlabel('$k$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{X}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.grid()

# Save or display the plot
plt.savefig('/home/dhruv/EE23010/Assignment2/figs/figure1.png')
plt.show()

