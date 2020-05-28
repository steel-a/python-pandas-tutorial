import pandas as pd
df = pd.read_csv('./pandas/00-biostats.csv')
df.columns = ['Name','Sex','Age','Height','Weight']

# New calculed column
df['BMI'] = df['Weight']/(df['Height']**2)

print(df.head())