# Объявим функцию суммирования элементов коллекции
def personal_summ(numbers):
  # становим значения результата суммы и счетчик некорректных данных
  result = 0
  incorrect_data = 0
  # Пробежим по значениям коллекции
  for num in numbers:
    # Суммируем элементы коллекции
    try:
      result = result + num
    # Если некорректные данные, то увеличим счетчик
    except TypeError:
      print(f'Не корректный тип данных: {num}')
      incorrect_data += 1

# Вернем результат работы функции
  return result, incorrect_data

# Объявим функцию подсчета среденго
def calculate_average (numbers):
  try:
    # Запросим результаты работы функции суммирования
    res_sum, incorrect_data = personal_summ(numbers)
    # Если в коллекции элементов строковые значения то изменим длинну коллекции
    # С учетом изменной длинны высчитаем среднее значение
    averange = res_sum / (len(numbers) - incorrect_data)
  # Обработка ошибки деления на ноль
  except ZeroDivisionError:
    return 0
  # Обработка ошибки введения не коллекции
  except TypeError:
    print(f'В списке numbers не корректный тип данных')
    return None
  return averange

# Подадим стровую коллекцию строка перебирается
print(f'Результат 1: {calculate_average("1, 2, 3")}')
# Сработает исключение функции personal_summ
# И исключение функции calculate_average "Деление на ноль"

 # Подадим список из переменных типа int и str строковые элементы отбросятся
 # Учитываются только 1 и 3
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
# Сработает исключение функции personal_summ

# Передадим не коллекцию
print(f'Результат 3: {calculate_average(567)}')
 # Сработает исключение функции calculate_average TypeError (Ошибка данных)

# Передадим корректные данные
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
# Исключений нет

