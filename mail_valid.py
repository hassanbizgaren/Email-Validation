# RegeX Methode 
import re # regular expression matching operations
email_condition = r"^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
user_email = input("Enter your email address: ")  

if re.match(email_condition, user_email):
    print("Email is valid!")
else:
    print("Error: Invalid email format")
    print("Email must start with a letter, contain only letters, numbers, '.', '_', '-', and '@'.")
    