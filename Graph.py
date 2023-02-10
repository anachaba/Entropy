import matplotlib.pyplot as plt
import numpy as np

#function to compute the entropy
def entropy(p):
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

p = np.linspace(0.001, 0.999, 1000)
h = entropy(p)

# ploting p on the x and h on the y
plt.plot(p, h)
plt.xlabel("p")
plt.ylabel("H(p)")
plt.title("Entropy H(p)")
plt.show()

