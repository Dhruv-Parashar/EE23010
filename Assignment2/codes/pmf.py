import math
import numpy as np
import matplotlib.pyplot as plt


plt.xlabel('k')
plt.ylabel('P(A=k)')
Amount = [-6,-3,-1,1.5,4]
Prob = [0.0625,0.25,0.375,0.25,0.0625]
plt.xlim([-7,5])
plt.ylim([0,1])
plt.stem(Amount,Prob)



plt.savefig('/home/dhruv/EE23010/Assignment2/figs/figure2.png')
plt.show()
