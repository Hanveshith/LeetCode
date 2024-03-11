# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res
        curr_s = 0
        
        while head:
            if head.val != 0:
                curr_s += head.val
            else:
                if curr_s != 0:
                    curr.next = ListNode(curr_s)
                    curr = curr.next
                curr_s = 0
            head = head.next
        
        if curr_s != 0:
            curr.next = ListNode(curr_s)
        
        return res.next