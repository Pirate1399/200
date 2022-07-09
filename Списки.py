from typing import Iterable, Optional, Any
from _collections_abc import MutableSequence  # from collection.abc import MutableSequence
from node import Node
from node import DoubleLinkedNode


class LinkedList(MutableSequence):
    CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0  # длинна списка
        self.head: Optional[Node] = None  # первый элемент
        self.tail = self.head  # Последний узел

        if data is not None:
            for value in data:
                self.append(value)

    def insert(self, index: int, value: Any) -> None:  # fixme реализовать insert
        """Вставка значения по указанному индексу"""
        node_value = self.step_by_step_on_nodes(index)
        return node_value

    def append(self, value: Any):
        """ Добавление элемента в конец списка. """
        append_node = Node(value)  # todo Node(value) -> self.CLASS_NODE(value) и можно унаследовать такой метод

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение шаг за шагом по списку. Return - узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        """ Метод формирует список из значений всех узлов"""
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __delitem__(self, key):
        if not 0 <= key < self.len:  # fixme DRY вынести в отдельный метод is_valid_index
            raise IndexError("Некорректный индекс")

        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым положительным числом")

        print(f"Узел со значением {self.step_by_step_on_nodes(key)} удален.")

        if key == 0:
            self.head = self.head.next
        elif key == self.len - 1:
            tail = self.step_by_step_on_nodes(key - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(key - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def __len__(self):
        """Возвращает количество узлов в списке"""
        return len(self.step_by_step_on_nodes(index=0))  # fixme исправить длину списка

    def clear(self):
        self.head = None
        self.tail = None

        self.len = 0

    def count(self, value) -> int:
        ...


class DoubleLinkedList(LinkedList):
    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


if __name__ == "__main__":
    gjiri = DoubleLinkedList([1, 2, 3, 4, 5, 6])
    print(gjiri[1])
    gjiri.__delitem__(1)
    print(gjiri.step_by_step_on_nodes(0).prev)
