import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt("fechas_manchas.dat")

x=datos[:, 0]
y=datos[:, 1]

plt.figure()
plt.plot(x, y)
plt.savefig("fechas_manchas.pdf")

