def anser(number):
    numberlist = [int(digit) for digit in str(number)]
    anser_chentie_value = 0
    anser_nechentie_value = 0
    for el in range(0, 6, 2):
        anser_chentie_value += numberlist[el]
    for el in range(1, 6, 2):
        anser_nechentie_value += numberlist[el]
    return int(str(anser_chentie_value) + str(anser_nechentie_value))
number = int(input())
while number / 100000 < 1:
    number = int(input())
print()
print(anser(number))