import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Green Room")
        self.guest = Guest("John")
        self.song = Song("Don't Stop Me Now", "Queen")

    def test_starts_with_no_guests(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_guests(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, self.room.guest_count())

    
    def test_can_check_out_guests(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(0, self.room.guest_count())

    def test_can_add_song_to_room(self):
        self.room.add_song(self.song)
        self.assertEqual(1, self.room.songs_count())

    