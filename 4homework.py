def anser(number):
    iteration = 1
    anser_list = [0,1]
    while anser_list[-1] != number:
        value = anser_list[-1] + anser_list[-2]
        anser_list.append(value)
        iteration += 1
        if value > number:
            return -1
    return iteration


number = int(input())
while number < 1:
    number = int(input())
print(anser(number))