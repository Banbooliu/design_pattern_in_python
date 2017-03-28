# -*- coding: utf-8 -*-
from ConcretePrototype import HumanPrototype

a = HumanPrototype('孙行者')
a.age = 500
print a

b = a.clone('者行孙')
print b

c = a.clone('六耳猕猴', age=200)
print c

d = c.clone('十八耳猢狲', ear=18)
print d
# print a

e = a.clone('哪吒', head=3, arm=6)
print e
