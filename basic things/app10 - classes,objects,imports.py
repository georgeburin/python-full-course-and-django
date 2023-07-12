class Myclass:
  x = 5
p1 = Myclass()
print(p1.x)

class Person:
  def __init__(self,name,age): # self is always here
    self.name = name # this is under the def __init__ function
    self.age = age
p1 = Person('John',87)
print(p1.name)
print(p1.age)
# can also name777=input('input name: ')
#p1 = Person(name777,87)
del p1 # deletes p1

class dog:
  pass
# this is so we dont get an error. without this word pass we would get an error

from app10_class_definition_in_separate_file import Student  #from filename import classname
# this is how we import a class from another python file

class Person2(Student): #this is python inheritance
  pass

p1=Person2()
print(p1.name)


'''
python shell: open IDLE Shell
you can run code there for testing
code runs as soon as you type it
for example: print('hello') would be printed as soon as you type this command
'''

import app10_class_definition_in_separate_file #there is a function in this file. WE CAN IMPORT IT LIKE THIS

app10_class_definition_in_separate_file.say_hi()

#pypi.org     
#pypi.org  
#pypi.org  this is a website where you can get modules for python
#modules are hosted online
# functions and classes already written by someone else that WE CAN USE
#PIP is used to install external modules to pyton
# go pypi.org -> frameworks -> django copy the line of code to download it, put it in command line.



# pip install django      install django in the computer
# pip install virtualenvwrapper-win               now we need a virtual environment
# mkvirtualenv myapp              creates and activates a virtual environment. (myapp) C:\Users\georg> now we are in vm called myapp
# pip install django      install django in the virtual environment once you are there
# deactivate - gets you out of the virtual env
# workon myapp - this is how you get into the vm
# go to the root directory where manage.py is located and:
# python manage.py startapp FirstDjangoProject
# python manage.py runserver

