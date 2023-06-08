# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем
# Устанавливается номер позиции элемента,
# который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

list = list(map(int, input("Введите целые числа через пробел: ").split()))

def sort(list):
    for i in range(1, len(list)):
        x = list[i]
        idx = i
        while idx > 0 and list[idx-1] > x:
            list[idx] = list[idx-1]
            idx -= 1
        list[idx] = x
    return list
array = sort(list)
print(array)

element = None
error = False

while not element:
    try:
        element = int(input("Введите любое целое число: "))
        if element < min(array) or element > max(array):
            print("Указанное число не входит в диапазон списка")
            error = True
        if element <= 0:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести целое число")
        error = True
    except Exception:
        print("Нужно ввести положительное число")
        error = True

def search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return search(array, element, left, middle - 1)
    else:
        return search(array, element, middle + 1, right)

result = search(array, element, 0, len(array)-1)

if result is False:
    for i in range(1, len(array)):
        if array[i] >= element:
            result = i
            break

if not error:
    if result - 1 < 0:
        print(f'Элемент является первым, индекс {result}')
    elif result >= len(array) - 1 and element == array[result]:
        print(f'Элемент является последним, индекс {result}')
    else:
        print(f'Индекс меньшего элемента: {result - 1}, индекс большего элемента: {result}')
