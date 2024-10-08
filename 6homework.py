def numorelog(count):
    iteration = 0
    for _ in range(0,count):
        value = int(input("Введите число:"))
        if value > 0:
            iteration += 1
    return iteration
count = int(input("Введите число последовательностей:"))
print(numorelog(count))