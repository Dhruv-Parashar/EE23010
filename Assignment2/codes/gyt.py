import numpy as np
from scipy.stats import bernoulli

x1 = bernoulli.rvs(size=10000, p=0.5)
x2 = bernoulli.rvs(size=10000, p=0.5)
x3 = bernoulli.rvs(size=10000, p=0.5)
x4 = bernoulli.rvs(size=10000, p=0.5)

possible_values_of_h = np.arange(0, 5)
successful_outcomes = x1 + x2 + x3 + x4
counts = np.bincount(successful_outcomes, minlength=5)
total_money = possible_values_of_h * 1 + (possible_values_of_h - 4) * 1.5
probabilities = counts / 10000

print("Total Money:", *map(lambda x: f"{x:.2f}", total_money))
print("Probability:", *map(lambda x: f"{x:.4f}", probabilities))

			
	
