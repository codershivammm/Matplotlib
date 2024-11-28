import matplotlib.pyplot as plt

Apps = ["Prime Video","Facebook","Instagram","Snapchat","Twitter"]
Ratings = [5,2,1,4,3]

plt.xlabel("Appliccation Names", fontsize = 15)
plt.ylabel("Ratings",fontsize = 15)
plt.title("Application Rating",fontsize = 20)

sizes = [200,500,250,600,400]
colors =[10,30,65,85,18]

plt.scatter(Apps,Ratings,sizes,colors,cmap="viridis",marker="*", edgecolors="k", linewidths=2)  #marker = shape of scatter ; edgecolor give border and linewidth adjusts the width of the border

t = plt.colorbar()  #cmap = colormap there are many color map in python u can hover internet to get it.
t.set_label("Color Bar",fontsize = 15)

plt.show()
