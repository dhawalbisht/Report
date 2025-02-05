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

