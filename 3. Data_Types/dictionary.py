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
