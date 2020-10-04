# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:01:05 2020

@author: GopalKrishna
"""

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        first = None
        head = None
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                current = ListNode(l1.val)
                l1 = l1.next
            else:
                current = ListNode(l2.val)
                l2 = l2.next
            
            if first == None:
                first = current
                head = current
            else:
                head.next = current
                head = head.next

            
        if l1 != None:
            if head == None:
                return l1
            else:
                head.next = l1
            
        if l2 != None:
            if head == None:
                return l2
            else:
                head.next = l2
            
        return first
    
    def mergeTwoListsNew(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = ListNode(-1)
        head = current
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
                
            current = current.next
            
        if l1:
            current.next = l1
            
        if l2:
            current.next = l2
            
        return head.next

if __name__ == '__main__':
    a = ListNode(1) 
    b = ListNode(2)
    c = ListNode(4)
    a.next = b
    b.next = c
    
    l1 = a
    
    a = ListNode(1) 
    b = ListNode(3)
    c = ListNode(4)
    a.next = b
    b.next = c
    
    l2 = a
    r = Solution().mergeTwoLists(l1, l2)
    print(r)