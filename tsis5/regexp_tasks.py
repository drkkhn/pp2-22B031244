import re
# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

pattern1 = re.compile("ab*")
print(pattern1.search("fdskfldkflddsdsab"))

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
pattern2 = re.compile("ab{2,3}")
print(pattern2.search("gjdfkabbbbfkkliu"))
# Write a Python program to find sequences of lowercase letters joined with a underscore.
pattern3 = re.compile("[a-z]+\_")
print(pattern3.findall("fdsfd_ fdjskfjdsk_ fdsf4ds_"))
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
pattern4 = re.compile("[A-Z]{1}[a-z]+")
print(pattern4.findall("Ffdsf GGfgrhr ImknkJtr"))
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
pattern5 = re.compile("a.+b\Z")
print(pattern5.search("kktngtag423b"))
print(pattern5.search("fjdjgfdb"))
print(pattern5.search("fdifafgnjgr3"))
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
pattern6 = re.compile("[ ,.]")
text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
print(pattern6.sub(":", text))
# Write a python program to convert snake case string to camel case string.

def snakeToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for word in words:
        camelCase+=word.capitalize()
    return camelCase

print(snakeToCamel("hello_world_wordle"))


# Write a Python program to split a string at uppercase letters.
def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:  
            res += " " + word
        else:
            res += word
    return res

print(modify("OneTwoThree"))

# Write a Python program to insert spaces between words starting with capital letters.
def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res

print(spaces("HelloWordlOneMoreTime"))
# Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res

print(camel_to_snake("SnakeCaseVar"))
