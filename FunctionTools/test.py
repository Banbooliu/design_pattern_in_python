# -*- coding: utf-8 -*-
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

# a[5]['z'] = 3

print 'a = ', a
print 'b = ', b
print 'c = ', c
print 'd = ', d


class A(object):
    a = [1,3,4]
    b = [1,2,3,4]
    c = {
        'a': {'1': 1},
        'b': {'2': 2}
    }

    def __init__(self):
        self.d = [1,23,4,5]

    def add(self):
        self.a.append(999)

    # def __repr__(self):
    #     return str(self.a) + str(self.b) + str(self.c)

x = A()
y = copy.copy(x)
z = copy.deepcopy(x)

z.add()
print x, id(x.d)
print y, id(y.d)
print z, id(z.d)

t1 = {
    'a': {
        'aa': {
            'aaa': {
                'aaaa': {
                    'aaaaa': 2
                }
            }
        }
    }
}

t2 = copy.deepcopy(t1)

t1['a']['aa']['aaa']['aaaa']['aaaaa'] = 999
print t2