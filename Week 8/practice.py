import math

def div(a, b):
    return a/b

def main():
    while True:
        input1 = int(input("Enter an integer: "))
        input2 = int(input("Enter an integer: "))

        result = div(input1, input2)
        print("resut: " + str(result))

if __name__ -- "__main__":
    main()