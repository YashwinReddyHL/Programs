import numpy as np

data = [1, 2, 2, 2, 3, 1, 1, 15, 2, 2, 2, 3, 1, 1, 2]

mean = np.mean(data)
std = np.std(data)

print('Mean of the dataset is:', mean)
print('Standard deviation is:', std)

threshold = 3
outliers = []

for i in data:
    z = (i - mean) / std
    if abs(z) > threshold:   # handles both sides
        outliers.append(i)

print('Outliers using Z-score:', outliers)