# -*- coding: utf-8 -*-
from AbstractIteratorMy import AbstractIterator


class ConcreteIterator(AbstractIterator):
    _obj = None
    _item = None
    _cursor_next = 0
    _cursor_previous = 0

    def __init__(self, obj):
        self._obj = obj  # ConcreteAggregate
        self._item = obj.get_obj()
        self._cursor_next = 0
        self._cursor_previous = obj.get_size() -1

    def my_previous(self):
        if self._cursor_previous > -1:
            self._cursor_previous -= 1

    def my_next(self):
        if self._cursor_next < self._obj.get_size():
            self._cursor_next += 1

    def my_is_first(self):
        return self._cursor_previous == -1

    def my_is_last(self):
        return self._cursor_next == self._obj.get_size()

    def my_get_previous_item(self):
        return self._obj.get(self._cursor_previous)

    def my_get_next_item(self):
        return self._obj.get(self._cursor_next)