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

  def test_throw_typeerror_on_invalid_input(self):
    with self.assertRaises(TypeError):
      gen_pass.generate_password('potato')

if __name__ == '__main__': 
    unittest.main()
