# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class CustomClass:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

cc = CustomClass()
cc.getString()
cc.printString()

# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self, length):
        self.length = length


    def area(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        print(self.length ** 2)
       
shape1 = Shape(1)
sq = Square(2)
shape1.area()
sq.area()

# 3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
class Rectange(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        print(self.length * self.width)


rect = Rectange(2,3)
rect.area()

# 4. Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

p1 = Point(1, 2)
p2 = Point(2, 3)
p1.get_coordinates()
p2.get_coordinates()
print(p1.dist(p2))
p1.move(2, 2)
p1.get_coordinates()

# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def check_balance(self):
        print(f"Balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited. Balance is {self.balance}")


    def withdrawal(self, amount):
        if amount > self.balance:
            print("Withdrawal is unavaliable. Balance is low")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from the deposit. Balance is {self.balance}")

ba1 = Account("Beket")
ba2 = Account("Medeu")

ba1.check_balance()
ba1.withdrawal(1000)
ba1.deposit(1000)
ba1.withdrawal(500)


