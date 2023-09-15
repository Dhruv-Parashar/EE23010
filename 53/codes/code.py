import random
import numpy as np

# Number of simulations
num_simulations = 100000

# Initialize an array to store the number of aces for each simulation
ace_counts = np.zeros(num_simulations)

# Simulate the scenario
for i in range(num_simulations):
    # Create a deck of cards with 4 aces and 48 non-aces (total 52 cards)
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    
    # Draw two cards without replacement
    cards_drawn = random.sample(deck, 2)
    
    # Count the number of aces in the drawn cards
    ace_count = cards_drawn.count('A')
    
    # Store the ace count in the array
    ace_counts[i] = ace_count

# Calculate the simulated mean and standard deviation
simulated_mean = np.mean(ace_counts)
simulated_std_dev = np.std(ace_counts)

# Theoretical mean and standard deviation (calculated previously)
theoretical_mean = 0.1538
theoretical_std_dev = 0.373

# Print the results
print("Simulated Mean:", simulated_mean)
print("Theoretical Mean:", theoretical_mean)
print("Simulated Standard Deviation:", simulated_std_dev)
print("Theoretical Standard Deviation:", theoretical_std_dev)

