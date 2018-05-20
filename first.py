import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 500)
y = 5*np.exp(-0.1*x)*np.sin(x)

noise = np.random.randn(*y.shape)
yn = y + noise

plt.plot(x, y, x, yn)
plt.show()

