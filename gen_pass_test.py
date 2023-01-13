import gen_pass
import unittest

class TestGenPass(unittest.TestCase):

  def test_returns_string(self):
    actual = generate_password()
    expected = ''
    self.assertEqual(actual, expected)
