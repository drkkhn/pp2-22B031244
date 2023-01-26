# Python arrays
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# What is an Array?
'''
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.
'''
# Access the Elements of an Array
# You refer to an array element by referring to the index number.
print(cars[0])

# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
print(len(cars))

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
for x in cars:
  print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array.
cars.append("Honda")

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
cars.pop(1)

#You can also use the remove() method to remove an element from the array.
cars.remove("Volvo")




