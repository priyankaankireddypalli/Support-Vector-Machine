# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:17:13 2021

@author: WIN10
"""


print("hello")


x = 5
y = "priya"
x
y


#python variables are case sensitive


#unpacking collections - assigniong values to a variables from a list / tupple.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#taking input from user and printing it
name = input("eneter the user name:")
print("name is " + name)

x = "hi"
y = "priya"
z = x + y
print(z)




#global and local 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# use keyword global to make it global within a func
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



x = 5
y = 10.7
z = -5j
cx = float(x)

# note: You cannot convert complex numbers into another number type

# random number

import random
print(random.randrange(1,10))


#strings
#accessing a particular letter at position 1
x = "hello, world!"
print(x[1])

#to traverse the entire string
for i in x:
    print(i)
    
#to find length
print(len(x))

#check string
#To check if a certain phrase or character is present in a string, we can use the keyword in
txt = "The best things in life are free!"
print("free" in txt)


if "free" in txt:
    print("free is present")
    
x = " Hello, world! "





a = "Hello"
b = "World"
c = a + b
print(c)




a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
print("My name is John, and I am {}" .format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#escape char
txt = "We are the so-called \"Vikings\" from the north."
x = "We are the so-called \\Vikings\\from the north."



#lists

list1 = ["apple", "banana", 28]

#another method to create list
list2 = list(("apple","banana","cherry"))
print(list2)
print(list1)
print(len(list1))
print(type(list1))
print(list1[1])
print(list1[-1])
#range of indexes
print(list1[:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
print("cherry" in list2)
#change items of list
#note : If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#note : If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
list1[2] = "cherry"
print(list1)
list1[1:3] = ["blackcurrent", "watermelon"]
print(list1)
list1[1:2] = ["blackcurrent", "watermelon"]
list1
list2[1:3] = ["blackcureent"]

#To insert a new list item, without replacing any of the existing values, we can use the insert
#The insert() method inserts an item at the specified index:
thislist.insert(2, "watermelon")

#append - end of the list append() method
thislist.append("orange")

#extend

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print(type(thislist))
# The remove() method removes the specified item.
thislist.remove("banana")
thislist

#The pop() method removes the specified index.



thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print(thislist.pop()) #Remove the last item:
    
#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


del thislist #delets the entire list

tropical.clear() #clears the content
tropical


#loop lists
# for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
    
#looping through index numbers
#Use the range() and len() functions to create a suitable iterable
# for
for x in range(len(thislist)):
    print(thislist[x])



#while

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  
[print(x) for x in thislist]


thislist = ["apple", "banana", "cherry"]
found = []
for x in thislist:
    if x.startswith('a'):
        found.append(x)
        
print(found)
        
        
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# syntax for list comprehension
# newlist = [expression for item in iterable if condition == True]
list2=[x for x in fruits if "a" in x]
list2


list3 = [i for i in fruits if i != "apple"]
list3


[print(i) for i in range(10)]
newlist = [x for x in range(10)]
newlist

newlist = [x for x in range(10) if x < 5]



newlist = [x.upper() for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]


#sort
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#custom sort function
#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)#Sort the list based on how close the number is to 50:
print(thislist)


#Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() # therefore, key = thislist.lower
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower).lower
print(thislist)


#reverse
#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#therefore, copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#join two lists
# 1) + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]


# 2) appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list3 = list1 + list2
print(list3)
# append ( list within list) - thats why traverse and append each element
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.append(list2)

print(list1)


# extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)

print(list1)


#TUPLE
mytuple = ("apple", "banana", "cherry")
print(mytuple)


#create a tuple with one item
#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = tuple(("apple", "banana", "cherry"))
#Access Tuple Items
print(mytuple[1])
print(mytuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])
print("apple" in thistuple)


#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
thislist = list(thistuple)

# change value of a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#add element to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# remove item from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists


#Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list
#Assign the rest of the values as a list called "red":
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, tropic, *red) = fruits

print(green)
print(tropic)
print(red)

#ex - 2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# LOOPS through tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Numbers
for i in range(len(thistuple)):
    print(thistuple[i])
    
#while loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

#join two tuples
# 1) + oper
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


#Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


#sets
thisset = {"apple", "banana", "cherry"}
thisset


thisset = set(("apple", "banana", "cherry"))
type(thisset)


for x in thisset:
    print(x)
for x in thisset:
    if "banana" in x:
        print("present")
print("banana" in thisset)
#Add Items
To add one item to a set use the add() method.
thisset.add("orange")
#Add Sets
#To add items from another set into the current set, use the update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
thisset
#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)#

#Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#The clear() method empties the set:

thisset.clear()
thisset

#The del keyword will delete the set completely:
    
del thisset

#LOOP

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
    
#Join Two Sets
#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

set1 = {"a","b","c"}
set2 = {"1","2","3"}

set3 = set1.union(set2)
set3

set1.update(set2)
set1

#The intersection_update() method will keep only the items that are present in both sets.
set1 = {"a","b","c","d"}
set2 = {"d","1","a","2"}

set1.intersection_update(set2)
set1
#The intersection() method will return a new set, that only contains the items that are present in both sets.
set3 = set1.intersection(set2)
set3


#Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


#Dictionary

thisdict = {"name" : "priya", "age" : 28}
thisdict
type(thisdict)
print(thisdict["name"])
x = thisdict.get("model") # get() method
y = thisdict.keys() #The keys() method will return a list of all the keys in the dictionary.
y
type(y)

#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


#String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#he values() method will return a list of all the values in the dictionary.
y = thisdict.values()
y
#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#Get a list of the key:value pairs
#************The items() method will return each item in a dictionary, as tuples in a list
x = thisdict.items()

#Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
##[('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]


#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
for x in car:
    if "model" in x:
        print("yes")
car["year"]=2018
car
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
car.update({"color":"black"})

#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
car["color"]="black"  
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added. 
car.update({"country":"usa"})
# remove items
#The pop() method removes the item with the specified key name:
x = car.pop("country")
x
#The del keyword removes the item with the specified key name:
del car["year"]   
del car #The del keyword can also delete the dictionary completely:
#The clear() method empties the dictionary:
thisdict
thisdict.clear()

#Loop Through a Dictionary

#print the keys one by one
for x in car:
    print(x)
#print values one by one:
for x in car:
    print(car[x])
#You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)
#Example
#You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)
#Example
#Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)


#Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
x = thisdict.copy()
#Another way to make a copy is to use the built-in function dict().
x = dict(thisdict)
#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
#Create a dictionary that contain three dictionaries:
nestmydict = {
    "child1":{"name":"priya","year": 1997},
    "child2":{"name":"gouthu","year":1995}
    
   }

#o/p-{'child1': {'name': 'priya', 'year': 1997},
#'child2': {'name': 'gouthu', 'year': 1995}}

#Create a dictionary that contain three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}




#if 
a = 100
b = 20
if a>b:
    print(a)

#Elif
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 32
b = 32
if a>b:
    print(a)
elif a==b:
    print("equal")
    
#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 100
b = 20
if a<b:
    print(a)
else : #You can also have an else without the elif:
    print(b)
    
    
    
    
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
#Short Hand If
if a>b: print(" a is greater")

#Ternary Operators, or Conditional Expressions.
#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")


#multiple else 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
a = 100
b = 20
c = 150
if a>b and c>a:
    print("both conditions are true")
#The or keyword is a logical operator, and is used to combine conditional statements:
a = 100
b = 20
c = 150
if b>a or b<c:
    print("atleast one condition is true")
#Nested If
#You can have if statements inside if statements, this is called nested if statements.
x = 24
if x>10:
    print("above 10")
    if x>20:
        print("above 20")
    else:
        print("less than 20")
#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.:
if x==24:
    pass
#****************************    
a =100
b = 20
if a>b:
    print("hello world")

if a>b:
    print("yes")
else:
    print("no")
    
#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i<6:
    print(i)
    i=i+1
    
    
#break : With the break statement we can stop the loop even if the while condition is true:
i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i = i+1
    
#The continue Statement
#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i<6:
    i +=1
    if i == 3:
       continue
    print(i)
#else statement : With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
# for loops
Print each fruit in a fruit list:

    , "cherry"]
for x in fruits:
  print(x)
#Looping Through a String

for x in "banana":
  print(x)
  
#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:

#Exit the loop when x is "banana":    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

    
#Exit the loop when x is "banana", but this time the break comes before the print:
for x in fruits:
    if x == "banana":
        break
    print(x)
    
#The continue Statement
#do not print banana
for x in fruits:
    if x == "banana":
        continue
    print(x)
    
#The range() Function
for i in range(6):
    print(i)
#Using the start parameter:
for i in range(1,6):
    print(i)
#Increment the sequence with 3 (default is 1):
for i in range(1,31,3):
    print(i)
#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:#Note: The else block will NOT be executed if the loop is stopped by a break statement.
  print("Finally finished!")


for i in range(6):
    if i == 3:
        break
    print(i)
else:
    print("finish")
    
#Nested Loops
#The "inner loop" will be executed one time for each iteration of the "outer loop":
#Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
        
#The pass Statement
for x in [0, 1, 2]:
  pass


#Python Functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#Creating a Function
def my_function():
    print("hello from my function")
    
my_function() #calling a function


def my_function(fname):
    print("good evening " + fname)
my_function("priya")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids): #This way the function will receive a tuple of arguments
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid): #This way the function will receive a dictionary of arguments
  print("His last name is " + kid["lname"])
  
  
  
#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

my_function(fname = "Tobias", lname = "Refsnes")


#Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement
def my_none():
    pass

#Recursion
#Python also accepts function recursion, which means a defined function can call itself.
# note : The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



#lambda function
#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.
# syntax - lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.

#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
 return lambda a : a * n
#Use that function definition to make a function that always doubles the number you send in:


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)
      
      
      