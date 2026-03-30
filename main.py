class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"{self.number}-xona band qilindi.")
        else:
            print("Xona band.")

    def checkout(self):
        self.is_booked = False
        print(f"{self.number}-xona bo'shadi.")

    def get_info(self):
        status = "Band" if self.is_booked else "Bo'sh"
        return f"Xona {self.number} | {self.price} so'm | {status}"


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        print("\nXonalar:")
        for room in self.rooms:
            print(room.get_info())

    def find_room(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None


def run_hotel():
    hotel = Hotel()

    r1 = Room(101, 200000)
    r2 = Room(102, 250000)
    r3 = Room(103, 300000)

    hotel.add_room(r1)
    hotel.add_room(r2)
    hotel.add_room(r3)

    hotel.show_rooms()

    room = hotel.find_room(101)

    if room:
        room.book()

    hotel.show_rooms()

    if room:
        room.checkout()

    hotel.show_rooms()


run_hotel()
