from person import Person
from kassa import Kassa
from train import Train

test_man = Person("Ilon Musk", 55)
test_man.earn(25000)
# test_man.pay(13000)
test_man.show()

# test_ticket = Ticket("Алматы", "Сантьяго", 
#                     test_man.name, 
#                     test_man.iin, 
#                     test_man.age)
# test_ticket.show()

kassa = Kassa()
price = kassa.get_price("Алматы", "Сантьяго")
#print(price)

kassa.buy_ticket("Алматы", "Сантьяго", test_man)
if test_man.ticket:
    test_man.ticket.show()

test_man.show()

train = Train("Алматы", "Сантьяго")
train.show()

train.board(test_man)
if test_man.ticket is None:
    print("Билета больше нет")