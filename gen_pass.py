import string
import random
import re

def generate_password(length, special=None):
  if type(length) != int:
    raise TypeError('Integers are the only valid input.')
  elif special != None and type(special) != bool:
    raise ValueError('Must be bool or none.')
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

if __name__ == '__main__':
  pass_length = int(input('Length of password (2-100): '))
  special_chars = input('Special characters? (Yes/No/Y/N): ').lower()

  if re.match('(yes)|(y)', special_chars) == None:
    print(generate_password(pass_length))
  else:
    print(generate_password(pass_length, True))
