"""
234. Palindrome Linked List (Easy)
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        aaa = head
        res = []
        while aaa:
            res.append(aaa.val)
            aaa = aaa.next
        if res == res[::-1]:
            return True
        else:
            return False


a = ListNode(1)
b = ListNode(8)
c = ListNode(9)
d = ListNode(2)
a.next = b
b.next = c
c.next = d
obj = Solution().isPalindrome(a)
