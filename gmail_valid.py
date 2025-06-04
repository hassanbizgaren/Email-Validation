email = input("Enter your email address: ")  # g@g.in
k, j, d = 0, 0, 0  # Initialize all variables
invalid_char = ''  # To store the invalid character if found

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:  # check number of @ in mail (if @ = 1 valid)
            if email[-4] == "." or email[-3] == ".":
                for char in email:
                    if char.isspace():
                        k = 1
                        break
                    elif char.isalpha():
                        if char.isupper():
                            j = 1
                    elif char.isdigit():
                        continue
                    elif char in [".", "_", "-", "@"]:  # Added @ as valid character
                        continue
                    else:
                        d = 1
                        invalid_char = char
                        break
                
                if k == 1:
                    print("Error: Email contains spaces")
                elif j == 1:
                    print("Error: Email contains uppercase letters")
                elif d == 1:
                    print(f"Error: Invalid character '{invalid_char}' found in email")
                    print("Only letters, numbers, dots, underscores, hyphens, and @ are allowed")
                else:
                    print("Email is valid!")
            else:
                print("Error: Check the dot (.) in your email")
        else:
            print("Error: Check the @ symbol in your email")
    else:
        print("Error: Email must start with a letter")
else:
    print("Error: Email must be at least 6 characters long")