#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Python Math

#Sometimes Python doesn't have exactly what we need built-in. Luckily, there are things called
#libraries that are made by great programmers that add cool functions to Python so that we don't
#have to reinvent the wheel.
import math

#Let's create two variables, using x and y to make things quicker, and have them ask for user
#input for two different numbers.
x = int(input("Give me a number: "))
y = int(input("Give me another number: "))

#Here's the correct symbols to use for mathematical operations in python:

#Addition
int_sum = x + y
print(int_sum)

#Subtraction
print(x - y)

#Multiplication
print(x * y)

#Exponent
print(x ** y)

#Division
print(x / y)

#Modulo
print(x % y)

#Square Root
print(math.sqrt(x))

#Absolute Value
print(abs(y))

#You can also round using different functions.

#Round rounds up or down, same as you would in math
print(round(3.1415926))

#You can also specify to what decimal point it rounds to
print(round(3.1415926, 2))

#Ceiling, or ceil, always rounds up.
print(math.ceil(3.14))

#Floor always rounds down.
print(math.floor(3.99998))

#And of course, we can't forget pi
print(math.pi)