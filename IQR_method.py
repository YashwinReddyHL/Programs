import numpy as np
import matplotlib.pyplot as plt

np.random.seed(102)

# Generate data
grades = np.concatenate([
    [50,52,53,55,56,60,61,62,65,67] * 20,
    np.random.randint(0, 101, size=300)
])

# Quartiles and IQR
Q1, Q3 = np.percentile(grades, [25, 75])
IQR = Q3 - Q1

# Bounds
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Outliers
outliers = grades[(grades < lower_limit) | (grades > upper_limit)]

print("Outliers:", outliers)

# Plot
hypo = np.random.randint(20, 81, size=500)

plt.figure(figsize=(6, 5))
plt.boxplot([grades, hypo], widths=0.5)

plt.xticks([1, 2], ['Actual Data', 'Hypothetical Data'])
plt.ylabel('Grade')
plt.title('Box Plot of Midterm Grades')

plt.show()