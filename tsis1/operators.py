'''
Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators
'''

# Arithmetic operators
print(1 + 2) # addition
print(1 - 2) # substraction
print(2 * 4) # multiplication
print(4 / 2) # division
print(5 % 2) # modulus
print(5 ** 2) # exponential or power
print(5 // 2) # floor or integer division

# Assignment operators
a = 0 # assigning 0 to a
a += 1 # increasing a by one
a -= 1 # decreasing a by one
a *= 2 # multipliying a by 2 and assigning it to a
a /= 2 # dividing a by 2 and assigning the value to a
a %= 2 # modulus a by 2 and assigning it to a
a //= 2 # floor dividing by 2 and assigning back
a **= 3 # finding a power 3 and assigning it to a
# a &= 1 # assigning result of a AND 1 to a
# a |= 1 # assigning result of a OR 1 to a
# a ^= 1 # assigning result of a XOR 1 to a
# a >>= 1 # shifting bits of a to 1 left and assigning back to a
# a <<= 1 # shifting bits of a to 1 right and assigning back to a

# Comparison operators
x = 1
y = 2
print(x == y) # is x eqauls y
print(x != y) # is x not equals to y
print(x > y) # is x greater than y
print(x < y) # is x less than y
print(x >= y) # is x greater or equals to y
print(x <= y) # is x less or equals to y

#Python logical operators
# and &
# or |
# not !
# xor ^

#Python bitwise operators
x = 3
y = 1
print(x & y) # bitwise AND
print(x | y) # bitwise OR
print(x ^ y) # bitwise XOR
print(~x) # bitwise NOT
x >>= 1 # bitwise shift left to 1
print(x) 
x <<= 1 # bitwise shift right to 1
print(x)
