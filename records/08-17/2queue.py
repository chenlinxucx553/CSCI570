__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/17/2020 4:17 PM'


class Solution:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA.append(node)

    def pop(self):
        # return xx
        if len(self.stackB) == 0:
            if len(self.stackA) == 0:
                return None
            else:
                for _ in range(len(self.stackA)):
                    self.stackB.append(self.stackA.pop())

        return self.stackB.pop()


class So:

    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, item):
        self.queueA.append(item)

    def show(func):  # func接收body
        def warpper(self, *args, **kwargs):  # self,接收body里的self,也就是类实例
            print(func(self, *args, **kwargs))

        return warpper

    @show
    def pop(self):
        if len(self.queueB) == 0:
            if len(self.queueA) != 0:
                for _ in range(len(self.queueA) - 1):
                    self.queueB.append(self.queueA.pop(0))
                val = self.queueA.pop()
                self.queueA, self.queueB = self.queueB, self.queueA
                return val
            else:
                return None

        return self.queueB.pop()


if __name__ == '__main__':
    ss = So()
    ss.push("a")
    ss.push("b")
    ss.pop()
    ss.push("c")
    ss.pop()
