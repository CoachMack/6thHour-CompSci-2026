#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three values that each randomly generate a number between 1 and 100
num_100_list = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]
#3. Print the list.
print(num_100_list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if num_100_list[0] >= num_100_list[1] and num_100_list[0] >= num_100_list[2]:
    print(f"{num_100_list[0]} is the largest number.")
    num = num_100_list[0]
elif num_100_list[1] >= num_100_list[0] and num_100_list[1] >= num_100_list[2]:
    print(f"{num_100_list[1]} is the largest number.")
    num = num_100_list[1]
elif num_100_list[2] >= num_100_list[0] and num_100_list[2] >= num_100_list[1]:
    print(f"{num_100_list[2]} is the largest number.")
    num = num_100_list[2]


#5. Tie the result (the largest number) from #4 to a variable called "num".
#DONE

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3")
    else:
        print(f"{num} is divisible by 2 but not 3")
else:
    if num % 3 == 0:
        print(f"{num} is divisible by 3 but not 2")
    else:
        print(f"{num} is divisible by neither")