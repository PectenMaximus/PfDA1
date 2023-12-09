# This code generates random variables for temperature (in degrees), salnity (in parts per million) and Moonphase.
# Based on the variables the code determines an oyster sites probability of spawning new spat: High, Medium or Low.

import numpy as np
import random 
import matplotlib.pyplot as plt

# Declare variables
MoonPhase = ["Full", "Half", "Quarter"]            
SpatProduction = ["High", "Medium","Low"]

# Generating Random Temperatures
TempRange = np.random.default_rng(12345)
Temp = TempRange.integers(low=7 , high=18, size=100)

# Generating Random Salinities
SalinityRange = np.random.default_rng(12345)
Sal = SalinityRange.integers(low=10 , high=35, size=100)

# Generating Random Moonphase
MPRange = np.random.choice(MoonPhase, size=100)

# Generating Random SpatProduction
SpatRange = np.random.choice(SpatProduction, size=100)

#Print the Full Range for all results
for iLoop in range (0, 99):
    print(Temp[iLoop],Sal[iLoop],MPRange[iLoop],SpatRange[iLoop])

# Temperature against Salinty for Full Moon - Spat Production High=Green, Medium=Orange, Low=red.
MasterArray = np.array []
for iLoop in range (0,99):
    if (MPRange[iLoop]=="Full"):
        print(Temp[iLoop],Sal[iLoop],MPRange[iLoop],SpatRange[iLoop])
        FullMoonTemp = (Temp[iLoop])
        FullMoonSal = (Sal[iLoop])
        MasterArray = [Temp[iLoop],Sal[iLoop]]

# Temperature against Salinty for Half Moon - Spat Production High=Green, Medium=Orange, Low=red.
for iLoop in range (0,99):
    if (MPRange[iLoop]=="Half"):
        print(Temp[iLoop],Sal[iLoop],MPRange[iLoop],SpatRange[iLoop])

# Temperature against Salinty for Quarter Moon - Spat Production High=Green, Medium=Orange, Low=red.
for iLoop in range (0,99):
    if (MPRange[iLoop]=="Quarter"):
        print(Temp[iLoop],Sal[iLoop],MPRange[iLoop],SpatRange[iLoop])
         

#plt.bar(["T1","S1"],[Temp[0],Sal[0]])
#plt.title("SpatProduction")
#plt.xlabel("Events")
#plt.ylabel("TempValue")
#plt.show()

# Temperature against Salinity   
plt.scatter([Temp],[Sal])  
plt.axis((1,25,0,40))
plt.xlabel("Temperature")
plt.ylabel("Salinity")
plt.xscale("linear")
plt.show()