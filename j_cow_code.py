"""

"""

import math

###Defining Constants###
g = -9.81 #gravitational constant
k = -1 #wind resistance constant
m = 1000 #mass of cow
dt = 1 #arbitrary time step, in seconds

###Defining Initial Position Conditions###
x0 = 0 #init x position is at origin
y0 = h #init y position defined as some arbitrary height
t0 = 0 #init time set to 0

###Defining Initial Velocity Conditions###
vx0 = 3 #arbitrary
vy0 = 4 #arbitrary

###Defining vectors that describe initial conditions###
r0 = math.sqrt(((x0)^2)+((y0)^2))
v0 = math.sqrt(((vx0)^2)+((vy0)^2))

###Defining Functions###
xt = x0 + vx*t #x after dt
yt = y0 + vy*t #y after dt
j_
vxt = vx0 + xt/t
vyt = vy0 + yt/t


r = math.sqrt(((xt)^2)+((yt)^2))
v = math.sqrt(((vxt)^2)+((vyt)^2))

def total_force_vector(r,v):
    Fgrav = m*g
    Fdrag = k*(v^2)
    tot_F = Fgrav+Fdrag
    return tot_F

def v_and_r_after_small_time(r,v,tot_F,time_step)
    



# for tuesday, have basic script that can run indicated example, dont necesarily need to have questions answered

