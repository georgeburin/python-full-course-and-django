'''
x = int(input('input an int: '))
print(x)
is you do this code and type string its going to return 
ValueError: invalid literal for int() with base 10: 'asd'
'''

try:
  x = int(input('input an int: '))
  print(x)
except: #except without value is if there is any error at all
  print('something went wrong') #if there is an error then the code doesnt crash

try:
  x = int(input('input an int: '))
  print(x)
except ValueError: #if there is a ValueError (when you type in string instead of number)
  # print('value is not an int'+name) this is a NameError
  print('value is not an int')
else:
  print('nothing went wrong') # if we input int then its going to run the code in try:  and then print
  #('nothing went wrong') IF THERE IS ERROR THEN THIS IS NOT PRINTED

try:
  x = int(input('input an int: '))
  print(x)
except:
  print('something went wrong')
finally:
  print('try except finished') #THIS IS GOING TO BE PRINTED NO MATTER IF WE HAVE AN ERROR OR NOT