# Просим пользователя ввести число
from math import *
ye = input("Введите число: ")
# Проверка того, ввел пользователь число или что-то другое
if ye.isnumeric() is True:
    print(ye)
    # если мы проходим проверку выше, то умножаем число на 2 и выводим
    ye = ye * 2
    print("Введенное число, умноженное на 2 будет равно: ", ye)
else:
    # Если не прошли проверку в if, выводим ошибку ввода
    print("Вы ввели не число")

