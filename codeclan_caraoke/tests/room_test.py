import unittest

from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def test_starts_with_no_guests(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_guests(self):
        guest = Guest("John")
        self.room_name.check_in(guest)
        self.assertEqual(1, self.room_name.guest_count())

    
    # def test_can_drop_off_passenger(self):
    #     person = Person("Guido van Rossum", 64)
    #     self.bus.pick_up(person)
    #     self.bus.drop_off(person)
    #     self.assertEqual(0, self.bus.passenger_count())
  