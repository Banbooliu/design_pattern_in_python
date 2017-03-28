# -*- coding: utf-8 -*-
from AbstractAggregateMy import AbstractAggregate
from ConcreteIteratorMy import ConcreteIterator
from NextIterator import NextIterator
from PreviousIteratorMy import PreviousIterator


class ConcreteAggregate(AbstractAggregate):
    """
    具体聚合类
    具体工厂
    """
    def __init__(self, obj):
        super(ConcreteAggregate, self).__init__(obj)

    def create_iterator(self):
        # return NextIterator(self)  # 正序遍历
        # return PreviousIterator(self)  # 倒序遍历
        return ConcreteIterator(self)  # 两种遍历都有
