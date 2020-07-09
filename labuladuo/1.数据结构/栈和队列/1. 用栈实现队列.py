"""
232. Implement Queue using Stacks (Easy)
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack --
which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example,
no pop or peek operations will be called on an empty queue).
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
            return self.B.pop()
        else:
            return self.B.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
            return self.B[-1]
        else:
            return self.B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.B) == 0 and len(self.A) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
x, y, z = 2, 3, 4
obj.push(x)
obj.push(y)
obj.push(z)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
