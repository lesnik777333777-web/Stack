class Stack:
    """Класс, реализующий стек (LIFO) на основе списка."""

    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек. Возвращает True, если пуст, иначе False."""
        return len(self.items) == 0

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека.
        Если стек пуст, генерирует исключение IndexError."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Возвращает верхний элемент стека без его удаления.
        Если стек пуст, генерирует исключение IndexError."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self) -> int:
        """Возвращает количество элементов в стеке."""
        return len(self.items)


def is_balanced(brackets: str) -> bool:
    """
    Проверяет, является ли строка скобок сбалансированной.

    Аргументы:
        brackets (str): строка, содержащая только скобки (например, "()[]{}").

    Возвращает:
        bool: True, если скобки сбалансированы, иначе False.
    """
    matching = {')': '(', ']': '[', '}': '{'}
    stack = Stack()

    for ch in brackets:
        if ch in matching:  # закрывающая скобка
            if stack.is_empty() or stack.pop() != matching[ch]:
                return False
        else:  # открывающая скобка
            stack.push(ch)

    return stack.is_empty()


if __name__ == "__main__":
    brackets = input("Введите строку со скобками: ").strip()
    if is_balanced(brackets):
        print("Сбалансированно")
    else:
        print("Несбалансированно")