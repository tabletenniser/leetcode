'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n):
        self.val = x
        self.next = n

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(None, None)
        root.next = head
        prev, cur = root, head
        i = 1
        while i < n:
            if i >= m:
                next_node = cur.next
                assert(next_node)
                cur.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
            else:
                prev = prev.next
                cur = cur.next
            i += 1
        return root.next

n1 = ListNode(1, None)
n2 = ListNode(2, n1)
n3 = ListNode(3, n2)

s = Solution()
s.reverseBetween(n3, 1, 3)
