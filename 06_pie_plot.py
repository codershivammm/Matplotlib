import matplotlib.pyplot as plt

x = [10,20,30,40]
language = ["Java","C","C++","Python"] 
ex = [0.3,0.0,0.0,0.0]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  # Define colors for each slice

plt.title("Popularity of Programing Language", loc= "center",y=1,fontsize=20)

plt.pie(x,explode=ex,labels=language,radius=1,autopct="%0.1f%%",shadow=True, textprops={"fontsize":15},labeldistance=1.2
        ,wedgeprops={'edgecolor': 'black', 'linewidth': 2},colors=colors,frame=True)
plt.legend(title="Languages")
plt.show()




#autopct function is used to display percentage of pie chart 
#explode fuction takes out the part for which parameter is greater than 0.0
#radius parameter adjust the size of piechart 
#textprops parameter can be used to give property to text such as size underline bold etc 