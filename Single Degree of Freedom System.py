# Virbrations of Single Degree of Freedom Systems (SDOF)
# Chris Dillow
# April 14, 2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import sin, cos, pi

def SDOF(X,t): # call this function for integration
    m = 100 # mass (kg)
    c = 5 # dampening
    k = 50 # stiffness (always higher than dampening)
    F0 = 100 # force amplitude (Newtons)
    w = 5 # frequency (omega)
    u = X[0]
    v = X[1]

    dudt = v # derivative du / dt = matrix 'v'
    dvdt = ((F0 * np.sin(w*t))/m) - (c*v/m) - (k*u/m)

    return dudt, dvdt


time = np.linspace(0,15,500)

# ----- Initial Conditions ----- #
X0 = [0,3] #1st Position: Initial Displacement; 2nd Position: Initial Velocity
solution = odeint(SDOF,X0,time) # Integrate the function SDOF with the initial conditions of X0 with respect to time

displacement = solution[:,0] #All rows, only first column
velocity = solution[:,1] #All rows and only the last column

# ----- Configure Plots ----- #
plt.figure(figsize=(8,5))
plt.plot(time,displacement,label="Displacement vs. Time",color='black')
plt.plot(time,velocity,label="Velocity vs. Time",color='red')
plt.legend()
plt.xlim(time[0],time[-1])
plt.show()