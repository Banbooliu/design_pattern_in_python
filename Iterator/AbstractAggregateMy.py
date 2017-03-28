# -*- coding: utf-8 -*-
class AbstractAggregate(object):
    """
    抽象聚合类
    抽象工厂
    """
    _obj = list()

    def __init__(self, obj):
        self._obj = obj

    def add_item(self, item):
        self._obj.append(item)

    def remove_item(self, item):
        self._obj.remove(item)

    def get_obj(self):
        return self._obj

    def get_size(self):
        return len(self._obj)

    def create_iterator(self):
        pass

    def get(self, item):
        return self._obj[item]

    def set(self, key, value):
        self._obj[key] = value
