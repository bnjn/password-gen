def generate_password(length):
  if type(length) != int:
    raise TypeError('Integers are the only valid input')

  return 'x'*length