# Syntax
print("Hello, World!")

"""
Hello sir,
this is python
basics task.
"""
print("Hello,Dhawal")

# Indentation
if 5 > 2:
  print("True")

# Variables
x = 5
y = "test"
print(x)
print(y)


x = 10       # x is of type int
x = "Dhawal" # x is now of type str
print(x)


# Casting
a = str(15)    # x will be '15'
b = int(15)    # y will be 15
c = float(15)  # z will be 15.0

# Geting  the Data Types
x = 5
y = "abcd"
print(type(x))
print(type(y))

# Case-Sensitive
a = 4
A = "Dhawal"
print(a)
print(A)


# Variable Names
'''
Rules for Python variables:
> A variable name must start with a letter or the underscore character.
> A variable name cannot start with a number.
> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
> Variable names are case-sensitive (age, Age and AGE are three different variables)
> A variable name cannot be any of the Python keywords.
'''
# Examples
myvar = "Dhawal"
my_var = "Dhawal"
_my_var = "Dhawal"
myVar = "Dhawal"
MYVAR = "Dhawal"
myvar2 = "Dhawal"

'''
Camel Case -> myVariableName = "John"
Pascal Case -> MyVariableName = "John"
Snake case -> my_variable_name = "John"
'''

# Assign Multiple Values
x, y, z = "Dhawal", "Dev", "Manpreet"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Test"
print(x)
print(y)
print(z)

# Unpack a list
cars = ["car1", "car1", "car2"]
x, y, z = cars
print(x)
print(y)
print(z)

# Output multiple variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # or print(x + y + z)

x = 5
y = "John"
# print(x + y)  # give an error as they are of different data types
print(x,y)

# Global Variables
x = "Dhawal"

def myfunc():
  print("Hi", x)
myfunc()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)


# Global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Data types

x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType



# Type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
import random
print(random.randrange(1, 100))


# Python Casting
x = int(2.8) # 2
x = float(2)   # 2.0
x = str(2)    # '2'


# Python Strings
a = "Hello"
print(a)

a = '''
hello my 
name is 
Dhawal
Bisht'''
print(a)

# Looping Through a String
for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

# Check String
a = "The best things in life are free!"
print("free" in a)

# Slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']


# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)


# Format - Strings/F-Strings : we can't combine strings and numbers with just '+'
age = 21
info = f"My name is Dhawal, I am {age}"
print(info)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Characters : '\'
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

def myFunction() :
  return True

print(myFunction())


# Lists
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))

list1 = ["abc", 34, True, 40, "male"]
print(list1[-1])
list1[1] = "strawberry"

# Insert new item
list1.insert(0, "xyz")

# Append : to add item at the end

list1.append("car")
print(list1)

# Extend : to append elements from another list to the current list
l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']
l1.extend(l2)
print(l1)

# Remove Specified Item
l1.remove('a')
print(l1)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# Clear the List
thislist.clear()


# Loop Through a List
thislist = ["aryan", "dhawal", "dev"]
for x in thislist:
  print(x)


# Looping Using List Comprehension/Short hand for loop
thislist = ["aryan", "dhawal", "dev"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# Tuples
tup = ('a', 'b', 'c', 'd')
print(tup)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

print(tuple1[1])

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print(tuple3.count(False))



# Sets : Set items are unchangeable, meaning that we cannot change the items after the set has been created.

myset = {"apple", "banana", "cherry"}
print(myset)


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) # True and 1 is considered the same value
print(len(thisset))


# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {'a'}

# Intersection
set3 = set1.intersection(set2)
print(set3)


# Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

x = thisdict["model"]
print(x)

print(thisdict.keys())
print(thisdict.values())


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

thisdict.update({"year": 2020})

thisdict["color"] = "red"
thisdict.pop("model")
print(thisdict)

for x in thisdict:
  print(x)


# If ... Else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# The pass Statement
a = 33
b = 200

if b > a:
  pass

# While Loops
i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

# Functions
def first_function():
  print("Hello from func.")
first_function()

def my_function(fname):
  print(fname + " QL")

my_function("Dhawal")
my_function("Dev")
my_function("Man")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Dhawal", "Bisht")

# Arbitrary Arguments, *args : If we do not know how many arguments that will be passed into your function
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("a", "b", "c")


# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# File Handling
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''


# Open a File on the Server
f = open("test.txt")
print(f.read())

f = open("test.txt")
print(f.read(5))  #read some part of file


f = open("test.txt", "r")
print(f.readline())

f = open("test.txt", "r")
for x in f:
  print(x)


# Close the file when you are finished 

f = open("test.txt", "r")
print(f.readline())
f.close()

# File Write
f = open("test.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())

# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Delete a File
import os
os.remove("test.txt")



# Check if file exists, then delete it:

import os
if os.path.exists("test.txt"):
  os.remove("test.txt")
else:
  print("The file does not exist")




