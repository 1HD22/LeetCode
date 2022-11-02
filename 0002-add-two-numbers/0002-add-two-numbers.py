# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mx = l1
        my = l2
        head = ListNode()
        mp = head
        
        while ((mx != None) or (my != None)):
            if (mx == None):
                sum = my.val + mp.val
            elif (my == None):
                sum = mx.val + mp.val
            else:
                sum = mx.val + my.val + mp.val
            
            mp.val = sum % 10
            
            if (sum // 10 == 0) and (mx == None or mx.next == None) and (my == None or my.next == None):
                break
            
            mp.next = ListNode()
            
            mp.next.val = sum // 10
            
           #if mp.next.val == 0 and mx.next == None and my.next == None:
               # mp.next = None
            
            if mx != None:
                mx = mx.next
            
            if my != None:
                my = my.next
            
            if mp != None:
                mp = mp.next
        
        return head
        