import pandas as pd

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
