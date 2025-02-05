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