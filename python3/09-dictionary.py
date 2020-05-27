# Create a dictionary
data = dict() # or
data = {'name':'Paul', 'age':25}

# Print a field value
print(data['name'])
print(data['age'])

# Add new field
data['weight'] = 70.2
print('Added new field', data)

# Del a field
del data['age']
print('Del new field', data)

# Printing keys, values and items
print(data.keys(), data.values(), data.items())

# Iterate key and values
for k,v in data.items():
    print(k,v,end=', ')
print('')

# Copy of a dictionary
dicBackup = data.copy()

# Dictionaries in lists
listMovies = [{'title':'Star Wars', 'year':1977},{'title':'Matrix', 'year':2000}]
print(listMovies[0]['title'])
print(listMovies[1]['year'])