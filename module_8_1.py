# Создадим функцию которая принимает два параметра
def add_everything_up(a, b):
  # Тут возможно возникновение ошибок
  try:
    # Если возможно то вернем сумму
    return a + b
  # Если случится ошибка типа TypeError
  except TypeError:
    # Если нельзя сложить раные типы, преобразуем типы
    return str(a) + str(b)
# Подадаим число и строку (будет ошибка)
print(add_everything_up(1234, 'string'))
# Подадим два числа (ошибок нет)
print(add_everything_up(1, 7))
# Подадим строку и число (будет ошибка)
print(add_everything_up('duple', 17))
# Подадим две строки (ошибок нет)
print(add_everything_up('Привет ', 'незнакомец'))
# Подадим два числа типа float (ошибок нет)
print(add_everything_up(12.3567, 344.5))

