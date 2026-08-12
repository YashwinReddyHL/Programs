import pandas as pd

nums = [1, 2, 3, 5, 7, 9, 7, 2, 7, 6]

df = pd.DataFrame(nums, columns=['Numbers'])

print(df)

print("Mean:", df.mean())

print("Mode:" , df.mode())

print("Standard Deviation:", df.std())

print("Skewness:", df.skew())