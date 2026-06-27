# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
correct_credentials = None


#if username_input == correct_username and password_input == correct_password:
#    print("Access Granted")
#else:
#    print("Access Denied")

username_status = username_input == correct_username
password_status = password_input == correct_password

if username_status and password_status:
    print("Access Granted")
else:
    print("Access Denied")