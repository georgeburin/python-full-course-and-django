a = 2
b = 3 
if a>b:
  print(a, 'is greater than', b)

a=True
b=True
if a==b:
  print('a=b')

a = 2
b = 3 
if a==b:
  print(a, 'is equal to', b)
else:
  print(a,'is not equal to '+str(b))

a = 2
b = 3 
if a>b:
  print(a, 'is bigger than', b)
elif a<b:                       #elif statement!!! ELSE IF
  print(a,'is less than '+str(b))
else:
  print(a, 'is equal toooo', b)

boy=True
short=True
if boy==True or short==True:  #can also use and!!!
  print('he is a short or boy')
elif boy==False:
  print('he is not a boy')

if type(boy) == str:
  print(boy,'is a string')
elif type(boy) == int:
  print(boy,'is an int')
elif type(boy) == bool:
  print(boy,'is a bool')

value=5
if value%5==0:   #value should be int
  print(value,'can be divided by five')
else:
  print(value,'can NOT be divided by five')

# num4 = int(input('enter a number: ))  this is how we input a number. so we dont get a string