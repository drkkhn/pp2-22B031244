# assigning string to a variable
s1 = "Hello"
print(type(s1))
# multiline strings
multi_string1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

multi_string2 = '''
This is the multiline string
that can contain multiple lines of text
in a single string variable 
'''

# String as an array
# Strings are arrays or lists of characters, thus particular character in a string can be accessed using its index
my_str = "Seoul National university"
ch1 = my_str[0]
ch2 = my_str[-1]

print(ch1, ch2)

# Looping through a string
#for i in range(len(my_str)):
#    print(my_str[i])

#for ch in my_str:
#    print(ch)

# Length of string
print(len("Hello World"));

# Check existence of a substring in a string
if "Seoul" in my_str:
    print("Yes")
else:
    print("No")

if "Private" not in my_str:
    print("national")
    
else:
    print("private")

# slicing strings
"""You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string"""

print(my_str[:5])
print(my_str[6:14])
print(my_str[15:])
print(my_str[-5:-2:-1])

# Modifying strings
a = "Kendrik Lamar"
print(a.upper()) # string to uppercase
print(a.lower()) # string to lowercaes
print(a.strip()) # remove whitespace from left and right
print(a.replace('K', 'G')) # replace certain char or string
print(a.split(' ')) # split string into list of strings through whitespaces

# Concatenate strings
name = "Beket"
surname = "Barlykov"
fullname = surname + " " + name
print(fullname)

