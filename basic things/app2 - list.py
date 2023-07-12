countries=['UK', 'US', 'Russia', 'Ukraine',True, 4, 'Russia', 'Ukraine']  #LISTS ARE MUTABLE
print(countries)
print(countries[0]) # UK
print(countries[0][1]) #K
print(countries[1:]) # from particular index to the end. from US to the end
print(countries[1:3]) # from US to Ukraine BUT NOT INCLUDING UKRAINE
number=3
print(type(number)) # integer
print(type(countries)) # this is a list
countries[0]='AUSTRALIA'
print(countries[0])
print(countries[-1]) #Ukraine. Now we take from the back
print(countries[-2]) # Russia
print('the length of the list is',len(countries))

countries2=list(('nigeria',34,False)) # another way of defining a list
print(type(countries2))


# EXTEND, APPEND, REMOVE, INSERT, INDEX, CLEAR
list1 = [1,2,3,4,5]
list2 = ['bananna', 'apples','mango','orange']
list1.extend(list2) #adds entire list2 to the back of list1
print('the list1 is now:',list1) 
list2.append('cherry') #adds 'cherry' to the back of the list2
list2.insert(1,'dog') #adds 'dog' at index 1 of the list2
print('the list2 is now:',list2)
list2.remove('bananna') #removes bananna from list2
print('the index of mango is :', list2.index('mango')) #2
print(list2.count('mango')) # 1 because 'mango' only appears once in the list2
list2.clear() # deletes all elements in the list, but not the list itself
print(list2)
print('__________________________________________________')
print('\n')


# SORT
list3=[3,2,5,1,4]
print(list3)
list3.sort()
print(list3) # you sort first then print. now the list is sorted 1, 2, 3, 4, 5
list3.reverse() # reverses the list
print(list3)
list4= list3.copy()
print('this is the new copied list',list4)
list4.pop() # removes the last item in the list
list4.pop(1) #removes the element with index 1 of the list4
del list4[0] # removes the element wiht index 0 of the list4
del list4 # deletes the list4 itself with all variables there, would be undefined later

my_list = [ # list inside the list
  [1,2,3],
  [4,5,6,],
  [7,8,9,]
]