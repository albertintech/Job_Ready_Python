import math
import ast

number = ast.literal_eval(input("Please provide a decimal number and I will truncate it: "))

print(f"You entered {number}. The trancated value is:")
print(math.trunc(number))
