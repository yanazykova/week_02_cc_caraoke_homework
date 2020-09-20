import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Don't Stop Me Now", "Queen")

    def test_song_has_title(self):
        self.assertEqual("Don't Stop Me Now", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song.artist)

    