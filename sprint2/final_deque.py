# ID успешной посылки: 88285680
"""
Дек

Реализована структура данных Дек (двусторонняя очередь) с максимальным
размером. Однако, при большом количестве элементов программа работает медленно
из-за неэффективных операций.
Реализуйте эффективную версию дека с использованием кольцевого буфера.

Формат ввода:
- В первой строке записано число команд `n` (не более 100000).
- Во второй строке записан максимальный размер дека `m` (не более 50000).
- Затем следуют `n` строк с командами:
    * `push_back(value)`: добавить элемент value в конец дека.
    Если дек уже содержит максимальное количество элементов, вывести "error".
    * `push_front(value)`: добавить элемент value в начало дека.
    Если дек уже содержит максимальное количество элементов, вывести "error".
    * `pop_front()`: вывести и удалить первый элемент дека.
    Если дек пуст, вывести "error".
    * `pop_back()`: вывести и удалить последний элемент дека.
    Если дек пуст, вывести "error".
    * `value`: целое число, по модулю не превосходящее 1000.

Формат вывода:
- Для каждой команды выводить результат на отдельной строке.
  Успешные запросы push_back(x) и push_front(x) не требуют вывода.
"""


class Deque:
    def __init__(self, max_n):
        self.deque = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_n

    def push_back(self, value):
        if self.is_full():
            raise IndexError("дек достиг максимального значения")
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise IndexError("дек достиг максимального значения")
        self.head = (self.head - 1) % self.max_n
        self.deque[self.head] = value
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError("дек пуст")
        self.tail = (self.tail - 1) % self.max_n
        value = self.deque[self.tail]
        self.deque[self.tail] = None
        self.size -= 1
        return value

    def pop_front(self):
        if self.is_empty():
            raise IndexError("дек пуст")
        value = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return value


if __name__ == "__main__":
    """
    Примеры ввода и вывода:

    1.  Ввод:
            4
            4
            push_front 861
            push_front -819
            pop_back
            pop_back

        Вывод:
            861
            -819

    2.  Ввод:
            7
            10
            push_front -855
            push_front 0
            pop_back
            pop_back
            push_back 844
            pop_back
            push_back 823

        Вывод:
            -855
            0
            844
    """
    number_of_commands = int(input())
    max_deck_size = int(input())
    deque = Deque(max_deck_size)

    for _ in range(number_of_commands):
        command, *value = input().split()
        try:
            result = getattr(deque, command)(*value)
            if result is not None:
                print(result)
        except IndexError:
            print("error")
