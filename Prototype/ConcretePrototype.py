# -*- coding: utf-8 -*-
from copy import deepcopy, copy
from Prototype import AbstractPrototype


class HumanPrototype(AbstractPrototype):
    """
    放在这里的类变量不能通过deepcopy成功复制
    只有在__init__里的属于实例的变量可以用deepcopy复制
    """
    cannot_deepcopy = {}

    def __init__(self, name, **kwargs):
        self._name = name
        # 其他信息选填
        if 'age' in kwargs:
            self.age = kwargs['age']
            del kwargs['age']
        self._info = kwargs

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def _set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_cannot_deepcopy(self, value):
        self.cannot_deepcopy = value

    def clone(self, name, **kwargs):
        # 姓名必填
        obj = deepcopy(self)
        # obj = copy(self)

        obj._set_name(name)
        # 其他信息选填
        if 'age' in kwargs:
            obj.age = kwargs['age']
            del kwargs['age']
        if 'cannot_deepcopy' in kwargs:
            obj.cannot_deepcopy = kwargs['cannot_deepcopy']
        obj._info.update(kwargs)
        return obj

    def clone2(self, name, **kwargs):
        obj = HumanPrototype(name)
        if 'age' in kwargs:
            obj.age = kwargs['age']
            del kwargs['age']
        else:
            obj.age = self._age
            del kwargs['age']
        obj._info.update(kwargs)
        return obj

    def __repr__(self):
        return '姓名：' + self._name + ', 年龄：' + str(self._age) + ', info:' + str(self._info)
        # return '姓名：' + self._name + ', 年龄：' + str(self._age) + ', info:' + str(self._info) + ', cannot_deepcopy: ' + str(self.cannot_deepcopy)
