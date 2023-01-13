import gen_pass
import unittest

class TestGenPass(unittest.TestCase):

  def test_returns_string(self):
    actual = gen_pass.generate_password(2)
    expected = str
    self.assertEqual(type(actual), expected)

  def test_returns_correct_string_length(self):
    actual = gen_pass.generate_password(10)
    expected = 10
    self.assertEqual(len(actual), expected)
