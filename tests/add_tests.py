import unittest

from testing_travis.add import add

class AddTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 1 + 2)
