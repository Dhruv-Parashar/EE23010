import numpy as np

# Number of simulations
num_simulations = 1000000

# Initialize counters for events more than 1 unit for both storms
count_X1_more_than_1 = 0
count_X2_more_than_1 = 0

for _ in range(num_simulations):
    # Simulate X1 and X2 from their respective distributions
    x1 = np.random.exponential(scale=1)  # Exponential with parameter 1
    x2 = np.random.exponential(scale=0.5)  # Exponential with parameter 2

    # Check if X1 and X2 are both greater than 1
    if x1 > 1:
        count_X1_more_than_1 += 1
    if x2 > 1:
        count_X2_more_than_1 += 1

# Estimate the probabilities
probability_X1_more_than_1 = count_X1_more_than_1 / num_simulations
probability_X2_more_than_1 = count_X2_more_than_1 / num_simulations

# Probability of the union of events
probability_more_than_1 = probability_X1_more_than_1 + probability_X2_more_than_1

print(f"Probability of X1 > 1: {probability_X1_more_than_1:.2f}")
print(f"Probability of X2 > 1: {probability_X2_more_than_1:.2f}")
print(f"Probability of more than 1 unit of storm event: {probability_more_than_1:.2f}")

