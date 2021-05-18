import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def f(x,y):
    return (x**2)-(y**2)

res=100

x=np.linspace(-10,10,res)
y=np.linspace(-10,10,res)
x, y = np.meshgrid(x,y)

z=f(x,y)

fig, ax = plt.subplots(subplot_kw={'projection':'3d'})


surf=ax.plot_surface(x,y,z, cmap=cm.cool)
fig.colorbar(surf)

fig2, ax2 = plt.subplots()
level_map = np.linspace(np.min(z), np.max(z), res)

cp=ax2.contourf(x,y,z, levels=level_map, cmap=cm.cool)
fig2.colorbar(cp)

plt.show()