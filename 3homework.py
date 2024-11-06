def anser(numbers):
    summ_number = 0
    for symbol in range(0, numbers):
        number = float(input("Введите натуральное число:"))
        summ_number += number
    return summ_number / numbers
numbers = int(input("Введите натуральное число:"))
while numbers < 1:
    numbers = int(input("Ошибка. Вы ввели не натуральное число.\n Введите натуральное число:"))
print("Ответ:",anser(numbers))