# ID успешной посылки: 88669164
"""
B. Эффективная быстрая сортировка
Требуется реализовать алгоритм быстрой сортировки ("in-place") для таблицы
результатов соревнования по спортивному программированию. Каждый участник
имеет уникальный логин, количество решённых задач Pi и размер штрафа Fi.
Сортировка должна выполняться в следующем порядке: сначала сравниваются
количество решённых задач, затем размер штрафа, и, наконец, логины в алфавитном
порядке. Результатом должен быть отсортированный список участников, где каждый
логин выводится на отдельной строке.
Основной фокус задачи заключается в реализации эффективной "in-place"
сортировки для большого числа участников без использования
дополнительной памяти.

Формат ввода:
- Число участников n (1 ≤ n ≤ 100 000).
- Для каждого участника в следующих n строках указывается:
   * Уникальный логин (строка из маленьких латинских букв длиной не более 20).
   * Число решённых задач Pi (целое число от 0 до 10^9).
   * Размер штрафа Fi (целое число от 0 до 10^9).

Формат вывода:
- Отсортированный список логинов участников, по одному на каждой строке.
"""


from dataclasses import dataclass


@dataclass
class Student:
    name: str
    problems: int
    penalty: int

    def __lt__(self, other):
        return (-self.problems, self.penalty, self.name) < (
            -other.problems, other.penalty, other.name)

    def __str__(self):
        return self.name


def quicksort_in_place(arr, low, high):
    """Быстрая сортировка списка в "in-place" режиме."""
    if low >= high:
        return
    mid = low + (high - low) // 2
    pivot = arr[mid]
    left = low
    right = high
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while pivot < arr[right]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    quicksort_in_place(arr, low, right)
    quicksort_in_place(arr, left, high)


if __name__ == "__main__":
    """
    Примеры ввода и вывода:
    1.  Ввод:
            5
            alla 4 100
            gena 6 1000
            gosha 2 90
            rita 2 90
            timofey 4 80

        Вывод:
            gena
            timofey
            alla
            gosha
            rita

    2.  Ввод:
            5
            alla 0 0
            gena 0 0
            gosha 0 0
            rita 0 0
            timofey 0 0

        Вывод:
            alla
            gena
            gosha
            rita
            timofey
    """
    number_of_players = int(input())
    users = []
    for i in range(number_of_players):
        name, problems, penalty = input().split()
        users.append(Student(name, int(problems), int(penalty)))
    quicksort_in_place(users, low=0, high=len(users) - 1)
    print(*users, sep="\n")
