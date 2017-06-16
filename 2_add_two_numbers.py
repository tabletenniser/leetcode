"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(-1)
        cur_node = dummy_node
        carry = 0
        l1_p, l2_p = l1, l2
        while l1_p != None or l2_p != None:
            sum = carry
            if l1_p != None:
                sum += l1_p.val
                l1_p = l1_p.next
            if l2_p != None:
                sum += l2_p.val
                l2_p = l2_p.next

            new_node = ListNode(sum % 10)
            carry = sum / 10
            cur_node.next = new_node
            cur_node = cur_node.next

        if carry == 1:
            new_node = ListNode(1)
            cur_node.next = new_node

        return dummy_node.next
