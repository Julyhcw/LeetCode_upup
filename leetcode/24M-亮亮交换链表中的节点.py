# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''递归'''
        if head == None or head.next == None:
            return head
        res = head.next
        head.next = self.swapPairs(res.next)
        res.next = head
        return res
        
        '''非递归'''
        res = ListNode(0)
        cur, res.next = res, head
        while cur.next and cur.next.next:
            pre = cur
            cur = cur.next
            
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = cur
        return res.next
            
            
            
            
            
            
            
            
            
            
            