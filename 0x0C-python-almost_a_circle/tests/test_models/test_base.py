#!/usr/bin/python3

import unittest
import sys
sys.path.append("../../")

from models.base import Base

class TestBase(unittest.TestCase):

    def test_init(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)
        base4 = Base()
        self.assertEqual(base4.id, 4)

    def test_init_twi(self):
        base5 = Base()
        base5.id = 10
        self.assertEqual(base5.id, 10)
