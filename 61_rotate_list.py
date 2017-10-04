'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n):
        self.val = x
        self.next = n

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        length = 0
        cur = head
        last = cur
        while cur != None:
            length += 1
            last = cur
            cur = cur.next
        k = (length - k % length) % length

        prev, cur = None, head
        while k > 0:
            prev = cur
            cur = cur.next
            k -= 1
        if prev != None:
            prev.next = None
            last.next = head
        return cur

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

s = Solution()
node = s.rotateRight(a, 4)
while node != None:
    print node.val
    node = node.next
