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
