import math

################################# Functions ################################# 

def total_force_vector(r,v):
    Fgrav = [0,-g]
    Fdrag = [-k*(v[0]), -k*(v[1])]
    tot_F = [Fgrav[0]+Fdrag[0],Fgrav[1]+Fdrag[1]]
    return tot_F

def r_and_v_after_dt(r,v,tot_F, dt):
    ax = tot_F[0]/m
    ay = tot_F[1]/m

    vxnew = v[0] + ax*dt
    vynew = v[1] + ay*dt
    vnew = [vxnew, vynew]

    xnew = r[0] + v[0]*dt + (1/2)*ax*(dt^2)
    ynew = r[1] + v[1]*dt + (1/2)*ay*(dt^2)
    rnew = [xnew, ynew]
    
    return [rnew, vnew]

def energies(r,v):
    T = (1/2)*m*((v[0])^2+ (v[1])^2)
    V = m*g*r[1]

    return [T,V]

################################# Constants and initial input #################################

g = -9.81   #gravitational constant
k = -1      #wind resistance constant
m = 1000    #mass of cow
dt = 1      #arbitrary time step, in seconds

r = [0,20]       #arbitrary initial coords 
#   [0],[1]
v = [3,4]     #arbitrary initial vel

################################# Main #################################

rlist = []
vlist = []
flist = []

while r[1] >= 0:

    fcurrent = total_force_vector(r,v)
    flist.append(fcurrent)

    rcurrent = r_and_v_after_dt(r,v,fcurrent,dt)[0]
    rlist.append(rcurrent)

    vcurrent = r_and_v_after_dt(r,v,fcurrent,dt)[1]
    vlist.append(vcurrent)

    dt = dt + 1

    r[0] = r[0] + rcurrent[0]
    r[1] = r[1] + rcurrent[1]

    v[0] = v[0] + vcurrent[0]
    v[1] = v[1] + vcurrent[1]


print(rlist)
print(vlist)





