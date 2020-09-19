class Room:

    def __init__(self, room):
        self.room = room
        self.song_list = []
        self.guest_list = []

    def guest_count(self):
        return len(self.guest_list)

    def check_in(self, guest):
        self.guest_list.append(guest)

    # def drop_off(self, person):
    #     self.passengers.remove(person)