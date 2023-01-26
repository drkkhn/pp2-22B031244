# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#  A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Get the Length of a Set
# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

#type()
# From Python's perspective, sets are defined as objects with the data type 'set':
print(type(thisset))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Access set items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thisset:
  print(x)

print("banana" in thisset)

# Add items into set
# add() method
thisset.add("orange")
print(thisset)

# To add items from another set into the current set, use the update() method.

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)

# Remove set items
# To remove an item in a set, use the remove(), or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")

print(thisset)

# Remove "apple" by using the discard() method:
thisset.discard("apple")
print(thisset)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset

# print(thisset) Raises NameError because set does not exist

# Loop sets 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join two sets
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1.update(set2)
print(set1)

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
