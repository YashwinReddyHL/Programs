# Import required libraries 
import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt 
 
# Reading the data 
df = pd.read_csv("data_out.csv") 
print(df.describe())