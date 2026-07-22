import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv("iris.csv", header=None)

plt.plot(iris[0], label="Sepal Length")
plt.plot(iris[1], label="Sepal Width")
plt.plot(iris[2], label="Petal Length")
plt.plot(iris[3], label="Petal Width")


plt.title("Iris Dataset")
plt.legend()

plt.show()
