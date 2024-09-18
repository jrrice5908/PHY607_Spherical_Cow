import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

########### force vec ###########

def spring_force(v, pos, k):
	force = -1*k*pos
	return force 

########## pos vec update ############
def spring_update3(v,pos,step,k):
	y = np.add(pos, v*step)
	force1 = spring_force(v, y, k)
	v1 = np.add(v, force1/ m * step)
	pos1 = np.add(pos, v1*step)

	force2 = spring_force(v, pos, k)
	pos2 = np.add(pos, v*step)
	v2 = np.add(v, force2 * step / m)

	v = np.add(v1, v2)/2
	pos = np.add(pos1, pos2)/2

	return v, pos
	
	

def spring_update2(v, pos, step, k):
	y = np.add(pos, v*step)
	force = spring_force(v, y, k)
	v = np.add(v, force/ m * step)
	pos = np.add(pos, v*step)
	return v, pos

def spring_update(v, pos, step, k):
	force = spring_force(v,pos,k)
	pos = np.add(pos, v * step)
	v = np.add(v, force * step / m)
	
	return v, pos

def spring_update4(v, pos, step, k):
	v1, pos1 = spring_update(v, pos, step, k)
	v2, pos2 = spring_update2(v, pos, step, k)
	v = np.add(v1,v2)/2
	pos = np.add(pos1, pos2)/2
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
	v, pos = spring_update4(v, pos, step, k)
	kin, pot, energ = spring_energy(v,pos)
	x.append(pos[0])
	y.append(pos[1])
	Ti.append(kin)
	Vi.append(pot)
	Ei.append(energ)
t = np.arange(len(x))*step
plt.plot(t,x)
plt.ylabel('x - m')
plt.xlabel('t - s')	
plt.savefig('spring_figures/spring_fig_implicit.png')	
plt.clf()
plt.plot(t, Ti, label = "kinetic")
plt.plot(t,Vi, label = 'potential')
plt.plot(t, Ei, label = 'Energy')
plt.legend()
plt.ylabel('Energy - J')
plt.xlabel('time - s')
plt.savefig('spring_figures/spring_fig2_implicit.png')
