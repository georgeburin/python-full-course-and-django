my_dict = {
  'name':'Tim',
  'name':'george',
  'name2':'george',
  'age': 87,
  'is_tall':True,
  'nationality':'african',
  'qualification':'college',
  'friends': ['peter','paul','precious'] # can also have a list in the dictionary
}

#IN DICTIONARY WE CAN HAVE NUMBERS,TRUE,FALSE. IN JSON THERE ARE ONLY STRINGS
# in dictionaries keys cant be repeated. in JSON they can

print(my_dict) # notice how 'name':'Tim', doesnt get printed!!! cant have duplicates like this
print(my_dict['is_tall'])

x=my_dict['name']
print(x)