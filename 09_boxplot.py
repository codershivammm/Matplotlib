import matplotlib.pyplot as plt

x = [10,20,30,40,50,60,70]
y = [10,20,30,40,50,60,70,80,90]
z = [10,20,30,40,50]
k = [x,y,z]

plt.boxplot(k,labels=["I am 1st label","I am 2nd lable","I am 3rd label"] , showmeans=True, boxprops={"color": "r"}, whiskerprops={"color": "g"}, capprops={"color": "m"})

plt.show()

#Box Plot is also known as Whisker Plot