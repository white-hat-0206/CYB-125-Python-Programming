# Ian Grimm
# CYB 125 Scripting Python
# Week 7 Functions Debug Exercise

import sys
from datetime import datetime

GLOBAL_ALERT_COUNT = 0

# Prints banner 
def print_banner():
    print("=== mySploit PenTest Reconnaissance Tool ===")
    print("This tool aids in the preparation for a pentest by determining if there are any suspicious ports open on a target ip.\n\n")

# Returns a numeric risk score.
def calculate_risk(port):
    if port == 443:
        score = 70
    elif port == 22:
        score = 80
    elif port == 3389:
        score = 90
    else:
        score = 10
    return score #1 added a return


# Should return True if score > 70, otherwise False.
def is_high_risk(score):
    if score > 70:
        return True #2 changed print into return
    else:
        return False           

# formats a log message with timestamp and warn level
def format_alert_message(ip, port, level="INFO"):
    if level == "WARN":
        message = f"Suspicious service exposure: {ip}:{port}"
    else: 
        message = f"Port open: {ip}:{port}"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"\n[{level}]  [{timestamp}]  {message}"
    return formatted_message #3 changed print to return (again)

# Checks to see if an ip address is formatted properly
def ipv4_format_checks(ip_address):
    parts = ip_address.split(".") #4 changed address to "ip address"
    if len(parts) != 4:
        print("IP format is invalid.\n") #swapped valid and invalid messages and removed valid
        return False #5 return false for invalid
    else:
        return True #6 continue steps for valid

# Increases the global GLOBAL_ALERT_COUNT by 1.
def increment_alerts():
    global GLOBAL_ALERT_COUNT #7 set declare to global
    GLOBAL_ALERT_COUNT = GLOBAL_ALERT_COUNT + 1  

def get_port_from_user():
    while True:
        text = input("Enter a port number (e.g., 22): ")
        try:
            return int(text)
        except ValueError: #8 value error instead of key
            print("Invalid port. Must be a number.\n")

# Prompts user for a port number and returns an int.
def get_ipv4_address_from_user():
    ip=""
    while not ip:
        ip = input("Enter target IP (e.g., 192.168.1.10): ")
        if not ipv4_format_checks(ip):
            ip = ""
        else:
            return ip

# Main program
def main():
    print("=== mySploit PenTest Reconnaissance Tool ===")
    print("This tool aids in the preparation for a pentest by determining if there are any suspicious ports open on a target ip.\n")

    while True:
        try:
            ip = get_ipv4_address_from_user() #9 added function call
            port = get_port_from_user()

            risk = calculate_risk(port)

            if is_high_risk(risk):
                alert = format_alert_message(ip, port, "WARN")
                print(alert)
                increment_alerts()
            else:
                print(format_alert_message(ip, port))
            
            print("\nTotal alerts:", GLOBAL_ALERT_COUNT, "\n")
        except KeyboardInterrupt: #catches ^c to send special message
            sys.exit("\nHappy Hunting!")

if __name__ == "__main__":
    main()