import numpy as np
import matplotlib.pyplot as plt 

x=np.linspace(0, 2*np.pi, 100)
y=np.sin(x)

plt.figure()
plt.plot(x,y)
plt.ylim(-2,2)
plt.show()

