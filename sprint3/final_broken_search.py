# ID успешной посылки: 88572396
"""
A. Поиск в сломанном массиве

Алла скопировала данные из отсортированного по возрастанию кольцевого буфера в
обычный массив, но сдвинула данные исходной отсортированной последовательности.
Новый массив не является отсортированным. Требуется реализовать функцию,
которая осуществляет поиск элемента в сломанном массиве за время O(log n),
где n - длина массива. Массив содержит уникальные натуральные числа.
Функция должна вернуть индекс искомого элемента, если он присутствует в
массиве, и -1, если элемент не найден. Массив изменять нельзя.

Формат ввода:
- Массив натуральных чисел и искомый элемент k.
- Длина массива n не превосходит 10000.
- Элементы массива и число k не превосходят 10000.

Формат вывода:
- Функция должна вернуть индекс элемента, равного k, если такой есть в массиве
(нумерация с нуля).
- Если элемент не найден, функция должна вернуть -1.

Для отсечения неэффективных решений функция будет запускаться
от 100000 до 1000000 раз.
"""


def broken_search(numbers_array, target_number, left=0, right=None):
    """Бинарный рекурсивный поиск элемента в неотсорт. массиве."""
    if right is None:
        right = len(numbers_array) - 1
    if right < left:
        return -1
    mid = (left + right) // 2
    if numbers_array[mid] == target_number:
        return mid
    elif numbers_array[left] <= numbers_array[mid]:
        if numbers_array[left] <= target_number < numbers_array[mid]:
            return broken_search(
                numbers_array, target_number, left=left, right=mid - 1)
        else:
            return broken_search(
                numbers_array, target_number, left=mid + 1, right=right)
    else:
        if numbers_array[mid] < target_number <= numbers_array[right]:
            return broken_search(
                numbers_array, target_number, left=mid + 1, right=right)
        else:
            return broken_search(
                numbers_array, target_number, left=left, right=mid - 1)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == "__main__":
    """
    Примеры ввода и вывода:
    1.  Ввод:
            9
            5
            19 21 100 101 1 4 5 7 12

        Вывод:
            6

    2.  Ввод:
            2
            1
            5 1

        Вывод:
            1
    """
    len_array = int(input())
    target_number = int(input())
    numbers_array = list(map(int, input().split()))

    print(broken_search(numbers_array, target_number, left=0, right=None))

    test()
