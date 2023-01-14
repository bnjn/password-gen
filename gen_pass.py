import string
import random

def generate_password(length, special=None):
  if type(length) != int:
    raise TypeError('Integers are the only valid input.')
  elif length < 2:
    raise ValueError('Length must be two or more.')
  elif length > 100:
    raise ValueError('Length must be less than a hundred.')
  letters = string.ascii_letters
  numbers = ''.join(str(i) for i in list((range(0, 10))))
  special_chars = string.punctuation + ' '
  chars = letters + numbers
  if special == True:
    chars += special_chars
  password = ''
  for i in range(length):
    password += random.choice(chars)
  return password
