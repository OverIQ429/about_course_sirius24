def numorelog(count):
    iteration = 0
    for _ in range(0,count):
        value = int(input())
        if value > 0:
            iteration += 1
    return iteration
count = int(input())
print(numorelog(count))