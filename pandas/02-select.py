import pandas as pd
df = pd.read_csv('./pandas/00-biostats.csv')
df.columns = ['Name','Sex','Age','Height','Weight']

print('Columns:',df.columns)

# Select One column
print(df['Age'].head())
print(df.Age.head())

#  Select more columns
print(df[['Age','Weight']].head())
print(df.filter(['Age','Weight']).head())
print(df.filter(items=['Age','Weight']).head())
print(df.filter(like='ight').head())
print(df.filter(regex='.eight').head())

# Select All columns, One column, Two columns and From-To columns
# lines between 0 and 2 (inclusive)
print(df.loc[0:2])
print(df.loc[0:2,'Age'])
print(df.loc[0:2,['Age','Weight']])
print(df.loc[0:2,'Age':'Weight'])

# Select All columns, One column and Two columns, lines 0 and 2
print(df.loc[[0,2]])
print(df.loc[[0,2],'Age'])
print(df.loc[[0,2],['Age','Weight']])

# lines between 0 and 2 (inclusive = 3 exclusive)
# column 3 (init at 0, column Height)
print(df.iloc[0:3,3])
# get same lines, columns interval (last number exclusive)
print(df.iloc[0:3,2:5])
# get same lines, non continuous columns interval
print(df.iloc[0:3,[2,4]])
# get same lines, First and Third columns with True/False
print(df.iloc[0:3,[True, False, True, False, False]])

# get list of a condition True/Falses
print(df['Age']>40)

# get regs where this contition are True
print(df[df['Age']>40])

# get regs where this contition are True - AND
print(df[(df['Age']>40) & (df['Height']<=70)])

# get regs where this contition are True - AND OR
print(df[(df['Age']>40) & ((df['Height']<=70) | (df['Weight']==175))])

# Same statement, using isin
print(df[(df['Age']>40) & ((df['Height']<=70) | (df.Weight.isin([174,175])))])

# get regs where this contition are True, show just Name column
print(df[(df['Age']>40) & (df['Height']<=70)]['Name'])

# Other isin use:
filter = df.isin({'Age':[30,31,53], 'Weight':[175]})
print(filter)
print(df[filter])
print(df[(filter.Age)&(filter.Weight)])