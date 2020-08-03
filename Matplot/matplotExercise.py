import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title('title')
ax.plot(x,y)

plt.show()