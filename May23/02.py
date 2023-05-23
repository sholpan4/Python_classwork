user_input = input("Сколько сейчас часов?")
hours = int(user_input)
user_input = input("Сколько сейчас минут?")
minutes = int(user_input)
#23 60
hours_remain = 23 - hours
minutes_remain = 60 - minutes

print("Осталось", hours_remain, 
        "ч", minutes_remain, "мин")