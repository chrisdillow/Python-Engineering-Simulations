# Non-Uniform Load Beam Analysis
# Chris D. | 4/5/2025

import numpy as np
import matplotlib.pyplot as plt

# ----- Inputs ----- #
length = 10 # meters
load_distribution = 50 # Newton-meters

# ----- Locators ----- #
dist_from_left = 3 # meters
load_dist = 5 # meters
dist_from_right = length - (dist_from_left + load_dist)

# ----- Reaction Formulas ----- #
reaction_1 = ((load_distribution * load_dist)/length) * (dist_from_right + load_dist/2) # Reaction at left end
reaction_2 = ((load_distribution * load_dist)/length) * (dist_from_left + load_dist/2) # Reaction at right end

length_bin = np.linspace(0,length,200)

# ----- Initialize Empty Plot Arrays ----- #
X = [] # Length array values
SF = [] # Shear force array values
M = [] # Moment array values

for x in length_bin:
    if x < dist_from_left: # Determine if occurs in Section 1
        sf = reaction_1
        m = reaction_1 * x
    elif dist_from_left < x < (dist_from_left + load_dist): # Determine if occurs in Section 2
        sf = reaction_1 - (load_distribution * (x - dist_from_left))
        m = (reaction_1 * x) - (load_distribution * ((x - dist_from_left)**2)/2)
    elif x > (dist_from_left + load_dist): # Determine if occurs in Section 3
        sf = -reaction_2
        m = (reaction_2 * (length - x))

    X.append(x) # Append current length to array
    SF.append(sf) # Append shear force to array
    M.append(m) # Append moment to array

# ----- Configure the Plots ----- #
plt.figure(figsize=(5,5),dpi=100)
plt.subplot(2,1,1) # Two rows, one column, place in 1st spot
plt.plot(X,SF,'g')
plt.fill_between(X,SF,color='green',hatch="||",alpha=0.5)
plt.title("Shear Force Diagram")
plt.ylabel("Shear Force (N)")
plt.xlabel("Length of Beam (m)")

plt.tight_layout(pad=3.0)
plt.subplot(2,1,2) # Two rows, one column, place in 2nd spot
plt.plot(X,M,'r')
plt.fill_between(X,M,color='red',hatch="||",alpha=0.5)
plt.title("Bending Moment Diagram")
plt.ylabel("Bending Moment (N/m)")
plt.xlabel("Length of Beam (m)")

plt.show()