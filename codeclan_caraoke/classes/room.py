class Room:

    def __init__(self, room):
        self.room = room
        self.song_list = []
        self.guest_list = []

    def guest_count(self):
        return len(self.guest_list)

    def check_in(self, guest):
        self.guest_list.append(guest)

    def check_out(self, guest):
        self.guest_list.remove(guest)

    def songs_count(self):
        return len(self.song_list)

    def add_song(self, song):
        self.song_list.append(song)

    # def add_to_queue(self, person):
    #     self.queue.append(person)