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

  def test_returns_different_passwords(self):
    first_gen = gen_pass.generate_password(6)
    second_gen = gen_pass.generate_password(6)

    self.assertNotEqual(first_gen, second_gen)

if __name__ == '__main__': 
    unittest.main()
