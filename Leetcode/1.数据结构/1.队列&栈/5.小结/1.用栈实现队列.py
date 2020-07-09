class UseStackToQueue:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 1:
                self.B.append(self.A.pop())
            return self.B.pop()
        else:
            return self.B.pop()

    def peek(self) -> int:
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
            return self.B[-1]
        else:
            return self.B[-1]

    def empty(self) -> bool:
        if len(self.B) == 0 and len(self.A) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = UseStackToQueue()
    x, y, z = 2, 3, 4
    obj.push(x)
    obj.push(y)
    obj.push(z)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
