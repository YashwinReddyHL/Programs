import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm



credit_df = pd.read_csv("credit_dataset.csv")
print(credit_df)


ax = credit_df.plot("Credit_Limit","Avg_Purchase",kind="scatter", color = "red",marker = "o",figsize=(10,7))
ax.set_xlabel("Credit_Limit")   
ax.set_ylabel("Avg_Purchase")   
ax.set_title("Credit_Limit vs Avg_Purchase",fontsize=16)


