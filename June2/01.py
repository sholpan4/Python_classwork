#alliace say = print say("Hello") можно много аллианс следать для принт

def show_manty_ingredients(total_kg):  #(total_kg, portions=99)
    meat    = 0.5 * total_kg
    flour   = 0.2 * total_kg
    carrots = 0.05 * total_kg
    pumpkin = 0.1 * total_kg
    onion   = 0.1 * total_kg
    potato  = 0.1 * total_kg
    template = """ Для %s кг порции мант вам потребуется:  
    - мясо: %.2f кг,
    - мука: %.2f кг,
    - морковь: %.2f кг,
    - тыква: %.2f кг,
    - лук: %.2f кг,
    - кортофель: %.2f кг.
    """
    message = template % (total_kg, meat, flour, carrots, pumpkin, onion, potato)  #убрали portion
    print(message)
    return int(total_kg * 2) #количество порции без добныйх

#show_manty_ingredients(8.5, 6)

user_in = input("Сколько кг мант вам нужно?")
user_kg = float(user_in)

portions = show_manty_ingredients(user_kg)   #(user_kg, 6)
print("Всего получиться порций:", portions)

#PS C:\Users\оразымбетоваш\Desktop\Python\My_classwork_Python> python -i "c:\Users\оразымбетоваш\Desktop\Python\My_classwork_Python\June2\01.py"