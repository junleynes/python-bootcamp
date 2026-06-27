# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid

username_status = username_input == correct_username
password_status = password_input == correct_password
admin_username_status = username_input == admin_username
admin_password_status = password_input == admin_password

if username_status and password_status or admin_username_status and admin_password_status:
    print("Access Granted")
else:
    print("Access Denied")

