# -*- coding: utf-8 -*-
from collections import namedtuple
"""
完美的例子
"""

User = namedtuple('User', ['name', 'age', 'gender'])

user_prototype = User('', 0, 0)

u1 = {'name': 'Mike', 'age': 10, 'gender': 1}
user1 = user_prototype._replace(name='Mike', age=20, gender=1)
print user1
user2 = user1._replace(name='John', age=21)
print user2
user3 = user2._replace(name='Marry', gender=2)
print user3

print '\nnow print all:'
print user1
print user2
print user3