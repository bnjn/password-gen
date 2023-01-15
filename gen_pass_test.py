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
    # Guard against chance of identical password edge case
    while first_gen == second_gen:
      if loop_number > 100:
        break
      second_gen = gen_pass.generate_password(6)
      loop_number += 1
    self.assertNotEqual(first_gen, second_gen)

  def test_does_not_return_same_chars(self):
    actual = gen_pass.generate_password(12)
    uniq_chars = set(list(actual))
    self.assertTrue(len(uniq_chars) > 1)

  def test_if_password_contains_numbers(self):
    actual  = gen_pass.generate_password(20)
    regex = '[0-9]+'
    self.assertRegex(actual, regex)

  def test_raises_type_error_if_length_over_hundred(self):
    with self.assertRaises(ValueError):
      gen_pass.generate_password(101)

  def test_generates_special_chars_if_passed_optional_param(self):
    actual = gen_pass.generate_password(50, True)
    regex = '[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\s]+'
    self.assertRegex(actual, regex)

  def test_raises_exception_if_optional_param_is_not_bool(self):
    with self.assertRaises(ValueError):
      gen_pass.generate_password(40, 77)


if __name__ == '__main__': 
    unittest.main()
