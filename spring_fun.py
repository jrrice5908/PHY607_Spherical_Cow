import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

########### force vec ###########

def spring_force(v, pos, k):
	force = -1*k*pos
	return force 

########## pos vec update ############
def spring_update2(v, pos, step, k):
	y = np.add(pos, x*step)
	force = spring_force(v, y, k)
	v = np.add(v, force/ m * step)
	pos = np.add(pos, v*step)
	return v, pos

def spring_update(v, pos, force, step):
	pos = np.add(pos, v * step)
	v = np.add(v, force * step / m)
	
	return v, pos
	
########## Energies ###########

def spring_energy(v, pos):
	T = 0.5 * (v.dot(v)) * m
	V = 0.5 * k * pos.dot(pos)
	E = T+V
	return T,V, E

v = np.array([1,0])
pos = np.array([10, 0])
step = 0.001
m = 1000
k = 4
x = []
y = []
Ti = []
Vi = []
Ei = []
for i in range(1000000):
	force = spring_force(v, pos, k)
	kin, pot, energ = spring_energy(v, pos)
	v, pos = spring_update(v, pos, force, step)
	x.append(pos[0])
	y.append(pos[1])
	Ti.append(kin)
	Vi.append(pot)
	Ei.append(energ)
t = np.arange(len(x))*step
plt.plot(t,x)
plt.ylabel('x - m')
plt.xlabel('t - s')	
plt.savefig('spring_figures/spring_fig.png')	
plt.clf()
#plt.plot(t, Ti, label = "kinetic")
#plt.plot(t,Vi, label = 'potential')
plt.plot(t, Ei, label = 'Energy')
plt.legend()
plt.ylabel('Energy - J')
plt.xlabel('time - s')
plt.savefig('spring_figures/spring_fid2.png')
