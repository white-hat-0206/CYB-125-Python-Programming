# debugger_demo.py

def average(nums):
    total = 0
   
    for i in range(len(nums)):
        total += nums[i]

    avg = total / len(nums)
    return avg


def find_max(numbers):
    max_value = numbers[0]

    for n in numbers:
        if n > max_value:
            max_value = n

    return max_value


def main():

    print("Enter numbers separated by spaces:")

    user_input = input("> ")

    numbers = user_input.split()

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    avg = average(numbers)

    print("Average:", avg)

    max_value = find_max(numbers)

    print("Maximum:", max_value)

    print("\nPrinting numbers:")
    for i in range(len(numbers)):
        print(numbers[i])

    print("\nInverse values:")
    for n in numbers:
        print(1 / (n))


main()