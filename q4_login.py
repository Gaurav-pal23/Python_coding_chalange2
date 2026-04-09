####-------question 4: Login Validation
Problem:
Verify username and password.
Code:
Python
username = "admin"
password = "1234"

# Stored credentials
correct_user = "admin"
correct_pass = "1234"

# Validation
if username == correct_user and password == correct_pass:
    print("Login Successful")
else:
    print("Invalid Credentials")
Output:

Login Successful
