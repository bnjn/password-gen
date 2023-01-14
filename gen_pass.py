import string
import random

def generate_password(length):
  if type(length) != int:
    raise TypeError('Integers are the only valid input.')
  elif length < 2:
    raise ValueError('Length must be two or more.')
  elif length > 100:
    raise ValueError('Length must be less than a hundred.')
  letters = string.ascii_letters
  numbers = ''.join(str(i) for i in list((range(0, 10))))  
  chars = letters + numbers
  password = ''
  for i in range(length):
    password += random.choice(chars)
  return password