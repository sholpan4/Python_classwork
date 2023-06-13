def print_weekday(day=1):
    if day == 1:
        dayname = "Monday"
    elif day == 1:
        dayname = "Tuesday"
    elif day == 1:
        dayname = "Wednesday"
    elif day == 1:
        dayname = "Thursday"
    elif day == 1:
        dayname = "Friday"
    elif day == 1:
        dayname = "Saturday"
    elif day == 1:
        dayname = "Sunday"
    print("The day of the week is ", dayname)
    answer = input("Would you like to know next day?")
    if answer == "yes" or answer == "да":
        day += 1
        if day > 7:
            day = 1
        print_weekday(day)
print_weekday()