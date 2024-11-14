# Объявим класс Car
class Car:
  # Иницируем параметры
  def __init__(self, model: str, vin: int, numbers: str):
    self.model = model
    # Инкапсулированные парметры
    self.__vin = vin
    self.__numbers = numbers
    self.__is_valid_vin()
    self.__is_valid_numbers()

  # Функция проверки валидности параметра vin
  def __is_valid_vin(self):
    # Проверка на тип vin (должен быть int)
    if not isinstance(self.__vin, int):
      # Если нет сбрасываемся в класс исключений IncorrectVinNumber
      raise IncorrectVinNumber('Некорректный тип vin номер')
    # Проверка на диапазон значений vin
    if not 1000000 <= self.__vin <= 9999999:
      # Если нет сбрасываемся в класс исключений IncorrectVinNumber
      raise IncorrectVinNumber('Неверный диапазон для vin номера')

  # Функция проверки валидности параметра numbers
  def __is_valid_numbers(self):
    # Проверка на тип numbers (должен быть str)
    if not isinstance(self.__numbers, str):
      # Если нет сбрасываемся в класс исключений IncorrectCarNumbers
      raise IncorrectCarNumbers('Некорректный тип данных для номеров')
    # Проверка на длинну numbers
    if not len(self.__numbers) == 6:
      # Если нет сбрасываемся в класс исключений IncorrectCarNumbers
      raise IncorrectCarNumbers('Неверная длина номера')

# Класс исключений для vin
class IncorrectVinNumber(Exception):
  def __init__(self, message):
    self.message = message

# Класс исключений для numbers
class IncorrectCarNumbers(Exception):
  def __init__(self, message):
    self.message = message

# Попробуем
try:
  # Создадим экземпляр класса Car
  first = Car('Model1', 1000000, 'f123dj')
# Если ошибка параметра vin
except IncorrectVinNumber as exc:
  print(exc.message)
# Если ошибка параметра numbers
except IncorrectCarNumbers as exc:
  print(exc.message)
# Если ошибок нет
else:
  print(f'{first.model} успешно создан')

try:
  # В этом экземпляре некорректное vin (маленькое)
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
   # В этом экземпляре некорректное numbers (слишком большое)
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

