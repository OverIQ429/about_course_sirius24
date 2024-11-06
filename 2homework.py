def anser(number):
    firstnumberlist = map(int, str(number))
    anser_chentie_value = list(filter(lambda x: x % 2 == 0, firstnumberlist ))
    secondnumberlist = map(int, str(number))
    anser_nechentie_value = list(filter(lambda x: x % 2 == 1, secondnumberlist ))
    return sum(anser_chentie_value), sum(anser_nechentie_value)
number = int(input("Введите шестизначное число:"))
while number / 100000 < 1:
    print("Ошибка. Введите шестизначное число")
    number = int(input("Введите шестизначное число:"))
print("Ответ:\n")
print(anser(number))