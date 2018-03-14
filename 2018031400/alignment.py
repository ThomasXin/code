# _*_ coding:utf-8 _*_
import exceptions
class Queue():

    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = []

    def enqueue(self, ele):
        if self.isfull():
            raise exceptions.Exception('queue is full')
        else:
            self.queue.append(ele)
            self.rear = self.rear + 1

    def dequeue(self):
        if self.isempty():
            raise exceptions.Exception('queue is empty')
        else:
            self.queue.pop(0)
            self.front = self.front + 1

    def isfull(self):
        return  self.rear - self.front + 1 == self.size
    def isempty(self):
        return self.front == self.rear
    def showQueue(self):
        print self.queue

q = Queue(10)
for i in range(5):
    q.enqueue(i)
q.showQueue()
for i in range(3):
    q.dequeue()
q.showQueue()

print q.isempty()
