# 1. A recipe you are reading states how many grams you need for the ingredient.
# Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
# def gramToOunce(gram):
#    return 28.3495231 * gram

# print(gramToOunce(10))

# 2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
# temp_fahrenheit = float(input())
# def fahrToCentigrade(fahreinheit):
#     return 5 / 9 * (fahreinheit - 32)

# print(fahrToCentigrade(temp_fahrenheit))

# 3. Write a program to solve a classic puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
"""
def solve(numheads, numlegs):
    num_chicks = 0
    num_rabbits = 0
    for i in range(1, numheads + 1):
        num_chicks = i
        num_rabbits = numheads - i
        if(num_chicks * 2 + num_rabbits * 4 == numlegs):
            break
    print(f"Number of rabbits = {num_rabbits} and Number of chicks = {num_chicks}")

solve(35, 94)
"""
# 4. You are given list of numbers separated by spaces.
# Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
"""
from math import sqrt


def filter_prime(nums):
    primes = []
    isPrime = True
    for num in nums:
        for div in range(2, int(sqrt(num))):
            if num % div == 0:
                isPrime = False
                break
        if isPrime is True:
            primes.append(num)
        isPrime = True
    return primes

nums = list(map(int, input().split()))
print(filter_prime(nums))
"""
# 5. Write a function that accepts string from user and print all permutations of that string.
"""
from itertools import permutations

def find_permutations(s):
    char_list = [s[i] for i in range(0, len(s))]
    char_list.sort()
    prms = permutations(char_list)
    for permutation in prms:
        print(permutation)

find_permutations("bcad")
"""

# 6.Write a function that accepts string from user, return a sentence with the words reversed.
# We are ready -> ready are We
"""
def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    print(''.join(words))

s = input()
reverse_sentence(s)
"""

# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""
def has_33(nums):
    isTrue = False
    for i in range(1, len(nums)):
        num = nums[i] * 10 + nums[i-1]
        if num == 33:
            isTrue = True
            break
    return isTrue

nums = list(map(int, input().split()))
print(has_33(nums))
"""
# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def spy_game(nums):
    is007 = False
    for i in range(2, len(nums)):
        agent = nums[i-2] * 100 + nums[i-1] * 10 + nums[i]
        if agent == 7:
            is007 = True
            break
    return is007

nums = list(map(int, input().split()))
print(spy_game(nums))
"""
# 9. Write a function that computes the volume of a sphere given its radius.
"""
from math import pi

def sphere_volume(r):
    return 4/3 * pi * r ** 3

print(sphere_volume(1))
"""
# 10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
"""
def uniques(elements):
    uniques = dict(())
    for elem in elements:
        if(elem not in uniques.keys()):
            uniques[elem] = 0
    return uniques.keys()

nums = list(map(int, input().split()))
print(uniques(nums))
"""
# 11. Write a Python function that checks whether a word or phrase is palindrome or not. 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(s):
    char_list = [s[i] for i in range(len(s))]
    char_list.reverse()
    s1 = ''.join(char_list)
    return s == s1

#print(is_palindrome('madam'))
#print(is_palindrome('apple'))

# 12. Define a function histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:

def histogram(values):
    curr = '*'
    for val in values:
        if val != 0:
            curr = curr * val
        else:
            curr = ''
        print(curr)
        curr = '*'


# histogram([1, 0, 2, 0, 3])

# Write a program able to play the "Guess the number" - game,
# where the number to be guessed is randomly chosen between 1 and 20. 
# This is how it should work when run in a terminal:
"""
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

"""
import random
name = input("Hello! What is your name?")
print("Well, KBTU, I am thinking of a number between 1 and 20.")

guessed_num = random.randint(1, 20)
guess = 0
num_guesses = 0
while guess != guessed_num:
    print("Take a guess")
    guess = int(input())
    num_guesses += 1
    if guess < guessed_num:
        print('Your guess is too low.')
    elif guess > guessed_num:
        print('Your guess is too high')
    else:
        print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
        break

"""
