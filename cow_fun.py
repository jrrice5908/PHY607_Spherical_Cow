import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

########### force vec ###########

def cow_force(v, pos):
	grav  = np.array([0, m * (-9.8)])
	w_res = -1 * np.linalg.norm(v) * np.sqrt(v.dot(v))**2
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
	return T,V

v = np.array([5,5])
pos = np.array([0, 20])
step = 0.1
m = 1000

x = []
y = []
T = []
V = []
while (pos[1] >= 0):
	force = cow_force(v, pos)
	k, pot = cow_energy(v, pos)
	v, pos = cow_update(v, pos, force, step)
	x.append(pos[0])
	y.append(pos[1])
	T.append(k)
	V.append(pot)
t = np.arange(len(x))*step
plt.plot(x,y)
plt.ylabel('y - m')
plt.xlabel('x - m')	
plt.savefig('cow_figures/cow_fig.png')	
plt.clf()
plt.plot(t, T, label = "kinetic")
plt.plot(t,V, label = 'potential')
plt.legend()
plt.ylabel('Energy - J')
plt.xlabel('time - s')
plt.savefig('cow_figures/cow_fid2.png')
