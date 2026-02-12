import sys
maxattempts = 0
password = ""
while password != "grimmi006":
    maxattempts += 1
    if maxattempts == 4:
        print("too many failed attempts, goodbye.")
        sys.exit()
    password = input("Password to launch: ")
    
print("ignition sequence starting:")

num = 3
while num > 0:
    print(num,"...")
    num -= 1
print("Ignition")