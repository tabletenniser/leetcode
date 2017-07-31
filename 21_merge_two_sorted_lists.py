'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = l1, l2
        result = None
        if n1 == None and n2 == None:
            return None
        if (n1 == None and n2 != None) or (n1 != None and n2 != None and n1.val > n2.val):
            result = n2
            n2 = n2.next
        else:
            result = n1
            n1 = n1.next
        cur = result

        while n1 != None or n2 != None:
            if n1 == None or (n1 != None and n2 != None and n1.val > n2.val):
                cur.next = n2
                n2 = n2.next
            else:
                cur.next = n1
                n1 = n1.next
            cur = cur.next
        return result
