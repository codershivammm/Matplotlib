import matplotlib.pyplot as plt

x = ["Shivam" , "Rahul", "Ravi" , "Simran"]
y = [96,23,85,56]
plt.xlabel("Name Of Students",fontsize = 10)
plt.ylabel("Marks Of Student" , fontsize = 10)
plt.title("Total Marks Of Student Out of 100",fontsize = 20)

c = ['r','y','b','g']  #passing color we can pass the color code too

plt.bar(x,y,color = c, width=0.5, edgecolor="black", linewidth = 5 , alpha = 0.7 ) #alpha parameter is used to control opacity varies from 0 to 1
#width paramenter is used to control the width of the each bar 
#linewidth is for the giving the edge for graph
plt.show()