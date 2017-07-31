'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import *
        h = []
        for l in lists:
            if l != None:
                heappush(h, (l.val, l))
        result = []
        while len(h) > 0:
            elem = heappop(h)
            result.append(elem[0])
            if elem[1].next != None:
                heappush(h, (elem[1].next.val, elem[1].next))
        return result
