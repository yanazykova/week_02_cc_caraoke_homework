class Room:

    def __init__(self, room_name):
        self.room_name = room_name
        self.song_list = []
        self.guest_list = []

    def guest_count(self):
        return len(self.guest_list)

    # def pick_up(self, person):
    #     self.passengers.append(person)

    # def drop_off(self, person):
    #     self.passengers.remove(person)