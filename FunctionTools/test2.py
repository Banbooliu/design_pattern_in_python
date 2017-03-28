from copy import deepcopy
class A(object):
    c = {'a': 3}
    def __init__(self):
        self.a = [1,2,3]
        self.b = '2222'

    def prpr(self):
        print self.a, self.b, self.c

    def clone(self):
        obj = deepcopy(self)
        return obj

    def get_id(self, uid=None):
        if uid is None:
            uid = 9
        return uid

x = A()
x.prpr()


y = x.clone()
y.prpr()


x.a.append(999)
x.c['b'] = 4

x.prpr()
y.prpr()

B = deepcopy(A)
m = B()

print B, id(B)
print A, id(A)
print id(x.c)
print id(y.c)