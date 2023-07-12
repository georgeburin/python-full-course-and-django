count_file = open('countries.txt', 'r') #to do file operations we should first open it like this.
#THe second paramenter is either 'r' or 'w' or 'a' or 'r+w' e.c.t.
#file should be in the same directory we use / (forward shash) not \
# instead of 'countries.txt' we could have also pasted the entire path such that C:/Users/bla/bla/bla/countries.txt

print(count_file.readable()) # True if we can read it

'''
print(count_file.readline()) # reads the first line
print(count_file.readline()) # reads the second line

print(count_file.readlines()) #puts ALL LINES of the file in a list, but if we also have the code above
# its going to read the lines not read already by the code above
# so the first two lines would not be read by this code
print(count_file.readlines()[0]) #gets the first line in a list
'''

for line in count_file.readlines():
  print(line)
count_file.close()




count_file1=open('country.txt','w') #if this file didnt exist and it is 'w' then we create it
#automatically. if this file existed and we write to it then it deletes everything in there
# that was there before
count_file1.write('This is the new world')
count_file1.write('This is the new world')
count_file1.close()


count_file2=open('country.txt','a') #appending file
count_file2.write('This is the new world')
count_file2.write('\nappending file')
count_file2.write('\nappending file')
count_file2.close()

#we are not limited to .txt files
openfile = open('openfileusingpython.py','w' ) #here we are creating a python file
openfile.write('print(\'this is a new file\')') # HAVE TO HAVE THOSE \' otherwise error
# now we have created a python file and put a print statement there

