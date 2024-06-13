from unittest import TestCase
from check import check

class Chk(TestCase):



    def setUp(self):
        self.chk = check()
        super().setUp()

    def test_length(self):
        self.assertEqual(1,self.chk.check_len('ASD', 'DSA'))

    def test_alpha(self):
        self.assertEqual(1,self.chk.check_alpha())

    def test_score(self):
        self.assertEqual(1, self.chk.score('123','123'))

    def test_length_compare_1(self):
        self.assertEqual(60,self.chk.check_len('ASD', 'DSA'))
        self.assertEqual(0, self.chk.check_len('A', 'BB'))
