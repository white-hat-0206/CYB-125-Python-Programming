# check auth logs
# to-do: make more readable 

u = input("Username: ")
n = input("errors ")
# checks errors on accounts in the system

x = int(n)
s = ""

if x > 6:
    s = "LOCK"
else:
    if x > 2:
        if len(u) < 5:
            s = "FLAG"
        else:
            s = "WARN"
    else:
        s = "OK"

print(u, s)
