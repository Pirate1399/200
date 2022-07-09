from typing import Any, Optional
class Node:
    """ Класс узлов для связанного списка. """
    def __init__(self, value, next_: Optional["Node"] = None):
        self.value = value
        self.next = None
        self.set_next(next_)

    def is_valid(self, node: Any):
        if not isinstance(node, (type(None), Node)):
            raise TypeError("Объект должен быть класса Node")

    def set_next(self, next_):
        self.is_valid(next_)
        self.next = next_

    def __repr__(self):
        return f"Node({self.value}, {self.next})"

    def __str__(self):
        return str(self.value)


class DoubleLinkedNode(Node):
    def __init__(self, prev_, value, next_):
        super().__init__(value=value, next_= next_)
        self.prev = prev_

    def __repr__(self):
        """ Переопределяем метод repr из родительского класса"""
        return f" Предыдущий узел {self.prev}, значение узла: {self.value}, значение следущего узла: {self.next}"

    @property
    def prev(self,):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        self.is_valid(prev_)
        self._prev = prev_


if __name__ == "__main__":
    a = DoubleLinkedNode(Node(1), 2, Node(8))

    listyy = [a]
    print(listyy)