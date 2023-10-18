import numpy as np
import matplotlib.pyplot as plt

# Define the PDFs for X1, X2, and X
def fX1(x):
    return np.exp(-x) * (x >= 0)

def fX2(x):
    return 2 * np.exp(-2 * x) * (x >= 0)

def fX(x):
    return 2 * (np.exp(-x) - np.exp(-2 * x)) * (x >= 0)

# Define the range of x values
x = np.linspace(0, 5, 100)

# Calculate the PDF values for X1, X2, and X
pdf_x1 = [fX1(val) for val in x]
pdf_x2 = [fX2(val) for val in x]
pdf_x = [fX(val) for val in x]

# Plot the PDFs
plt.figure(figsize=(10, 5))
plt.plot(x, pdf_x1, label="f_X1(x)")
plt.plot(x, pdf_x2, label="f_X2(x)")
plt.plot(x, pdf_x, label="p_X(x)")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.title("Probability Density Functions (PDFs)")
plt.savefig('/home/dhruv/EE23010/gate_49/figs/figure3')

