#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - For Loops

import time

#These are for loops. They work like while loops but have their own strengths and weaknesses.

#The "range" function in a for loop goes from the first number to the number JUST BEFORE the
#second number. For this, you can do something like "x + 1" or add 1 to the number you intend
#as an easy workaround.
x = 10
for i in range(1, x + 1):
    time.sleep(0.4)
    print(i)

#You can also add a third number to the "range" function to serve as the increment. 3 makes it go
#up by 3 each time, in this example.
for a in range(1, 50, 3):
    time.sleep(0.4)
    print(a)

#It can also count down by using negative numbers. Just make sure to have the big number go first!
for b in range(10, 0, -1):
    time.sleep(0.4)
    print(b)
else:
    print("Merry Unbirthday")

#You can also use for loops to print the values inside of a list, including strings!
fruits = ["kiwi", "strawberry", "pineapple", "cucumber", "lemon"]

for c in fruits:
    time.sleep(0.4)
    print(c)
    if c == "pineapple":
        break

#For loops can also spell out words if you make the "in" range just a single string.
#You can also put an input function in a similar scenario to put whatever word you want spelled out.
for d in input("Give me a word "):
    time.sleep(0.4)
    print(d)

#You can nest loops inside of each other to do multiple combinations of math or other functions.
#Get creative!
adj = ["nasty", "slippery", "tasty"]
animal = ["bird", "tiger", "monkey"]

for e in adj:
    for f in animal:
        print(e, f)

#You can put the "pass" function in an empty loop just to make the error go away while you're still working on it.
for g in []:
    pass
