import pandas as pd
df = pd.read_csv('./pandas/00-biostats.csv')
df.columns = ['Name','Sex','Age','Height','Weight']

# Sort by age
print(df.sort_values('Age').head())
print(df.sort_values(by='Age').head())
print(df.sort_values('Age', ascending=True).head())
print(df.sort_values('Age', ascending=False).head())

# Order is not persistent
print(df.head())

# Turning order persistent (can be used with other commands):
df.sort_values('Age', inplace = True) # or df2 = df.sort_values('Age')
print(df.head())

# Order by more columns
print(df.sort_values(['Age','Height']).head())
print(df.sort_values(by=['Age','Height']).head())
print(df.sort_values(['Age','Height'], ascending=[True,False]).head())
cols = ['Age','Height']
order = [True,False]
print(df.sort_values(cols, ascending=order).head())
