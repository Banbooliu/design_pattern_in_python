# -*- coding: utf-8 -*-
from Caretaker import TaskCaretaker
from Originator import Task

if __name__ == '__main__':
    task = Task(1, 1)
    client = TaskCaretaker(task.save())  # 保存初始状态
    client.do(task, x=2)
    client.do(task, y=3)
    client.do(task, x=9, y=9)
    client.do(task, x=20, y=20)
    client.undo(task, 1)
    client.undo(task, 1)
    client.undo(task, 1)
    client.undo(task, 1)
    client.undo(task, 1)  # 后退失败
    client.redo(task, 3)
    client.undo(task, 2)
    client.do(task, x=99, y=99)
    client.do(task, x=100)
    client.undo(task, 3)
