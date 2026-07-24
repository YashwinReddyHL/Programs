import pandas as pd
import numpy as np
credit_df= pd.read_csv("credit_dataset.csv")

q1 = credit_df["Age"].quantile(0.25)
q3 = credit_df['Age'].quantile(0.75)
iqr = q3-q1
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)


upperIndex = credit_df[credit_df['Age']>upper_bound].index
credit_df.drop(upperIndex,inplace=True)
lowerIndex = credit_df[credit_df['Age']<lower_bound].index
credit_df.drop(lowerIndex,inplace=True)
credit_df.info()

# using mean
m = np.mean(credit_df['Age'])
print('mean:',m)
for i in credit_df['Age']:
 if i<lower_bound or i>upper_bound :
  titanic_df['Age'] = titanic_df['Age'].replace(i,m)




# using median
m = credit_df['Age'].median()
print("median",m)
for i in credit_df['Age']:
 if i<lower_bound or i>upper_bound :
  credit_df['Age'] = credit_df['Age'].replace(i,m)



# using Zero
for i in credit_df['Age']:
 if i<lower_bound or i>upper_bound :
  credit_df['Age'] = credit_df['Age'].replace(i,0)