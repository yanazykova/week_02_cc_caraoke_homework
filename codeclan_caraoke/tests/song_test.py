import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Never Give Up")

    def test_song_has_title(self):
        self.assertEqual("Never Give Up", self.song.title)
