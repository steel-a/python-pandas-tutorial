import pandas as pd

##########################
####     CSV File     ####
##########################
path = './pandas/00-biostats.csv'
# Could be an url
#path = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'

# Just open
df = pd.read_csv(path)
######   Replace column names if necessary   ######
df.columns = ['Name','Sex','Age','Height','Weight']


####  More options to know  ####

# Tell what the encoding, separator, header line
# df = pd.read_csv(path, encoding='UTF-8', sep=',', header=0)

# Tell what columns we will use
# df = pd.read_csv(path, usecols=['Country'])

# Tell how many cols we will use
# df = pd.read_csv(path, nrows=10)

print(df.columns)
print(df.head())

##########################
####    Excel File    ####
##########################

path = './pandas/00-biostats.xlsx'

####### Open an Excel file so you can read any sheet #######
# How to see exel sheets
excelFile = pd.ExcelFile(path)
print(excelFile.sheet_names) #### Needs xlrd package
# Read sheet names
sheet1 = excelFile.parse('Sheet1')

####### Just read one sheet ########
# Open first sheet
df = pd.read_excel(path)
# Tell what sheet we will use
#df = pd.read_excel(path, sheet_name='Sheet1') # or sheet_name=0

print(df.head())