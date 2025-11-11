# Natural Frequency Calculation - Eigenvalue Problems
# Chris D. | 4/15/2025

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# ----- Masses in KG ----- #
m1 = 5
m2 = 5
m3 = 5

# ----- Spring Constants in N/m ----- #
k1 = 100
k2 = 100
k3 = 100

# ----- Matrices ----- #
M = np.array([[m1,0,0],[0,m2,0],[0,0,m3]]) # Mass Matrix
K = np.array([[k1 + k2,-k2,0],[-k2,k2 + k3,-k3],[0,-k3,k3]]) # Stiffness Matrix

# ===== Eigen Value Calculations ===== #
#   'u' is for Eigen Value (scalar) 'v' is for Eigen vector

u,v = linalg.eigh(K,M) # Will be a matrix/array

# ----- Natural Frequency (omega-sub(n)) ----- #

Wn = np.sqrt(u) # Natural frequency is the square root of the eigen values
print("First Natural Frequency:",Wn[0]," Hz")
print("Second Natural Frequency:",Wn[1]," Hz")
print("Third Natural Frequency:",Wn[2]," Hz")