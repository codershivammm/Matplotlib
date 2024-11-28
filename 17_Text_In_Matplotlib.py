import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,6,2,4,3]

#Setting X and Y Axis Limit
plt.axis([0,10,0,7])

plt.plot(x,y,color="r", marker = "o" , ms = 10 , mfc = "g")

plt.title("Step Plot Example",fontsize=20)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.text(2,6,"Peak Point",fontsize=15 , style = "italic")
plt.annotate("Lowest Point",fontsize=10 , xy = (3,2) , xytext=(8,5) , arrowprops={"facecolor":"k" , "shrink" : 100 , "width" : 0.7})

plt.grid()
plt.show()