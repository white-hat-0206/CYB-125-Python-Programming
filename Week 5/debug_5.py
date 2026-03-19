import random

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



