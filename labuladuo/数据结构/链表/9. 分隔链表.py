"""
725. Split Linked List in Parts(Medium)

给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，
也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，
并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> list:
        cur = root
        N = 0
        while cur:
            N += 1
            cur = cur.next
        width = N // k
        reminder = N % k
        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < reminder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                tmp = cur.next
                cur.next = None
                cur = tmp
            ans.append(head)
        return ans


def generateList(l: list) -> ListNode:  # 这是为了打印结果，写的生成链表的函数，传入列表list即可
    prenode = ListNode(0)  # 哑节点
    lastnode = prenode
    for val in l:  # 遍历传入的列表
        lastnode.next = ListNode(val)  # 不断创建新节点，并链接
        lastnode = lastnode.next  # 指针后移，不移动的话就是还在原位置后面创新新节点了
    return prenode.next  # 别把哑巴节点返回了啊


def printList(l: ListNode):  # 打印链表函数，传入的是链表哦
    while l:
        print("%d" % l.val, end='->')
        l = l.next
    print('NULL')


if __name__ == "__main__":
    l1 = generateList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 3
    printList(l1)
    s = Solution()
    out = s.splitListToParts(l1, k)
    for i in range(k):
        printList(out[i])
