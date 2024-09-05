
import math


#################################### global constants ####################################
gravf_strength = 9.81
mass = 1000
drag_const = 10 # can be anything

################################# user defined constants #################################
v0 = $1     # in (vx0, vy0), a touple
p0 = $2     # in (x0, y0)
v = []
p = []
v[0] = v0   # lists of touples
p[0] = p0   # lists of touples
num_of_timesteps = $3 # number of plot points, in time

if __name__ == "__main__":


### check if the initial values are valid
a = 1/2 * -gravf_strength
b = v[0][1]
c = p[0][1]
discriminant = b**2 - 4*a*c

if discriminant < 0:
    print('You have entered a set of non-realistic projectile motion parameters, please try again.')
else:
    ### solve for landing time using quadratic formula equation
    time_land = (-b + math.sqrt(discriminant)) / (2*a)
    size_of_timesteps = time_land / num_of_timesteps

    ##################################### functions ##########################################
    def find_force(v_now, p_now):
        """
        Finding the force acted on the cow at any given velocity vector and xy position.
            v_now -- a touple that shows the current velocity in vx, vy
            p_now -- a touple that shows the current position in px, py
        """
        force_x = drag_const * v_now[0] ** 2 * mass
        force_y = (-gravf_strength * drag_const * v_now[1] ** 2) * mass
        return (force_x, force_y)

    def find_vp(v_now, p_now, small_time): # small_time should be size_of_timesteps
        """
        Finding the next instance of velocity and position based on the current set.
            v_now -- a touple that shows the current velocity in vx, vy
            p_now -- a touple that shows the current position in px, py
            small_time -- the time step size in unit of seconds of the next instance
        """
        ax = find_force(v_now, p_now)[0] / mass
        ay = find_force(v_now, p_now)[1] / mass

        vx_new = v_now[0] + ax * small_time
        vy_new = v_now[1] + ay * small_time
        v_new = (vx_new, vy_new)

        px_new = p_now[0] + v_now[0] * small_time
        py_new = p_now[1] + v_now[1] * small_time
        p_new = (px_new, py_new)
        
        return (v_new, p_new)


    def find_energies(v_now, p_now):
        """
            Finding the kinetic and potential energy of any given velocity vector and xy coord.
            v_now -- a touple that shows the current velocity in vx, vy
            p_now -- a touple that shows the current position in px, py
        """
        PE = mass * gravf_strength * v_now[1]
        KE = 1/2 * mass * math.sqrt(v_now[0] ** 2 + v_now[1] ** 2)
        return (PE, KE, PE + KE)
    

