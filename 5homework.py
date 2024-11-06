def numerolog(number):
    checknumber = 1
    array = []
    while checknumber < number:
        array.append(checknumber)
        checknumber *= 2
    return array
number = int(input())
print(numerolog(number))