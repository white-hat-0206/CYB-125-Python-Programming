# mySploit Intrusion Detection Module
# Complete Phase 2. Data Processing
# You do not need to modify any code in Phase 1 or Phase 2.

print("""
----------------------------------------------------
             INTRUSION DETECTION MODULE
----------------------------------------------------

Welcome to the mySploit Intrusion Detection Module.

This exercise simulates how an intrusion detection system (IDS)
evaluates security-related events using simple rules and contextual data.

Select an event type to analyze:
  - login: Authentication and access activity
  - file: File system access or modification
  - network: Network traffic and connection behavior

    """)
event_type = input("Enter event type: \n>>> ")

if event_type not in ("login", "file", "network"):
    sys.exit(1)  # exit program on invalid user input

print("""
----------------------------------------------------

Identify the source of the event. Did the event originate
from inside or outside of the network?

Source Options:
  - internal: Originating from within the organization
  - external: Originating from outside the organization

    """)
event_source = input("Enter event source (internal/external):\n>>> ")

if event_source not in ("internal", "external"):
    sys.exit(1)  # exit program on invalid user input

risk = ""  # default

# -------------------------
# LOGIN EVENT TYPE
# -------------------------
if event_type == "login":
    print("""
----------------------------------------------------

Login Event Details:

Enter the username of the account that attempted 
and failed to login:""")

    username = input(">>> ")

    if username == "":
        sys.exit(1)  # invalid username
    else:
        username = username.strip().lower()

    str_attempts = input("\nEnter the number of failed login attempts observed:\n>>> ").strip()
    
    if not str_attempts.isdigit():
        sys.exit(1)  # invalid number
    else:
        attempts = int(str_attempts)

    # PHASE 2. DATA PROCESSING - Write your if / elif / else statements here.
    # Check to see if the user is privileged (admin or root)
    # Check for internal access by a standard user
    # Check for internal access by a privileged user
    # Check for external access by a standard user
    # Check for external access by a privileged user   

# -------------------------
# FILE EVENT TYPE
# -------------------------
elif event_type == "file":
    print("Not implemented") # You do not need to implement this for Programming Assignment #2

# -------------------------
# NETWORK EVENT TYPE
# -------------------------
elif event_type == "network":
    print("Not implemented") # You do not need to implement this for Programming Assignment #2

# PHASE 3. Final output
print("")
print("----------------------------------------------------")
print("RISK ASSESSMENT RESULT")
print("----------------------------------------------------")
print("Risk Level:", risk) # output risk calculated above
