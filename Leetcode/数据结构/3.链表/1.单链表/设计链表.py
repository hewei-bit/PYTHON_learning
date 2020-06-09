# 自定义单节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    """
    Initialization
    """

    def __init__(self):
        # 链表长度
        self._lenth = 0
        # 设置头结点
        self._head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index > self._lenth:
            return -1
        cur = self._head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self._lenth, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self._lenth:
            return None
        pre = self._head
        node = ListNode(val)
        for _ in range(index):
            pre = pre.next
        node.next = pre.next
        pre.next = node
        self._lenth += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self._lenth:
            return
        pre = self._head
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next
        self._lenth -= 1

    @property
    def lenth(self):
        return self._lenth

    @property
    def head(self):
        return self._head


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(435)
    obj.addAtTail(34234)
    obj.addAtIndex(1, 12313)
    print(obj.get(1))
    node = obj.head.next
    for i in range(obj.lenth):
        print(node.val, end=",")
        node = node.next
    print()
    obj.deleteAtIndex(1)
    for i in range(1, obj.lenth + 1):
        print(obj.get(i), end=",")
