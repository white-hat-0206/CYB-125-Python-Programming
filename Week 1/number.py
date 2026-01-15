# import the random library so we can use its functions
import random

# generate a random number between 1 and 10
num = random.randint(1, 999999)
remainder = num % 2

# any number divisible by 2 and even will have a remainder of 0
# any number not divisible by 2 is odd and will have a remainder of 1

# the statement (rmainder == 1) resolves to TRUE (1) or FALSE (0) so this statement is redundant
# we can simplify to just if remainder because it willresolve to either 1 or 0 (based on our num % 2 logic above)
if remainder:
    print("number is even")
else:
    print("number is odd")

print("the number is", num)