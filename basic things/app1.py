print('hello world')
print("hello world")
name = 'Tim'
age = 18
print(name)
print(name+' hello world '+name) #string concatenation have no use space
print(name,'hello world',age) #dont use space when using coma. smart feature of python. it adds the space
print('hello\nworld\'') # \n is a new line character
print(name[0]) #access T from the name Tim
print(name.isupper()) # console says false
print(name.upper())
print(name.index('i')) # console says 1
print(name.replace('i', 'GGGGGGGGGGG')) # replaces i in the word Tim with GGGGGGGGGGG
print(78+22) #100 works with decimals and / * - as well
print(20%6) #3 remainder operator
number=55
number2=str(number) #convert number to string
print('number is '+number2) 
print(abs(-5)) # absolute value function build-in
print(max(4,2,1,1,1,1,2,0)) #console says 4. this is a which one is greater function. outputs the greatest number
print(min(4,2,1,1,1,1,2,0)) # 0
print(round(3.2)) #console says 3
print(round(3.5)) # console says 4
print(bin(3)) # returns a binary number of number 3

#all of these functions above are built in python. sqrt or power functions need to be imported
from math import * #  * menas import everything
print(sqrt(100)) # 10.0

name3 = input('Input Your Name: ') # getting input from the user
age3 = int(input('Input Your age: ')) #convert string to an int
print('your name is '+name3+' and you are',age3,'years old' )



sentence = input("Enter your sentence: ")
print('Your sentence is '+ sentence)
word1 = input('enter the word to replace: ')
word2 = input('enter the word to replace it with: ')
print(sentence.replace(word1, word2))

countries=['UK', 'US', 'Russia', 'Ukraine']
print(countries)
print(countries[0])