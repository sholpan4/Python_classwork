user_in = input("Hours:")
hours = int(user_in)

user_in = input("Minutes:")
minutes = int(user_in)

user_in = input("Seconds:")
seconds = int(user_in)

#23 59 60
hours_remain = 23 - hours
minutes_remain = 59 - minutes
seconds_remain = 60 - seconds

print(hours_remain, ":", minutes_remain, ":", seconds_remain)