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