for j in range(1, 4):
    password = input("password attempt #" + str(j) + ": ")
    if password == "FIREINTHEHOLE":
        for k in range(3, 0, -1):
            print(k,"...")
        print("ignition")
        break
    