
list = [21, 23, 31, 38, 39, 42, 47, 68, 95, 98]

def getTotal(list):
    total = 0
    for num in list:
        total += num
    return total


#second function to track even numbers
def countEvens(list):
    count = 0
    for num in list:
        if num % 2 == 0:
            count += 1
    return count

print("Total is", getTotal(list))
print("Even count is", countEvens(list))