import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, num=1000)

y = np.sin(x) / np.cos(x) # f(x)=sen(x)/cos(x)

deriv_y = 1 / (np.cos(x)) ** 2 # f'(x)=1/cos²(x)

plt.grid()
plt.ylim(-10, 10)
plt.plot(x,y, 'r') # plot f(x)=sen(x)/cos(x)
plt.plot(x,deriv_y, 'b') # plot f'(x)=1/cos²(x)
plt.legend(['f(x)=sen(x)/cos(x)', "f'(x)=1/cos²(x)"])

plt.show()