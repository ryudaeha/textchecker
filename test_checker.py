from unittest import TestCase
from check import check

class Chk(TestCase):
    def test_length(self):
        chk = check()
        self.assertEqual(1,chk.check_len())

    def test_alpha(self):
        chk = check()
        self.assertEqual(1,chk.check_alpha())

    def test_score(self):
        chk = check()
        self.assertEqual(1, chk.score('123','123'))

