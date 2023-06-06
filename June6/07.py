import random
def get_random_int(min, max):
    result = random.random() * (max - min) + min
    return int(result)

def game(my_random, min, max):
    user_in = input("Guess the number from %s tll %s:" % (min, max))
    try:
        num = int(user_in)
    except ValueError:
        print("Enter only number!")
        game(my_random, min, max)
    else:
        if my_random > num:
            print("Take bigger")
            game(my_random, min, max)
        elif my_random < num:
            print("Take smaller")
            game(my_random, min, max)
        else:
            print("Congratulation! %d" % my_random)
            return

num = get_random_int(0, 20)
game(num, 0, 20)  #загаданное число будет работать если передать эти цифры в качестве аргумента в функцию