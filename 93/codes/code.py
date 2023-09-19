from scipy.stats import binom
import numpy as np
# Parameters
n = 5
p_defective = 1/10  # Probability of drawing a defective pen
p_non_defective = 9/10  # Probability of drawing a non-defective pen

# Calculate P(X = 0) and P(X = 1)
prob_X_0 = binom.pmf(0, n, p_defective)
prob_X_1 = binom.pmf(1, n, p_defective)

# Calculate P(X <= 1)
prob_X_at_most_1 = prob_X_0 + prob_X_1

print(f"Probability that at most one pen is defective: {prob_X_at_most_1:.4f}")

