import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,6,2,4,3]

plt.title("Step Plot Example",fontsize=20)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()
plt.step(x,y,color="r", marker = "o" , ms = 10 , mfc = "g")

plt.savefig("Step_plot_Graph_Example", dpi = 2000, facecolor ="skyblue" ,transparent = True)

plt.show()