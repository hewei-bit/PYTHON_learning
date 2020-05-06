"""
24. Swap Nodes in Pairs (Medium)
Given a linked list, swap every two adjacent nodes \
and return its head.

You may not modify the values in the list's nodes, \
only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b = c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next
