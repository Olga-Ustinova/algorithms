# ID успешной посылки: 88285408
"""
Калькулятор

Задача связана с обратной польской нотацией, которая используется для парсинга
арифметических выражений. В данной нотации операнды располагаются перед
знаками операций.

Пример 1:
3 4 +
означает 3 + 4 и равно 7

Пример 2:
12 5 /
Так как деление целочисленное, то в результате получим 2.

Необходимо вычислить значение выражения, записанного в обратной польской
нотации, используя стек для обработки символов по определенному алгоритму.
Арифметические операции могут быть: +, -, *, /.
Нужно считывать выражение слева направо и придерживаться следующих шагов:
1. Обработка входного символа:
    - Если на вход подан операнд, он помещается на вершину стека.
    - Если на вход подан знак операции, то эта операция выполняется над
    требуемым количеством значений, взятых из стека в порядке добавления.
    Результат выполненной операции помещается на вершину стека.
2. Если входной набор символов обработан не полностью, перейти к шагу 1.
3. После полной обработки входного набора символов результат вычисления
выражения находится в вершине стека. Если в стеке осталось несколько чисел,
то надо вывести только верхний элемент.

Формат ввода:
- В единственной строке дано выражение, записанное в обратной польской нотации.
Числа и арифметические операции записаны через пробел.

Формат вывода:
- Выведите единственное число — значение выражения, являющееся результатом
вычисления.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        raise IndexError("стек уже пуст")


def calculator(elements):
    """
    Примеры ввода и вывода:

    1.  Ввод:
        2 1 + 3 *

        Вывод:
        9

    2.  Ввод:
        7 2 + 4 * 2 +

        Вывод:
        38
    """
    stack = Stack()
    for element in elements:
        if element in "+-*/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            if element == "+":
                result = operand1 + operand2
            elif element == "-":
                result = operand1 - operand2
            elif element == "*":
                result = operand1 * operand2
            elif element == "/":
                result = operand1 // operand2
            stack.push(result)
        else:
            stack.push(int(element))
    try:
        return stack.pop()
    except IndexError:
        return "error"


if __name__ == "__main__":
    print(calculator(input().split()))
