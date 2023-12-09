# This code generates random variables for temperature (in degrees), salnity (in parts per million) and Moonphase.
# Based on the variables the code determines an oyster sites probability of spawning new spat: High, Medium or Low.

import numpy as np
import random 
import matplotlib as plt

# Declare variables
MoonPhase = ["Full", "Half", "Quarter"]            
SpatProduction = ["High", "Medium","Low"]

# Generating Random Temperatures
TempRange = np.random.default_rng(12345)
Temp = TempRange.integers(low=7 , high=18, size=100)

# Generating Random Salinities
SalinityRange = np.random.default_rng(12345)
Sal = SalinityRange.integers(low=10 , high=35, size=100)
print (Sal)

# Generating Random Moonphase
MPRange = np.random.choice(MoonPhase, size=100)
print (MPRange)

# Generating Random SpatProduction
SpatRange = np.random.choice(SpatProduction, size=100)
print (SpatRange)



   
