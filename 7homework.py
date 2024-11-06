value = int(input())
array = []
iteration = 0
array.append(value)
while value != 0:
    value = int(input())
    array.append(value)
for symbol in array:
    if symbol == max(array):
        iteration += 1
print(iteration)
