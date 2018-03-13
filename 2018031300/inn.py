# _*_ coding:utf-8 _*_

#  导入异常包
import exceptions
class stack():
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1
    # 压栈
    def push(self, x):
        # 判断是否满栈
        if self.isfull():
            raise exceptions.Exception('stack is full')

        else:
            self.stack.append(x)
            self.top = self.top + 1
    # 出栈
    def pop(self):
        # 判断是否空栈
        if self.isempty():
            raise exceptions.Exception('stack is empty')
        else:
            self.top = self.top -1
            self.stack.pop()
    def isfull(self):
        return self.top + 1 == self.size
    def isempty(self):
        return self.top == -1
    def showStack(self):
        print self.stack


S = stack(10)

for i in range(10):
    S.push(i)
S.showStack()
for i in range(4):
    S.pop()
S.showStack()

