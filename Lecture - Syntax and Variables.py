#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Syntax and Variables

#This is a print function. It prints out exactly what is inside the parentheses.
print("Hello 5th Hour Class")

#You can have multiple types of values inside of a print function when separated by a comma.
print("The 5th Hour Class has:", 17, "students.")

#You can sometimes use a plus sign (+) to "add" together values but they need to be of the same type.
print("The 5th Hour Class has:" + "17" + "students.")

#This is a variable. Variables are where you can store specific values to use for things. Typically,
#variables store one of three types of values: numbers, words, and boolean. Every variable is read
#by the program as variable_name = "variable value" so keep that in mind. The name ALWAYS comes first.
class_greetings = "Hello 5th hour class. How are you today?"

#You can print the value of variables by putting the name of the variable inside of a print statement.
print(class_greetings)

#You can name a variable whatever you want as long as it doesn't start with a number and doesn't contain spaces.
#To get past the second issue, there's two ways name a variable: underscores and camel case. Use whichever you prefer.
this_is_under_score = "This is Under Score"

thisIsCamelCase = "This is Camel Case"



#These are the different types of values you can assign to a variable.

#The three values are: strings, numbers, and boolean.
string_ex = "This is a string."
number_ex = 12
float_ex = 6.77777
bool_ex = False


#This is an input function. Input functions will pause and wait for the user to enter their own data
#before continuing. Inside the parentheses, you can add something to specify what you want the user to type.
#Whatever the user types will be the value of that variable. Remember, an input function NEEDS to be equal
#to a variable to store the value.
student_name = input("What is your name? ")

print(student_name)


#You can also put functions inside of other functions for various reasons. In this example, we put an input
#function inside of an int function so that it will only accept integers as a valid user response.
#If the user were to put a string (or word) as the response, the code would throw an error.
number_printing = int(input("Give me a whole number between 1 and 10: "))

print(number_printing)


#Python reads code line by line starting at line 1. You can manually change the value of a
#variable later on for whatever reason.
class_greetings = "I have changed the value of class_greetings."

print(class_greetings)






