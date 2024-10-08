numbers = str(input("Введите числа, разделив их пробелом")).split()
result = []
for symbol in numbers[0]:
    if symbol in numbers[1]:
        result.append(symbol)
print(result)