user_in = input("Enter your age:")

try:
    user_age = int(user_in)
except ValueError:
    user_age = ""

if type(user_age) is int:
    if 0 < user_age < 120:
        message = "Your age is real"
    else:
        message = "Your age unpeal"
else:
    message = "You've entered not number"

print(message)