import matplotlib.pyplot as plt

x = ["Shivam" , "Rahul", "Ravi" , "Simran"]
y = [96,23,85,56]
plt.subplot(2,2,1)
plt.bar(x,y)


Apps = ["Prime Video","Facebook","Instagram","Snapchat","Twitter"]
Ratings = [5,2,1,4,3]
plt.subplot(2,2,2)
plt.scatter(Apps,Ratings)


x = [10,20,30,40]
language = ["Java","C","C++","Python"]
plt.subplot(2,2,3) 
plt.pie(x)


x = [1,2,3,4,5]
y = [4,6,2,4,3]
plt.subplot(2,2,4)
plt.step(x,y,color="r", marker = "o" , ms = 10 , mfc = "g")
plt.show()