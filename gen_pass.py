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
  chars = string.ascii_letters + string.digits
  if special == True:
    chars += string.punctuation + ' '
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
