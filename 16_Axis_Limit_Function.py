import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,6,2,4,3]

#Axis Value pe Apne According Limit Lagana

#plt.xlim(0,10)
#plt.ylim(0,10)

#Another Method

plt.axis([0,10,0,7])

plt.plot(x,y,color="r", marker = "o" , ms = 10 , mfc = "g")

plt.title("Step Plot Example",fontsize=20)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()
plt.show()