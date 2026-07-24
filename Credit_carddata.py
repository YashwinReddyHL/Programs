import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


credit_df = pd.read_csv("credit_dataset.csv")
credit_df


credit_df.plot('Age','Income',kind='scatter',marker='o')


credit_df['Age'].plot(kind='box')


credit_df['Debt'].plot(kind='hist')

