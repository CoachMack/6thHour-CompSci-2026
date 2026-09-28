#Name: Coach Mack
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
fib_list = [0,1,2,3,5,8,13,21,34]
#2. Sort the list from highest to lowest.
fib_list.sort(reverse=True)
#3. Create an empty list.
emp_list = []
#4. Remove the median number from the first list and add it to the second list.
med_int = fib_list.pop(4)
emp_list.append(med_int)
#5. Remove the first number from the first list and add it to the second list.
first_int = fib_list.pop(0)
emp_list.append(first_int)
#6. Print both lists.
print(fib_list)
print(emp_list)
#7. Add the two numbers in the second list together and print the result.
emp_list_sum = emp_list[1] + emp_list[0] #sum(emp_list) works too!
print(emp_list_sum)
#8. Add the sum from #7 to the first list.
fib_list.append(emp_list_sum)
#9. Sort the first list from lowest to highest and print it.
fib_list.sort()
print(fib_list)