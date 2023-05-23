string = input("enter text:")
user_in = input("how many time repeat:")
repeats = int(user_in)

result = string * repeats
template = "Result: %s"

message = template % result #where & what to show

print(message [3:])