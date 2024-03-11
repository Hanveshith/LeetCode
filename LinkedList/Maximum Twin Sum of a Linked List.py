# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # st = []
        # temp = head
        # c = 0
        # while(temp):
        #     c+=1
        #     st.append(temp.val)
        #     temp = temp.next
        # res = 0
        # for i in range(c):
        #     if(res < (st[i] + st[c-i-1])):
        #         res = st[i] + st[c-i-1]
        # return res
        st = []
        res = 0
        slow = fast = head
        temp = head
        while(fast and fast.next):
            fast = fast.next.next
            st.append(slow.val)
            slow = slow.next
        while(slow):
            res = max(res,st.pop()+slow.val)
            slow = slow.next
        return res
        

