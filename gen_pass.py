import string
import random

def generate_password(length):
  if type(length) != int:
    raise TypeError('Integers are the only valid input')
  letters = string.ascii_letters
  return random.choice(letters)*length