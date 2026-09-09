#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Lists


#This is a list. In essence, it's a variable that has multiple values inside that
#you can pull from any of them without needing to make multiple variables for each
#piece of data. This is useful for cases where you have a lot of the same type of
#"thing", such as names in this example.
robot_santas_list = ["Matthew", "Owen", "Tucker", "Kayleigh", "Eden", "Jacob", "Cody",
                     "Huxley", "Brody", "Nate", "Owyn", "Jerrell", "Misa", "Kinsley",
                     "Raphael", "Bensen", "Malachi"]

#To print the list. You simply name the variable followed by [] with the
#number inside being its "index" location.
#Note that all indexes START AT ZERO. Not one. :)
print(robot_santas_list)
print(robot_santas_list[8], "is NAUGHTY!")
print(robot_santas_list[12], "is NAUGHTY!")
print(f"{robot_santas_list[16]} is NAUGHTY!")

#This is the append function. This allows you to tack on a new value or "object"
#to the end of the list.
robot_santas_list.append(input("Give me a name: "))
print(robot_santas_list)

#This is the remove function. It removes every instance of the value.
robot_santas_list.remove("Owen")
print(robot_santas_list)

#This is the insert function. It works like the append function but
#you can place the object anywhere inside of the list, not just at the end.
robot_santas_list.insert(1, "Owen")
print(robot_santas_list)

#This is the pop function. It lets you remove a specific value based on
#index location. Put the location of the value, not the value itself.
robot_santas_list.pop(6)
robot_santas_list.pop(6)
print(robot_santas_list)

#This is a number list. You can place any kind of object in a list,
#not just strings.
num_list = [4, 1312, 1206, 5, 11, 50689, 37, 17, 16, 84, 21, 2763, 12345, 91, 72, 3000001]
print(num_list)

#You can sort the list from lowest to highest. When you sort a list,
#it permanently changes the order of the list so keep that in mind.
num_list.sort()
print(num_list)

#You can also sort the list from highest to lowest using the
#reverse=True modifier.
num_list.sort(reverse=True)
print(num_list)

#You can do math with the numbers in a list. Simply call their
#index location. Reminder: START AT ZERO.
num_list_subsum = num_list[1] + num_list[2] + num_list[3]
print(num_list_subsum)

#If you need to add them all together, there is a sum function
#that lets you add the contents of a list together.
num_list_sum = sum(num_list)
print(num_list_sum)

#You can find the amount of objects in a list, called the "length",
#using the len function.
num_list_len = len(num_list)
print(num_list_len)

#You can also list different types of objects in the same list.
mixed_list = ["Fred", 10, False]
print(mixed_list)