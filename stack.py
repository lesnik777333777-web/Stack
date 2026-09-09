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
    # Словарь соответствия закрывающей скобки открывающей
    matching = {')': '(', ']': '[', '}': '{'}
    stack = Stack()

    for ch in brackets:
        if ch in matching:  # если это закрывающая скобка
            # Если стек пуст или верхний элемент не соответствует, то ошибка
            if stack.is_empty() or stack.pop() != matching[ch]:
                return False
        else:  # иначе это открывающая скобка
            stack.push(ch)

    # После обработки всех символов стек должен быть пустым
    return stack.is_empty()


# Примеры использования
if __name__ == "__main__":
    test_cases = [
        ("(((([{}]))))", True),
        ("[([])((([[[]]])))]{()}", True),
        ("{{[()]}}", True),
        ("}{}", False),
        ("{{[(])]}}", False),
        ("[[{())}]", False),
    ]

    for test, expected in test_cases:
        result = is_balanced(test)
        status = "Сбалансированно" if result else "Несбалансированно"
        print(f"{test:30} -> {status} (expected: {expected})")