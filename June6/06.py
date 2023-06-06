def game(my_random):
    user_in = input("Guess the number from 0 tll 100:")

    try:
        num = int(user_in)
    except ValueError:
        print("Enter only number!")
        game(my_random)
    else:
        if my_random > num:
            print("Take bigger")
            game(my_random)
        elif my_random < num:
            print("Take smaller")
            game(my_random)
        else:
            print("Congratulation! %d" % my_random)
            return

#num = get_random_int(0, 100) game(num)
game(40)