#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW4
import math

#1. Print "Hello World!"
print ("Hello World!")
#2. import the 'math' library

#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x = float(input("Give me a decimal"))
y = int(input("Give me an integer"))
#4. Create a variable with the value that is x and y added together.
z = x + y
#5. Print the variable from #4.
print(z)
#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
f = z / 3
#7. Print the variable from #6.
print(f)
#8. Create a variable with the value of the square root of y, then print the result.
sqrt_y = math.sqrt(y)
print(sqrt_y)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
round_x = round(x,1)
print(round_x)
#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
ceil_x = math.ceil(x)
print(ceil_x)
#11. Use the floor function to round x down to the nearest whole number. Print the result.
floor_x = math.floor(x)
print(floor_x)
