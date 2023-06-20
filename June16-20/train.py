from random import randint

class Train:
    source = ""
    destination = ""
    number = 0
    kassa = None

    def __init__(self, kassa, source, destination):
        self.source = source
        self.destination = destination
        self.number = randint(10000, 99999)
        self.kassa = kassa
        kassa.register_train(self)

    def board(self, person):
        ticket = self.kassa.get_ticket(person.iin, self.source, self.destination)
        if ticket:         
            message = "Добро пожаловать %s, ваш поезд №%s прибыл, от %s до %s." % (person.name, 
                                                        self.number, self.source, self.destination)
            print(message)
            self.kassa.delete_ticket(ticket)
        # if person.ticket:
        #     if self.source == person.ticket.source and self.destination == person.ticket.destination:
        #         message = "Добро пожаловать %s, ваш поезд №%s прибыл, от %s до %s." % (person.name, 
        #                                                 self.number, self.source, self.destination)
            # print(message)
            #     person.ticket = None
            # else:
            #     print("Неправильный билет")
        else:
            print("Нет билета")
    
    def show(self):
        message = "Поезд №%s, от  станции %s до станции %s" % (self.number, self.source, self.destination)
        print(message)

print("Это поезд", __name__)