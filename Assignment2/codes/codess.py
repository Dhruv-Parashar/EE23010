import numpy as np
from scipy.stats import binom
num_tosses = 4
p_head = 0.5  
p_tail = 0.5  
win_amount = 1.0  
lose_amount = -1.5  
sample_space = [win_amount * num_heads + lose_amount * (num_tosses - num_heads)
                for num_heads in range(num_tosses + 1)]
probabilities = [binom.pmf(num_heads, num_tosses, p_head) for num_heads in range(num_tosses + 1)]
print("Amount of Money | Probability")
print("----------------|------------")
for amount, prob in zip(sample_space, probabilities):
    print(f"      {amount:.2f}     |   {prob:.4f}")

