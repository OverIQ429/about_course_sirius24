def anser(numbers):
    summ_number = 0
    for symbol in range(0, numbers):
        number = float(input())
        if number % 3 == 0:
            summ_number += number
    if summ_number == 0:
        return -1
    return summ_number / numbers
numbers = int(input())
while numbers < 1:
    numbers = int(input())
print(anser(numbers))