"""
"Python has 2 primitive loop commands:

while loops
for loops
"""

# while loop
# In while loop we can execute code until the condition is false
my_list = [x for x in range(10)]
i = 0
while i < len(my_list):
    if i == 0:
        continue # With the continue statement we can stop the current iteration, and continue with the next:
    if i > 5:
        break # With the break statement we can stop the loop even if the while condition is true:
    print(my_list[i])
    i += 1


