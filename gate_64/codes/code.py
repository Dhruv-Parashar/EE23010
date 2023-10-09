import numpy as np

# Define the population distribution function
def population_cdf(x, theta):
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return 1 - (1 - x)**theta
    else:
        return 1

# True parameter values
theta_null = 1  # under H0
theta_alt = 2   # under H1

# Number of simulations
num_simulations = 10000

# Initialize counters for alpha and beta
alpha_count = 0
beta_count = 0

# Perform simulations
for _ in range(num_simulations):
    # Generate a random sample of size 1 from the population under H1
    sample = np.random.uniform(0, 1)

    # Calculate the test statistic (x)
    x = sample

    # Perform hypothesis test
    if x < 0.5:
        # Reject H0 when x < 0.5
        alpha_count += 1
    elif x >= 0.5 and population_cdf(x, theta_alt) < 0.5:
        # Do not reject H0 when x >= 0.5 and F(x | θ=2) < 0.5
        beta_count += 1

# Calculate actual alpha and beta
alpha = alpha_count / num_simulations
beta = beta_count / num_simulations

# Calculate alpha + beta
alpha_plus_beta = alpha + beta

# Print results
print("Theoretical Alpha:", 0.5)
print("Theoretical Beta:", 0.75)
print("Simulated Alpha:", alpha)
print("Simulated Beta:", beta)
print("Simulated Alpha + Beta:", alpha_plus_beta)

