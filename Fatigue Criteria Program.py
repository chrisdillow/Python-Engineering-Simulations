# Fatigue Criteria Program
# Chris D. | 4/9/2025

import numpy as np
import matplotlib.pyplot as plt

#X-axis will represent mean stress, sigma-m
#Y-axis will represent stress amplitude, sigma-a
#The three criteria are the Soderberg Line, the Gerber Line, and the Goodman Line

# ----- Inputs ----- #
stress_mean = 200
stress_amplitude = 300 #S_a

ultimate_strength = 450 # S_ut of material
yield_strength = 300 # S_yt of material
endurance_limit = 225 # S_e of material

# ----- Configure Plot ----- #
plt.figure(figsize=(8,8))
def yield_line(yield_strength): # Formulate the yield strength line
    plt.plot([0,yield_strength],[yield_strength,0],color='black',linestyle='--',label="Yield Line")
    plt.legend()
    plt.ylim(0,ultimate_strength)
    plt.xlim(0,ultimate_strength)
    plt.xlabel(r'$\sigma_m$',fontsize=20)
    plt.ylabel(r'$\sigma_a$',fontsize=20)
    return

yield_line(yield_strength) # Make and print the yield line

def goodman_line(ultimate_strength,endurance_limit): # Formulate the Goodman Line
    plt.plot([0,ultimate_strength], [endurance_limit,0],color='red',label="Goodman Line")
    plt.legend()
    plt.ylim(0,ultimate_strength)
    plt.xlim(0,ultimate_strength)
    return

goodman_line(ultimate_strength,endurance_limit) # Make and print the Goodman Line

def soderberg_line(endurance_limit,yield_strength): # Formulate the Soderberg Line
    plt.plot([0,yield_strength],[endurance_limit,0],color='blue',label="Soderberg Line")
    plt.legend()
    plt.ylim(0,ultimate_strength)
    plt.xlim(0,endurance_limit)
    return

soderberg_line(endurance_limit,yield_strength) # Make and print the Soderberg Line

def gerber_line(stress_mean,endurance_limit,ultimate_strength): # Formulate the Gerber Curve
    stress_mean = np.linspace(0,ultimate_strength,100) # Create the S_m value array
    sa = endurance_limit * (1 - (stress_mean/ultimate_strength)**2) # Calculate S_a amplitude values
    plt.plot(stress_mean,sa,color='green',label="Gerber Curve")
    plt.legend()
    plt.ylim(0,ultimate_strength)
    plt.xlim(0,ultimate_strength)
    return

gerber_line(stress_mean,endurance_limit,ultimate_strength) # Make and print the Gerber Curve

# ----- Stress Points ----- #
s_mean = [100,200,178,190] # Mean stress values
s_amplitude = [150,198,230,50] # Stress amplitude values
plt.scatter(s_mean,s_amplitude)

plt.show() # Show the plots