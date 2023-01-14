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

  def test_raises_exception_if_length_under_two(self):
    with self.assertRaises(ValueError):
      gen_pass.generate_password(1)

  def test_throw_typeerror_on_invalid_input(self):
    with self.assertRaises(TypeError):
      gen_pass.generate_password('potato')

  def test_returns_different_passwords(self):
    first_gen = gen_pass.generate_password(6)
    second_gen = gen_pass.generate_password(6)
    loop_number = 0
    while first_gen == second_gen:
      if loop_number > 100:
        break
      second_gen = gen_pass.generate_password(6)
      loop_number += 1
    self.assertNotEqual(first_gen, second_gen)

  def test_does_not_return_same_chars(self):
    actual = gen_pass.generate_password(12)
    different_chars = len(set(list(actual))) > 1
    self.assertTrue(different_chars)

if __name__ == '__main__': 
    unittest.main()
