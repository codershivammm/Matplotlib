import matplotlib.pyplot as plt

x = [10,20,30,40]
language = ["Java","C","C++","Python"] 

plt.pie(x,labels=language,radius=1)
plt.pie([1],colors="w",radius=0.5)
plt.legend()
plt.show()
