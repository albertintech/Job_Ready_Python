# Prompting the User
# Create a program that prompts the user to enter a number and then displays the type of the number entered(e.g., complex, integer, or float). For example, if the user enters 6, the output should be int(for integer).

# Balti, Haythem; Weiss, Kimberly A.. Job Ready Python(p. 97). Wiley. Kindle Edition.

# Note: Simple as this exercise sounds, the solution is beyond the scope of what has been taught in the book thus far.

import ast

number = ast.literal_eval(input("Please provide a number and hit enter: "))

print("The data type of your number is as follows:")
print(type(number))
