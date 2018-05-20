import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y = np.exp(x)*np.sin(x)

plt.plot(x, y)
plt.show()

noise = np.random.randn(y.shape)
yn = y+noise


