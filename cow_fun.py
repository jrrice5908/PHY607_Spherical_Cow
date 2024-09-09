import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

########### force vec ###########

def cow_force(v, pos):
	grav  = np.array([0, m * (-9.8)])
	w_res = np.linalg.norm(v) * np.sqrt(v.dot(v))
	force = np.add(grav, w_res)
	return force 

########## pos vec update ############

def cow_update(v, pos, force, step):
	pos = np.add(pos, v)
	v = np.add(v, force * step / m)
	return v, pos
	
########## Energies ###########

def cow_energy(v, pos):
	T = 0.5 * np.sqrt(v.dot(v)) **2 * m
	V = m * 9.8 * pos[1]
	return T,V

v = np.array([50,50])
pos = np.array([0, 200])
step = 0.1
m = 1000

x = []
y = []
t = []
T = []
V = []
for i in range(50):
	if pos[1] <= 0:
		t.append(step*i)
		x.append(pos[0])
		y.append(pos[1])
		T.append(0)
		V.append(0)
	else:
		t.append(step*i)
		force = cow_force(v, pos)
		k, pot = cow_energy(v, pos)
		v, pos = cow_update(v, pos, force, step)
		x.append(pos[0])
		y.append(pos[1])
		T.append(k)
		V.append(pot)
plt.plot(x,y)	
plt.savefig('cow_fig.png')	
plt.clf()
plt.plot(t, T)
plt.plot(t,V)
plt.savefig('cow_fid2.png')
