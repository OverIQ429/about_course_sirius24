def my_sort(array: list, anser = []):
    if len(array) > 1:
        for el in range(len(array[0])):
            anser.append(array[0][el])
        for el in range(1,len(array)):
            anser.append(array[el][-1])
        for el in range(len(array[-1])-2,-1,-1):
            anser.append(array[-1][el])
        for el in range(1,len(array)-1):
            anser.append(array[el][0])
    else:
        for el in range(len(array[0])):
            anser.append(array[0][el])
    if array:
        del(array[0])
    if array:
        del(array[-1])
    if array:
        for el in range(len(array)):
            del(array[el][0])
    if array:
        for el in range(len(array)):
            del(array[el][-1])
    if array:
        my_sort(array, anser)

    return anser

array = [["1","2","3",],["4","5","6"],["7","8","9"]]
print(my_sort(array))