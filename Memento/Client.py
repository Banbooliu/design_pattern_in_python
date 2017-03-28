# -*- coding: utf-8 -*-
from Caretaker import TaskCaretaker
from Originator import Task


class Client(object):
    """
    进行分支控制
    """
    def __init__(self, memento):
        self.caretaker = TaskCaretaker(memento)
        self.current_id = -1

    def do(self, task, x=0, y=0):
        if x:
            task.x = x
        if y:
            task.y = y
        self.caretaker.set_memento(task.save())
        self.current_id += 1
        print 'do: now', task.x, task.y

    def undo(self, task, count):
        print '后退%d步' % count
        task.restore(self.caretaker.get_memento(self.current_id-count))
        self.current_id -= count
        print 'undo: now', task.x, task.y

    def redo(self, task, count):
        print '重做%d步' % count
        task.restore(self.caretaker.get_memento(self.current_id+count))
        self.current_id += count
        print 'redo: now', task.x, task.y


if __name__ == '__main__':
    task = Task(1, 1)
    client = Client(task.save())
    client.do(task, x=2)
    client.do(task, y=3)
    client.do(task, x=9, y=9)
    client.do(task, x=20, y=20)
    client.undo(task, 1)
    client.undo(task, 1)
    client.undo(task, 1)
    client.redo(task, 3)
