import numpy as np

# Define the number of simulations
num_simulations = 100000

# Initialize variables to store simulation results
simulated_X = np.zeros(num_simulations)

# Perform simulations
for i in range(num_simulations):
    deck = np.array(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4)
    np.random.shuffle(deck)
    draws = deck[:2]
    num_aces = np.sum(draws == 'A')
    simulated_X[i] = num_aces

# Calculate mean and standard deviation
mean_X = np.mean(simulated_X)
variance_X = np.var(simulated_X)
std_deviation_X = np.sqrt(variance_X)

print(f"Mathematically calculated mean: {mean_X:.4f}")
print(f"Mathematically calculated standard deviation: {std_deviation_X:.4f}")

# Verify with simulation
simulated_mean_X = np.mean(simulated_X)
simulated_std_deviation_X = np.std(simulated_X)

print(f"Simulated mean: {simulated_mean_X:.4f}")
print(f"Simulated standard deviation: {simulated_std_deviation_X:.4f}")

