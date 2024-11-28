import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,2,6,3,4]

plt.stem(x,y,linefmt=":",markerfmt="*",basefmt="g" , orientation = "horizontal")
plt.show()