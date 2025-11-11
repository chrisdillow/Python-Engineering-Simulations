# Comparison of Projectile Motions
# Chris D. | 4/5/2025

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

# ----- Variable Declarations ----- #

release_velocity_1 = 40 # Velocity at release expressed in m/s
release_velocity_2 = 30
g = 9.81 # Acceleration of gravity expressed in m/s^2
theta_1 = 45 # Angle of projectile motion expressed in degrees
theta_2 = 30

v_x_component_1 = release_velocity_1 * cos(theta_1*(pi/180)) # X component of velocity expressed in m/s
v_y_component_1 = release_velocity_1 * sin(theta_1*(pi/180)) # Y component of velocity expressed in m/s
v_x_component_2 = release_velocity_2 * cos(theta_2*(pi/180))
v_y_component_2 = release_velocity_2 * sin(theta_2*(pi/180))

time_to_ground_1 = 2 * (v_y_component_1/g) # The time in seconds it will take the projectile to hit the ground after being launched
t_1 = np.linspace(0,time_to_ground_1,100) # The time since launch expressed in seconds
time_to_ground_2 = 2 * (v_y_component_2/g)
t_2 = np.linspace(0,time_to_ground_2,100)

x_displacement_1 = t_1 * v_x_component_1 # Current location in X expressed in meters
y_displacement_1 = (t_1 * v_y_component_1) - (.5 * g * t_1**2) # Current location in Y expressed in meters
x_displacement_2 = t_2 * v_x_component_2
y_displacement_2 = (t_2 * v_y_component_2) - (.5 * g * t_2**2)



# ----- Plot of the Object's Trajectory ----- #
plt.figure(figsize=(10,5))
plt.plot(x_displacement_1,y_displacement_1,label=f"Angle: {theta_1}; Initial Velocity: {release_velocity_1}") # Input the values of the x and y axes
plt.plot(x_displacement_2,y_displacement_2,label=f"Angle: {theta_2}; Initial Velocity: {release_velocity_2}")
plt.title("Graph of Projectile Motions")
plt.xlabel("X Location (m)")
plt.ylabel("Y Location (m)")
plt.legend()
plt.show()