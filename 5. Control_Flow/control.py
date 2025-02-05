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
