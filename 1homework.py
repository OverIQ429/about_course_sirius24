def anser(number):
    anser_value = 1
    for symbol in map(int, str(number)):
        anser_value *= symbol
    return anser_value
number = int(input("Введите пятизначное число:"))
while number / 10000 < 1:
    print("Ошибка. Введите пятизначное число")
    number = int(input("Введите пятизначное число:"))
print("Ответ:\n")
print(anser(number))