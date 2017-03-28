# -*- coding: utf-8 -*-
from ConcreteAggregateMy import ConcreteAggregate

products = ['python', 'php', 'java', 'lua', 'c++']

my_list = ConcreteAggregate(products)
my_iterator = my_list.create_iterator()

# while my_iterator.my_has_next():
#     print my_iterator.my_get_current_item(),
#     my_iterator.my_next()


print '正向遍历：'
while not my_iterator.my_is_last():
    print my_iterator.my_get_next_item(),
    my_iterator.my_next()

print '\n反向遍历：'
while not my_iterator.my_is_first():
    print my_iterator.my_get_previous_item(),
    my_iterator.my_previous()

