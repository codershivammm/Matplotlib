import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
area1 = [19,28,65,12,37]
area2 = [12,45,36,25,39]
area3 = [12,29,78,65,37]

plt.stackplot(x,area1,area2,area3,labels=["area1","area2","area3"])
plt.title("Area Plot or Stack Plot",fontsize=20)
plt.xlabel("X-Axis",fontsize=15)
plt.ylabel("Y-Axis",fontsize=15)
plt.legend()
plt.show()