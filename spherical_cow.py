
import math
import numpy as np
import matplotlib.pyplot as plt

#################################### global constants ####################################
gravf_strength = 9.81 # in m/s^2
mass = 1000
drag_const = 0.07 # for a spherical object

################################# user defined constants #################################
v0 = (10, 10)     # in (vx0, vy0), a touple
p0 = (0, 150)     # in (x0, y0)
v_list = []
p_list = []
PE_list = []
KE_list = []
TE_list = []

# num_of_timesteps = $3
size_of_timesteps = 0.05 # size of plot points, in seconds
 
##################################### helper functions ##########################################
def find_force(v_now, p_now):
    """
    Finding the force acted on the cow at any given velocity vector and xy position.
        v_now -- a touple that shows the current velocity in vx, vy
        p_now -- a touple that shows the current position in px, py
    """
    vx_now = v_now[0]
    vy_now = v_now[1]
    force_x = -drag_const * vx_now ** 2 * mass
    force_y = (-gravf_strength + drag_const * vy_now ** 2) * mass
    return force_x, force_y

def find_vp(v_now, p_now, small_time): # small_time should be size_of_timesteps
    """
    Finding the next instance of velocity and position based on the current set.
        v_now -- a touple that shows the current velocity in vx, vy
        p_now -- a touple that shows the current position in px, py
        small_time -- the time step size in unit of seconds of the next instance
    """
    force_x, force_y = find_force(v_now, p_now)
    ax = force_x / mass
    ay = force_y / mass

    vx_now, vy_now = v_now[0], v_now[1]
    vx_new = vx_now + ax * small_time
    vy_new = vy_now + ay * small_time
    v_new = (vx_new, vy_new)

    px_now, py_now = p_now[0], p_now[1]
    px_new = px_now + vx_now * small_time
    py_new = py_now + vy_now * small_time
    p_new = (px_new, py_new)
    
    return (v_new, p_new)


def find_energies(v_now, p_now):
    """
        Finding the kinetic and potential energy of any given velocity vector and xy coord.
        v_now -- a touple that shows the current velocity in vx, vy
        p_now -- a touple that shows the current position in px, py
    """
    height = p_now[1]
    PE = mass * gravf_strength * height

    vx_now, vy_now = v_now[0], v_now[1]
    # KE = 1/2 * mass * math.sqrt(vx_now ** 2 + vy_now ** 2) **2
    KE = 1/2 * mass * (vx_now ** 2 + vy_now ** 2)

    TE = PE + KE

    return (PE, KE, TE)


##################################### main method ##########################################

if __name__ == "__main__":
    '''
        Main Method
    '''
    v_list.append(v0)   # adding to the lists of touples for velocity
    p_list.append(p0)  # adding to the lists of touples for position
    v_current = v0
    p_current = p0
    PE, KE, TE = find_energies(v_current, p_current) # finding energy for now
    PE_list.append(PE) # append current energy to the energy list
    KE_list.append(KE)
    TE_list.append(TE)

    '''
    x_list2 = []
    y_list2 = []
    print(F"STARTING")
    time = np.arange(0,100,0.1)
    for i in time:
        if i == 0:
            print(f"time: {i}")
            v_cur, p_cur = find_vp(v_current, p_current, i)
            x_list2.append(p_cur[0])
            y_list2.append(p_cur[1])
            print(f"current vel: {v_cur}")
            print(f"current pos: {p_cur}")
        else:
            print(f"time: {i}")
            v_cur, p_cur = find_vp(v_cur, p_cur, i)
            x_list2.append(p_cur[0])
            y_list2.append(p_cur[1])
            print(f"current vel: {v_cur}") 
            print(f"current pos: {p_cur}")
        if p_cur[1]<0:
            break
    '''

    while (p_current[1] >= 0): # while the object has not hit the ground, or y is non-negative
        v_current, p_current = find_vp(v_current, p_current, size_of_timesteps)
        v_list.append(v_current)
        p_list.append(p_current)
        PE, KE, TE = find_energies(v_current, p_current) # finding energy for now
        PE_list.append(PE) # append current energy to the energy list
        KE_list.append(KE)
        TE_list.append(TE)
    

    x_list, y_list = zip(*p_list)
    # print(x_list)
    # print(y_list)

    plt.plot(x_list, y_list,
            color = '#fc5a50', # coral
            marker = "*",
            linestyle = "None",
            markersize = 10,
            label = "Position")
    plt.title('Spherical Cow - Position Trajectory')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()

    plot_destination = "cow_figures/cow_traj.png"
    plt.savefig(plot_destination)

    plt.clf()
    t = np.arange(len(p_list)) * size_of_timesteps

    plt.plot(t, PE_list, label = "Potential Energy")
    plt.plot(t, KE_list, label = "Kinetic Energy")
    plt.plot(t, TE_list, label = "Total Energy")

    plt.title('Spherical Cow - Energy')
    plt.xlabel('Time [s]')
    plt.ylabel('Energy [J]')
    plt.legend()

    plot_destination2 = "cow_figures/cow_energies.png"
    plt.savefig(plot_destination2) 

    '''
    plt.plot(x_list2, y_list2,
        color = '#fc5a50', # coral 
        marker = "d",
        linestyle = "None",
        markersize = 10,
        label = "Position")
    plt.title('Spherical Cow - Position Trajectory')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plot_destination = "cow_figures/cow_traj2.png"
    plt.savefig(plot_destination)
    '''
