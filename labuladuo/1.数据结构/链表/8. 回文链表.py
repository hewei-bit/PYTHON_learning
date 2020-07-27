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

"""
tips：快慢指针
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

    def isPalindrome_2(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next

        left = head
        right = self.reverse(slow)
        while right is not None and left is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head: ListNode):
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(8)
    e = ListNode(9)
    c = ListNode(8)
    d = ListNode(1)
    a.next = b
    b.next = e
    e.next = c
    c.next = d
    obj = Solution().isPalindrome_2(a)
