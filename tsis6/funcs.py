import functools as ft
import re
import time
import math
# Write a Python program with builtin function to multiply all the numbers in a list
def multNums():
    num_list = map(int, input().split())
    res = ft.reduce(lambda a, b: a*b, num_list)
    print(res)

# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def countLetters():
    inp_str = input()
    lwr_ptrn = re.compile("[a-z]")
    upr_ptrn = re.compile("[A-Z]")
    lwrs = lwr_ptrn.findall(inp_str)
    uprs = upr_ptrn.findall(inp_str)
    print(f"num of lower chars = {len(lwrs)}, num of upper chars = {len(uprs)}")

# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def isPalindrome(s):
    if s == str.join('',list(reversed(s))):
        print("Is palindrome")
    else:
        print("Not palindrome")

# Write a Python program that invoke square root function after specific milliseconds.
def sqrtDelayed(n, ms):
    print(time.time())
    time.sleep(ms/1000)
    print(f"Square root of {n} after {ms} milliseconds is {math.sqrt(n)}")
    print(time.time())

# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def isAllTrue(inp_tuple):
    return all(inp_tuple)

def main():
    true_t = (2, "wordle", True)
    false_t = (0, "wow", True)
    print(isAllTrue(true_t))
    print(isAllTrue(false_t))


if __name__ == "__main__":
    main() 
