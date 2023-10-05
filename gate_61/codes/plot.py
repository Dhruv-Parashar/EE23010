import numpy as np
import matplotlib.pyplot as plt

# Define the range of alpha values
alpha_values = np.linspace(0.25, 0.99, 100)  # Avoid 0 and 1 for logarithmic calculations

# Initialize an array to store I(X, Y) values
mutual_info_values = []

# Calculate I(X, Y) for each alpha
for alpha in alpha_values:
    # Calculate I(X, Y) based on the given formula
    mutual_info = np.log(3) + alpha * np.log(alpha) + (1 - alpha) * np.log(1 - alpha)
    
    mutual_info_values.append(mutual_info)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(alpha_values, mutual_info_values, label='$I(X, Y)$')
plt.xlabel('$\\alpha$')
plt.ylabel('$I(X, Y)$')
plt.title('$I(X, Y)$ vs. $\\alpha$')
plt.grid(True)
plt.legend()
plt.savefig('/home/dhruv/EE23010/gate_61/figs/figure2')


