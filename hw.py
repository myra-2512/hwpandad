import pandas as pd
import numpy as np

employee_data={'name':['Pankaj','Meghna','David','Lisa'],
               'role':['CEO',np.nan,np.nan,np.nan],
               'salary':[100,200,np.nan,np.nan]}
labels=['1','2','3','4']
df = pd.DataFrame(employee_data , index=labels)

print("original data frame:")
print(df)

print("first two rows of the data frame:")
print(df.head(2))
print("last two rows of the data frame:")
print(df.tail(2))

print("Summary of the basic information about this DataFrame and its data with counts of non-null values:")
print(df.info(show_counts=True))

print("Data frame after removing rows with missing values:")
new_employee_data = df.dropna()
print(new_employee_data)

print("Data frame after replacing missing values:")
df['salary'].fillna('300', inplace=True)
df['role'].fillna('CEO ', inplace=True)

print(df)