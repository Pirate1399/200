import unittest

from Списки import LinkedList

class TestCase(unittest):

    def test_count_from_empty_list(self):
        value = 10
        ll = LinkedList()
        message = "Значение должно быть 0"
        self.assertEqual(ll.count(value), 0, message)
        """ Количество от пустого списка должно быть 0. """

    def test_count_from_list(self):
        value = 1
        ll = LinkedList([1,2,1,5,6,7])
        message = "Что-то пошло не так, должно быть 2"
        self.assertEqual(ll.count(value), 2, message)
        """ Количество искомого элемента в списке. """




