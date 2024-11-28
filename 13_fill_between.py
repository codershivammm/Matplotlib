import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(1, 6)
y1 = [3, 5, 7, 6, 8]
y2 = [2, 3, 4, 5, 6]

# Plot
plt.fill_between(x, y1, label='Series 1', alpha=0.5)
plt.fill_between(x, y2, label='Series 2', alpha=0.5)

# Add labels and legend
plt.title("Area Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
