# -*- coding: utf-8 -*-
from Memento import TaskMemento


class Task(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.memento = TaskMemento(self)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.memento = self.memento.clone(x=value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.memento = self.memento.clone(y=value)

    def save(self):
        return self.memento

    def restore(self, memento):
        self._x = memento.x
        self._y = memento.y
        self.memento = memento

