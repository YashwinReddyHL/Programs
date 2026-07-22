import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', names=['sepal length','sepal width','petal length','petal-width','class'])
print(iris.head())
colors = {'Iris-setosa':'r','Iris-versicolor':'g', 'Iris-virginica':'b'}
# create a figure and axis 
fig, ax = plt.subplots() # plot each data-point for
for i in range(len(iris['sepal length'])):
 ax.scatter(iris['sepal length'][i],iris['sepal width'][i],color=colors[iris['class'][i]])
# set a title and labels 
ax.set_title('IrisDataset') 
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width') 
plt.show()