# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(thisdict["brand"])

# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
print(type(thisdict))

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "Beket", age = 22, country = "Kazakhstan")
print(thisdict)

# Access dictionary items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

x = thisdict["name"]
print(x)

# There is also a method called get() that will give you the same result:
x = thisdict.get("name")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
print(thisdict.keys())

# Get Values
# The values() method will return a list of all the values in the dictionary.
print(thisdict.values())

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
print(thisdict.items())

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
print("name" in thisdict)
print("class" in thisdict)

# Change Values
# You can change the value of a specific item by referring to its key name:

thisdict = {
  "brand": "Hyundai",
  "model": "Sonata",
  "year": 2010
}
print(thisdict['year'])
thisdict["year"] = 2022
print(thisdict['year'])

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict.update({"model": "Grandeur"})
print(thisdict)

# Adding Dictionary Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"] = "white"
print(thisdict)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict.update({'engine_volume': 2.5})
print(thisdict)

# Removing Items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:
thisdict.pop('color')
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:

del thisdict['year']
print(thisdict)

# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
thisdict = {
  "brand": "Hyundai",
  "model": "Sonata",
  "year": 2010
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)


# Loop through both keys and values, by using the items() method:
for keys, values in thisdict.items():
    print(keys, values)

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().

dict_copy = thisdict.copy()
print(dict_copy)

# Another way to make a copy is to use the built-in function dict().
dict_copy1 = dict(thisdict)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

uni_dict = {
    "uni1": {
        "name": "KBTU",
        "rank": 1
    },
     "uni2": {
        "name": "SDU",
        "rank": 2
    },
     "uni3": {
        "name": "IITU",
        "rank": 3
    }
}
print(uni_dict)

# Or, if you want to add three dictionaries into a new dictionary:

uni1 = {
        "name": "KBTU",
        "rank": 1
}
uni2 = {
        "name": "SDU",
        "rank": 2

}
uni3 = {
    "name": "IITU",
    "rank": 3

}
uni_dict1 = {
    "uni1": uni1,
    "uni2": uni2,
    "uni3": uni3
}

print(uni_dict1)
