#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:14:43 2023

@author: bruno.souza
"""

# Generate four graphics in an image

import numpy as np                            # scientific computing library  
import matplotlib.pyplot as plt               # library for creating charts and plots  


# Parameters
a = 0.5                                       # amplitude
f= 10                                         # frequency    
dt = 0.01                                     # time step
t = np.arange(0, 10, dt)                      # time


# # random noise
# nse1 = np.random.randn(len(t))                # white noise 1
# nse2 = np.random.randn(len(t))                # white noise 2
# nse3 = np.random.randn(len(t))                # white noise 3
# nse4 = np.random.randn(len(t))                # white noise 4

# fixed noise
nse1 = np.linspace(0,0,len(t))                # white noise 1
nse2 = np.linspace(0,0,len(t))                # white noise 2
nse3 = np.linspace(0,0,len(t))                # white noise 3
nse4 = np.linspace(0,0,len(t))                # white noise 4



# Four signals with a coherent part at frequency (f) and a random part (nse)
s1 = np.sin(a * np.pi * f * t) + nse1
s2 = np.cos(a * np.pi * f * t) + nse2
s3 = np.sin(a * np.pi * f * t) + nse3         
s4 = np.cos(a * np.pi * f * t) + nse4


# Plot
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2)
fig.suptitle('Figure title', fontsize=14)


# Features of the 1st chart
ax1.plot(t,s1,color='black')
ax1.plot(t,s2,color='red')
ax1.set_xlim(0,1)
ax1.set_ylim(-4,4)
ax1.set_xlabel('variable a')
ax1.set_ylabel('A (a)')
ax1.set_title('sublot 1')
ax1.grid(True)

# Features of the 2nd chart
ax2.plot(t,s2,color='blue')
ax2.plot(t,s3,color='purple')
ax2.set_xlim(0,1)
ax2.set_ylim(-4,4)
ax2.set_xlabel('variable b')
ax2.set_ylabel('B (b)')
ax2.set_title('sublot 2')                      
ax2.grid(True)

# Features of the 3rd chart
ax3.plot(t,s3,color='orange')
ax3.plot(t,s4,color='green')
ax3.set_xlim(0,1)
ax3.set_ylim(-4,4)
ax3.set_xlabel('variable c')
ax3.set_ylabel('C (c)')
ax3.set_title('sublot 3')
ax3.grid(True)

# Features of the 4th chart
ax4.plot(t,s4,color='gold')
ax4.plot(t,s1,color='coral')
ax4.set_xlim(0,1)
ax4.set_ylim(-4,4)
ax4.set_xlabel('variable d')
ax4.set_ylabel('D (d)')
ax4.set_title('sublot 4')
ax4.grid(True)


plt.tight_layout()                              # adjust the padding between and around subplots
plt.savefig('4_Subplots',dpi=1000)              # save the figure