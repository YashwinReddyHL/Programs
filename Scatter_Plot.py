'''
import pandas as pd
import matplotlib.pyplot as plt

col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

iris = pd.read_csv('iris.csv', header=None, names=col_names)

fig, ax = plt.subplots()

ax.scatter(iris['sepal_length'], iris['sepal_width']) 
ax.set_title('Iris Dataset') 
ax.set_xlabel('sepal_length') 
ax.set_ylabel('sepal_width')

plt.show()
'''



import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', names=['sepal length','sepal width','petal length','petal-width','class'])
print(iris.head())
fig, ax = plt.subplots()
  

ax.scatter(iris['sepal length'], iris['sepal width'])  
ax.set_title('Iris Dataset') 
ax.set_xlabel('sepal_length') 
ax.set_ylabel('sepal_width')
plt.show()