#Von Mises Failure Theory Plots
#Chris D. | 4/5/2025

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

mat_yield_strength = 200 # Material Yield Strength expressed in MPa (Pa = N/m^2)
applied_stress_dir1 = 150 # Expressed in MPa (Pa = N/m^2), notated sigma1
applied_stress_dir2 = 80 # notated sigma2

sigma_v = np.sqrt(applied_stress_dir1**2 - (applied_stress_dir1 * applied_stress_dir2) + applied_stress_dir2**2)

a = np.sqrt(2) * mat_yield_strength # Semi-major axis of ellipse
b = np.sqrt(2/3) * mat_yield_strength # Semi-minor axis of ellipse

theta = np.linspace(0,360*(pi/180),720) # Generate an array of 720 points along 360 degrees of rotation as converted to radians

x_coordinate = a*cos(theta) # Original point X
y_coordinate = b*sin(theta) # Original point Y

rot_theta_deg = 45 # Rotation angle of the ellipse in degrees
rot_theta = rot_theta_deg * (pi/180) # Rotation angle of the ellipse in radians
xf_coordinate = (x_coordinate * cos(rot_theta)) - (y_coordinate * sin(rot_theta))
yf_coordinate = (x_coordinate * sin(rot_theta)) + (y_coordinate * cos(rot_theta))

# ----- Shear Stress Coordinates ----- #
shear_stress_x = [mat_yield_strength,mat_yield_strength,0,-mat_yield_strength,-mat_yield_strength,0,mat_yield_strength]
shear_stress_y = [0,mat_yield_strength,mat_yield_strength,0,-mat_yield_strength,-mat_yield_strength,0]

# ----- Test Stress Points ----- #
sp_x = [200,160,80,60]
sp_y = [-80,210,50,40]

# ----- Plot the Ellipse ----- #
plt.figure(figsize=(7.5,5))
plt.plot(xf_coordinate,yf_coordinate,label="Von Mises Region")
plt.plot(shear_stress_x,shear_stress_y,linestyle='--',label="Max Shear Region")
plt.scatter(sp_x,sp_y,label="Stress Points")
plt.legend()
plt.show()