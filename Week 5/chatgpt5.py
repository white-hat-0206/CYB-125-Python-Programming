import sys

for attempt in range(3):
    password = input("Password to launch: ")

    if password == "grimmi006":
        print("Ignition sequence starting:")
        break
    else:
        print("Incorrect password.")

else:
    print("Launch aborted.")
    sys.exit()

for num in range(3, 0, -1):
    print(num, "...")
print("Ignition")