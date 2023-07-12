i = 1
while i<6 or i ==10: # runs 5 times. 1 to 5 if use and then nothing runs
  print(i)
  i=i+1   # i += 1
  
print('\n')

for letter in 'Hello':
  print(letter)

print('\n')

for values in 'LOOP THROUGH':
  print(values)
print('\n')

mydict = {
  'name':'John',
  'age':12,
}
for values in mydict:
  print(values)
print('\n')

mylist=['ji','ju','jo']
for values in mylist:
  print(values)
  if values == 'ju':
    break
print('\n')

for x in range(4):
  print(x)  # 0 1 2 3    not 4
else:
  print('finished printing')  #so first it finishes the loop then does else

print('\n')

my_list = [ # list inside the list
  [1,2,3],
  [4,5,6,],
  [7,8,9,]
]
for lists in my_list: # a loop inside the loop
  for row in lists:
    print(row)

'''
this is a multi line comment


'''