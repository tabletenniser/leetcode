'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        if cur != None and cur.next != None:
            head = cur.next
        while cur != None and cur.next != None:
            next_cur = cur.next.next
            cur.next.next = cur
            if next_cur == None:
                cur.next = None
            elif next_cur.next == None:
                cur.next = next_cur
            else:
                cur.next = next_cur.next
            #print 'cur', cur.val, cur.next.val
            cur = next_cur
        return head
