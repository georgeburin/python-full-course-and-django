def greetings_function(name, age): #this is how you define a function
  print('greetings '+str(name)+ ' you are '+str(age)+' years old') #the identation is important

greetings_function('George', 5) # calling the functuion

def hello_fucntion(*names): #if we dont know how many arguments to pass in the fucntion then we use *
  print('Hello',names[0])
# print('hello',names)
greetings_function('George', 5) # calling the functuion

hello_fucntion('george', 'kirill', 'victoer')
hello_fucntion('george')

def hello_fucntion1(name1): #if we dont know how many arguments to pass in the fucntion then we use *
  print('Hello',name1)

#name232=input('what is your name? ')
#hello_fucntion1(name232)


num1= int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
def add_numbers(num1,num2):
  return num1+num2 #anything after return is not part of code. its not going to run

print(add_numbers(2,3))
