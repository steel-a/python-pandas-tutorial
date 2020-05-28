import pandas as pd
df = pd.read_csv('./pandas/00-biostats.csv')
df.columns = ['Name','Sex','Age','Height','Weight']

# Max Age, Min Age and Mean Age between all regs
print(df.Age.max(), df.Age.min(), df['Age'].mean())

# Mean age of person with >= 170 Weight
print(df[df['Weight']>=170]['Age'].mean())

# Group by: See mean Weight of Man and Woman
print(df[['Sex','Weight']].groupby(['Sex']).mean())

# Group by: See mean Weight of Man and Woman with more then 40 years
print(df[df['Age']>=40][['Sex','Weight']].groupby(['Sex']).mean())
