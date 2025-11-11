# Beam Analysis Program
# Shear Force and Bending Moment Diagrams
# Chris D. | 4/5/2025

import numpy as np
import matplotlib.pyplot as plt

# ----- Inputs ----- #

length = 10 # length of beam
uniform_dist_load = 500 # N/m

# ----- Reactions ----- #

shear_reaction = (uniform_dist_load * length)/2
x_range = np.linspace(0,length,100) # Divide length into segments and calculate shear force and moment across each point

# ----- Initialize Empty Coordinate Arrays ----- #
X = [] #X Value
SF = [] #Shear Force
M = [] #Moment

# ----- Calculate Cooridnate Arrays ----- #
for length in x_range:
    shear_force = shear_reaction - (uniform_dist_load * length)
    moment = (shear_reaction * length) - ((uniform_dist_load * length**2)/2)
    X.append(length) # Append current length to array
    M.append(moment) # Append current moment to array
    SF.append(shear_force) # Append current shear force to array

# ----- Plot Configuration ----- #

plt.figure(figsize=(7.5,5),dpi=100)
plt.subplot(2,1,1) # Set up to show two graphs, in one column, this one in 1st plot
plt.plot(X,SF,'g')
plt.fill_between(X,SF,color='green',alpha=0.5,hatch="||")
plt.title("Shear Force Diagram")
plt.ylabel("Shear Force")
plt.xlabel("Point on Length")
plt.tight_layout(pad=4.0)

plt.subplot(2,1,2) # Set up to show two graphs, in one column, this one in 2nd plot
plt.plot(X,M,'r')
plt.fill_between(X,M,color='red',alpha=0.5,hatch="||")
plt.title("Bending Moment Diagram")
plt.ylabel("Bending Moment")
plt.xlabel("Point on Length")
plt.tight_layout(pad=4.0)
plt.show()