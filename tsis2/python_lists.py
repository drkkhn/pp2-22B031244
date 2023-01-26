# Python Lists
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

my_list = [1, 2, 3]
print(my_list)

'''
List Items

List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value
'''
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List length
# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types
# List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
print(type(list1))

# the list() constructor
# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Accessing list items
# List items are indexed and you can access them by referring to the index number:
print(thislist[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc
print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# vBy leaving out the start value, the range will start at the first item:
print(thislist[:4])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
print(thislist[-4:-1])

#Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value
# To change the value of a specific item, refer to the index number:
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:
thislist.insert(2, "watermelon")
print(thislist)
# To append elements from another list to the current list, use the extend() method.
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove List Items
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
# del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
# del thislist

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist.clear()
print(thislist)

# Looping through the list
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop
#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
[print(x) for x in thislist]

# List Comprehension
my_list = [x for x in range(1, 11)]
print(my_list)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_upper = [x.upper() for x in fruits]
print(fruits_upper)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#Sort lists
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
num_list = [1, 3, 7, 2, 4]
num_list.sort()
print(num_list)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
num_list.sort(reverse=True)
print(num_list)

#Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort
# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
# There are ways to make a copy, one way is to use the built-in List method copy().

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


