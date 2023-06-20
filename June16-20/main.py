from person import Person
from kassa import Kassa
from train import Train

if __name__ == "__main__":

    print("Главная программа", __name__)

    test_man = Person("Ilon Musk", 55)
    test_man.earn(250000)
    # test_man.pay(13000)
    test_man.show()

    # test_ticket = Ticket("Алматы", "Сантьяго", 
    #                     test_man.name, 
    #                     test_man.iin, 
    #                     test_man.age)
    # test_ticket.show()

    almaty1 = Kassa()
    price = almaty1.get_price("Алматы", "Сантьяго")
    #print(price)

    almaty1.buy_ticket("Алматы", "Сантьяго", test_man)
    # if test_man.ticket:
    #     test_man.ticket.show()
    almaty1.buy_ticket("Алматы", "Ош", test_man)
    almaty1.buy_ticket("Ош", "Бишкек", test_man)
    almaty1.buy_ticket("Земля", "Марс", test_man)


    test_man.show()

    train = Train(almaty1,"Алматы", "Сантьяго")
    train.show()

    print(almaty1.tickets)
    train.board(test_man)
    print(almaty1.tickets)

    

    # train.board(test_man)
    # if test_man.ticket is None:
    #     print("Билета больше нет")