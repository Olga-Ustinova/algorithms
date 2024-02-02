# ID успешной посылки: 87897700
"""
Ловкость рук

В задаче участники играют на квадратной клавиатуре размером 4х4. На клавишах
может быть изображена точка или цифра от 1 до 9. Два игрока играют вместе и в
момент времени t должны одновоременно нажать на все клавиши с цифрой t. Каждый
игрок может нажать до k клавиш в один момент времени. Если оба игрока могут
нажать все необходимые клавиши, они получают 1 балл.
Программа должна принимать следующие данные для каждого раунда:
- Значение k (количество клавиш, которые может нажать каждый игрок).
- Значения для клавиш на клавиатуре (представлены в виде строк, где каждый
символ - точка или цифра от 1 до 9).
Задача состоит в вычислении количества баллов, которое будут набраны игроками
в данном раунде.

Формат ввода:
- В первой строке задается целое число k (1 ≤ k ≤ 5).
- В следующих четырех строках заданы значения для клавиш на клавиатуре (по 4
символа в каждой строке). Каждый символ может быть точкой или цифрой от 1 до 9.
Символы в одной строке идут подряд и не разделяются пробелами.

Формат вывода:
- Выводится единственное число - количество баллов, которое игроки наберут в
раунде.
"""


def calculate_score(k, buttons):
    """
    пример_входных_параметров1:
    3
    1231
    2..2
    2..2
    2..2
    пример_результата1:
    2

    пример_входных_параметров2:
    4
    1111
    9999
    1111
    9911
    пример_результата2:
    1
    """
    score = 0
    max_button = max(buttons)
    if max_button == '.':
        return score

    for i in '123456789':
        count = buttons.count(i)
        if 0 < count <= 2 * k:
            score += 1
    return score


def main():
    k = int(input())
    buttons = ''.join(input() for _ in range(4))
    print(calculate_score(k, buttons))


if __name__ == "__main__":
    main()
