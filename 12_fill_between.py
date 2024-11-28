import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(1,6)
y = np.arange(1,6)

plt.plot(x,y , color ="k")
plt.fill_between(x,y,color = "r",where=(x>=2) & (x<=4), alpha = 0.5) #fills from x axis 2 to 5
plt.title("Fill Between Example",fontsize = 20) 
plt.xlabel("X-Axis",fontsize = 15)
plt.ylabel("Y-Axis",fontsize = 15)
plt.show()