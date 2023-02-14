from functools import reduce

numbers = [(1, 2, 3), (5, 2), (5, 1, 7, 3, 8)]

for idx, t in enumerate(numbers):
    numbers[idx] = reduce(lambda x, y: x * y, t)

print(numbers)
