import unittest

from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Orange")

    def test_starts_with_no_guests(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_guests(self):
        guest = Guest("John")
        self.room.check_in(guest)
        self.assertEqual(1, self.room.guest_count())

    
    def test_can_check_out_guests(self):
        guest = Guest("John")
        self.room.check_in(guest)
        self.room.check_out(guest)
        self.assertEqual(0, self.room.guest_count())

        
  