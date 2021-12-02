import random # модуль, с помощью которого перемешиваем массив

def sort_by_inserts(list_input):
    list_int = list_input
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

order_numbers_string = input("Введите последовательность чисел через пробел: ")
element = int(input("Введите любое число для поиска в отсортированном списке: "))

order_numbers_list = list(map(int, order_numbers_string.split(sep=" ")))

roster_sorting = sort_by_inserts(order_numbers_list)
print("Сортировка списка по возрастанию: ", roster_sorting)

# запускаем алгоритм на левой и правой границе
element_index = binary_search(roster_sorting, element, 0, len(roster_sorting))

print("Индекс элемента, введенного числа, в отсортированном списке: ", element_index)