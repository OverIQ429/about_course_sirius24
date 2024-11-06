def anser(number):
    anser_value = 1
    for symbol in map(int, str(number)):
        anser_value *= symbol
    return anser_value
number = int(input())
while number / 10000 < 1:
    number = int(input())
print()
print(anser(number))