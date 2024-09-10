import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

########### force vec ###########

def cow_force(v, pos, k):
	grav  = np.array([0, m * (-9.8)])
	w_res = (-1) *k * v/np.linalg.norm(v) * (v.dot(v))
	force = np.add(grav, w_res)
	return force 

########## pos vec update ############

def cow_update(v, pos, force, step):
	pos = np.add(pos, v * step)
	v = np.add(v, force * step / m)
	return v, pos
	
########## Energies ###########

def cow_energy(v, pos):
	T = 0.5 * np.sqrt(v.dot(v)) **2 * m
	V = m * 9.8 * pos[1]
	E = T+V
	return T,V, E

v = np.array([1,100])
pos = np.array([0, 1000])
step = 0.001
m = 1000
k = 4
x = []
y = []
Ti = []
Vi = []
Ei = []
while (pos[1] >= 0):
	force = cow_force(v, pos, k)
	kin, pot, energ = cow_energy(v, pos)
	v, pos = cow_update(v, pos, force, step)
	x.append(pos[0])
	y.append(pos[1])
	Ti.append(kin)
	Vi.append(pot)
	Ei.append(energ)
t = np.arange(len(x))*step
plt.plot(x,y)
plt.ylabel('y - m')
plt.xlabel('x - m')	
plt.savefig('cow_figures/cow_fig.png')	
plt.clf()
plt.plot(t, Ti, label = "kinetic")
plt.plot(t,Vi, label = 'potential')
plt.plot(t, Ei, label = 'Energy')
plt.legend()
plt.ylabel('Energy - J')
plt.xlabel('time - s')
plt.savefig('cow_figures/cow_fid2.png')
