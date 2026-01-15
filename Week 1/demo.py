#we need to type-cast our sting to an integer for the comarison operator >= to work
#for now just think of int() as a function that converts your sring to an integer
grade = int(input("what's your grade ")) 

secretNum = 92

if grade == 92:
    print("target reached")
if grade >= 100: #exit condition - when do you stop your programming?
    print("Beast Mode")
elif grade >= 90: #only runs if the previous condition is false
    print("A Game")
elif grade >= 80: #only runs if the previous condition is false
    print("Beta Ohio")
elif grade >= 70: #only runs if the previous condition is false
    print("Okey Dokey")
elif grade < 70: #only runs if the previous condition is false
    print("Keep Trying")
