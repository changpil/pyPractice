from datetime import datetime
from datetime import timedelta
import time

class Ticket:
    def __init__(self, in_time, perCharge=5):
        self._in_time= in_time
        self._out_time = None
        self.perCharge = perCharge

class CreditCard:
    def __init__(self, cardNumber, expirationdate, securityNumber):
        self.cardNumber = cardNumber
        self.expirationdate = expirationdate
        self.securityNumber = securityNumber

    def charge(self, amount):
        time.sleep(5)
        print(f"Card# {self.cardNumber} is charged ${amount}")

def readCreditCard():
    return CreditCard("12345","10/05","345")

class ParkingLot:
    def __init__(self, num_of_lot):
        self._num_of_lot = num_of_lot
        self._lot = [None for _ in range(num_of_lot)]
        self._num_of_car = 0

    def getTicket_num(self):
        if self._num_of_lot <= self._num_of_car:
            raise ValueError("This parkinglot is full")
        for i in range(self._num_of_lot):
            if self._lot[i] == None:
                return i

    def in_car(self):
        new_num = self.getTicket_num()
        self._lot[new_num] = Ticket(datetime.now())
        self._num_of_car += 1

    def out_car(self, ticket_num):
        _ticket = self._lot[ticket_num]
        _ticket._out_time = datetime.now() + timedelta(minutes=45)
        charge = self.calculate_charge(_ticket)
        card = readCreditCard()
        card.charge(charge)
        self._lot[ticket_num] = None
        self._num_of_car -= 1

    def calculate_charge(self, ticket):
        time_in_seconds =  (ticket._out_time - ticket._in_time).total_seconds()
        time_in_minutes, _ = divmod(time_in_seconds,60)
        payment_cycle, _  = divmod(time_in_minutes, 30)
        return (payment_cycle + 1) * ticket.perCharge


def main():
    p = ParkingLot(5)
    p.in_car()
    p.in_car()
    p.in_car()
    p.out_car(1)
    p.out_car(2)
    from pprint import pprint as pp
    pp(p._lot)

if __name__ == "__main__":
    main()