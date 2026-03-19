# Ian grimm
# CYB 125 Scripting Python
# Week 5 Loop Debug Exercise
# Note: If your program gets stuck in an infinite loop, press CTRL+C to stop the program.

import random

def service_call() -> bool:
    return random.random() < 0.05

# ------------------------------------------------------------
# START HERE 
# 
# Loop #1 - Fix this loop so it prints "Scanning..." exactly 4 times.
# ------------------------------------------------------------

count = 1
while count != 5:
    print("Scanning...: ", str(count))
    count += 1

# ------------------------------------------------------------
# Loop #2 - Fix this so it asks a user to enter a number until they guess the secret number
# ------------------------------------------------------------

guess = 0
secret = 42
while guess != secret:
    guess = int(input("\nChoose a number (1 to 100):"))
print("The secret number was ", str(secret))

# ------------------------------------------------------------
# Loop #3 - Fix the loop so it checks ALL ports in the list (including the last one).
# ------------------------------------------------------------

ports = [22, 80, 443, 3389]
for index in range(0, len(ports)):
    print("Checking port: ", str(ports[index]))


# ------------------------------------------------------------
# Loop #4 - Fix this so each user in the list only gets 2 password attempts.
#         - Keep the nested structure (outer loop over users).
#         - The inner loop should run exactly twice for each user.
# ------------------------------------------------------------

print("\nTwo attempts per user")
users = ["alice", "bob", "charlie"]
for user in users:
    attempt = 0
    print("\nUser: ", user)
    while attempt < 2:
        print(f"  Attempt {attempt + 1} for {user}")
        attempt += 1

# ------------------------------------------------------------
# Loop #5 - Fix the loop so that it retries the service call up to 5 times max and stops early if it succeeds.
#       The "service call" is simulated to succeed randomly (only 5% of the time).
#       If the service call fails 5 times, exit the loop
# ------------------------------------------------------------

def service_call():
    return random.random() < 0.05  # 5% chance of success

retries = 0
while retries < 5:
    if service_call():
        print("Service succeeded!")
        break
    print(f"Service failed... retrying (attempt {retries + 1} of 5)")
    retries += 1
else:
    print("Service failed 5 times, giving up.")
