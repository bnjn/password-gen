import string
import random

def generate_password(length):
  if type(length) != int:
    raise TypeError('Integers are the only valid input.')
  if length < 2:
    raise ValueError('Length must be two or more.')
  letters = string.ascii_letters
  password = ''
  for i in range(length):
    password += random.choice(letters)
  return password