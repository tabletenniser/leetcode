'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node

    def __str__(self):
        return str(self.__dict__)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_val = None
        result_node = ListNode('haha')
        res_head = result_node
        cur = head
        while cur != None:
            cur_val = cur.val
            if cur_val != prev_val:
                result_node.next = ListNode(cur_val)
                result_node = result_node.next
                prev_val = cur_val
            cur = cur.next
        return res_head.next

s = Solution()
node3 = ListNode(3, None)
node2 = ListNode(2, node3)
node1 = ListNode(2, node2)
head = ListNode(1, node1)
print s.deleteDuplicates(head).next.next
