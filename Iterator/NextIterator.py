# -*- coding: utf-8 -*-
from AbstractIteratorMy import AbstractIterator


class NextIterator(AbstractIterator):
    _obj = None
    _item = None
    _cursor = 0

    def __init__(self, obj):
        self._obj = obj
        self._item = obj.get_obj()
        self._cursor_next = 0
        print '正序遍历'

    def my_next(self):
        if self._cursor_next < self._obj.get_size():
            self._cursor_next += 1

    def my_has_next(self):
        return self._cursor_next < self._obj.get_size()

    def my_get_current_item(self):
        return self._obj.get(self._cursor_next)
