def add_everything_up(a, b):
  try:
    return a + b
  except TypeError:
    return str(a) + str(b)

print(add_everything_up(1234, 'string'))

print(add_everything_up(1, 7))

print(add_everything_up('duple', 17))

print(add_everything_up('Привет ', 'незнакомец'))

print(add_everything_up(12.3567, 344.5))

