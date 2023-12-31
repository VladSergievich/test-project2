import unittest
import sys, os


sys.path.append(os.getcwd())
from main import *

class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEquals(nitro_salt(1000), 10)
        self.assertEquals(nitro_salt(1500), 15)
        self.assertEquals(nitro_salt(800), 8)

    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_receives_string_returns_integer(self):
        self.assertEquals(nitro_salt('1000'), 10)

    def test_nitro_salt_receives_alpha_string_returns_zero(self):
        self.assertEquals(nitro_salt('asdsfas'), 0)


if __name__ == '__main__':
    unittest.main()

