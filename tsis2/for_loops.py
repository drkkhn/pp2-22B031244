# For loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

uni_list = ['KBTU', 'SDU', 'NU']

for i, uni in enumerate(uni_list):
    print(f'{i} {uni}')

# Loopng through a stirng
# Even strings are iterable objects, they contain a sequence of characters:

for x in "Kazakh-British Technical University":
    if x == ' ':
        break # With the break statement we can stop the loop before it has looped through all the items:
    if x == 't':
        continue # With the continue statement we can stop the current iteration of the loop, and continue with the next:
    print(x)


'''
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified numbe
'''
s1 = 'python'
for i in range(len(s1)):
    print(s1[i])

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for i in range(1, 11):
    print(i)
else:
    print('Finished counting to ten')


#
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjs:
  for fruit in fruits:
    print(adj + ' ' + fruit)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
