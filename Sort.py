#ф-ция сортировки
def sort_AZ (array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    return array
#ф-ция поиска указанного элемента
def binary_search(array, element, left, right): #3-9
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  #6
    #if array[middle] == element:  # если элемент в середине,//
    if (array[middle-1] < element) and (element <= array[middle+1]):
        return middle-1  # возвращаем этот индекс
    elif element < array[middle]:  #
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1) #
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


array = list(map(int, input("Введите последовательность чисел через пробел:").split())) #<class 'list'>
element = int(input("Введите любое число:"))

#print(sort_AZ(array), " - отсортированный массив")
print("result= ", binary_search(array, element, 0, len(array)-1))
