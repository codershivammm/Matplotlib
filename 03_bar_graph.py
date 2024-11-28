import matplotlib.pyplot as plt
import numpy as np

x = ["Shivam","Rahul","Ravi","Aman"]
y = [85,69,35,15]
z = [69,65,45,87]

width = 0.2
p = np.arange(len(x))       #This Part of Code deals with how to add two bar graphs side by side
p1 = [q+width for q in p]   #plotting 2nd bar graph

plt.xlabel("Name of Student")
plt.ylabel("Marks")
plt.title("Marks of Student in Science and maths")

plt.bar(p,y,width,color ="r" , label="Maths Marks")
plt.bar(p1,z,width,color="y", label="Science Marks")
plt.xticks(p+width/2,x) #converts the p array into x
plt.legend()
plt.show()

#For Horizontal Bar Graph we use barh instead of bar 
