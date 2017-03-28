# -*- coding: utf-8 -*-
class TaskCaretaker(object):
    def __init__(self, memento):
        self.memento_list = [memento]
        self.current_id = 0

    def set_memento(self, memento):
        self.memento_list.append(memento)

    def get_memento(self, index):
        return self.memento_list[index]

    def is_undo(self):
        if self.current_id + 1 < len(self.memento_list):
            return True
        else:
            return False

    def do(self, task, x=0, y=0):
        print '前进1步',
        # undo后再do时，应覆盖掉之前的分支
        if self.is_undo():
            print '之前分支已被覆盖'
            self.memento_list = self.memento_list[:self.current_id+1]
        if x:
            task.x = x
        if y:
            task.y = y
        self.set_memento(task.save())
        self.current_id += 1
        self.display(task)

    def undo(self, task, count):
        if self.current_id-count < 0:
            print '一共能退%d步，退过了！' % self.current_id
            # task.restore(self.get_memento())
            return
        print '后退%d步' % count,
        self.current_id -= count
        task.restore(self.get_memento(self.current_id))
        self.display(task)

    def redo(self, task, count):
        print '重做%d步' % count,
        self.current_id += count
        task.restore(self.get_memento(self.current_id))
        self.display(task)

    def display(self, task):
        print 'x = %d, y = %d, 已保存%d个位置，当前位置%d' % (task.x, task.y, len(self.memento_list), self.current_id+1)


if __name__ == '__main__':
    pass