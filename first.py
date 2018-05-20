import numpy as np
import matplotlib.pyplot as plt

Amp = 5
noData = 500
t0 = 0
t1 = 10
tau = -0.1

x = np.linspace(t0, t1, noData)
y = Amp*np.exp(tau*x)*np.sin(x)

noise = np.random.randn(*y.shape)
yn = y + noise

plt.plot(x, y, x, yn)
plt.show()

y1 = Amp/2*np.cos(2*x)
y1n = yn + y1

plt.plot(x, y1n)
plt.show()
