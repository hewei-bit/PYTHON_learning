"""
445. Add Two Numbers II (Medium)

You are given two non-empty linked lists
representing two non-negative integers.
The most significant digit comes first
and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
 except the number 0 itself.
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

Follow up:
What if you cannot modify the input lists?
In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        def list2num(l3: ListNode) -> int:
            res = 0
            while l3:
                res = res * 10 + l3.val
                l3 = l3.next
            return res

        result = list2num(l1) + list2num(l2)
        newList = ListNode(0)
        start_node = newList
        for i in str(result):
            newList.next = ListNode(int(i))
            newList = newList.next
        return start_node.next


a = ListNode(1)
b = ListNode(8)
c = ListNode(9)
d = ListNode(2)
a.next = b
c.next = d
obj = Solution().addTwoNumbers(a, c)
print(obj.val, obj.next.val, obj.next.next.val)
