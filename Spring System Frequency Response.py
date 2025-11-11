# Frequency Response of a Spring Mass System
# April 15, 2025
# Chris Dillow

import numpy as np
import matplotlib.pyplot as plt

# ----- Inputs ----- #
frequency_ratio = np.linspace(0,3,300) # W / W_n
zeta = [0.1,0.2,0.3,0.4,0.5,0.6] # 0 - 1; Damping Ratio; any number of values stored as an array

# ----- Configure Plot(s) ----- #
plt.figure(figsize=(7.5,5),dpi=150)

for z in zeta:
    first_block = (1 - (frequency_ratio**2))**2
    second_block = (2 * z * frequency_ratio)**2
    evaluation = np.sqrt(first_block + second_block)
    frequency = (1 / evaluation)
    plt.plot(frequency_ratio,frequency,label=r'$\zeta={}$'.format(z)) # Plot and label color per z value of zeta

plt.title("Frequency Ratio to Frequency Response")
plt.xlabel("Frequency Ratio")
plt.ylabel("Frequncy")
plt.legend(loc='best') # Fit to best location
plt.grid(which='major',color='gray')
plt.minorticks_on()
plt.grid(which='minor',color='gray',linestyle='--',alpha=0.4)
plt.xlim(frequency_ratio[0],frequency_ratio[-1])
plt.show()