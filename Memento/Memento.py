# -*- coding: utf-8 -*-
from copy import deepcopy


class TaskMemento(object):
    def __init__(self, task):
        self._x = task.x
        self._y = task.y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # 原型模式，通过clone来使得每次只需要改部分参数，而不是完全更新
    def clone(self, x=0, y=0):
        obj = deepcopy(self)
        if x:
            obj.x = x
        if y:
            obj.y = y
        return obj
