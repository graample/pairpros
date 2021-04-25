"""ray and tasha's first pair programming exercise :)"""

# defines the phrase with a string in quotations
phrase = "python says "

"""introduces the "say_hello" variable and attaches a set of instructions involving print
and everything after the + operator"""

def say_hello(str):
    print(str + "hello world!")

# combines the two into one function call
say_hello(phrase)

"""This function should add two numbers together."""

# introduces num1 and num2, and defines them with an integer and a float respectively
num1 = 42
num2 = 6.0

# introduces the add_nums() function and involves num1 and num2
def add_nums(num1, num2):

    # add_nums will now add num1 and num2 together
    return num1 + num2 # We didn't print to console

# tells the console to output the instructions in add_nums
print(add_nums(num1, num2))

"""We want to practice writing an if/else conditional."""

# introduces the check_light_color() function and uses a parameter called color to establish the color
def check_light_color(color):
    # if color is set to green, print "The light is green."
    if color == "green":
        print("The light is green.")
        return color

    # else if the color is set to yellow, print "the light is " plus the color.
    elif color == "yellow":
        print("The light is " + color)
        return color

    # else print "The light is " plus any string passed into the function.
    else:
        print("The light is " + color)
        return color

# defines purple_light variable as "purple".
purple_light = "purple"
# defines invalid_light variable as "42" as a string, not an integer.
invalid_light = "42"
# performs the check_light_color function using the purple_light variable as the string.
check_light_color(purple_light)
# performs the check_light_color function using the invalid_light variable as the string.
check_light_color(invalid_light)