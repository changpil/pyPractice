class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return (range(1,23), "ABCDE")



class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return (range(1,56), "ABCDEFGH")


class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <=9999):
            raise ValueError(f"Invalid route number '{number}'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        # seat '12C' or '21F'
        row, letter = self._parse_seat(seat)
        self._seating[row][letter] = passenger

    def print_seats(self):
        from pprint import pprint as pp
        pp(self._seating)

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self.seating[from_row][from_letter] is None:
            raise ValueError(f"No passengerto reloacate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self.seating[to_row][to_letter] is not None:
            raise ValueError(f"Saet{to_seat} already occupied")

        self.seating[to_row][to_letter] = self._seating[from_row][to_row]
        self._seating[from_row][to_row] = None

    def num_avilable_seats(self):
        return sum(sum(1 for s in row.vlaues() if s is None) for row in self._seating if row is not None)

    def make_boarduing_card(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")



def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}"  \
             f"  Flight: {flight_number}"   \
             f"  Seat: {seat}"   \
             f"  Aircraft: {aircraft}"   \
              " |"
    banner = "+" + "-" * (len(output) -2) + "+"
    border = "|" + " " * (len(output) -2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()

def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))

    f.allocate_seat("12A", "A")
    f.allocate_seat("1C", "B")
    f.allocate_seat("2D", "c")
    f.allocate_seat("3E", "d")

    f.print_seats()
    f.make_boarduing_card(console_card_printer)

    g = Flight("AF72", Boeing777("F-GSPS"))

    g.allocate_seat("12A", "A")
    g.allocate_seat("1C", "B")
    g.allocate_seat("2D", "c")
    g.allocate_seat("3E", "d")
    g.allocate_seat("4F", "e")
    g.allocate_seat("5B", "f")

    g.print_seats()
    g.make_boarduing_card(console_card_printer)
    return f, g

make_flights()