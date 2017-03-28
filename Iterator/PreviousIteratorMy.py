# -*- coding: utf-8 -*-
from AbstractIteratorMy import AbstractIterator


class PreviousIterator(AbstractIterator):
    _obj = None
    _item = None
    _cursor = -1

    def __init__(self, obj):
        self._obj = obj
        self._item = obj.get_obj()
        self._cursor = obj.get_size() -1
        print '倒序遍历'

    def my_next(self):
        if self._cursor > -1:
            self._cursor -= 1

    def my_has_next(self):
        return self._cursor > -1

    def my_get_current_item(self):
        return self._obj.get(self._cursor)
