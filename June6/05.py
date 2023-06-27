import random


def get_random_int(min, max):
    result = random.random() * (max - min) + min

    return int(result)

def game():
    user_in = input("Guess the number from 0 tll 100:")

    try:
        num = int(user_in)
    except ValueError:
        print("Enter only number!")
        game()
    else:
        if my_random > num:
            print("Take bigger")
            game()
        elif my_random < num:
            print("Take smaller")
            game()
        else:
            print("Congratulation! %d" % my_random)
            return

my_random = get_random_int (0, 100)
game()