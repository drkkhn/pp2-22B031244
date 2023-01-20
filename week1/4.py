from math import ceil

num, var = input().split()
num = int(num)
try:
    var = int(var)
except ValueError:
    print(f"Variable {var} is a string")
    print(var * num)
else:
    print(f"Variable {var} is a digit")
    print(f"{var} / {num} = {ceil(var/num)}")

