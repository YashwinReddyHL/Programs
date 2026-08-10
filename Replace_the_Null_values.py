import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
df = pd.read_csv('titanic.csv')

#Replace null values   
   
df.replace(np.nan,'0',inplace = True)   
   
#Check the changes now 
print(df.isnull().sum())