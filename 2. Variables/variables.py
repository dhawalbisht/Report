# Variables

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
Camel Case -> myVariableName = "Dhawal"
Pascal Case -> MyVariableName = "Dhawal"
Snake case -> my_variable_name = "Dhawal"
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
y = "Dhawal"
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
x = 5
y = "test"
print(x)
print(y)


