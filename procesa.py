import numpy as np
import matplotlib.pyplot as plt


datos=np.loadtxt("monthrg.dat")
years=datos[:, 0]
manchas=datos[:, 3]
mes=datos[:, 1]

ii=years>1900
matriz=np.array([years[ii], manchas[ii]])
np.savetxt("fechas_manchas.dat", matriz.T)


