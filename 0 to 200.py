number = 200
while number % 17 != 0:
    number = number + 1
    if number % 17 == 0:
        print("Минимальное число, которое больше 200 и делится на 17 без остатка: ", number)
