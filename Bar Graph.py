#Bar Graph using Matplotlib
import matplotlib.pyplot as plt

#Initialising values for x and y axis 
plt.bar([1,3,5,7,9],[5,2,7,8,2], label = "Eg 1")   #x and y axis coordinates for bar graph 1
plt.bar([2,4,6,8,10],[8,6,2,5,6], label = "Eg 2",color = "g")  #x and y axis coordinates for bar graph 2

plt.legend()

#Naming
plt.xlabel('bar no.')
plt.ylabel('Bar Height')
plt.title(BarGraph)

#Displaying the bar graphs
plt.show()
