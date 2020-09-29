#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
a = str(input("username?"))
b = str(input("password?"))
if a == "admin" and b == "12345":
    print ("Access granted")
else:
    print ("Access denied")
