import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(0, 10, 100)

# Calculate the corresponding y values for e^(-x)
y = np.exp(-x)

# Create the plot
plt.plot(x, y, label='e^(-x)')

# Shade the region under the graph
plt.fill_between(x, y, color='lightblue', alpha=0.5, label='Shaded Area')

# Add labels and a legend
plt.xlabel('x')
plt.ylabel('f_X1')
plt.legend()

# Show the plot
plt.grid()
plt.savefig('/home/dhruv/EE23010/gate_49/figs/figure1')

