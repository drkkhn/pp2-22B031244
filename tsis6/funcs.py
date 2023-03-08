import functools as ft
import re
import time
import math
# Write a Python program with builtin function to multiply all the numbers in a list
def mult_nums():
    num_list = map(int, input().split())
    res = ft.reduce(lambda a, b: a*b, num_list)
    print(res)

def mult_nums1():
    num_list = map(int, input().split())
    res = 1
    for num in num_list:
        res *= num
    print(res)
    

# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_letters():
    inp_str = input()
    lwr_ptrn = re.compile("[a-z]")
    upr_ptrn = re.compile("[A-Z]")
    lwrs = lwr_ptrn.findall(inp_str)
    uprs = upr_ptrn.findall(inp_str)
    print(f"num of lower chars = {len(lwrs)}, num of upper chars = {len(uprs)}")

def count_letters1():
    inp_str = input()
    count_lower = 0
    count_upper = 0
    for i in range(len(inp_str)):
        if inp_str[i].islower():
            count_lower += 1
        elif inp_str[i].isupper():
            count_upper += 1
    print(f"num of lower chars = {count_lower}, num of upper chars = {count_upper}")


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
    print("Task 1")
    mult_nums1()
    print("Task 2")
    count_letters1()

if __name__ == "__main__":
    main() 
