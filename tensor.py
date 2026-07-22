
import pandas as pd
data={"country":["brasil","russia","india"],
  "capital":["brasilia","moscow","new delhi"],
  "area":[8.21,4965,33421],
  "population":[4354,4343.5,453.5]}
data_table=pd.DataFrame(data)
print(data_table)